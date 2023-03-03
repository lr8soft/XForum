<template>
  <div id="info-box">
    <p id="info-area">
      页面不存在 <br/>
      404 Page Not Found
    </p>
  </div>

</template>

<script>
export default {
  name: "PageNotFoundComp"
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