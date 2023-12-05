#%%
import requests
from IPython import display
from dotenv import load_dotenv
import hashlib
import hmac
import os
import base64
import urllib.parse as urlparse

load_dotenv()

# Pull in API key and Secret key from .env

APIKEY = os.environ.get("API_KEY")
SECRET = os.environ.get("SECRET")


#%%
# Google API documentation code for signing API requests
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




# %%d
def get_image(location, size='600x400',heading=120, fov=90, saveImage=False, imgFileName=None):
    """
    Function to get images from Street View API, with options to save and name saved images.

    Params:
        location: Coordinates of image
        size: Size of image, default 600x400
        heading: Direction of camera, ranges from 0-360
        fov: Fov controls the zoom level, where 90 is the default zoom, ranges from 0-120
        saveImage: bool that if set to true will save image to data directory
        imgFileName: name of image that will be assigned if saveImage is true

    Returns:
    Image display object to visualize request, calling display.display(returned object) will visualize image generated.
    
    """
    URL = f"https://maps.googleapis.com/maps/api/streetview?key={APIKEY}&size={size}&location={location}&heading={heading}&fov={fov}"
    SignedURL = sign_url(input_url=URL, secret=SECRET)
    response = requests.get(SignedURL)
    if saveImage:
        with open(f'data/images/{imgFileName}.jpg', 'wb') as file:
            file.write(response.content)
        response.close()
    return display.Image(response.content)
    
OH_coords = ["32.75234,-117.1281",
            "32.7523,-117.129",
            "32.75211,-117.129",
            "32.7521093453396,-117.129497857777",
            "32.75224,-117.129"
]

OH1 = [{'coord':"32.75234,-117.12818", 'heading':105}, 
        {'coord':"32.75234,-117.12805", 'heading':105}, 
        {'coord':"32.75225,-117.1278", 'heading':180}, 
        {'coord':"32.75225,-117.1277", 'heading':230},
        {'coord':"32.75225,-117.12755", 'heading':260}]

OH2 = [{'coord':"32.7522,-117.12882", 'heading':280},
        {'coord':"32.7522,-117.12895", 'heading':315},
        {'coord':"32.7523,-117.1291", 'heading':15},
        {'coord':"32.7523,-117.1292", 'heading':45},
        {'coord':"32.7523,-117.1293", 'heading':65}
]

OH3 = [{'coord':"32.7522,-117.12882", 'heading':240},
        {'coord':"32.7522,-117.1289", 'heading':235},
        {'coord':"32.7523,-117.1291", 'heading':140},
        {'coord':"32.7523,-117.12929", 'heading':105},
        {'coord':"32.7523,-117.1294", 'heading':100}
]

OH4 = [{'coord':"32.7522,-117.1292", 'heading':250},
        {'coord':"32.7522,-117.1293", 'heading':240},
        {'coord':"32.7522,-117.12951", 'heading':160},
        {'coord':"32.7522,-117.12968", 'heading':100},
        {'coord':"32.7522,-117.12985", 'heading':100}

]

OH5 = [{'coord':"32.7522,-117.1292", 'heading':290},
        {'coord':"32.7522,-117.1293", 'heading':300},
        {'coord':"32.7522,-117.12951", 'heading':30},
        {'coord':"32.7522,-117.12968", 'heading':60},
        {'coord':"32.7522,-117.12985", 'heading':70}    

]





UG1 = [{'coord':"32.75225,-117.13059", 'heading':60},
        {'coord':"32.75225,-117.1305", 'heading':45},
        {'coord':"32.75223,-117.13033", 'heading':10},
        {'coord':"32.75224,-117.1302", 'heading':300},
        {'coord':"32.75237,-117.13017", 'heading':245}
]

UG2 = [{'coord':"32.75406,-117.1305", 'heading':245}]

UG3 = [{'coord':"32.75357,-117.13078", 'heading':340},
        {'coord':"32.75366,-117.13078", 'heading':325},
        {'coord':"32.75376,-117.13078", 'heading':235},
        {'coord':"32.7538,-117.13078", 'heading':200},
        {'coord':"32.7539,-117.13078", 'heading':190}
]

UG4 = [{'coord':"32.75407,-117.130025", 'heading':115},
        {'coord':"32.75406,-117.12996", 'heading':145},
        {'coord':"32.75405,-117.12985", 'heading':210},
        {'coord':"32.75405,-117.12975", 'heading':240},
        {'coord':"32.75405,-117.12965", 'heading':250}
]


UG5 = [{'coord':"32.75405,-117.12815", 'heading':300},
        {'coord':"32.75405,-117.12825", 'heading':320},
        {'coord':"32.75405,-117.12835", 'heading':340},
        {'coord':"32.75405,-117.12841", 'heading':350},
        {'coord':"32.75405,-117.12851", 'heading':35}
        ]


OHstrucs = [OH1, OH2, OH3, OH4, OH5]
UGstrucs = [UG1, UG2, UG3, UG4, UG5]


# Uses preselected coordinates and headings from above to make generate API requests
# to generate image dataset.

def get_dataset():
    for struct_idx in range(len(OHstrucs)):
        currStruct = OHstrucs[struct_idx]
        for view_idx in range(len(currStruct)):
            loc = currStruct[view_idx]['coord']
            heading = currStruct[view_idx]['heading']
            for f in [90, 60, 25]:
                fName = f"OH_{struct_idx}_v{view_idx}_f{f}" 
                get_image(loc, heading=heading,fov=f, saveImage=True, imgFileName=fName)


    for struct_idx in range(len(UGstrucs)):
        currStruct = UGstrucs[struct_idx]
        for view_idx in range(len(currStruct)):
            loc = currStruct[view_idx]['coord']
            heading = currStruct[view_idx]['heading']
            for f in [90, 60, 25]:
                fName = f"UG_{struct_idx}_v{view_idx}_f{f}" 
                get_image(loc, heading=heading,fov=f, saveImage=True, imgFileName=fName)






# %%
