<template>
  <div id="thread-body">
    <el-table :data="tableData" >
      <el-table-column prop="title" label="标题" align="left">
        <template #default="scope">
          <router-link v-bind:to='"/topic/"+scope.row.id'>{{scope.row.title}}</router-link>
        </template>
      </el-table-column>
      <el-table-column prop="name" label="用户" width="180" align="left" />
      <el-table-column prop="date" label="日期" width="180" align="left"/>

    </el-table>
  </div>

  <el-card class="create-topic-card">
    <template #header>
      <div class="card-header">
        <span>发表新主题</span>
      </div>
    </template>
    <el-input v-model="formData.title" placeholder="标题"/>
    <div style="margin: 5px 0" />
    <el-input
        v-model="formData.article"
        :autosize="{ minRows: 4}"
        type="textarea"
        placeholder="内容"
    />
    <div style="margin: 5px 0" />
    <el-button type="primary" @click="submitNewTopic" :disabled="!userData.isLogin">发布</el-button>
  </el-card>
</template>

<script>
import serviceApi from "@/services/serviceApi";
import {ElMessage} from "element-plus";
import {useGlobalData} from "@/services/globalData";

export default {
  name: "ThreadComp",
  data() {
    return {
      formData: {
        title: '',
        article: ''
      },
      tableData: [
        {
          date: '2023-03-02',
          name: 'LT_',
          title: '测试测试',
          id: 0
        },
        {
          date: '2023-03-02',
          name: 'lrsoft',
          title: 'Hello world',
          id: 1
        }
      ],
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