import Vue from 'vue';
import Vuex from 'vuex';
import { getNearbyPlaces, getPriceHistory } from '@/api';

Vue.use(Vuex);

const QUERY_DEFAULT_SEARCH_DISTANCE = 1000;
const QUERY_DEFAULT_NEED_WALKING_DISTANCE = true;
const QUERIES = {
  types: [
    {
      name: 'school',
      keyword: 'school',
    },
    {
      name: 'mall',
      keyword: 'mall',
    },
    {
      name: 'mrt',
      keyword: 'mrt',
    },
    {
      name: 'bus stop',
      keyword: 'bus stop',
    },
  ],
};

const store = new Vuex.Store({
  state: {
    user_input_address: '',
    user_input_address_loc: { lat: 1.3521, lng: 103.8198 },
    near_by_places: [],
    map_markers: [],
    selected_type: '',
    page_loading: false,
    page_content_loaded: false,
    price: 1000000,
    price_history: [],
  },
  getters: {
    getUserInputAddress: state => state.user_input_address,
    getUserInputAddressLoc: state => state.user_input_address_loc,
    getNearbyPlaces: state => state.near_by_places,
    getMapMarkers: state => state.map_markers,
    getPageLoading: state => state.page_loading,
    getPageContentLoaded: state => state.page_content_loaded,
    getPrice: state => state.price,
    getPriceHistory: state => state.price_history,
  },
  mutations: {
    EDIT_USER_INPUT_ADDRESS: (state, addr) => {
      state.user_input_address = addr;
    },
    EDIT_USER_INPUT_ADDRESS_LOC: (state, loc) => {
      state.user_input_address_loc = loc;
    },
    SET_NEARBY_PLACES: (state, places) => {
      state.near_by_places = places;
    },
    SET_MAP_MARKERS: (state, markers) => {
      state.map_markers = markers;
    },
    SET_PAGE_LOADING: (state, bool) => {
      state.page_loading = bool;
    },
    SET_PAGE_CONTENT_LOADED: (state, bool) => {
      state.page_content_loaded = bool;
    },
    RESET_USER_INPUT_ADDRESS: (state) => {
      state.user_input_address = '';
    },
    SET_PRICE_HISTORY: (state, priceHistory) => {
      state.price_history = priceHistory;
    },
  },
  actions: {
    requestNearbyPlaces({ commit }, { loc }) {
      const query = JSON.parse(JSON.stringify(QUERIES));
      query.location = JSON.parse(loc);
      query.radius = QUERY_DEFAULT_SEARCH_DISTANCE;
      query.need_distance = QUERY_DEFAULT_NEED_WALKING_DISTANCE;
      return new Promise((resolve, reject) => {
        getNearbyPlaces(query).then((result) => {
          const places = [];
          const resultObj = JSON.parse(result.body);
          resultObj.forEach((resultByType) => {
            resultByType.places.forEach((e) => {
              e.type = resultByType.type;
            });
            places.push(...resultByType.places);
          });
          commit('SET_NEARBY_PLACES', places);
          resolve();
        }).catch(error => reject(error));
      });
    },
    requestPriceHistory({ commit }, { street, block, flatType }) {
      const query = {};
      query.street = street;
      query.blk = block;
      query.flat_type = flatType;
      return new Promise((resolve, reject) => {
        getPriceHistory(query).then((result) => {
          const resultObj = JSON.parse(result.body);
          const priceHistory = [];
          resultObj.forEach((record) => {
            const priceRecord = {};
            priceRecord.date = record[0];
            priceRecord.price = record[1];
            priceHistory.push(priceRecord);
          });
          commit('SET_PRICE_HISTORY', priceHistory);
          resolve();
        }).catch((error) => {
          commit('SET_PRICE_HISTORY', []);
          reject(error);
        });
      });
    },
  },
});

export default store;
