const API_NEARBY_SEARCH = 'https://1nrw5aj4h1.execute-api.ap-southeast-1.amazonaws.com/develop/';

/**
 * @param {Object} query
 */
export function getNearbyPlaces(query) {
  return fetch(API_NEARBY_SEARCH, {
    method: 'POST',
    body: JSON.stringify(query),
  }).then(response => response.json());
}

export function getNearByPlacesv2() {
  return null;
}
