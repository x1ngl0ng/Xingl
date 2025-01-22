import ElementUI from 'element-plus'
import 'element-plus/dist/index.css'
import * as ElementPlusIconsVue from '@element-plus/icons-vue'
import {createApp} from 'vue'
import App from './App.vue'
import router from './router'
import store from './store/store.js'
import {createPinia} from 'pinia'
import VueCookies from 'vue-cookies'



// 封装 ElementPlusIconsVue 处理逻辑
function registerElementPlusIcons(app) {
    for (const [key, component] of Object.entries(ElementPlusIconsVue)) {
        app.component(key, component)
    }
}


// routerAppend 工具函数
function routerAppend(path, pathToAppend) {
    if (!path || !pathToAppend) return null
    return path + (path.endsWith('/') ? '' : '/') + pathToAppend
}

const app = createApp(App)

const pinia = createPinia()

try {
    app.use(pinia)
    app.use(store)
    app.use(router)
    app.use(ElementUI)
    app.use(VueCookies)
    // app.use(VueMarkdownEditor);
    registerElementPlusIcons(app)
    // 设置 Element UI 默认配置
    app.config.globalProperties.$ELEMENT = {
        size: 'small',
        zIndex: 3000,
        message: {
            offset: '400px' // 设置消息提示框距离顶部的距离
        }
    };

} catch (error) {
    console.error('应用初始化错误:', error)
}

app.mount('#app')
