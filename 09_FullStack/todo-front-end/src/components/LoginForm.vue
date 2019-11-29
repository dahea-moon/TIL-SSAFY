<template>
    <div class="login-form">
        <div v-if="isLoading" class="spinner-border" role="status">
            <span class="sr-only">Loading</span>
        </div>

        <form v-else class="login-input" @submit="login">
            <div class="error-list alert alert-danger" v-if="errors.length">
                <h4>아래의 오류를 해결해 주세요</h4>
                <ul>
                    <li v-for="(error, idx) in errors" :key="idx">{{ error }}</li>
                </ul>
            </div>
            <div class="form-group">
                <label for="username">ID</label>
                <input @keyup.enter="login" v-model="credentials.username" type="text" class="form-control" id="id"
                    placeholder="아이디를 입력해주세요">
            </div>
            <div class="form-group">
                <label for="password">Password</label>
                <input @keyup.enter="login" v-model="credentials.password" type="password" class="form-control" id="password"
                    placeholder="비밀번호를 입력해주세요">
            </div>
            <button @click="login" class="btn btn-primary">로그인</button>
        </form>
    </div>
</template>

<script>
    import router from '../router'; // '../router/index.js'
    const axios = require('axios');
    
    export default {
        name: 'LoginForm',
        data() {
            return {
                credentials: {
                    username: '',
                    password: '',
                }, // id/password에 해당하는 data
                isAuthenticated: false, // 인증여부
                isLoading: false,
                errors: [],
            }
        },
        methods: {
            login() {
                this.isLoading = true;
                if (this.checkUserInput()) {
                    axios.post('http://localhost:8000/api-token-auth/', this.credentials)
                        .then(res => {
                            this.isLoading = false
                            this.$session.start() // sessionsStorage.session-id: sess: + Date.now()
                            this.$session.set('jwt', res.data.token)
                            this.$store.dispath('login', res.data.token)
                            router.push('/');
                        })
                        .catch(err => {
                            if (!err.response) {
                                this.errors.push('Network Error..')
                            } else if (err.response.status === 400) {
                                this.errors.push('Invalid username or password')
                            } else if (err.response.status === 500) {
                                this.errors.push('Invalid Server error. Please try again later')
                            } else {
                                this.errors.push('Some error occured')
                            }
                            this.isLoading=false;
                        })
                } else {
                    console.log('검증실패! 다시 작성하세요')
                    this.isLoading = false;
                }
            },
            checkUserInput() {
                this.errors = [];
                if (!this.credentials.username) {
                    this.errors.push("username을 입력하세요");
                } 
                if (this.credentials.password.length < 8) {
                    this.errors.push("password는 8자 이상이어야 합니다.");
                }
                if (!this.errors.length) {
                    return true;
                }
            }
        }
    }
</script>

<style>

</style>