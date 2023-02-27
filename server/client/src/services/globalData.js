import {getCurrentInstance, onMounted} from "vue";

export default {
    setup(){
        const { proxy } = getCurrentInstance();
        onMounted(()=>{
            proxy.$isLogin = false
            proxy.$token = ''
        })
    },

    getIsLogin(){
        const { proxy } = getCurrentInstance()
        return proxy.$isLogin
    },
    setIsLogin(value){
        const { proxy } = getCurrentInstance()
        print(proxy)
        proxy.$isLogin = value
    }
}