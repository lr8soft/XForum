<template>
  <UniformHead/>
  <div v-if="userData.isLogin">
    <ThreadComp/>
  </div>
  <div v-else>
    <LoginComp/>
  </div>
  <RegistComp/>
</template>

<script>
import UniformHead from "@/components/UniformHead.vue";
import RegistComp from "@/components/RegistComp.vue";
import LoginComp from "@/components/LoginComp.vue";
import {useGlobalData} from "@/services/globalData";
import ThreadComp from "@/components/ThreadComp.vue";
export default {
  name: 'App',
  data(){
    return{
      userData: useGlobalData()
    }
  },
  components: {
    ThreadComp,
    UniformHead, RegistComp, LoginComp
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
