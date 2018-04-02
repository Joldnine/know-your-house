// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue';
import Element from 'element-ui';
import locale from 'element-ui/lib/locale/lang/en';
import 'element-ui/lib/theme-chalk/index.css';
import * as VueGoogleMaps from 'vue2-google-maps';
import 'chart.js';
import 'hchs-vue-charts';
import VueFire from 'vuefire';
import firebase from 'firebase/app';
import 'firebase/firestore';
// import CountUp from 'countup.js';
// import vueCountUpV2 from 'vue-countup-v2';
import store from './store';
import App from './App';
import router from './router';

Vue.use(Element, { size: 'small', locale });
// Vue.use(CountUp);
// Vue.use(vueCountUpV2);

Vue.use(VueGoogleMaps, {
  load: {
    key: 'AIzaSyDVK9Xd5pNqceBBnl_LLyos6ANTZCLteFs',
    libraries: 'places',
  },
});

Vue.use(window.VueCharts);

Vue.use(VueFire);
firebase.initializeApp({
  apiKey: 'AIzaSyA6uso8-9fjMjaQIojmVC4J1947tZ2L5Os',
  authDomain: 'cs5224-1521280264976.firebaseapp.com',
  databaseURL: 'https://cs5224-1521280264976.firebaseio.com',
  projectId: 'cs5224-1521280264976',
  storageBucket: 'cs5224-1521280264976.appspot.com',
  messagingSenderId: '1035770641969',
});

const db = firebase.firestore();

export default db;

Vue.config.productionTip = false;

/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  store,
  components: { App },
  template: '<App/>',
});
