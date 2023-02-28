import {defineStore} from "pinia";

export const useGlobalData = defineStore('globaldata',{
    state: () => ({
        is_login: false,
        user_token: ''
    }),
    getters: {
        isLogin: (state) => state.is_login,
        token: (state) => state.user_token
    },
    actions: {
        setIsLogin(value){
            this.is_login = value
        },
        setToken(value){
            this.user_token = value
        }
    }
})