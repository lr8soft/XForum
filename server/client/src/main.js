import { createApp } from 'vue'
import ElementPlus from 'element-plus'
import App from './App.vue'
import 'element-plus/theme-chalk/index.css'

const app = createApp(App)
app.config.globalProperties.$isLogin=false
app.config.globalProperties.$token=''

app.use(ElementPlus)
app.mount('#app')

