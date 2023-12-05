import os
from sys import api_version
from dotenv import load_dotenv
import requests
from IPython.display import display, Image
import hashlib
import hmac
import base64
import urllib.parse as urlparse

# Load environment variables from .env file
load_dotenv()
api_key = os.getenv("API_KEY")
digital_signature = os.getenv("SECRET")

# Ensure the API key and digital signature are loaded correctly
if api_key is None or digital_signature is None:
    raise ValueError("API key or digital signature is not set in the environment variables.")

def sign_url(input_url=None, secret=None):
    """ Sign a request URL with a URL signing secret.
      Args:
      input_url - The URL to sign
      secret    - Your URL signing secret
      Returns:
      The signed request URL
    """
    if not input_url or not secret:
        raise Exception("Both input_url and secret are required")
    # Parse the input URL
    url = urlparse.urlparse(input_url)
    
     # Concatenate the URL path and query to sign
    url_to_sign = url.path + "?" + url.query
    
     # Decode the secret key
    decoded_key = base64.urlsafe_b64decode(secret)
    
    # Create the signature
    signature = hmac.new(decoded_key, str.encode(url_to_sign), hashlib.sha1)
    
    # Encode the signature in base64
    encoded_signature = base64.urlsafe_b64encode(signature.digest())
    
    # Reconstruct the original URL with scheme and netloc
    original_url = url.scheme + "://" + url.netloc + url.path + "?" + url.query

    # Append the signature to the URL as a query parameter
    return original_url + "&signature=" + encoded_signature.decode()

def fetch_image(lat, lon, heading, fov, api_key=api_key, secret_key=digital_signature):
    # Google Street View API endpoint
    base_url = "https://maps.googleapis.com/maps/api/streetview"
    # Parameters for the API request
    params = {
        'size': '600x400',
        'location': f'{lat},{lon}',
        'heading': str(heading),
        'fov': str(fov),
        'key': api_key
    }
    # Construct the URL with parameters
    url = base_url + "?"
    for key, value in params.items():
        url += f"{key}={value}&"
    url = url.rstrip("&") # Remove any trailing ampersand
    
    # Sign the URL with your secret key
    signed_url = sign_url(url, secret_key)
    
    # Send the request to the API and return the image content
    response = requests.get(signed_url)
    return response.content

def save_image(image_content, filename):
    # Directory to save images
    directory = 'data/images/'
    # Create directory if it doesn't exist
    if not os.path.exists(directory):
        os.makedirs(directory, exist_ok=True)
    # Full path for the image file
    file_path = os.path.join(directory, filename)
    # Write the image content to the file
    with open(file_path, 'wb') as file:
        file.write(image_content)
    # Log the saved image path
    print(f"Image saved at: {file_path}")

# Main function to execute the script
def derek_create_images():
    # Zoom levels for image capture
    zoom_levels = [150, 100, 80]

    # Coordinates with starting angles
    coordinates = [
        # Each tuple contains latitude, longitude, and starting angle
        (32.9666273, -117.1864764, 40),
        (32.966116, -117.1872297, 270),
        (32.9661106, -117.1874447, 120),
        (32.96601, -117.188, 120),
        (32.9657772, -117.1890632, 80)
    ]

    # Loop over each coordinate to fetch and save images
    for lat, lon, starting_angle in coordinates:
        # Calculate angles by incrementing the starting angle
        angles = [(starting_angle + 20 * i) % 360 for i in range(5)]

        # Loop over angles and zoom levels to fetch and save images
        for angle in angles:
            for zoom in zoom_levels:
                image_content = fetch_image(lat, lon, angle, zoom, api_key, digital_signature)
                # Generate a filename for each image
                filename = f"image_lat{lat}_lon{lon}_angle{angle}_zoom{zoom}.jpg"
                save_image(image_content, filename)

if __name__ == "__main__":
    derek_create_images()