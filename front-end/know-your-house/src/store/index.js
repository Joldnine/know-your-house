import Vue from 'vue';
import Vuex from 'vuex';
// import {  } from '@/api';

Vue.use(Vuex);

const store = new Vuex.Store({
  state: {
    user_input_address: 'Singapore',
    user_input_address_loc: { lat: 1.3521, lng: 103.8198 },
    map_markers: [{
      position: { lat: 1.3521, lng: 103.8198 },
      infoText: 'Singapore',
    }],
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
    submitForm({ commit }, form) {
      // TODO call api to get price and price trends
      commit('EDIT_USER_INPUT_ADDRESS', form.addr);
    },
  },
  getters: {
    getUserInputAddress: state => state.user_input_address,
    getUserInputAddressLoc: state => state.user_input_address_loc,
    getMapMarkers: state => state.map_markers,
  },
});

export default store;
