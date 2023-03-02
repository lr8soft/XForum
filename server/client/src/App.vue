<template>
  <el-container>
    <el-header>
      <UniformHead/>
    </el-header>
    <el-main>
      <router-view></router-view>
    </el-main>
  </el-container>
</template>

<script>
import UniformHead from "@/components/UniformHead.vue";
import {useGlobalData} from "@/services/globalData";
export default {
  name: 'App',
  data(){
    return{
      userData: useGlobalData()
    }
  },
  components: {
    UniformHead
  }
}
</script>
<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
}
</style>
