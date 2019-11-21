// auth.js 인증관련 모든 state를 작성
// state에 접근/변경 하는 모든 로직은 여기로

const state = {
    token: null,
}

// Vuex에서는 arrow function을 쓴다
const getters = {
    isLoggedIn: state => !!state.token, // 특정 값을 true/flase로 바꾸는 구문
}

const mutations = {
    setToken: (state, token) => state.token = token,
}

const actions = {
    // logOut: (options) => {
    //     // mutations.setToken(state, null) === very bad
    //     options.commit('setToekn', null) // Great
    // }
    logout: ({ commit }) => {
        commit('setToken', null)
    },

    logIn: ({ commit }, token) => {
        commit('setToken', token)
    }
}

export default {
    state, getters, mutations, actions
}
