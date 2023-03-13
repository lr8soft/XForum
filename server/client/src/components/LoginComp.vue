<template>
  <el-form class="login-form">
    <p>登录</p>
    <div class="login-form-item">
      <el-input v-model="formData.username" placeholder="用户名" size="large"/>
    </div>
    <div class="login-form-item">
      <el-input v-model="formData.password" placeholder="密码" type="password" size="large"/>
    </div>
    <div class="login-form-item">
    <el-button type="primary" @click="onSubmit" size="large">登录</el-button>
    </div>

    <div class="login-form-item">
      <router-link to="/regist">没有账号？点此注册</router-link>
    </div>
  </el-form>

</template>

<script>
import {ElMessage} from "element-plus";
import serviceApi from "@/services/serviceApi";
import {useGlobalData} from "@/services/globalData";

export default {
  name: "LoginComp",
  data(){
    return{
      formData: {
        username: '',
        password: ''
      },
      userData: useGlobalData()
    }
  },
  methods: {
    onSubmit() {
      serviceApi.TryLogin(this.formData)
          .then(response => {
            var result = serviceApi.GetApiResult(response)
            this.userData.setIsLogin(serviceApi.GetApiResult(response))
            if(result){
              this.userData.setUserName(this.formData.username)
              ElMessage({
                message: "登录成功",
                type: 'success'
              })
              this.$router.push('/')
            }else{
              ElMessage({
                message: serviceApi.GetApiResultExplain(response),
                type: 'error'
              })
            }
          })
    }
  }
}

</script>

<style scoped>
.login-form{
  width: 400px;
  height: 320px;
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

router-link{
  font-size: 15px;
  color: lightgrey;
}
a{
  font-size: 15px;
  color: lightgrey;
}

</style>