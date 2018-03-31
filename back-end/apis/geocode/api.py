import googlemaps
import json

# Event example:
# {
#   "address": "5 Dover Crescent",
# }


def post(event, context):
    event = json.loads(event['body'])  # comment this line if it is in aws
    city = 'Singpore'

    google_api = GoogleApi()
    if 'google_key' in event:
        google_api = GoogleApi(event['google_key'])
    geocode = google_api.geocode(event['address'], city)

    return {"body": json.dumps(geocode), "statusCode": 200}


class GoogleApi(object):
    def __init__(self, key='AIzaSyBtoWfKhyiLdLrv_6VfkvTyNi0lzEWofRU', region='SG'):
        self.key = key
        self.client = googlemaps.Client(self.key)
        self.language = 'en-SG'
        self.region = region

    def geocode(self, addr, city):
        addr = addr + ', ' + city
        return self.client.geocode(addr)[0]['geometry']['location']
