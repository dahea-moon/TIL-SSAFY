import Vue from 'vue';
import App from './App'; // App.vue를 알아서 확장자 버리고 읽음

new Vue({
    // el: '#app',
    render: h => h(App), // 유일하게 method인데 arrow function
    // render(h) {
    //     h(App)
    // },
    // render: function (createElement) {
    //     return createElement(App);
    // }
}).$mount('#app') // el: '#app'와 같은 역할