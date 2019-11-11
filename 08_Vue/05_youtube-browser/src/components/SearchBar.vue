<template>
<!-- HTML -->
    <div>
        <!-- method는 내가 인자를 추가로 넘긴다면 (ARG) 붙이고 -->
        <!-- 그게 아니라면 () 안 붙임 -->
        <!-- v-on: 을 줄려서 @ -->
        <!-- <input @input="onInput" type="text"> -->
        <input @keypress.enter="onInput" type="text">
    </div>
</template>

<script>
export default {
    name: 'SearchBar', // new comp: 0. 이름 적기
    methods: {
        onInput: function (e) {
            // this.$emit('Event이름', 전송할 값): 자식 comp에서 부모 comp로 데이터를 올려보낼 때
            this.$emit('inputChange', e.target.value);
        }
    }
}
</script>

<style lang="">
    
</style>