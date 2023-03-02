<template>
  <div id="userinfo-body">
    <el-descriptions
        class="margin-top"
        title="个人空间"
        :column="3"
        :size="large"
        border
    >

      <el-descriptions-item>
        <template #label>
          <div class="cell-item">
            <el-icon class="icon-body">
              <user />
            </el-icon>
            用户名
          </div>
        </template>
        {{username}}
      </el-descriptions-item>

      <el-descriptions-item>
        <template #label>
          <div class="cell-item">
            <el-icon class="icon-body">
              <message />
            </el-icon>
            电子邮箱
          </div>
        </template>
        {{email}}
      </el-descriptions-item>

      <el-descriptions-item>
        <template #label>
          <div class="cell-item">
            <el-icon class="icon-body">
              <timer />
            </el-icon>
            上次登录
          </div>
        </template>
        {{lastLogin}}
      </el-descriptions-item>

    </el-descriptions>
  </div>
</template>

<script>
import {
  User,Message, Timer
} from '@element-plus/icons-vue'

export default {
  name: "UserInfoComp",
  data(){
    return{
      username: "LT_TEST",
      email: "test@test.com",
      lastLogin: "2023-03-02 15:00:00"
    }
  }
}
</script>

<style scoped>
#userinfo-body{
  width: 80%;
  margin: auto;
}
.icon-body{
  width: 28px;
  height: 28px;
  margin: auto;
}
</style>