import os
import requests
from dotenv import load_dotenv
import hashlib
import hmac
import base64
import urllib.parse as urlparse

# Load environment variables
load_dotenv()

# Google Street View API key and secret
API_KEY = os.getenv('API_KEY')
SECRET = os.getenv('SECRET') 

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

    url_to_sign = url.path + "?" + url.query
    decoded_key = base64.urlsafe_b64decode(secret)
    signature = hmac.new(decoded_key, str.encode(url_to_sign), hashlib.sha1)
    encoded_signature = base64.urlsafe_b64encode(signature.digest())
    original_url = url.scheme + "://" + url.netloc + url.path + "?" + url.query
    return original_url + "&signature=" + encoded_signature.decode()

# Function to fetch and save an image
def fetch_save_image(location, heading, fov, image_name, outpath='data/images/'):
    base_url = "https://maps.googleapis.com/maps/api/streetview"
    params = {
        "size": "600x400",
        "location": location,
        "heading": heading,
        "fov": fov,
        "key": API_KEY
    }
    # Construct the unsigned URL
    unsigned_url = base_url + "?" + "&".join(f"{key}={value}" for key, value in params.items())
    # Sign the URL
    signed_url = sign_url(unsigned_url, SECRET)
    # Make the request using the signed URL
    response = requests.get(signed_url)
    if response.status_code == 200:
        with open(os.path.join(outpath, f"{image_name}.jpg"), "wb") as file:
            file.write(response.content)

def create_images(outpath='data/images/'):
    # List of structures with their respective latitudes and longitudes
    structures = [
        # ("latitude,longitude", "structure_id"),
        ("32.91297,-117.135", "D2726872851"),
        ("32.9134082,-117.133654", "D2727072907"),
        ("32.91357,-117.136", "D104800"),
        ("32.9136991,-117.1357685", "D128975"),
        ("32.78408856,-117.1689693", "P179320J"),
        ("32.78385,-117.169", "P179344"),
        ("32.78384,-117.168", "P179322"),
        ("32.78316,-117.168", "P203544"),
        ("32.78278,-117.169", "P179347")
    ]

    # Default angles and zoom levels
    default_angles = [300, 320, 340, 350, 360]
    default_zoom_levels = [120, 90, 60]

    # Special cases
    special_cases = {
        "P179320J": {
            "angles": [50, 60, 80, 90, 100],
            "zoom_levels": [120, 90, 60]
        },
        "P179322": {
            "angles": [80, 90, 100, 110, 120],
            "zoom_levels": [120, 90, 60]
        },
        "D2727072907": { 
            "angles": [310, 320, 340, 350, 360],
            "zoom_levels": [120, 90, 60]
        },
        "D128975": { 
            "angles": [230, 240, 250, 260, 270],
            "zoom_levels": [120, 90, 60]
        }
    }

    # Fetch and save images for each structure
    for location, structure_name in structures:
        if structure_name in special_cases:
            angles = special_cases[structure_name]["angles"]
            zoom_levels = special_cases[structure_name]["zoom_levels"]
        else:
            angles = default_angles
            zoom_levels = default_zoom_levels

        # Fetch and save images with the specified angles and zoom levels
        for angle in angles:
            for zoom in zoom_levels:
                image_name = f"{structure_name}_angle_{angle}_zoom_{zoom}"
                fetch_save_image(location, angle, zoom, image_name, outpath)

if __name__ == "__main__":
    create_images()
