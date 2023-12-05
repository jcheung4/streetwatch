import os
import requests


API_KEY = os.getenv('API_KEY')

CONFIG = {
    'api_key': API_KEY,
    'image_size': '640x480',
    'data': {

        #UG
        #D160649
        "32.7773283,-117.1547448": [
            {'heading': 250.79, 'fov': 90, 'pitch': -27.43},
            {'heading': 248.1, 'fov': 35.9, 'pitch': -18.73},
            {'heading': 246.7, 'fov': 15, 'pitch': -15}
        ],
        "32.7772356,-117.1547079": [
            {'heading': 308.28, 'fov': 75, 'pitch': -16.27},
            {'heading': 309.96, 'fov': 25.1, 'pitch': -8.99},
            {'heading': 310.4, 'fov': 15, 'pitch': -8.14}
        ],
        "32.7771481,-117.1546743": [
            {'heading': 320.97, 'fov': 75, 'pitch': -7.25},
            {'heading': 324.18, 'fov': 26.7, 'pitch': -3.84},
            {'heading': 325.04, 'fov': 15, 'pitch': -3.34}
        ],
        "32.7774246,-117.1547794": [
            {'heading': 191.37, 'fov': 75, 'pitch': -12.02},
            {'heading': 191.37, 'fov': 43.8, 'pitch': -9.5},
            {'heading': 193.28, 'fov': 15, 'pitch': -8.71}
        ],
        "32.7775246,-117.1548136": [
            {'heading': 179.99, 'fov': 75, 'pitch': -7.82},
            {'heading': 179.99, 'fov': 35.6, 'pitch': -6.47},
            {'heading': 180.37, 'fov': 15, 'pitch': -5.9}
        ],

        #D201872
        "32.7734596,-117.1536334": [
            {'heading': 187.78, 'fov': 90, 'pitch': -13.2},
            {'heading': 185.37, 'fov': 53.7, 'pitch': -10.63},
            {'heading': 181.05, 'fov': 15, 'pitch': -5}
        ],
        "32.7734088,-117.1535186": [
            {'heading': 241.64, 'fov': 90, 'pitch': -17.69},
            {'heading': 245.28, 'fov': 37, 'pitch': -12.4},
            {'heading': 245.03, 'fov': 15, 'pitch': -11.75}
        ],
        "32.7734171,-117.1534753": [
            {'heading': 246.26, 'fov': 75, 'pitch': -14.9},
            {'heading': 247.83, 'fov': 37.2, 'pitch': -11.95},
            {'heading': 248, 'fov': 15, 'pitch': -8.59}
        ],
        "32.7734877,-117.1537424": [
            {'heading': 146.77, 'fov': 75, 'pitch': -11.26},
            {'heading': 144.14, 'fov': 23.7, 'pitch': -2.75},
            {'heading': 143.34, 'fov': 15, 'pitch': -2.17}
        ],
        "32.773518,-117.1538419": [
            {'heading': 134.25, 'fov': 75, 'pitch': -4.97},
            {'heading': 132.06, 'fov': 41.2, 'pitch': -3.28},
            {'heading': 131.5, 'fov': 15, 'pitch': -2.85}
        ],

        #D213913
        "32.773109,-117.1580629": [
            {'heading': 235.98, 'fov': 90, 'pitch': -22.79},
            {'heading': 238.19, 'fov': 51.2, 'pitch': -15.72},
            {'heading': 238.53, 'fov': 15, 'pitch': -14.8}
        ],
        "32.7730452,-117.1579819": [
            {'heading': 283.02, 'fov': 75, 'pitch': -12.46},
            {'heading': 283.81, 'fov': 34.6, 'pitch': -7.63},
            {'heading': 284.71, 'fov': 15, 'pitch': -7.33}
        ],
        "32.7729819,-117.1579022": [
            {'heading': 293.85, 'fov': 75, 'pitch': -3.4},
            {'heading': 296.04, 'fov': 18.3, 'pitch': -4.02},
            {'heading': 295.95, 'fov': 15, 'pitch': -3.94}
        ],
        "32.7731748,-117.1581475": [
            {'heading': 169.32, 'fov': 75, 'pitch': -14.03},
            {'heading': 168.02, 'fov': 45, 'pitch': -10.43},
            {'heading': 168.02, 'fov': 15, 'pitch': -10.43}
        ],
        "32.7732373,-117.1582435": [
            {'heading': 143.91, 'fov': 75, 'pitch': -7.2},
            {'heading': 147.54, 'fov': 37.5, 'pitch': -7.65},
            {'heading': 147.5, 'fov': 15, 'pitch': -5.25}
        ],

        #D218174
        "32.7802224,-117.1417077": [
            {'heading': 336.77, 'fov': 90, 'pitch': -13.38},
            {'heading': 336.77, 'fov': 45, 'pitch': -13.38},
            {'heading': 336.77, 'fov': 15, 'pitch': -13.38}
        ],
        "32.7802017,-117.1418202": [
            {'heading': 036.93, 'fov': 75, 'pitch': -16.05},
            {'heading': 034.55, 'fov': 45, 'pitch': -7.15},
            {'heading': 033.98, 'fov': 15, 'pitch': -6.44}
        ],
        "32.7802507,-117.1415978": [
            {'heading': 291.38, 'fov': 75, 'pitch': -21.08},
            {'heading': 290.40, 'fov': 37.5, 'pitch': -11.06},
            {'heading': 289.63, 'fov': 15, 'pitch': -9.8}
        ],
        "32.7802804,-117.1415552": [
            {'heading': 274.06, 'fov': 75, 'pitch': -18.09},
            {'heading': 277.33, 'fov': 37.5, 'pitch': -9.65},
            {'heading': 276.65, 'fov': 15, 'pitch': -6.92}
        ],
        "32.780178,-117.1419289": [
            {'heading': 050.45, 'fov': 75, 'pitch': -2.73},
            {'heading': 051.05, 'fov': 37.5, 'pitch': -0.75},
            {'heading': 053.18, 'fov': 15, 'pitch': -2.53}
        ],

        #D2189071148
        "32.7650874,-117.1884345": [
            {'heading': 161.34, 'fov': 90, 'pitch': -27.61},
            {'heading': 158.34, 'fov': 45, 'pitch': -15.67},
            {'heading': 157.22, 'fov': 15, 'pitch': -11.68}
        ],
        "32.7651237,-117.1883235": [
            {'heading': 217.61, 'fov': 75, 'pitch': -11.29},
            {'heading': 220.9, 'fov': 37.5, 'pitch': -7.09},
            {'heading': 221.09, 'fov': 15, 'pitch': -5.17}
        ],
        "32.7651582,-117.1882132": [
            {'heading': 228, 'fov': 75, 'pitch': -7},
            {'heading': 234.39, 'fov': 37.5, 'pitch': -2.12},
            {'heading': 234.39, 'fov': 15, 'pitch': -3.11}
        ],
        "32.7650513,-117.1885453": [
            {'heading': 130.76, 'fov': 90, 'pitch': -10.63},
            {'heading': 165, 'fov': 75, 'pitch': -3.54},
            {'heading': 160, 'fov': 35, 'pitch': -6.05}
        ],
        "32.7650142,-117.1886527": [
            {'heading': 084.42, 'fov': 75, 'pitch': -8.72},
            {'heading': 083.32, 'fov': 37.5, 'pitch': -6.65},
            {'heading': 084.09, 'fov': 15, 'pitch': -2.34}
        ],

        #OH
        #P36971
        "32.787746,-117.1007104": [
            {'heading': 181.69, 'fov': 75, 'pitch': 9.4},
            {'heading': 194.16, 'fov': 51.1, 'pitch': 12.75},
            {'heading': 200.94, 'fov': 23.4, 'pitch': 11.69}
        ],
        "32.7877453,-117.1006029": [
            {'heading': 232.46, 'fov': 75, 'pitch': 0},
            {'heading': 232.68, 'fov': 41.8, 'pitch': 4.72},
            {'heading': 230.88, 'fov': 15, 'pitch': 2.07}
        ],
        "32.7877454,-117.1004955": [
            {'heading': 239.98, 'fov': 75, 'pitch': -3.3},
            {'heading': 241.66, 'fov': 44.9, 'pitch': -2},
            {'heading': 245.08, 'fov': 19.2, 'pitch': 5.54}
        ],
        "32.7877422,-117.1008124": [
            {'heading': 152.88, 'fov': 75, 'pitch': -0.71},
            {'heading': 155.66, 'fov': 30.9, 'pitch': -0.55},
            {'heading': 155.33, 'fov': 15, 'pitch': 23.87}
        ],
        "32.7877429,-117.1009196": [
            {'heading': 127.09, 'fov': 75, 'pitch': 2.82},
            {'heading': 126.11, 'fov': 49, 'pitch': 1.98},
            {'heading': 122.5, 'fov': 15, 'pitch': 0.64}
        ],

        #P836364
        "32.7902254,-117.1430592": [
            {'heading': 010.08, 'fov': 75, 'pitch': 16.34},
            {'heading': 009.02, 'fov': 44.4, 'pitch': 2.09},
            {'heading': 010.65, 'fov': 18, 'pitch': -11.4}
        ],
        "32.7901808,-117.1431531": [
            {'heading': 044.26, 'fov': 75, 'pitch': 1.2},
            {'heading': 045.35, 'fov': 46.1, 'pitch': 4.11},
            {'heading': 43.12, 'fov': 22.7, 'pitch': 6.72}
        ],
        "32.7901389,-117.1432495": [
            {'heading': 061.32, 'fov': 75, 'pitch': 0.73},
            {'heading': 062.38, 'fov': 47, 'pitch': -0.27},
            {'heading': 062.43, 'fov': 20.7, 'pitch': 3.42}
        ],
        "32.7903205,-117.1428712": [
            {'heading': 255.44, 'fov': 75, 'pitch': 1.17},
            {'heading': 248.76, 'fov': 47.8, 'pitch': 11.1},
            {'heading': 252.12, 'fov': 15, 'pitch': 6.39}
        ],
        "32.7903672,-117.1427762": [
            {'heading': 241.37, 'fov': 75, 'pitch': -0.72},
            {'heading': 239.36, 'fov': 49.2, 'pitch': 0.23},
            {'heading': 245.76, 'fov': 15, 'pitch': 2.2}
        ],

        #P105329
        "32.7594006,-117.1437984": [
            {'heading': 058.95, 'fov': 90, 'pitch': 20.08},
            {'heading': 059.48, 'fov': 57.4, 'pitch': 2.24},
            {'heading': 062.27, 'fov': 27.1, 'pitch': -10.34}
        ],
        "32.7595871,-117.1437925": [
            {'heading': 170.91, 'fov': 75, 'pitch': 2.78},
            {'heading': 175.21, 'fov': 46.9, 'pitch': 10.52},
            {'heading': 169.73, 'fov': 21.4, 'pitch': 1.39}
        ],
        "32.7596807,-117.1437867": [
            {'heading': 178.11, 'fov': 75, 'pitch': -1.35},
            {'heading': 182.67, 'fov': 29.9, 'pitch': 6.38},
            {'heading': 178.47, 'fov': 15, 'pitch': 4.67}
        ],
        "32.7593048,-117.1437995": [
            {'heading': 010.95, 'fov': 75, 'pitch': 11.13},
            {'heading': 010.99, 'fov': 50.4, 'pitch': 10.77},
            {'heading': 020.61, 'fov': 15, 'pitch': -2.11}
        ],
        "32.7591631,-117.1437546": [
            {'heading': 355.99, 'fov': 75, 'pitch': -1.69},
            {'heading': 355.41, 'fov': 61.3, 'pitch': 2.39},
            {'heading': 352.44, 'fov': 36.4, 'pitch': 9.54}
        ],

        #P105393
        "32.7610023,-117.1419846": [
            {'heading': 182.73, 'fov': 90, 'pitch': 0.68},
            {'heading': 178, 'fov': 54.7, 'pitch': 7.38},
            {'heading': 176.06, 'fov': 28.6, 'pitch': 15.27}
        ],
        "32.761002,-117.1417713": [
            {'heading': 231.58, 'fov': 75, 'pitch': 1.92},
            {'heading': 232.23, 'fov': 50.5, 'pitch': 4.13},
            {'heading': 232.97, 'fov': 26.1, 'pitch': 8.43}
        ],
        "32.7610105,-117.1416738": [
            {'heading': 245.15, 'fov': 75, 'pitch': -3.32},
            {'heading': 242.79, 'fov': 26.3, 'pitch': 2.11},
            {'heading': 242.52, 'fov': 15, 'pitch': -1.35}
        ],
        "32.7610023,-117.1420919": [
            {'heading': 135.34, 'fov': 75, 'pitch': 0.93},
            {'heading': 139.85, 'fov': 45.5, 'pitch': 8.08},
            {'heading': 143.14, 'fov': 19, 'pitch': 3.5}
        ],
        "32.7609697,-117.1425536": [
            {'heading': 099.61, 'fov': 80.3, 'pitch': 0},
            {'heading': 101.96, 'fov': 51.1, 'pitch': -0.92},
            {'heading': 104.5, 'fov': 15, 'pitch': 3.82}
        ],

        #P105392
        "32.7609688,-117.1426076": [
            {'heading': 119.53, 'fov': 75, 'pitch': 4.42},
            {'heading': 110.29, 'fov': 42.2, 'pitch': 6.38},
            {'heading': 110.08, 'fov': 18, 'pitch': 2.2}
        ],
        "32.7609671,-117.1427161": [
            {'heading': 092.72, 'fov': 75, 'pitch': -5.63},
            {'heading': 097.59, 'fov': 43.1, 'pitch': -2.3},
            {'heading': 100.98, 'fov': 15, 'pitch': -1}
        ],
        "32.7609657,-117.1428259": [
            {'heading': 090.0, 'fov': 75, 'pitch': -0.89},
            {'heading': 093.5, 'fov': 42.1, 'pitch': 0.06},
            {'heading': 097.64, 'fov': 15, 'pitch': 2.49}
        ],
        "32.7610023,-117.1420919": [
            {'heading': 242.3, 'fov': 90, 'pitch': -0.68},
            {'heading': 246.02, 'fov': 53.8, 'pitch': 0},
            {'heading': 247.39, 'fov': 27.5, 'pitch': 2.8}
        ],
        "32.7610023,-117.1419846": [
            {'heading': 254.7, 'fov': 75, 'pitch': -3.43},
            {'heading': 252.88, 'fov': 45.1, 'pitch': 4.89},
            {'heading': 253.37, 'fov': 15, 'pitch': 4.24}
        ]                       
    }
}


def save_image(content, image_counter, image_dir):
    with open(f'{image_dir}streetview_image_{image_counter}.jpg', 'wb') as f:
        f.write(content)
    print(f'Image {image_counter} saved as streetview_image_{image_counter}.jpg')


def fetch_streetview_images(data, api_key, image_dir, image_size='640x480'):
    image_counter = 0

    for location, image_parameters in data.items():
        for params in image_parameters:
            params['location'] = location
            params['size'] = image_size
            params['key'] = api_key

            url = 'https://maps.googleapis.com/maps/api/streetview'
            response = requests.get(url, params=params)

            if response.status_code == 200:
                save_image(response.content, image_counter, image_dir)
            else:
                print(f'Failed to retrieve image {image_counter}. Status code:', response.status_code)
                print(response.text)

            image_counter += 1


def main(image_dir):
    fetch_streetview_images(image_dir=image_dir, **CONFIG)
