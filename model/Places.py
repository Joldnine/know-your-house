import googlemaps

class Places(object):

   def __init__(self, key):
       self.key = key
       self.client = googlemaps.Client(self.key)
       self.type = 'liquor_store'
       self.language = 'en-AU'

   def get_geocode(self, street, city):
       place = '{}, {}'.format(street, city)
       return self.client.geocode(place)[0]['geometry']['location']

   def get_nearby_place_geocode(self, location, place_type, qty):
       places = self.client.places_nearby(location, rank_by='distance', type=place_type)['results']
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

   def mrt_dist(self,locate):
      street_location = self.get_geocode(locate, 'Singapore')
      nearby_mrt = self.get_nearby_place_geocode(street_location, 'subway_station', 1)
      return self.get_directions(street_location, nearby_mrt[0]['location'], 'walking')['distance']['text']