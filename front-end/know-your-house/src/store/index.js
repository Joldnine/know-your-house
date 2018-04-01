import Vue from 'vue';
import Vuex from 'vuex';
import { getNearbyPlaces } from '@/api';

Vue.use(Vuex);

const QUERY_DEFAULT_SEARCH_DISTANCE = 1000;
const QUERY_DEFAULT_NEED_WALKING_DISTANCE = true;
const QUERIES = {
  schools: {
    types: [
      {
        name: 'school',
        keyword: 'school',
      },
    ],
  },
  malls: {
    types: [
      {
        name: 'mall',
        keyword: 'mall',
      },
    ],
  },
  mrt: {
    types: [
      {
        name: 'mrt',
        keyword: 'mrt',
      },
    ],
  },
  busStop: {
    types: [
      {
        name: 'bus stop',
        keyword: 'bus stop',
      },
    ],
  },
};

const store = new Vuex.Store({
  state: {
    user_input_address: '',
    user_input_address_loc: { lat: 1.3521, lng: 103.8198 },
    near_by_places: [],
    selected_type: '',
    price: 1000000,
  },
  getters: {
    getUserInputAddress: state => state.user_input_address,
    getUserInputAddressLoc: state => state.user_input_address_loc,
    getNearbyPlaces: state => state.near_by_places,
    getPrice: state => state.price,
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
    RESET_USER_INPUT_ADDRESS: (state) => {
      state.user_input_address = '';
    },
  },
  actions: {
    requestNearbyPlaces({ commit }, { type, loc }) {
      const query = JSON.parse(JSON.stringify(QUERIES[type]));
      query.location = JSON.parse(JSON.stringify(loc));
      query.radius = QUERY_DEFAULT_SEARCH_DISTANCE;
      query.need_distance = QUERY_DEFAULT_NEED_WALKING_DISTANCE;
      return new Promise((resolve, reject) => {
        getNearbyPlaces(query).then((result) => {
          const places = [];
          const resultObj = JSON.parse(result.body);
          resultObj.forEach((resultByType) => {
            places.push(...resultByType.places);
          });
          commit('SET_NEARBY_PLACES', places);
          resolve();
        }).catch(error => reject(error));
      });
    },
  },
});

export default store;
