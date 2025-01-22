<template>
  <div class="home">
    <div class="header">
      <el-input v-model="url" placeholder="请输入图片url" style="width: 200px;margin-right: 20px;"/>
      <el-button type="primary" @click="to3D" :loading="loading">生成</el-button>
    </div>
    <div class="content" style="height: 80px">
      <div class="model_box">
        <h2>meshy</h2>
      </div>
      <div class="model_box">
        <h2>tripo3d</h2>
      </div>
      <div class="model_box">
        <h2>hyper3d</h2>
      </div>
    </div>
    <div class="content" v-for="(item, index) in model_list" :key="index">
      <div class="model_box">
        <show3D :url="item.model.meshy" class="model"></show3D>
      </div>
      <div class="model_box">
        <show3D :url="item.model.tripo3d" class="model"></show3D>
      </div>
      <div class="model_box">
        <show3D :url="item.model.hyper3d" class="model"></show3D>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios';
import serverConfig from "@/config.js";
import Show3D from "@/components/show3D.vue";

export default {
  components: {Show3D},
  data() {
    return {
      url: '',
      model_list: [],
      loading: false
    };
  },
  mounted() {
    axios.get(serverConfig.baseURL + '/api/list')
        .then(response => {
          console.log('Response:', response.data);
          for (let i = response.data.length - 1; i >= 0; i--) {
            this.model_list.push({
              originalImage: response.data[i].original_image,
              model: {
                meshy: response.data[i].glb_file1,
                hyper3d: response.data[i].glb_file2,
                tripo3d: response.data[i].glb_file3
              }
            });
          }
        }).catch(error => {
      console.error('Error:', error);
      this.model_list[0]['model'][type] = '';
    });
  },
  methods: {
    async to3D() {
      const originalImage = this.url;

      // 简单判断是否为URL
      if (!this.isValidUrl(originalImage)) {
        console.error("Invalid URL");
        return;
      }

      this.loading = true

      try {
        const newModel = {
          originalImage: originalImage,
          model: {
            hyper3d: '1',
            meshy: '1',
            tripo3d: '1'
          }
        };

        this.model_list.unshift(newModel);

        const generateFile = (type) => {
          const urlMap = {
            hyper3d: serverConfig.baseURL + "/api/generated-files/generate/hyper3d/",
            meshy: serverConfig.baseURL + "/api/generated-files/generate/meshy/",
            tripo3d: serverConfig.baseURL + "/api/generated-files/generate/tripo3d/"
          };

          const url = urlMap[type];
          if (!url) {
            throw new Error(`Unsupported type: ${type}`);
          }

          axios.post(url, {
            original_image: originalImage
          }, {
            headers: {
              'Content-Type': 'application/json'
            }
          }).then(response => {
            console.log('Response:', response.data);
            this.model_list[0]['model'][type] = response.data.glb; // 获取 glb 字段的值
          }).catch(error => {
            console.error('Error:', error);
            this.model_list[0]['model'][type] = '';
          });
        };

        setTimeout(() => {
          generateFile('hyper3d')
        })
        setTimeout(() => {
          generateFile('meshy')
        })
        setTimeout(() => {
          generateFile('tripo3d')
        })

        while (true) {
          console.log(this.model_list[0]['model'])
          if (this.model_list[0]['model']['meshy'] !== '1' && this.model_list[0]['model']['hyper3d'] !== '1' && this.model_list[0]['model']['tripo3d'] !== '1') {
            break;
          }
          await new Promise(resolve => setTimeout(resolve, 1000));
        }

        // 构建保存请求的数据
        const saveData = {
          original_image: originalImage,
          glb_file1: newModel.model.meshy,
          glb_file2: newModel.model.hyper3d,
          glb_file3: newModel.model.tripo3d
        };

        // 发起保存请求
        const saveResponse = await axios.post(serverConfig.baseURL + "/api/generated-files/update/", saveData);
        console.log(saveResponse.data.msg);
      } catch (e) {
        console.log(e)
      } finally {
        this.loading = false
      }
    },
    isValidUrl(string) {
      try {
        new URL(string);
        return true;
      } catch (_) {
        return false;
      }
    }
  }
}
;
</script>

<style scoped>
.header {
  margin-bottom: 20px;
  height: 200px;
  padding: 20px;
  display: flex;
  align-items: center;
}

.home {
  margin: 0 auto;
  width: 100%;
  padding: 20px;
  max-width: 1200px;
}

.content {
  display: flex;
  justify-content: space-around;
  align-items: center;
  flex-wrap: nowrap;
  width: 100%;
  height: 300px;
  overflow: hidden;
  margin-bottom: 30px;
}

.model_box {
  width: 30%;
  height: 100%;
}

.model {
  width: 100%;
  height: 100%;
}
</style>
