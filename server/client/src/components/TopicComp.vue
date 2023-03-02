<template>
  <div id="topic-body">
    <el-breadcrumb separator="/">
      <el-breadcrumb-item :to="{ path: '' }">测试大版A</el-breadcrumb-item>
      <el-breadcrumb-item><a href="">测试板块1</a></el-breadcrumb-item>
      <el-breadcrumb-item>{{ title }}</el-breadcrumb-item>
    </el-breadcrumb>
  </div>
</template>

<script>
export default {
  name: "TopicComp",
  data(){
    return{
      title: "测试文章"
    }
  }
}
</script>

<style scoped>
#topic-body{
  width: 90%;
  margin: auto;
}
</style>