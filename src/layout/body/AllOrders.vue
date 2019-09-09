<template>
  <div>
    <el-row>
      <el-col :span="16" :offset="3">
        <el-table :data="tableData" stripe style="width: 100%">
          <el-table-column prop="date" label="日期" width="180"></el-table-column>
          <el-table-column prop="name" label="姓名" width="180"></el-table-column>
          <el-table-column prop="address" label="地址"></el-table-column>
        </el-table>
      </el-col>
    </el-row>
  </div>
</template>

<script>
export default {
  props: {},
  data() {
    return {
      tableData: [ 
      ]
    };
  },
  methods: {}
};
</script>

<style scoped lang="scss">
</style>
