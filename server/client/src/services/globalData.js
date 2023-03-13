import {defineStore} from "pinia";
export const useGlobalData = defineStore('globaldata',{
    state: () => ({
        is_login: false,
        user_name: ''
    }),
    persist: {
        enabled: true,
        strategies: [{
            storage: localStorage,
            paths: ['is_login'],
            key: "is_login"
        }, {
            storage: sessionStorage,
            paths: ['is_login'],
            key: "is_login"
        }, {
            storage: localStorage,
            paths: ['user_name'],
            key: "user_name"
        }, {
            storage: sessionStorage,
            paths: ['user_name'],
            key: "user_name"
        }
        ],
    },
    getters: {
        isLogin: (state) => state.is_login,
        userName: (state) => state.user_name
    },
    actions: {
        setIsLogin(value){
            this.is_login = value
        },
        setUserName(value){
            this.user_name = value
        }
    }
})