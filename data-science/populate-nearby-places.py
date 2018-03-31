import googlemaps
import json


class GoogleApi(object):
    def __init__(self, key='AIzaSyDX_p3RqFd88q9nHHzg3AkmDvuSUJ8McSs'):
        self.key = key
        self.client = googlemaps.Client(self.key, connect_timeout=5, read_timeout=5)
        self.language = 'en-SG'
        self.region = 'SG'

    def get_geocode(self, addr, city):
        if 'C\'' in addr:
            addr = addr.replace('C\'', 'Common ')
        place = '{}, {}'.format(addr, city)
        return self.client.geocode(place)[0]['geometry']['location']

    def get_nearby(self, location, loc_type, radius, need_distance):
        type_name = loc_type['name']
        keyword = loc_type['keyword']
        places = self.client.places_nearby(location, keyword=keyword, type=type_name, radius=radius,
                                           language=self.language)['results']
        if need_distance:  # if need distance, get the distance
            for place in places:
                direction = self.get_directions(location, place['geometry']['location'], 'walking')
                place['direction'] = {
                    'distance': direction['distance'],
                    'duration': direction['duration']
                }
        results = []
        for place in places:
            result = {
                'name': place['name'],
                'location': place['geometry']['location']
            }
            if need_distance:
                result['direction'] = place['direction']
            results.append(result)
        return results

    def get_directions(self, original, desc, mode):
        direction = self.client.directions(original, desc, mode=mode)[0]['legs'][0]
        return {
            'distance': direction['distance'],
            'duration': direction['duration']
        }

GOOGLE_API = GoogleApi()


def post(event):
    """
    :param event: request contents
    :type event: dict
        example:
        {
            "location": {
                "lat": 1.3040632,
                "lng": 103.7804663
            },
            "radius": 1000,
            "types": [{
                "name":"mall",
                "keyword": "mall"
            }],
            "need_distance": true  # optional
            "google_key": "gfweygfawyegfawyfg"  # optional
        }
    """
    response_body = []
    need_distance = False

    if 'need_distance' in event:
        need_distance = event['need_distance']

    for loc_type in event['types']:
        response_body.append({
            'type': loc_type['name'],
            'places': GOOGLE_API.get_nearby(event['location'], loc_type, event['radius'], need_distance)
        })
    return response_body


def count_type_places(result, type_name):
    for type_places in result:
        if type_places['type'] == type_name:
            return len(type_places['places'])
    return 0


def get_place_type_num(loc):
    city = 'Singapore'
    result = post({
        "location": GOOGLE_API.get_geocode(loc, city),
        "radius": 1000,
        "types": [{
                "name": "mall",
                "keyword": "mall"
            },
            {
                "name": "school",
                "keyword": "school"
            },
            {
                "name": "bus stop",
                "keyword": "bus stop"
            },
            {
                "name": "mrt",
                "keyword": "mrt"
            },
        ]
    })
    return {
        "address": loc,
        "num_mall": count_type_places(result, 'mall'),
        "num_school": count_type_places(result, 'school'),
        "num_bus_stop": count_type_places(result, 'bus stop'),
        "num_mrt": count_type_places(result, 'mrt'),
    }

if __name__ == '__main__':
    # with open('data/addresses.txt', 'r') as file:
    #     addr_list = json.loads(file.read())
    # result_list = []
    # for addr in addr_list:
    #     result_list.append({
    #         "address": addr,
    #         "num_mall": '',
    #         "num_school": '',
    #         "num_bus_stop": '',
    #         "num_mrt": ''
    #     })
    # with open('data/address_type_num.json', 'w') as outfile:
    #     json.dump(result_list, outfile, indent=4)

    with open('data/address_type_num.json', 'r') as file:
        result_list = json.load(file)
        file.close()
    try:
        for item in result_list[200:]:
            if not item['num_mall'] and item['num_mall'] != 0:
                print('Fetch:' + item['address'])
                item_with_num = get_place_type_num(item['address'])
                for key in item:
                    item[key] = item_with_num[key]
    except Exception as e:
        print(e)
        with open('data/address_type_num.json', 'w') as outfile:
            json.dump(result_list, outfile, indent=4)
            file.close()

    with open('data/address_type_num.json', 'w') as outfile:
        json.dump(result_list, outfile, indent=4)
        file.close()


