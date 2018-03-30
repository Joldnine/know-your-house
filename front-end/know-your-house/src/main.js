// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue';
import Element from 'element-ui';
import 'element-ui/lib/theme-chalk/index.css';
import * as VueGoogleMaps from 'vue2-google-maps';
import App from './App';
import router from './router';

Vue.use(Element, { size: 'small' });

Vue.use(VueGoogleMaps, {
  load: {
    key: 'AIzaSyDVK9Xd5pNqceBBnl_LLyos6ANTZCLteFs',
    libraries: 'places',
  },
});

Vue.config.productionTip = false;

/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  components: { App },
  template: '<App/>',
});
