import requests
import os
import shutil
#import getImages
import hashlib
import hmac
import base64
import urllib
import urllib.parse as urlparse
from dotenv import load_dotenv

load_dotenv()

# API
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


# if __name__ == "__main__":
#     input_url = input("URL to Sign: ")
#     secret = input("URL signing secret: ")
#     print("Signed URL: " + sign_url(input_url, secret))

def get_image(main_loc, filename, coord, size="600x400", fov=100, heading=400, pitch=10, api_key=API_KEY,
              secret=SECRET):
    base_url = "https://maps.googleapis.com/maps/api/streetview?"

    url = f"{base_url}size={size}&location={coord[0]},{coord[1]}&fov={fov}&heading={heading}&pitch={pitch}&key={api_key}"

    params = {
        "size": size,
        "location": f"{coord[0]},{coord[1]}",
        "fov": fov,
        "heading": heading,
        "pitch": pitch,
        "key": api_key
    }

    # signed = sign_url(url, secret)
    # response = requests.get(signed)

    # Padding error when signing
    response = requests.get(url, params=params)

    if response.status_code == 200:
        with open('data/images/' + filename, 'wb') as f:
            f.write(response.content)


def create_images():
    ##### 16644 Camino San Bernardo #################################################
    main_location1 = "loc1"
    # os.mkdir(main_location1) #Creates directory

    get_image(main_location1, "rr1_" + main_location1 + ".jpg", [33.01062, -117.11], fov=50, heading=275, pitch=2)
    get_image(main_location1, "rr1_zoom_" + main_location1 + ".jpg", [33.01062, -117.11], fov=20, heading=275, pitch=-3)
    get_image(main_location1, "rr1_zoomzoom_" + main_location1 + ".jpg", [33.01062, -117.11], fov=0, heading=275,
              pitch=-6)
    get_image(main_location1, "r1_" + main_location1 + ".jpg", [33.01062809229904, -117.11012366540932], fov=50,
              heading=270, pitch=0)
    get_image(main_location1, "r1_zoom_" + main_location1 + ".jpg", [33.01062809229904, -117.11012366540932], fov=20,
              heading=265, pitch=-7)
    get_image(main_location1, "r1_zoomzoom_" + main_location1 + ".jpg", [33.01062809229904, -117.11012366540932], fov=0,
              heading=265, pitch=-7)
    get_image(main_location1, "l1_" + main_location1 + ".jpg", [33.01054375324931, -117.11035386198377], fov=80,
              heading=395, pitch=0)
    get_image(main_location1, "l1_zoom_" + main_location1 + ".jpg", [33.01054375324931, -117.11035386198377], fov=40,
              heading=390, pitch=-2)
    get_image(main_location1, "l1_zoomzoom_" + main_location1 + ".jpg", [33.01054375324931, -117.11035386198377],
              fov=15, heading=390, pitch=-3)
    get_image(main_location1, "ll1_" + main_location1 + ".jpg", [33.0104744, -117.1104761], fov=60, heading=395,
              pitch=0)
    get_image(main_location1, "ll1_zoom_" + main_location1 + ".jpg", [33.0104744, -117.110476], fov=35, heading=405,
              pitch=0)
    get_image(main_location1, "ll1_zoomzoom_" + main_location1 + ".jpg", [33.0104744, -117.1104761], fov=0, heading=404,
              pitch=0)
    get_image(main_location1, "c1_" + main_location1 + ".jpg", [33.0105534, -117.1102822], fov=100, heading=342,
              pitch=-6)
    get_image(main_location1, "c1_zoom_" + main_location1 + ".jpg", [33.0105534, -117.1102822], fov=60, heading=342,
              pitch=-6)
    get_image(main_location1, "c1_zoomzoom_" + main_location1 + ".jpg", [33.0105534, -117.1102822], fov=15, heading=343,
              pitch=-13)

    ##### 15720 Paseo Del Sur #################################################
    main_location2 = "loc2"
    # os.mkdir(main_location2)

    get_image(main_location2, "ll2_" + main_location2 + ".jpg", [33.0190283, -117.142136], fov=50, heading=415, pitch=0)
    get_image(main_location2, "ll2_zoom_" + main_location2 + ".jpg", [33.0190283, -117.142136], fov=30, heading=415,
              pitch=-3)
    get_image(main_location2, "ll2_zoomzoom_" + main_location2 + ".jpg", [33.0190283, -117.142136], fov=0, heading=415,
              pitch=-3)
    get_image(main_location2, "l2_" + main_location2 + ".jpg", [33.0190442, -117.1420296], fov=80, heading=40, pitch=0)
    get_image(main_location2, "l2_zoom_" + main_location2 + ".jpg", [33.0190442, -117.1420296], fov=50, heading=400,
              pitch=0)
    get_image(main_location2, "l2_zoomzoom_" + main_location2 + ".jpg", [33.0190442, -117.1420296], fov=0, heading=398,
              pitch=-8)
    get_image(main_location2, "c2_" + main_location2 + ".jpg", [33.019054, -117.141923], fov=120, heading=-10, pitch=0)
    get_image(main_location2, "c2_zoom_" + main_location2 + ".jpg", [33.019054, -117.141923], fov=60, heading=-10,
              pitch=0)
    get_image(main_location2, "c2_zoomzoom_" + main_location2 + ".jpg", [33.019054, -117.141923], fov=0, heading=-17,
              pitch=-10)
    get_image(main_location2, "r2_" + main_location2 + ".jpg", [33.0190595, -117.141817], fov=80, heading=-50,
              pitch=-10)
    get_image(main_location2, "r2_zoom_" + main_location2 + ".jpg", [33.0190595, -117.141817], fov=30, heading=-50,
              pitch=-10)
    get_image(main_location2, "r2_zoomzoom_" + main_location2 + ".jpg", [33.0190595, -117.141817], fov=0, heading=-55,
              pitch=-8)
    get_image(main_location2, "rr2_" + main_location2 + ".jpg", [33.0190687, -117.1417678], fov=80, heading=-50,
              pitch=-10)
    get_image(main_location2, "rr2_zoom_" + main_location2 + ".jpg", [33.0190687, -117.1417678], fov=50, heading=-50,
              pitch=-10)
    get_image(main_location2, "rr2_zoomzoom_" + main_location2 + ".jpg", [33.0190687, -117.1417678], fov=0, heading=-67,
              pitch=-8)

    ##### 10304 Camino Del Sur #################################################
    main_location3 = "loc3"
    # os.mkdir(main_location3)

    get_image(main_location3, "ll3_" + main_location3 + ".jpg", [33.020971, -117.1230685], fov=100, heading=100,
              pitch=-10)
    get_image(main_location3, "ll3_zoom_" + main_location3 + ".jpg", [33.020971, -117.1230685], fov=45, heading=110,
              pitch=-10)
    get_image(main_location3, "ll3_zoomzoom_" + main_location3 + ".jpg", [33.020971, -117.1230685], fov=0, heading=110,
              pitch=-5)
    get_image(main_location3, "l3_" + main_location3 + ".jpg", [33.0209183, -117.1229857], fov=100, heading=100,
              pitch=-10)
    get_image(main_location3, "l3_zoom_" + main_location3 + ".jpg", [33.0209183, -117.1229857], fov=45, heading=110,
              pitch=-10)
    get_image(main_location3, "l3_zoomzoom_" + main_location3 + ".jpg", [33.0209183, -117.1229857], fov=0, heading=95,
              pitch=-9)
    get_image(main_location3, "c3_" + main_location3 + ".jpg", [33.0208643, -117.1229008], fov=120, heading=50,
              pitch=-10)
    get_image(main_location3, "c3_zoom_" + main_location3 + ".jpg", [33.0208643, -117.1229008], fov=70, heading=40,
              pitch=-10)
    get_image(main_location3, "c3_zoomzoom_" + main_location3 + ".jpg", [33.0208643, -117.1229008], fov=20, heading=30,
              pitch=-16)
    get_image(main_location3, "r3_" + main_location3 + ".jpg", [33.0208091, -117.1228138], fov=120, heading=30,
              pitch=-10)
    get_image(main_location3, "r3_zoom_" + main_location3 + ".jpg", [33.0208091, -117.1228138], fov=70, heading=5,
              pitch=-10)
    get_image(main_location3, "r3_zoomzoom_" + main_location3 + ".jpg", [33.0208091, -117.1228138], fov=0, heading=-25,
              pitch=-9)
    get_image(main_location3, "rr3_" + main_location3 + ".jpg", [33.0207544, -117.1227279], fov=100, heading=-25,
              pitch=-10)
    get_image(main_location3, "rr3_zoom_" + main_location3 + ".jpg", [33.0207544, -117.1227279], fov=60, heading=-25,
              pitch=-10)
    get_image(main_location3, "rr3_zoomzoom_" + main_location3 + ".jpg", [33.0207544, -117.1227279], fov=0, heading=-37,
              pitch=-5)

    ##### 10630 Rancho Bernardo Rd #################################################

    main_location4 = "loc4"
    # os.mkdir(main_location4)

    get_image(main_location4, "ll4_" + main_location4 + ".jpg", [33.0200773, -117.1085206], fov=45, heading=70,
              pitch=-10)
    get_image(main_location4, "ll4_zoom_" + main_location4 + ".jpg", [33.0200773, -117.1085206], fov=20, heading=70,
              pitch=-6)
    get_image(main_location4, "ll4_zoomzoom_" + main_location4 + ".jpg", [33.0200773, -117.1085206], fov=0, heading=65,
              pitch=-3)
    get_image(main_location4, "l4_" + main_location4 + ".jpg", [33.0200928, -117.1084148], fov=80, heading=65,
              pitch=-10)
    get_image(main_location4, "l4_zoom_" + main_location4 + ".jpg", [33.0200928, -117.1084148], fov=50, heading=65,
              pitch=-6)
    get_image(main_location4, "l4_zoomzoom_" + main_location4 + ".jpg", [33.0200928, -117.1084148], fov=0, heading=50,
              pitch=-9)
    get_image(main_location4, "c4_" + main_location4 + ".jpg", [33.0201115, -117.1083097], fov=120, heading=0,
              pitch=-10)
    get_image(main_location4, "c4_zoom_" + main_location4 + ".jpg", [33.0201115, -117.1083097], fov=70, heading=-5,
              pitch=-9)
    get_image(main_location4, "c4_zoomzoom_" + main_location4 + ".jpg", [33.0201115, -117.1083097], fov=15, heading=-5,
              pitch=-20)
    get_image(main_location4, "r4_" + main_location4 + ".jpg", [33.0201335, -117.1082048], fov=120, heading=-50,
              pitch=-10)
    get_image(main_location4, "r4_zoom_" + main_location4 + ".jpg", [33.0201335, -117.1082048], fov=70, heading=-50,
              pitch=-9)
    get_image(main_location4, "r4_zoomzoom_" + main_location4 + ".jpg", [33.0201335, -117.1082048], fov=10, heading=-73,
              pitch=-13)
    get_image(main_location4, "rr4_" + main_location4 + ".jpg", [33.0201596, -117.1081009], fov=100, heading=-50,
              pitch=-10)
    get_image(main_location4, "rr4_zoom_" + main_location4 + ".jpg", [33.0201596, -117.1081009], fov=40, heading=-80,
              pitch=-9)
    get_image(main_location4, "rr4_zoomzoom_" + main_location4 + ".jpg", [33.0201596, -117.1081009], fov=0, heading=-90,
              pitch=-6)

    ##### 10630 Rancho Bernardo Rd #################################################

    main_location5 = "loc5"
    # os.mkdir(main_location5)

    get_image(main_location5, "ll5_" + main_location5 + ".jpg", [33.0200928, -117.1084148], fov=80, heading=70,
              pitch=-10)
    get_image(main_location5, "ll5_zoom_" + main_location5 + ".jpg", [33.0200928, -117.1084148], fov=45, heading=70,
              pitch=-10)
    get_image(main_location5, "ll5_zoomzoom_" + main_location5 + ".jpg", [33.0200928, -117.1084148], fov=0, heading=60,
              pitch=-3)
    get_image(main_location5, "l5_" + main_location5 + ".jpg", [33.0201115, -117.1083097], fov=120, heading=70,
              pitch=-10)
    get_image(main_location5, "l5_zoom_" + main_location5 + ".jpg", [33.0201115, -117.1083097], fov=45, heading=50,
              pitch=-10)
    get_image(main_location5, "l5_zoomzoom_" + main_location5 + ".jpg", [33.0201115, -117.1083097], fov=11, heading=45,
              pitch=-8)
    get_image(main_location5, "c5_" + main_location5 + ".jpg", [33.0201335, -117.1082048], fov=100, heading=-15,
              pitch=-10)
    get_image(main_location5, "c5_zoom_" + main_location5 + ".jpg", [33.0201335, -117.1082048], fov=80, heading=-15,
              pitch=-10)
    get_image(main_location5, "c5_zoomzoom_" + main_location5 + ".jpg", [33.0201335, -117.1082048], fov=20, heading=-17,
              pitch=-18)
    get_image(main_location5, "r5_" + main_location5 + ".jpg", [33.0201596, -117.108100], fov=120, heading=-50,
              pitch=-10)
    get_image(main_location5, "r5_zoom_" + main_location5 + ".jpg", [33.0201596, -117.108100], fov=80, heading=-60,
              pitch=-10)
    get_image(main_location5, "r5_zoomzoom_" + main_location5 + ".jpg", [33.0201596, -117.108100], fov=10, heading=-77,
              pitch=-10)
    get_image(main_location5, "rr5_" + main_location5 + ".jpg", [33.0201894, -117.1079984], fov=110, heading=-70,
              pitch=-10)
    get_image(main_location5, "rr5_zoom_" + main_location5 + ".jpg", [33.0201894, -117.1079984], fov=50, heading=-85,
              pitch=-10)
    get_image(main_location5, "rr5_zoomzoom_" + main_location5 + ".jpg", [33.0201894, -117.1079984], fov=10,
              heading=-92, pitch=-6)

    ##### 5174 Bellvale Ave #################################################

    main_location6 = "loc6"
    # os.mkdir(main_location6)

    get_image(main_location6, "ll6_" + main_location6 + ".jpg", [32.8272602, -117.1789547], fov=120, heading=70,
              pitch=0)
    get_image(main_location6, "ll6_zoom_" + main_location6 + ".jpg", [32.8272602, -117.1789547], fov=60, heading=90,
              pitch=6)
    get_image(main_location6, "ll6_zoomzoom_" + main_location6 + ".jpg", [32.8272602, -117.1789547], fov=40, heading=90,
              pitch=6)
    get_image(main_location6, "l6_" + main_location6 + ".jpg", [32.827252, -117.1788497], fov=120, heading=70, pitch=0)
    get_image(main_location6, "l6_zoom_" + main_location6 + ".jpg", [32.827252, -117.1788497], fov=80, heading=90,
              pitch=5)
    get_image(main_location6, "l6_zoomzoom_" + main_location6 + ".jpg", [32.827252, -117.1788497], fov=59, heading=90,
              pitch=10)
    get_image(main_location6, "c6_" + main_location6 + ".jpg", [32.8272303, -117.17875], fov=120, heading=70, pitch=10)
    get_image(main_location6, "c6_zoom_" + main_location6 + ".jpg", [32.8272303, -117.17875], fov=100, heading=60,
              pitch=15)
    get_image(main_location6, "c6_zoomzoom_" + main_location6 + ".jpg", [32.8272303, -117.17875], fov=95, heading=60,
              pitch=16)
    get_image(main_location6, "r6_" + main_location6 + ".jpg", [32.8271913, -117.1786577], fov=120, heading=-10,
              pitch=10)
    get_image(main_location6, "r6_zoom_" + main_location6 + ".jpg", [32.8271913, -117.1786577], fov=100, heading=-10,
              pitch=15)
    get_image(main_location6, "r6_zoomzoom_" + main_location6 + ".jpg", [32.8271913, -117.1786577], fov=85, heading=-10,
              pitch=15)
    get_image(main_location6, "rr6_" + main_location6 + ".jpg", [32.8271427, -117.1785778], fov=120, heading=-10,
              pitch=10)
    get_image(main_location6, "rr6_zoom_" + main_location6 + ".jpg", [32.8271427, -117.1785778], fov=80, heading=-30,
              pitch=15)
    get_image(main_location6, "rr6_zoomzoom_" + main_location6 + ".jpg", [32.8271427, -117.1785778], fov=54,
              heading=-30, pitch=11)

    ##### 5320 Vergara St #################################################
    main_location7 = "loc7"
    # os.mkdir(main_location7)

    get_image(main_location7, "ll7_" + main_location7 + ".jpg", [32.827949, -117.1768318], fov=120, heading=300,
              pitch=0)
    get_image(main_location7, "ll7_zoom_" + main_location7 + ".jpg", [32.827949, -117.1768318], fov=60, heading=270,
              pitch=6)
    get_image(main_location7, "ll7_zoomzoom_" + main_location7 + ".jpg", [32.827949, -117.1768318], fov=43, heading=265,
              pitch=8)
    get_image(main_location7, "l7_" + main_location7 + ".jpg", [32.8279585, -117.1769407], fov=120, heading=270,
              pitch=0)
    get_image(main_location7, "l7_zoom_" + main_location7 + ".jpg", [32.8279585, -117.1769407], fov=80, heading=270,
              pitch=10)
    get_image(main_location7, "l7_zoomzoom_" + main_location7 + ".jpg", [32.8279585, -117.1769407], fov=69, heading=267,
              pitch=13)
    get_image(main_location7, "c7_" + main_location7 + ".jpg", [32.8279769, -117.1770463], fov=120, heading=210,
              pitch=15)
    get_image(main_location7, "c7_zoom_" + main_location7 + ".jpg", [32.8279769, -117.1770463], fov=90, heading=210,
              pitch=10)
    get_image(main_location7, "c7_zoomzoom_" + main_location7 + ".jpg", [32.8279769, -117.1770463], fov=69, heading=210,
              pitch=7)
    get_image(main_location7, "r7_" + main_location7 + ".jpg", [32.8280081, -117.177142], fov=120, heading=145,
              pitch=15)
    get_image(main_location7, "r7_zoom_" + main_location7 + ".jpg", [32.8280081, -117.177142], fov=90, heading=145,
              pitch=10)
    get_image(main_location7, "r7_zoomzoom_" + main_location7 + ".jpg", [32.8280081, -117.177142], fov=75, heading=143,
              pitch=14)
    get_image(main_location7, "rr7_" + main_location7 + ".jpg", [32.8280519, -117.1772334], fov=120, heading=145,
              pitch=15)
    get_image(main_location7, "rr7_zoom_" + main_location7 + ".jpg", [32.8280519, -117.1772334], fov=90, heading=145,
              pitch=10)
    get_image(main_location7, "rr7_zoomzoom_" + main_location7 + ".jpg", [32.8280519, -117.1772334], fov=50,
              heading=130, pitch=9)


if __name__ == "__main__":
    create_images()