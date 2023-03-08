import {defineStore} from "pinia";
export const useGlobalData = defineStore('globaldata',{
    state: () => ({
        is_login: false,
    }),
    persist: {
        enabled: true,
        strategies: [{
            storage: localStorage,
            paths: ['is_login'],
            key: "is_login"
        },{
            storage: sessionStorage,
            paths: ['is_login'],
            key: "is_login"
        }],
    },
    getters: {
        isLogin: (state) => state.is_login
    },
    actions: {
        setIsLogin(value){
            this.is_login = value
        }
    }
})