import googlemaps
import json

# Event example:
# {
# 	"location": {
# 		"lat": 1.3040632,
# 		"lng": 103.7804663
# 	},
# 	"radius": 1000,
# 	"types": [{
# 		"name":"mall",
# 		"keyword": "mall"
# 	}],
# 	"need_distance": true  # optional
# }

def post(event, context):
    # event = json.loads(event['body'])  # comment this line if it is in aws lambda
    location = Location()
    response_body = []
    need_distance = False
    if 'need_distance' in event:
        need_distance = event['need_distance']
    print(event['types'])
    for loc_type in event['types']:
        response_body.append({
            'type': loc_type['name'],
            'places': location.get_nearby(event['location'], loc_type, event['radius'], need_distance)
        })
    return {"body": json.dumps(response_body), "statusCode": 200}


class Location(object):
    def __init__(self):
        self.key = 'AIzaSyBtoWfKhyiLdLrv_6VfkvTyNi0lzEWofRU'
        self.client = googlemaps.Client(self.key)
        self.language = 'en-SG'
        self.region = 'SG'

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
