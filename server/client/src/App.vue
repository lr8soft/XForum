<template>
  <UniformHead />
  <LoginComp/>
  <RegistComp/>
</template>

<script>
import UniformHead from "@/components/UniformHead.vue";
import LoginComp from "@/components/LoginComp.vue";
import RegistComp from "@/components/RegistComp.vue";
export default {
  name: 'App',
  components: {
    UniformHead, LoginComp, RegistComp
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
