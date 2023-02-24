import axios from 'axios'

const serviceApi = axios.create({
    baseURL: 'http://127.0.0.1:8000//api',
    timeout: 1000,
    withCredentials: true
})

// 添加请求拦截器
serviceApi.interceptors.request.use(
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
serviceApi.interceptors.response.use(
    function (response) {
        console.log(response)
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


export default serviceApi
