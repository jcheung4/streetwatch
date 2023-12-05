#%%
from dotenv import load_dotenv
import os
import requests
import io
from PIL import Image
import json
import hashlib
import hmac
import base64
import urllib.parse as urlparse

load_dotenv()

API_KEY = os.environ.get("API_KEY")
SECRET = os.environ.get("SECRET")

#%%
def sign_url(input_url=None, secret=None):
    """
    https://developers.google.com/maps/digital-signature
    Sign a request URL with a URL signing secret.
    """
    if not input_url or not secret:
        raise Exception("Both input_url and secret are required")

    url = urlparse.urlparse(input_url)
    url_to_sign = url.path + "?" + url.query
    decoded_key = base64.urlsafe_b64decode(secret)
    signature = hmac.new(decoded_key, str.encode(url_to_sign), hashlib.sha1)
    encoded_signature = base64.urlsafe_b64encode(signature.digest())
    original_url = url.scheme + "://" + url.netloc + url.path + "?" + url.query

    return original_url + "&signature=" + encoded_signature.decode()


def get_image(params, key=API_KEY, secret=SECRET):
    base_url = "https://maps.googleapis.com/maps/api/streetview"
    url = base_url + "?size={size}&location={location}&heading={heading}&pitch={pitch}&fov={fov}".format(**params)
    url = url + f"&key={key}"
    signed_url = sign_url(url, secret)
    response = requests.get(signed_url)
    if response.status_code == 200:
        return response.content
    else:
        print("API Request Error:", response.status_code)


def save_image(params, output_dir, key=API_KEY, secret=SECRET):
    image_data = get_image(params, key, secret)
    image = Image.open(io.BytesIO(image_data))
    image_name = f"{params['id']}_{params['angle']}_{params['zoom']}.png"
    os.makedirs(output_dir, exist_ok=True)
    image.save(output_dir + image_name)
    print(f"Saved " + image_name + "into " + output_dir)


def read_json_data(file):
    with open(file, 'r') as json_file:
        docs = json.load(json_file)
        return docs


def add_image_data(data, filepath):
    '''
    Adds image data to json file

    data = { 
        'fov': 150,
        'heading': 110,
        'id': 'D150379',
        'location': '32.864945,-117.225454',
        'pitch': 0,
        'size': '640x640'
        'angle': 0,
        'zoom': 0
    }
    '''
    json_list = read_json_data(filepath)    
    json_list.append(data)

    with open(filepath, 'w') as f:
        json.dump(json_list, f, indent=4, separators=(',',': '))
        print("Added data:")
        print(data)


def create_images(data_file, outpath):
    data = read_json_data(data_file)
    os.makedirs(outpath, exist_ok=True)
    for image_params in data:
        save_image(image_params, outpath)

#%%
if __name__ == "__main__":
    create_images(data_file='data/joshua_structures.json', outpath='/data/images/')

