<template>
  <el-menu
      :default-active="activeIndex"
      mode="horizontal"
      background-color="#545c64"
      text-color="#fff"
      active-text-color="#ffd04b"
      :ellipsis="false">
    <!--这标题呢-->
    <el-menu-item index="1">{{title}}</el-menu-item>
    <div class="flex-grow" />
    <el-menu-item index="2">首页</el-menu-item>
    <el-menu-item index="3">分区</el-menu-item>
    <el-menu-item index="4">个人空间</el-menu-item>

  </el-menu>
</template>

<script>
export default {
  name: "UniformHead",
  props:{
    title: {
      type: String,
      default: ()=> "XForum"
    }
  }
}
</script>

<style scoped>
.flex-grow {
  flex-grow: 1;
}
</style>