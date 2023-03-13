
import LoginComp from "@/components/LoginComp.vue";
import ThreadComp from "@/components/ThreadComp.vue";
import RegistComp from "@/components/RegistComp.vue";
import UserInfoComp from "@/components/UserInfoComp.vue";
import TopicComp from "@/components/TopicComp.vue";
import PageNotFoundComp from "@/components/PageNotFoundComp.vue";
import LogoutComp from "@/components/LogoutComp.vue";


const routes = [
    { path:'/', component: ThreadComp },
    { path:'/login', component: LoginComp },
    { path:'/regist', component: RegistComp },
    { path:'/userinfo', component: UserInfoComp },
    { path:'/topic/:id', component: TopicComp },
    { path:'/logout', component: LogoutComp },
    // 最后匹配的就是404页面
    { path:'/:pathMatch(.*)', component: PageNotFoundComp }
]

export default routes