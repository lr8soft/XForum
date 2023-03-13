<template>
  <div id="thread-body">
    <el-table :data="topicData" >
      <el-table-column prop="title" label="标题" align="left">
        <template #default="scope">
          <router-link v-bind:to='"/topic/"+scope.row.id'>{{scope.row.title}}</router-link>
        </template>
      </el-table-column>
      <el-table-column prop="author" label="用户" width="180" align="left" />
      <el-table-column prop="date" label="日期" width="240" align="left">
        <template #default="scope">
          {{dayjs(scope.row.date).format("YYYY-MM-DD HH:mm:ss")}}
        </template>
      </el-table-column>

    </el-table>

    <div style="margin: 10px 0">
      <el-pagination
          v-model:current-page="currentPage"
          background
          layout="prev, pager, next, jumper"
          :page-count="pageCount"
          :page-size="pageItemCount"
          @current-change="handleCurrentChange"
      />
    </div>
  </div>

  <el-card class="create-topic-card">
    <template #header>
      <div class="card-header">
        <span>发表新主题</span>
      </div>
    </template>
    <el-input v-model="formData.title" placeholder="标题"/>
    <div style="margin: 5px 0" />
    <RichTextComp v-model="formData.article" />
    <div style="margin: 5px 0" />
    <el-button type="primary" @click="submitNewTopic" :disabled="!userData.isLogin">发布</el-button>
  </el-card>
</template>

<script>
import serviceApi from "@/services/serviceApi";
import {ElMessage} from "element-plus";
import {useGlobalData} from "@/services/globalData";
import RichTextComp from "@/components/RichTextComp.vue";
import dayjs from "dayjs";

export default {
  name: "ThreadComp",
  computed: {
    dayjs() {
      return dayjs
    }
  },
  components: {RichTextComp},
  mounted() {
    this.handlePageChange()
  },
  data() {
    return {
      currentPage: 1,
      pageCount: 0,
      pageItemCount: 0,
      formData: {
        title: '',
        article: ''
      },
      topicData: [],
      userData: useGlobalData()
    }
  },
  methods: {
    submitNewTopic() {
      serviceApi.CreateNewTopic(this.formData).then(response =>{
        var result = serviceApi.GetApiResult(response)
        if(result){
          ElMessage({
            message: "发布成功",
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
    },
    handleCurrentChange(val){
      this.currentPage = val
      this.handlePageChange()
    },
    handlePageChange(){
      // 默认读取currentPage页
      serviceApi.GetPaginationTopics(this.currentPage).then(response=>{
        var result = serviceApi.GetApiResult(response)
        if(result){
          this.pageCount = response.result.pageCount
          this.pageItemCount = response.result.pageItemCount
          this.topicData = response.result.topics
        }
      })
    }
  }
}
</script>

<style scoped>
#thread-body{
  width: 90%;
  margin: auto;
}

.create-topic-card{
  width: 90%;
  margin: 20px auto;
}

.card-header {
  justify-content: space-between;
  align-items: center;
  font-weight: bold;
}
</style>