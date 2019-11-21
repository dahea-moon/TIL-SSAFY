<template>
  <div id="app">
    <div id="nav">
      <router-link to="/">Home</router-link> |
      
      <span v-if="!isLoggedIn">
        <router-link to="/login">Login</router-link>        
      </span>
     
      <span v-else>
        <a @click.prevent="logout" href="">LogOut</a>
      </span>
    </div>
    <div class="container col-6">
      <router-view/>
    </div>
  </div>
</template>

<script>
import { mapActions, mapGetters} from 'vuex'

export default {
  name: 'App',
  methods: {
    ...mapGetters(['isLoggedIn']),
    ...mapActions(['logout'])
  }
}
</script>>

<style>
/*
  1. 컴포넌트 마다 비슷한/같은 함수들을 정의 해야함 + 정리 안됨
  2. 사용자 auth 정보 & todos 목록을 컴포넌트끼리 공유하지 못함

  Vuex(State Mnagement System)
*/
</style>
