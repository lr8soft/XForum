import {createRouter, createWebHistory} from "vue-router";
import routes from "@/router/routers";

const router = createRouter({
    routes: routes,
    history: createWebHistory(process.env.BASE_URL)
})

export default router