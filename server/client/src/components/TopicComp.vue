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

        <!--下面这堆是回复-->
        <el-table :data="replies" class="reply-table">
          <el-table-column>
            <template #default="scope">
              <el-container>
                <!--左边的用户信息区域-->
                <el-aside class="user-plate">
                  <el-image class="avatar-image" :src="scope.row.avatar" fit="fill">
                    <template #error>
                      <el-image class="avatar-image" :src="require('@/assets/defaultAvatar.png')" fit="fill"/>
                    </template>
                  </el-image>
                  <p class="author-info">{{ scope.row.author }}</p>
                  <p class="floor-info">{{ scope.row.floor + 1 }}#</p>
                </el-aside>
                <!--右边回复区域-->
                <el-main>
                  <p class="article-area">{{ scope.row.reply }}</p>
                </el-main>
              </el-container>
            </template>

          </el-table-column>
        </el-table>

      </el-card>
    </el-main>

  </div>
</template>

<script>

export default {
  name: "TopicComp",
  data(){
    return {
      title: "测试主题",
      replies: [
        {
          author: "lrsoft",
          avatar: "/upload/defaultAvatar.png",
          reply: "前面忘了，中间忘了，后面也忘了",
          floor: 0
        },{
        author: "testuser1",
        avatar: "/upload/defaultAvatar.png",
        reply: "这是回复！TEST!!!!!!!!",
        floor: 1
      },
        {
          author: "testuser2",
          avatar: "/upload/defaultAvatar.png",
          reply: "Hello world!",
          floor: 2
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

.reply-table{
  --el-table-border-color: none;
}

.user-plate{
  width: 120px;
  height: 200px;
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
  margin: auto;
}

.author-info{
  font-size: 16px;
  margin-top: 20px;
}

.floor-info{
  font-size: 14px;
  color: lightgrey;
}

</style>