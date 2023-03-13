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
                  <p class="floor-info">{{ scope.row.floor }}#</p>
                </el-aside>
                <!--右边回复区域-->
                <el-main style="position: relative;">
                  <RichTextComp class="article-area" v-model="scope.row.article" :editable="false"/>
                  <div class="article-info-area">
                    <div style="float:right;">
                      发布于 {{scope.row.date}}
                      <el-button
                          link type="primary"
                          v-if="(scope.row.author==userData.userName || author==userData.userName) && scope.row.floor > 1"
                          @click='DeleteReply(scope.row.id)'>删除</el-button>
                    </div>

                  </div>
                </el-main>
              </el-container>
            </template>
          </el-table-column>

        </el-table>
        <div class="replies-pagination">
          <el-pagination
              v-model:current-page="currentPage"
              layout="prev, pager, next, jumper"
              :page-count="pageCount"
              :page-size="pageItemCount"
              @current-change="handleCurrentChange"
          />
        </div>

      </el-card>

      <!--这是用户回复区-->
      <el-card class="create-reply-card">
        <template #header>
          <div class="card-header">
            <span>发表回复</span>
          </div>
        </template>

        <RichTextComp v-model="replyFormData.reply" />

        <el-button class="create-reply-button" type="primary" @click="submitMessage" :disabled="!userData.isLogin">发布</el-button>
      </el-card>
    </el-main>

  </div>
</template>

<script>
import {getCurrentInstance, onMounted, reactive, ref, shallowRef} from "vue";
import {ElMessage} from "element-plus";
import serviceApi from "@/services/serviceApi";
import {useRoute} from "vue-router";
import {useGlobalData} from "@/services/globalData";
import RichTextComp from "@/components/RichTextComp.vue";

export default {
  name: "TopicComp",
  computed: {
    serviceApi() {
      return serviceApi
    }
  },
  components: {RichTextComp},
  mounted() {
    const route = useRoute()
    var topicId = route.params.id
    this.replyFormData.id = topicId
    this.getPaginationReplies()
  },
  data(){
    return {
      title: "测试主题",
      author: '',
      currentPage: 1,
      pageCount: 0,
      pageItemCount: 0,
      repliesCount: 0,
      replies: [],
      replyFormData:{
        id: 0,
        reply: ''
      },
      userData: useGlobalData(),
      editorRef: shallowRef()
    }
  },
  methods:{
    handleCurrentChange(val){
      this.currentPage = val
      this.getPaginationReplies()
    },
    handleCreated(editor){
      this.editorRef.value = editor
    },
    getPaginationReplies(){
      // 读取主题下面的帖子
      serviceApi.GetPaginationReplies(this.replyFormData.id, this.currentPage).then(response=>{
        if(serviceApi.GetApiResult(response)){
          this.author = response.result.author
          this.title = response.result.title
          this.pageCount = response.result.pageCount
          this.pageItemCount = response.result.pageItemCount
          this.replies = response.result.replies
          this.repliesCount = response.result.replies.length
        }
      })
    },
    submitMessage(){
      // 在帖子下创建新回复
      serviceApi.CreateNewReply(this.replyFormData).then(response=>{
        if(serviceApi.GetApiResult(response)){
          ElMessage({
            message: "发布成功",
            type: 'success'
          })
        }else{
          ElMessage({
            message: serviceApi.GetApiResultExplain(response),
            type: 'error'
          })
        }
      })
    },
    DeleteReply(Id){
      serviceApi.DeleteReply(Id).then((response)=>{
        if(serviceApi.GetApiResult(response)){
          ElMessage({
            message: "回复已删除",
            type: 'success'
          })
          this.$router.go(0)
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

.article-info-area{
  position: absolute;
  width: 90%;
  bottom: 0;
  right: 0;
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