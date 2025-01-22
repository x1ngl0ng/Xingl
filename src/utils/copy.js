import {ElMessage} from "element-plus";

export const  copy = async (text) =>{
    try {
        if (!navigator.clipboard) {
            // 兼容性处理：对于不支持navigator.clipboard的环境，使用回退方案
            const input = document.createElement('input');
            input.value = text;
            document.body.appendChild(input);
            input.select();
            document.execCommand('copy');
            document.body.removeChild(input);

            ElMessage({
                message: '已复制',
                type: 'success',
            });
        } else {
            await navigator.clipboard.writeText(text);
            ElMessage({
                message: '已复制',
                type: 'success',
            });
        }
    } catch (err) {
        // 增强的错误处理：区分错误类型
        if (err.name === 'SecurityError') {
            ElMessage({
                message: '复制失败：请允许浏览器访问剪贴板',
                type: 'error',
            });
        } else {
            ElMessage({
                message: '复制失败',
                type: 'error',
            });
        }
    }
}
