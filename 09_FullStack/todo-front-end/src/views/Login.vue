<template>
    <div class="login">
        <h1>로그인 페이지 입니다.</h1>
        <LoginForm></LoginForm>
    </div>
</template>

<script>
import LoginForm from '../views/LoginForm.vue'
// import router from '../router'

export default {
    name: 'Login',
    components: {
        LoginForm,
    }
}
</script>

<style>

</style>