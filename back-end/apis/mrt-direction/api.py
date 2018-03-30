import googlemaps
import json

# Event example:
# {
#   "street": ["5 Dover Crescent"]
#   ""
# }


def post(event, context):
    event = json.loads(event['body'])  # comment this line if it is in aws lambda
    response_body = []
    loc_type, keyword = 'mrt'
    for street in event['street']:
        street_location = Places().get_geocode(street, 'Singapore')
        nearby_mrt = Places().get_nearby_place_geocode(street_location, loc_type, keyword, 1)
        direction_walking_nearest_mrt = Places().get_directions(street_location, nearby_mrt[0]['location'], 'walking')
        response_body.append({
            'original': {
                'street': street,
                'location': street_location
            },
            'nearest_mrt': nearby_mrt[0],
            'direction': direction_walking_nearest_mrt
        })
    return {"body": json.dumps(response_body), "statusCode": 200}


class Places(object):

    def __init__(self):
        self.key = 'AIzaSyBtoWfKhyiLdLrv_6VfkvTyNi0lzEWofRU'
        self.client = googlemaps.Client(self.key)

    def get_geocode(self, street, city):
        place = '{}, {}'.format(street, city)
        return self.client.geocode(place)[0]['geometry']['location']

    def get_nearby_place_geocode(self, location, loc_type, keyword, qty):
        places = self.client.places_nearby(location, rank_by='distance', type=loc_type, keyword=keyword)['results']
        count = 0
        total_qty = len(places)
        results = []
        for place in places:
            count += 1
            if count > total_qty or count > qty:
                break
            results.append({
                'location': place['geometry']['location'],
                'name': place['name'],
                'place_id': place['place_id']
            })
        return results

    def get_directions(self, original, desc, mode):
        direction = self.client.directions(original, desc, mode=mode)[0]['legs'][0]
        return {
            'distance': direction['distance'],
            'duration': direction['duration']
        }
