<template>
  <div id="info-box">
    <p id="info-area">
      已登出 <br/>
      将自动返回首页
    </p>
  </div>

</template>

<script>
import serviceApi from "@/services/serviceApi";
import {useGlobalData} from "@/services/globalData";

export default {
  name: "LogoutComp",
  data(){
    return{
      userData: useGlobalData()
    }
  },
  mounted() {
    this.userData.setIsLogin(false)
    this.userData.setUserName('')
    serviceApi.GoLogout().then(()=>{
      setTimeout(()=>{
        this.$router.push('/')
      }, 1000)
    })
  }
}
</script>

<style scoped>
#info-box{
  width: 350px;
  height: 180px;
  margin: 120px auto;
  text-align: center;
  align-items: center;
  border-radius: 10px;
  border: 1px solid var(--el-border-color);
  box-shadow: var(--el-box-shadow-dark);
}
#info-area{
  font-size: 20px;
  margin: 60px auto;
}
</style>