import {fileURLToPath, URL} from 'node:url'

import {defineConfig} from 'vite'
import vue from '@vitejs/plugin-vue'
import server from './src/config.js'
import WindiCSS from 'vite-plugin-windicss'
import VueSetupExtend from 'vite-plugin-vue-setup-extend'

// https://vitejs.dev/config/
export default defineConfig({
    optimizeDeps: {
        // include: ['three', 'three/examples/jsm/controls/OrbitControls'],
        exclude: ['@google/model-viewer'] // 确保 Vite 不优化这个模块
    },
    plugins: [
        VueSetupExtend(),
        vue(),
        WindiCSS(),
        
    ],
    resolve: {
        alias: {
            '@': fileURLToPath(new URL('./src', import.meta.url))
        }
    },
    build: {
        chunkSizeWarningLimit: 1000 * 1024,
        // minify: "terser",
        terserOptions: {
            compress: {
                drop_console: true, // 删除console.log
                drop_debugger: true, // 删除debugger语句
            },
        },
    },
    server: {
        host: server.host,
        port: server.port, // 或您选择的任何端口
        open: true, // 可选：自动在浏览器中打开
        proxy: {
            '/api': {
                target: 'http://127.0.0.1:8000',
                changeOrigin: true,
                secure: true,
                rewrite: (path) => path.replace(/^\/api/, '/api'),
            },
        },
    },
})
