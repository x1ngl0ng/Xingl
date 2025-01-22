// 创建 axios 请求实例
import axios from 'axios';
import serverConfig from '../config.js';
import * as querystring from "querystring"; // 修正导入模块
axios.defaults.withCredentials = true;
const serviceAxios = axios.create({
    baseURL: serverConfig.baseURL, // 基础请求地址
    // baseURL: "",
    timeout: 1000000, // 请求超时设置
    withCredentials: true, // 跨域请求是否需要携带 cookie
})
// 封装处理HTTP状态码的函数
const handleHttpStatus = (status) => {
    switch (status) {
        case 302:
            return '接口重定向了！'
        case 400:
            return '参数不正确！'
        case 401:
            return '您未登录，或者登录已经超时，请先登录！'
        case 403:
            return '您没有权限操作！'
        case 404:
            return `请求地址出错`
        case 408:
            return '请求超时！'
        case 409:
            return '系统已存在相同数据！'
        case 500:
            return '服务器内部错误！'
        case 501:
            return '服务未实现！'
        case 502:
            return '网关错误！'
        case 503:
            return '服务不可用！'
        case 504:
            return '服务暂时无法访问，请稍后再试！'
        case 505:
            return 'HTTP 版本不受支持！'
        default:
            return '异常问题，请联系管理员！'
    }
}
// 假设存在一个非HttpOnly的cookie用于指示token是否存在，实际应用中请根据情况调整
function getTokenFromCookie() {
    const cookies = document.cookie.split(';');
    for (let i = 0; i < cookies.length; i++) {
        const cookie = cookies[i].trim();
        if (cookie.startsWith('token=')) {
            return cookie.substring('token='.length, cookie.length);
        }
    }
    return null;
}
// 创建请求拦截
serviceAxios.interceptors.request.use(
    (config) => {
        // 检查 token 是否存在，避免空字符串赋值
        // const token = localStorage.getItem('token') || '';
        // if (serverConfig.useTokenAuthorization && token) {
        //   config.headers['Authorization'] = `Bearer ${token}`; // 请求头携带 token
        // }
        const token = getTokenFromCookie();
        if (serverConfig.useTokenAuthorization && token) {
            config.headers['Authorization'] = `Bearer ${token}`;
        }
        // 设置请求头
        if (!config.headers['content-type']) {
            // 如果没有设置请求头
            if (config.method === 'post') {
                if (config['contentType']) {
                    config.headers['content-type'] = config['contentType'];
                } else {
                    config.headers['content-type'] = 'application/x-www-form-urlencoded';
                }
                // config.data = querystring.stringify(config.data); // 序列化,比如表单数据
                // console.log('请求数据', config.data)
            } else {
                config.headers['content-type'] = 'application/json'; // 默认类型
            }
        }
        // console.log('请求配置', config);
        return config;
    },
    (error) => {
        return Promise.reject(error);
    }
)

// 创建响应拦截
serviceAxios.interceptors.response.use(
    (res) => {
        return res.data;
    },
    (error) => {
        console.log(error)
        let message = '';
        if (error && error.response) {
            message = handleHttpStatus(error.response.status);
        }
        return Promise.reject(message);
    }
)

export default serviceAxios;