import Vue from 'vue';
import Vuex from 'vuex';
import { getNearbyPlaces } from '@/api';

Vue.use(Vuex);
const QUERY_DEFAULT_SEARCH_DISTANCE = 1000;
const QUERY_DEFAULT_NEED_WALKING_DISTANCE = false;
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
  sports: {
    types: [
      {
        name: 'sports',
        keyword: 'sports',
      },
    ],
  },
  transport: {
    types: [
      {
        name: 'mrt',
        keyword: 'mrt',
      },
      {
        name: 'bus stop',
        keyword: 'bus stop',
      },
    ],
  },
};

const store = new Vuex.Store({
  state: {
    user_input_address: 'Singapore',
    user_input_address_loc: { lat: 1.3521, lng: 103.8198 },
    map_markers: [{
      position: { lat: 1.3521, lng: 103.8198 },
      infoText: 'Singapore',
    }],
    selected_tab: '',
  },
  mutations: {
    EDIT_USER_INPUT_ADDRESS: (state, addr) => {
      state.user_input_address = addr;
    },
    EDIT_USER_INPUT_ADDRESS_LOC: (state, loc) => {
      state.user_input_address_loc = loc;
    },
    SET_MAP_MARKERS: (state, markers) => {
      state.map_markers = markers;
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
      return new Promise((resolve) => {
        getNearbyPlaces(query).then((result) => {
          const markers = [];
          const resultObj = JSON.parse(result.body);
          resultObj.forEach((resultByType) => {
            resultByType.places.forEach((place) => {
              const marker = {};
              marker.position = place.location;
              marker.infoText = place.name;
              markers.push(marker);
            });
          });
          commit('SET_MAP_MARKERS', markers);
        });
        resolve();
      });
    },
  },
  getters: {
    getUserInputAddress: state => state.user_input_address,
    getUserInputAddressLoc: state => state.user_input_address_loc,
    getMapMarkers: state => state.map_markers,
  },
});

export default store;
