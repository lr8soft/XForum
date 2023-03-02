import { createApp } from 'vue'
import ElementPlus from 'element-plus'
import App from './App.vue'
import { createPinia } from 'pinia'

import * as ElementIcons from '@element-plus/icons-vue'
import 'element-plus/theme-chalk/index.css'

import router from "@/router";

const pinia = createPinia()
const app = createApp(App)

for (const key in ElementIcons) {
    app.component(key, ElementIcons[key])
}

app.use(pinia)
app.use(ElementPlus)
app.use(router)
app.mount('#app')

