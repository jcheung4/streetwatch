# %%
import os
import io
import json
import time
import hmac
import base64
import requests
import hashlib
import pyproj
import pandas as pd
import urllib.parse as urlparse
from PIL import Image
from dotenv import load_dotenv
from tqdm import tqdm

load_dotenv()

API_KEY = os.environ.get("API_KEY")
SECRET = os.environ.get("SECRET")


# %%
def read_structure_excel(excel_file):
    """
    Read excel file containing list of structures
    """
    cols = ['Structure ID','LATITUDE','LONGITUDE']
    df = pd.read_excel(excel_file, usecols=cols, sheet_name='Phi')
    return df


# %%
def _sign_url(input_url, secret):
    """https://developers.google.com/maps/digital-signature"""
    url = urlparse.urlparse(input_url)
    url_to_sign = url.path + "?" + url.query
    decoded_key = base64.urlsafe_b64decode(secret)
    signature = hmac.new(decoded_key, str.encode(url_to_sign), hashlib.sha1)
    encoded_signature = base64.urlsafe_b64encode(signature.digest())
    original_url = url.scheme + "://" + url.netloc + url.path + "?" + url.query
    return original_url + "&signature=" + encoded_signature.decode()


# %%
def get_pano_metadata(latitude, longitude, api_key=API_KEY, secret=SECRET, **kwargs):
    """
    Get the panorama ID and capture date for a specific set of coordinates using the Street View Metadata API.
    """
    base_url = "https://maps.googleapis.com/maps/api/streetview/metadata"
    payload = {
        "location": f"{latitude},{longitude}",
        "key": api_key,
    }
    payload.update(**kwargs)
    r = requests.Request('GET', base_url, params=payload)
    url = r.prepare().url
    if secret:
        url = _sign_url(url, secret)
    response = requests.get(url)
    if response.status_code == 200:
        return json.loads(response.text)


# %% 
def _prepare_streetview_url(api_key, secret, **kwargs):
    """
    Generate URL for streetview download
    """
    base_url = "https://maps.googleapis.com/maps/api/streetview"
    payload = {
        "key": api_key,
    }
    payload.update(**kwargs)
    r = requests.Request('GET', base_url, params=payload)
    url = r.prepare().url
    if secret:
        url = _sign_url(url, secret)
    return url


# %%
def create_session(api_key=API_KEY):
    """
    Create a new session for the Street View API.
    """
    base_url = "https://tile.googleapis.com/v1/createSession"
    headers = {'Content-Type': 'application/json'}
    payload = {
        "key": api_key,
        "mapType": "streetview",
        "language": "en-US",
        "region": "US",
    }
    response = requests.post(base_url, params=payload, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(response.json()['error']['message'])


# %%
def get_tile_metadata(session, pano_id, api_key=API_KEY):
    """
    Create a new session for the Street View API.
    """
    base_url = "https://tile.googleapis.com/v1/streetview/metadata"
    headers = {'Content-Type': 'application/json'}
    payload = {
        "session": session,
        "key": api_key,
        "panoId": pano_id
    }    
    response = requests.get(base_url, params=payload, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(response.json()['error']['message'])


# %%
def get_adjacent_panos(primary_pano, session, api_key=API_KEY, total_panos=5, sleep=0.2):
    """
    Grab adjacent panos using tiles metadata api until total and reach or no more links
    Returns list of (panoId, lat, lon)
    """
    panos = []; queue = []
    queue.append(primary_pano)
    while queue and len(panos) < total_panos:
        p = queue.pop(0)
        m = get_tile_metadata(session, p, api_key=api_key)
        panos.append((m['panoId'], m['lat'], m['lng']))
        links = [p['panoId'] for p in m['links']]
        new_links = [l for l in links if l not in [p[0] for p in panos]]
        queue += new_links
        time.sleep(sleep)
    return panos


# %%
def heading_angle(pano_lat, pano_lon, struc_lat, struc_lon):
    """
    Function that uses python pyproj to find the "heading" angle between two coordinates, given that 0 degrees is north
    Use the azimuth angle
    """
    geodesic = pyproj.Geod(ellps='WGS84')
    heading, _, _ = geodesic.inv(pano_lon, pano_lat, struc_lon, struc_lat)
    return (heading % 360 + 360) % 360


# %%
def download_streetview_image(size="600x400", api_key=API_KEY, secret=SECRET, **params):
    """
    Download a Google Street View image for a specific panorama.
    """
    url = _prepare_streetview_url(api_key=api_key, secret=secret, size=size, **params)
    response = requests.get(url)
    if response.status_code == 200:
        return response.content
    elif "ZERO_RESULTS" in response.text:
        return None 
    else:
        raise Exception(response.content)


# %%
def show_image(pano_id, **params):
    i = download_streetview_image(pano=pano_id, **params)
    img = Image.open(io.BytesIO(i))
    return img

    
# %%
def save_images_for_structure(
    structureid: str, 
    lat: float, 
    lon: float,
    session: str,
    output_dir: str,
    progressbar: bool=True,
    sleep: float=0.2,
    api_key: str=API_KEY,
    secret: str=SECRET
) -> None:
    primary_pano = get_pano_metadata(lat, lon, api_key, secret)['pano_id']
    panos = get_adjacent_panos(primary_pano, session, api_key)
    with tqdm(disable=not progressbar, desc=structureid) as total:
        for pano, pla, plo in panos:
            heading = heading_angle(pla, plo, lat, lon)
            for fov in [60, 90, 120]:
                im = download_streetview_image(
                    size="600x400", 
                    api_key=api_key, 
                    secret=secret,
                    pano=pano,
                    heading=heading, 
                    fov=fov
                )
                img = Image.open(io.BytesIO(im))
                img_name = f"{structureid}_{pano}_{fov}.jpg"
                img.save(output_dir+img_name)
                total.update(1)
                time.sleep(sleep)
    total.close()


# %%
def create_images(excel_file, outpath, progressbar=True):
    df = read_structure_excel(excel_file)
    os.makedirs(outpath, exist_ok=True)
    s = create_session()['session']
    for _, structureid, lat, lon in df.itertuples():
        save_images_for_structure(structureid, lat, lon, s, outpath, progressbar)


# %%
if __name__== "__main__":
    create_images(excel_file='data/Q1ProjectStructureList.xlsx', outpath='data/images/')