<template>
  <div class="box" id="box">
    <div ref="threeCanvas" v-loading="loading" class="Canvas">
    </div>
  </div>
</template>
<style scoped>
.box {
  position: relative;
  height: 100%;
  /*width:100%;*/
  background: rgb(240, 240, 240);
}

.Canvas {
  width: 100%;
  height: 100%
}

.btn {
  position: absolute;
  bottom: 10px;
  right: 10px;
  z-index: 50;
}
</style>

<script>import * as THREE from 'three';
import {GLTFLoader} from 'three/examples/jsm/loaders/GLTFLoader';
import {OrbitControls} from 'three/examples/jsm/controls/OrbitControls';
import {FullScreen} from "@element-plus/icons-vue";
import debounce from "lodash/debounce.js";
import serverConfig from "@/config.js";

export default {
  components: {FullScreen},
  data() {
    return {
      controls: '',
      renderer: '',
      show: '',
      loading: false,
      resizeObserver: null,
    }
  },
  props: {
    url: {
      type: String,
      required: false,
      default: '',
    },
    upload: {
      type: Boolean,
      required: false,
      default: false,
    },
  },
  watch: {
    url(val) {
      console.log(val)
      if (!val) {
        this.loading = false
      }
      if (val === '1') {
        this.loading = true
      }
      if (val && val !== '1') {
        setTimeout(() => {
          if (!this.show) {
            this.loading = true
          }
        }, 300)
        this.initThree();
        // window.addEventListener('resize', this.onWindowResize);
      }
    }
  },
  mounted() {
    console.log('a')
    if (this.url && this.url !== '1') {
      setTimeout(() => {
        if (!this.show) {
          this.loading = true
        }
      }, 300)
      this.initThree();
      // window.addEventListener('resize', this.handleResize);
      this.debouncedHandleResize = debounce(this.handleResize, 80)
      this.resizeObserver = new ResizeObserver(this.debouncedHandleResize);
      this.resizeObserver.observe(document.getElementById('box'));
    } else if (this.url === "1") {
      this.loading = true
    }
  },
  unmounted() {
    window.removeEventListener('resize', this.handleResize);
    console.log('unmounted')
    this.show = ''
    if (this.resizeObserver) {
      this.resizeObserver.disconnect();
    }
  },
  methods: {
    captureAndSaveImage() {
      // 获取canvas元素
      const canvas = this.renderer.domElement;

      // 使用toDataURL方法获取图像数据URL
      const dataUrl = canvas.toDataURL('image/png');

      // 动态创建一个链接元素
      const link = document.createElement('a');
      link.href = dataUrl;
      link.download = 'screenshot.png'; // 设置下载的文件名

      // 触发点击事件以下载图像
      // document.body.appendChild(link);
      // link.click();
      // document.body.removeChild(link);
    },
    handleResize() {
      this.renderer.setSize(this.$refs.threeCanvas.clientWidth, this.$refs.threeCanvas.clientHeight);
      this.renderer.setPixelRatio(window.devicePixelRatio);
      if (this.camera) {
        this.camera.aspect = this.$refs.threeCanvas.clientWidth / this.$refs.threeCanvas.clientHeight;
        this.camera.updateProjectionMatrix();
      }
    },
    initThree() {
      const scene = new THREE.Scene();
      const camera = new THREE.PerspectiveCamera(75, this.$refs.threeCanvas.clientWidth / this.$refs.threeCanvas.clientHeight, 0.1, 1000);
      this.renderer = new THREE.WebGLRenderer({antialias: true});
      this.renderer.setSize(this.$refs.threeCanvas.clientWidth, this.$refs.threeCanvas.clientHeight);

      this.$refs.threeCanvas.innerHTML = ''
      this.$refs.threeCanvas.appendChild(this.renderer.domElement);


      this.renderer.setClearColor(0xf0f0f0);

      camera.position.set(0, 0, 2); // 将相机向后移动，远离模型

      const loader = new GLTFLoader();
      loader.load(serverConfig.baseURL + "/api/generated-files/" + this.url, gltf => {
        this.loading = false
        scene.add(gltf.scene);
        // console.log(gltf.scene)
        this.show = scene.uuid
        // 调整模型位置和大小
        gltf.scene.scale.set(1, 1, 1); // 缩小模型
        // gltf.scene.position.set(0, 0, 0); // 如果模型原本就在原点，这行可以省略
        // 可以尝试将模型向上或向后移动，使其远离相机
        // gltf.scene.position.y = 10; // 向上移动
        // gltf.scene.position.z = -50; // 向后移动
        animate();
        this.captureAndSaveImage();
      });

      // 添加 OrbitControls
      this.controls = new OrbitControls(camera, this.renderer.domElement);
      this.controls.enableDamping = true; // 平滑移动

      const animate = () => {
        // console.log('animate')
        // console.log(this.show, scene.uuid)
        if (this.show !== scene.uuid) {
          return
        }
        requestAnimationFrame(animate);
        this.controls.update(); // 必须在渲染前调用
        this.renderer.render(scene, camera);
      };

      // const ambientLight = new THREE.AmbientLight(0xffffff);
      // scene.add(ambientLight);
      // const directionalLight = new THREE.DirectionalLight(0xffffff, 1);
      // directionalLight.position.set(0, 0, 0).normalize();
      // scene.add(directionalLight);

      const ambientLight = new THREE.AmbientLight(0xffffff); // 更改为白色，亮度最大
      scene.add(ambientLight);

      // 添加四个方向的定向光，分别代表前后左右上下
      const directionalLightFront = new THREE.DirectionalLight(0xffffff, 1);
      directionalLightFront.position.set(1, 0, 0);
      scene.add(directionalLightFront);

      const directionalLightBack = new THREE.DirectionalLight(0xffffff, 1);
      directionalLightBack.position.set(-1, 0, 0);
      scene.add(directionalLightBack);

      const directionalLightLeft = new THREE.DirectionalLight(0xffffff, 1);
      directionalLightLeft.position.set(0, 0, 1);
      scene.add(directionalLightLeft);

      const directionalLightRight = new THREE.DirectionalLight(0xffffff, 1);
      directionalLightRight.position.set(0, 0, -1);
      scene.add(directionalLightRight);

      const directionalLightTop = new THREE.DirectionalLight(0xffffff, 1);
      directionalLightTop.position.set(0, 1, 0);
      scene.add(directionalLightTop);

      const directionalLightBottom = new THREE.DirectionalLight(0xffffff, 1);
      directionalLightBottom.position.set(0, -1, 0);
      scene.add(directionalLightBottom);

      // 增加光线强度
      // directionalLight.intensity = 2;

    }
  }
}
</script>