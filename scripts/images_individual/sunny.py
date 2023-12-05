#%%
import os
import requests
from dotenv import load_dotenv
import json
import base64
import hmac
import urllib.parse as urlparse
import hashlib

load_dotenv()

API_KEY = os.environ.get("API_KEY")
SECRET = os.environ.get("SECRET")
pic_base = 'https://maps.googleapis.com/maps/api/streetview?'

#%%
def sign_url(input_url=pic_base, secret=SECRET):


    if not input_url or not secret:
        raise Exception("Both input_url and secret are required")

    url = urlparse.urlparse(input_url)

    url_to_sign = url.path + "?" + url.query
    decoded_key = base64.urlsafe_b64decode(secret)
    signature = hmac.new(decoded_key, str.encode(url_to_sign), hashlib.sha1)
    encoded_signature = base64.urlsafe_b64encode(signature.digest())
    original_url = url.scheme + "://" + url.netloc + url.path + "?" + url.query

    # Return signed URL
    return original_url + "&signature=" + encoded_signature.decode()

#%%
def gen_url(params, input_url=pic_base):
    out = input_url
    for i in params:
        out = out+"&"+str(i)+"="+str(params[i])
    return out
#%%
def get_oh(outpath, structure_json):
    for i,st in enumerate(structure_json):
        for j,pic in enumerate(st):
            for f in [20,60,90]:
                pic_params = {'key': API_KEY,
                        'location': pic['loc'],
                        'size': "640x640",
                        'heading':pic['heading'],
                        'fov':f
                        }
                if SECRET:
                    pic_response = requests.get(sign_url(input_url=gen_url(pic_params)))
                else:
                    pic_response = requests.get(input_url=gen_url(pic_params))
                with open(os.path.join(outpath,'OH'+str(i)+'_'+str(j)+'_'+str(f)+'.jpg'), 'wb') as file:
                    file.write(pic_response.content)



# %%
def get_ug(outpath, structure_json):
    for i,st in enumerate(structure_json):
        for j,pic in enumerate(st):
            for f in [20,60,90]:
                pic_params = {'key': API_KEY,
                        'location': pic['loc'],
                        'size': "640x640",
                        'heading':pic['heading'],
                        'pitch':-10,
                        'fov':f
                        }
                if SECRET:
                    pic_response = requests.get(sign_url(input_url=gen_url(pic_params)))
                else:
                    pic_response = requests.get(input_url=gen_url(pic_params))
                with open(os.path.join(outpath,'UG'+str(i)+'_'+str(j)+'_'+str(f)+'.jpg'), 'wb') as file:
                    file.write(pic_response.content)
# %%
def collect_struct_json(jsonpath, outpath):
    f = open(jsonpath)
    os.makedirs(outpath, exist_ok=True)
    data = json.load(f)
    OH = data['OH']
    UG = data['UG']
    get_oh(outpath, OH)
    get_ug(outpath, UG)
# %%
