import Vue from 'vue'
import App from './App.vue'
import store from './store'
import vuetify from './plugins/vuetify';
import router from './router'


if (process.env.NODE_ENV == 'development') {
  Vue.config.productionTip = true
  Vue.config.devtools = true
  window.eel.set_host("ws://localhost:8686");
} else {
  Vue.config.productionTip = false
  Vue.config.devtools = false
}


new Vue({
  store,
  vuetify,
  router,
  render: h => h(App)
}).$mount('#app')
