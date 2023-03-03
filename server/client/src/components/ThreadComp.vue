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
</template>

<script>
export default {
  name: "ThreadComp",
  data() {
    return {
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
      ]
    }
  }
}
</script>

<style scoped>
#thread-body{
  width: 90%;
  margin: auto;
}
</style>