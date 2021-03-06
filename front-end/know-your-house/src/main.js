// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue';
import Element from 'element-ui';
import locale from 'element-ui/lib/locale/lang/en';
import 'element-ui/lib/theme-chalk/index.css';
import * as VueGoogleMaps from 'vue2-google-maps';
import 'chart.js';
import 'hchs-vue-charts';
import store from './store';
import App from './App';
import router from './router';

Vue.use(Element, { size: 'small', locale });

Vue.use(VueGoogleMaps, {
  load: {
    key: 'AIzaSyDVK9Xd5pNqceBBnl_LLyos6ANTZCLteFs',
    libraries: 'places',
  },
});

Vue.use(window.VueCharts);

Vue.config.productionTip = false;

/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  store,
  components: { App },
  template: '<App/>',
});
