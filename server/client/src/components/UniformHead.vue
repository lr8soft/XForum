<template>
  <div>
    <el-menu
        mode="horizontal"
        active-text-color="#007FFF"
        :ellipsis="false">
      <el-menu-item id="title-name" index="1">
        <router-link to="/">XForum</router-link>
      </el-menu-item>
      <div class="flex-grow"/>
      <el-menu-item index="2">
        <router-link to="/">首页</router-link>
      </el-menu-item>
      <el-menu-item index="3">分区</el-menu-item>
      <el-menu-item index="4">
        <el-sub-menu v-if="userData.isLogin">
          <template #title>账号信息</template>
          <el-menu-item>
            <router-link to="/userinfo">个人空间</router-link>
          </el-menu-item>
          <el-menu-item>
            <router-link to="/logout">登出</router-link>
          </el-menu-item>
        </el-sub-menu>

        <router-link to="/login" v-else>登录</router-link>
      </el-menu-item>

    </el-menu>
  </div>

</template>

<script>
import {useGlobalData} from "@/services/globalData";

export default {
  name: "UniformHead",
  data() {
    return {
      userData: useGlobalData()
    }
  }
}
</script>

<style scoped>
#title-name{
  font-size: 28px;
  font-weight: bold;
}

.flex-grow {
  flex-grow: 1;
}
a{
  text-decoration: none;
}
.router-link-active {
  text-decoration: none;
}
</style>