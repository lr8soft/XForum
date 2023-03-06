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
            <span>{{ title }}</span>
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
        <div class="replies-pagination">
          <el-pagination
              v-model:current-page="currentPage"
              layout="prev, pager, next, jumper"
              :total="repliesCount"
              @size-change="handleSizeChange"
              @current-change="handleCurrentChange"
          />
        </div>

      </el-card>

      <!--这是用户回复区，一页显示10个回复-->
      <el-card class="create-reply-card">
        <template #header>
          <div class="card-header">
            <span>发表回复</span>
          </div>
        </template>
        <el-input
            v-model="replyInfo"
            :autosize="{ minRows: 4}"
            type="textarea"
            placeholder="发表你的看法"
        />
        <el-button class="create-reply-button" type="primary" @click="submitMessage">发布</el-button>
      </el-card>
    </el-main>

  </div>
</template>

<script>
import {ref} from "vue";
import {ElMessage} from "element-plus";

export default {
  name: "TopicComp",
  data(){
    return {
      title: "测试主题",
      currentPage: 1,
      repliesCount: 20,
      replyInfo: '',
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
  },
  methods:{
    handleSizeChange(val){
      console.log(`${val} items per page`)
    },
    handleCurrentChange(val){
      console.log(`current page: ${val}`)
    },
    submitMessage(){
      ElMessage({
        message: "发布成功",
        type: 'success'
      })
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

.create-reply-card{
  width: 90%;
  margin: 20px auto;
}

.create-reply-button{
  margin-top: 5px;
}

.card-header {
  justify-content: space-between;
  align-items: center;
  font-weight: bold;
}

.reply-table{
  --el-table-border-color: none;
}

.replies-pagination{
  align-items: center;
  margin: 5px auto;
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