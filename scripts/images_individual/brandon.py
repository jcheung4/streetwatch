import requests
import hashlib
import hmac
import base64
import urllib
import urllib.parse as urlparse
import os
from dotenv import load_dotenv


load_dotenv()
api_key = os.getenv("API_KEY")
secret = os.getenv("SECRET")

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

def get_street_view_image(location, size="600x400", heading=None, pitch=None, fov=None):
    base_url = "https://maps.googleapis.com/maps/api/streetview?"
    parameters = {
        "size": size,
        "location": location,
        "key": api_key,
    }
    
    if heading is not None:
        parameters["heading"] = heading

    if pitch is not None:
        parameters["pitch"] = pitch

    if fov is not None:
        parameters["fov"] = 130 - (fov * 10)

    signed_url = sign_url(base_url + urllib.parse.urlencode(parameters), secret=secret)
    # print(signed_url)
    # response = requests.get(base_url, params=parameters)
    response = requests.get(signed_url)
    
    if response.status_code == 200:
        return response.content
    else:
        print("Error: Unable to fetch Street View image")
        return None
def save_street_view_image(image_data, file_name):
    # os.makedirs(folder, exist_ok=True)
    # file_path = os.path.join(folder, file_name)
    with open(file_name, "wb") as file:
        file.write(image_data)
    # response.close()

def collect_imgs(outpath):
    loc_dict = {'OH1': {'loc': ["32.85375,-117.184", "32.8537252,-117.1839452", "32.8536624,-117.1838662", "32.8534917,-117.1837151", "32.8534468,-117.1836238"], 'heading': [115, 100, 70, 340, 330], 'pitch': [0, 10, 20, 0, 0], 'fov': [[1,3,5], [1,3,5], [1,3,5], [1,3,5], [1,3,5]]}, 'OH2': {'loc': ["32.85023657,-117.1978705", "32.8501438,-117.1978682", "32.850065,-117.1979105", "32.8503165,-117.1978014", "32.8503995,-117.1977577"], 'heading': [270, 330, 350, 260, 250], 'pitch': [15, 10, 10, 10, 10], 'fov': [[1,3,5], [1,3,5], [1,3,5], [1,3,5], [1,3,5]]}, 'OH3': {'loc': ["32.8555683,-117.2094497", "32.8554762,-117.2094495", "32.85539,-117.209", "32.8552001,-117.2094514", "32.855109,-117.2094547"], 'heading': [160, 140, 80,20,20], 'pitch': [10, 10, 10, 10, 10], 'fov': [[1,3,5], [1,3,5], [1,3,5], [1,3,5], [1,3,5]]}, 'OH4': {'loc': ["32.8388097,-117.1870385", "32.8389025,-117.1870632", "32.8389929,-117.1870379", "32.8391742,-117.187058", "32.8392682,-117.1870338"], 'heading': [350,340, 320, 210, 210], 'pitch': [10, 10, 10, 10, 10], 'fov': [[1,3,5], [1,3,5], [1,3,5], [1,3,5], [1,3,5]]}, 'OH5': {'loc': ["32.8378025,-117.187466", "32.8378,-117.187359", "32.8377956,-117.187257", "32.8378031,-117.1875741", "32.8378042,-117.1876826"], 'heading': [140, 222, 235, 122, 100], 'pitch': [0, 10, 20, 0, 0], 'fov': [[1,3,5], [1,3,5], [1,3,5], [1,3,5], [1,3,5]]}, 'UG1': {'loc': ["32.8613709,-117.2211502", "32.8613759,-117.221048", "32.8613751,-117.2209401", "32.8613733,-117.2208313","32.8613711,-117.2207234"], 'heading': [60, 60, 30, 310, 290], 'pitch': [10, 10, 0, 0, 0], 'fov': [[1,3,5], [1,3,5], [1,3,5], [1,3,5], [1,3,5]]}, 'UG2':{'loc': ["32.8712,-117.224", "32.87116,-117.2238914", "32.8711147,-117.2237941", "32.8710661,-117.2236934", "32.871005,-117.2236064"], 'heading': [95, 75, 50, 350, 330], 'pitch': [0, 0, 0, 0, 0], 'fov': [[1,3,5], [1,3,5], [1,3,5], [1,3,5], [1,3,5]]}, 'UG3': {'loc': ["32.86909,-117.225", "32.8689736,-117.2247661", "32.8688827,-117.2247637", "32.8687866,-117.2247628", "32.8686897,-117.2247613"], 'heading': [140, 130, 55, 20, 10], 'pitch': [0, 0, 0, 0, 0], 'fov': [[1,3,5], [1,3,5], [1,3,5], [1,3,5], [1,3,5]]}, 'UG4': {'loc': ["32.8684157,-117.2210601", "32.8685279,-117.2210097", "32.868614,-117.2209804", "32.8683332,-117.22107", "32.8682465,-117.2211173"], 'heading': [90, 150, 160, 50, 10], 'pitch': [0, 0, 0, 0, 0], 'fov': [[1,3,5], [1,3,5], [1,3,5], [1,3,5], [1,3,5]]}, 'UG5': {'loc': ["32.8664987,-117.2200092", "32.866569,-117.2199398", "32.8666394,-117.2198706", "32.8667105,-117.2198014", "32.8667818,-117.2197339"], 'heading': [20, 360, 290, 250, 240], 'pitch': [0, 0, 0, 0, 0], 'fov': [[1,3,5], [1,3,5], [1,3,5], [1,3,5], [1,3,5]]}}
    for structure in loc_dict:
        for i in range(5):
            for j in range(3):
                param = loc_dict[structure]
                image_data = get_street_view_image(location=param['loc'][i], heading=param['heading'][i], pitch=param['pitch'][i], fov=param['fov'][i][j])
                if image_data:
                    file_name = f"{outpath}{structure}_angle{i}_fov{j}.jpg"
                    save_street_view_image(image_data, file_name)
if __name__ == "__main__":
    collect_imgs(outpath="data/images/")