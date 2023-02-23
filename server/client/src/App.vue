<template>
  <UniformHead />
  <LoginComp/>
</template>

<script>
import UniformHead from "@/components/UniformHead.vue";
import LoginComp from "@/components/LoginComp.vue";
export default {
  name: 'App',
  components: {
    UniformHead, LoginComp
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
