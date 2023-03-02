
import LoginComp from "@/components/LoginComp.vue";
import ThreadComp from "@/components/ThreadComp.vue";
import RegistComp from "@/components/RegistComp.vue";


const routes = [
    { path:'/', component: ThreadComp},
    { path:'/login', component: LoginComp },
    { path:'/regist', component: RegistComp},
]

export default routes