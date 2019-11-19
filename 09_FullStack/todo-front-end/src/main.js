import Vue from 'vue'
import App from './App.vue'
import router from './router' // from './router/index.js'
import VueSession from 'vue-session' // 발급받은 token을 session storage에 저장하는 걸 도와줌

Vue.config.productionTip = false
Vue.use(VueSession) // Vue에게 vueSession 이라는 middleware 등록

new Vue({
  router, // router/index.js 에서 악수 하고, 본격적으로 일을 시작.
  render: h => h(App)
}).$mount('#app')
