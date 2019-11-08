<template>
  <!-- 반드시, template 안에는 "단 1개"의 태그(노드) 만이 있어야 한다-->
  <div>
    <h1>Hi</h1>
    <input type="text" v-model="input">
    <p>{{ filteredInput }}</p>
  </div>
</template>

<script>
/* eslint-disable no-console */
export default {
    name: 'App',
    // 왜인지는 모르겠지만, 이제부터는 data를 function으로 만들어야 해..
    data() {
      return {
        input: 'type something',
      }
    },
    methods: {
      
    },
    computed: {
      filteredInput: function () {
        // [바보] 가 들어오면, **로 바꿔서 return 하도록 한다
        return this.input.replace(/바보|멍청이/g, '**')
      }
    },
}
</script>

<style>
  
</style>