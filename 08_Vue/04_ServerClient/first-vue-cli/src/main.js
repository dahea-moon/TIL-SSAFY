import Vue from 'vue'
import App from './App.vue' // .vue는 안써도 알아서 동작함

// 개발(dev) => 배포(deployment) => 운영(production)
Vue.config.productionTip = false

new Vue({
  // el: '#app', ==== .$mount('#app') => 둘이 같다!
  // method(함수 in 객체) 정의할 때, () => {} 금지이지만, 여기서만 쓴다
  render: h => h(App),
}).$mount('#app')