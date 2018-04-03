const API_NEARBY_SEARCH = 'https://1nrw5aj4h1.execute-api.ap-southeast-1.amazonaws.com/develop/';
const API_GEOCODE = 'https://spk60bp336.execute-api.ap-southeast-1.amazonaws.com/develop/';
const API_PRICE_PREDICTION = 'https://d4elvu6k04.execute-api.ap-southeast-1.amazonaws.com/develop/';
const API_PRICE_HISTORY = 'https://gaa2oz491g.execute-api.ap-southeast-1.amazonaws.com/develop/';

/**
 * @param {Object} query
 */
export function getNearbyPlaces(query) {
  return fetch(API_NEARBY_SEARCH, {
    method: 'POST',
    body: JSON.stringify(query),
  }).then(response => response.json());
}

/**
 * @param {String} address
 */
export function getGeocode(address) {
  return fetch(API_GEOCODE, {
    method: 'POST',
    body: JSON.stringify({
      address,
    }),
  }).then(response => response.json());
}

/**
 * @param {Object} query
 */
export function getPricePrediction(query) {
  return fetch(API_PRICE_PREDICTION, {
    method: 'POST',
    body: JSON.stringify(query),
  }).then(response => response.json());
}

/**
 * @param {Object} query
 */
export function getPriceHistory(query) {
  return fetch(API_PRICE_HISTORY, {
    method: 'POST',
    body: JSON.stringify(query),
  }).then(response => response.json());
}
