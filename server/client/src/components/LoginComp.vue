<template>
  <el-form class="login-form">
    <el-form-item />
      <p>登录</p>
    <el-form-item>
      <el-input v-model="form.username" placeholder="用户名" />
    </el-form-item>
    <el-form-item>
      <el-input v-model="form.password" placeholder="密码" type="password" />
    </el-form-item>
    <el-form-item>
      <el-input v-model="form.cert" placeholder="验证码"/>
    </el-form-item>
    <el-form-item>
      <el-button type="primary" @click="onSubmit" size="large">登录</el-button>
    </el-form-item>
  </el-form>
</template>

<script>
import { reactive } from 'vue'
export default {
  name: "LoginComp",
  data(){
    return{
      form: reactive({
        username: '',
        password: '',
        cert: ''
      })
    }
  },
  methods:{
    onSubmit(){
      alert(this.form.username + " " + this.form.password + " " + this.form.cert)
    }
  }
}

</script>

<style scoped>
.login-form{
  width: 480px;
  height: 400px;
  margin: 120px auto;
  text-align: center;
}
p{
  font-size: 28px;
}
el-form-item{
  width: 80%;
}
</style>