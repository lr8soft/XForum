<template>
  <div id="thread-body">
    <el-table :data="tableData">
      <el-table-column prop="title" label="标题"/>
      <el-table-column prop="date" label="日期" width="180" />
      <el-table-column prop="name" label="用户" width="180" />
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
        },
        {
          date: '2023-03-02',
          name: 'lrsoft',
          title: 'Hello world',
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