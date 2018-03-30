import Vue from 'vue';
import Vuex from 'vuex';
// import {  } from '@/api';

Vue.use(Vuex);

const store = new Vuex.Store({
  state: {
    user_input_address: '',
  },
  mutations: {
    EDIT_USER_INPUT_ADDRESS: (state, addr) => {
      state.user_input_address = addr;
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
  },
});

export default store;
