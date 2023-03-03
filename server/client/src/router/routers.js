
import LoginComp from "@/components/LoginComp.vue";
import ThreadComp from "@/components/ThreadComp.vue";
import RegistComp from "@/components/RegistComp.vue";
import UserInfoComp from "@/components/UserInfoComp.vue";
import TopicComp from "@/components/TopicComp.vue";
import PageNotFoundComp from "@/components/PageNotFoundComp.vue";


const routes = [
    { path:'/', component: ThreadComp },
    { path:'/login', component: LoginComp },
    { path:'/regist', component: RegistComp },
    { path:'/userinfo', component: UserInfoComp },
    { path:'/topic/:id', component: TopicComp },

    // 最后匹配的就是404页面
    { path:'/:pathMatch(.*)', component: PageNotFoundComp }
]

export default routes