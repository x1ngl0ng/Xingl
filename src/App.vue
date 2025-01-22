<template>
  <div id="app">
    <router-view/>
  </div>
</template>

<script>
import {getUserInfo} from "@/api/user.js";
import {useRoute} from "vue-router";

export default {
  name: 'App',
  data() {
    return {
    }
  },
  mounted() {

  },
  methods: {

  }
}
</script>

<style>

</style>
