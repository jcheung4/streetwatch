#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import requests

from PIL import Image
from io import BytesIO

from dotenv import load_dotenv
load_dotenv()

import os
import yaml

api_key = os.getenv("API_KEY")
secret = os.getenv("SECRET")


# In[1]:


""" Signs a URL using a URL signing secret """

import hashlib
import hmac
import base64
import urllib.parse as urlparse


def sign_url(input_url=None, secret=None):
    """ Sign a request URL with a URL signing secret.
      Usage:
      from urlsigner import sign_url
      signed_url = sign_url(input_url=my_url, secret=SECRET)
      Args:
      input_url - The URL to sign
      secret    - Your URL signing secret
      Returns:
      The signed request URL
  """

    if not input_url or not secret:
        raise Exception("Both input_url and secret are required")

    url = urlparse.urlparse(input_url)

    # We only need to sign the path+query part of the string
    url_to_sign = url.path + "?" + url.query

    # Decode the private key into its binary format
    # We need to decode the URL-encoded private key
    decoded_key = base64.urlsafe_b64decode(secret)

    # Create a signature using the private key and the URL-encoded
    # string using HMAC SHA1. This signature will be binary.
    signature = hmac.new(decoded_key, str.encode(url_to_sign), hashlib.sha1)

    # Encode the binary signature into base64 for use within a URL
    encoded_signature = base64.urlsafe_b64encode(signature.digest())

    original_url = url.scheme + "://" + url.netloc + url.path + "?" + url.query

    # Return signed URL
    return original_url + "&signature=" + encoded_signature.decode()



# In[ ]:q


def save_image_file(latitude, longitude, heading, pitch, fov, secret, api_key, name, outpath):

    size = '400x400'
    
    url = f'https://maps.googleapis.com/maps/api/streetview?size={size}&location={latitude},{longitude}&heading={heading}&pitch={pitch}&fov={fov}&key={api_key}'

    s = sign_url(url, secret)
    response = requests.get(s)

    if response.status_code == 200:

        n = outpath + name + ".jpg"
        with open(n, 'wb') as f:
            f.write(response.content)
    
    else:
        print(f'Error: {response.status_code}')


# In[ ]:


def get_images(yaml_file, outpath):
    with open(yaml_file, 'r') as file:
        existing_data = yaml.safe_load(file)

        c = 0 #counter variable for naming only
        for img in existing_data:
            for fov in [50,75,90]:
                c = c + 1
                if c > 15:
                    c = 1
                name = img['name'] + "_" + str(c)+"_" + str(fov)
                save_image_file(img['latitude'], img['longitude'],img['heading'],img['pitch'], fov, secret, api_key, name, outpath)
            

