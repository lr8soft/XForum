<template>
  <div id="topic-body">
    <el-header>
      <el-breadcrumb separator="/">
        <el-breadcrumb-item :to="{ path: '' }">测试大版A</el-breadcrumb-item>
        <el-breadcrumb-item><a href="">测试板块1</a></el-breadcrumb-item>
        <el-breadcrumb-item>{{ title }}</el-breadcrumb-item>
      </el-breadcrumb>
    </el-header>

    <el-main>
      <el-card class="box-card">
        <template #header>
          <div class="card-header">
            <span>{{title}}</span>
          </div>
        </template>

        <el-container>
          <el-aside class="user-plate">
            <el-image class="avatar-image" :src="avatar" fit="fill">
              <template #error>
                <el-image class="avatar-image" :src="require('@/assets/defaultAvatar.png')" fit="fill"/>
              </template>
            </el-image>
            <p>{{author}}</p>
          </el-aside>
          <el-main>
              <p class="article-area">{{article}}</p>
          </el-main>
        </el-container>

      </el-card>
    </el-main>

  </div>
</template>

<script>

export default {
  name: "TopicComp",
  data(){
    return{
      title: "测试主题",
      article: "这是正文这是正文",
      author: "lrsoft",
      avatar: "upload/defaultAvatar.png",
      replies: [{
        author: "testuser1",
        avatar: "/upload/defaultAvatar.png",
        reply: "这是回复！</br>TEST!!!!!!!!"
      },
        {
        author: "testuser2",
        avatar: "/upload/defaultAvatar.png",
        reply: "Hello world!"
      }]
    }
  }
}
</script>

<style scoped>
#topic-body{
  width: 90%;
  margin: auto;
}

.box-card {
  width: 90%;
  margin: auto;
}

.card-header {
  justify-content: space-between;
  align-items: center;
  font-weight: bold;
}

.user-plate{
  width: 120px;
  height: 160px;
  padding-top: 20px;
  align-items: center;
  text-align: center;
}

.avatar-image{
  display: block;
  margin: 0 auto;
  width: 80px;
  height: 80px;
}

.article-area{
  width: 90%;
  margin: 0px auto;
}

</style>