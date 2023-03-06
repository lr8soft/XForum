import axios from 'axios'

axios.defaults.withCredentials=true
const requestHelper = axios.create({
    timeout: 2000, // 请求超时时间,
    headers: {
        //关键
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8'
    },
    withCredentials: true
})

// 添加请求拦截器
requestHelper.interceptors.request.use(
    function (config) {
        // 在发送请求之前做些什么
        return config
    },
    function (error) {
        // 对请求错误做些什么
        console.log(error)
        return Promise.reject(error)
    }
)

// 添加响应拦截器
requestHelper.interceptors.response.use(
    function (response) {
        // 2xx 范围内的状态码都会触发该函数。
        // 对响应数据做点什么
        // dataAxios 是 axios 返回数据中的 data
        const dataAxios = response.data
        return dataAxios
    },
    function (error) {
        // 超出 2xx 范围的状态码都会触发该函数。
        // 对响应错误做点什么
        console.log(error)
        return Promise.reject(error)
    }
)


export default requestHelper
