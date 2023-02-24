import { createApp } from 'vue'
import ElementPlus from 'element-plus'
import App from './App.vue'
import 'element-plus/theme-chalk/index.css'
import serviceApi from "@/axiosInstance"

const app = createApp(App)
app.use(ElementPlus)
app.mount('#app')
app.config.globalProperties.$serviceApi = serviceApi
