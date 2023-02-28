<template>
  <form class="login-form">
    <p>登录</p>
    <div class="login-form-item">
      <el-input v-model="formData.username" placeholder="用户名" size="large"/>
    </div>
    <div class="login-form-item">
      <el-input v-model="formData.password" placeholder="密码" type="password" size="large"/>
    </div>
    <div class="login-form-item">
      <el-input v-model="formData.cert" placeholder="验证码" size="large"/>
    </div>
    <el-button type="primary" @click="onSubmit" size="large">登录</el-button>
  </form>
</template>

<script>
import serviceApi from "@/services/serviceApi";
import {useGlobalData} from "@/services/globalData";

export default {
  name: "LoginComp",
  data(){
    return{
      formData: {
        username: '',
        password: '',
        cert: ''
      },
      userData: useGlobalData()
    }
  },
  methods: {
    onSubmit() {
      serviceApi.TryLogin(this.formData)
          .then(response => {
            this.userData.setIsLogin(serviceApi.GetApiResult(response))
          })
    }
  }
}

</script>

<style scoped>
.login-form{
  width: 400px;
  height: 380px;
  margin: 120px auto;
  text-align: center;
  border-radius: 10px;
  border: 1px solid var(--el-border-color);
  box-shadow: var(--el-box-shadow-dark);
}

.login-form-item{
  width: 84%;
  margin-left: 8%;
  margin-right: 8%;
  margin-bottom: 20px;
}

p{
  font-size: 28px;
}

</style>