import { createApp } from 'vue'
import ElementPlus from 'element-plus'
import App from './App.vue'
// pinia与持久化插件
import { createPinia } from 'pinia'
import piniaPluginPersist from "pinia-plugin-persist";
// element-ui-plus相关
import * as ElementPlusIconsVue from '@element-plus/icons-vue'
import 'element-plus/theme-chalk/index.css'

import router from "@/router";

const pinia = createPinia()
pinia.use(piniaPluginPersist);

const app = createApp(App)

for (const [key, component] of Object.entries(ElementPlusIconsVue)) {
    app.component(key, component)
}

app.use(pinia)
app.use(ElementPlus)
app.use(router)
app.mount('#app')

