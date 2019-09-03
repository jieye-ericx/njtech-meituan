<template>
  <div>
    <el-table :data="tableData" stripe style="width: 100%">
      <el-table-column prop="name" label="团购名称" width="180"></el-table-column>
      <el-table-column prop="num" label="数量"></el-table-column>
      <el-table-column prop="date" label="时间" width="180"></el-table-column>
      <el-table-column prop="remark" label="备注" width="180"></el-table-column>
      <el-table-column prop="total" label="金额" width="180"></el-table-column>
    </el-table>
  </div>
</template>

<script>
export default {
  props: {},
  data() {
    return {
      tableData: [
        {
          date: "2016-05-02",
          name: "大保健套餐",
          num:"2",
          total:"1000",
          remark:"要开发票"
        }
      ]
    };
  },
  methods: {}
};
</script>

<style scoped lang="scss">
</style>
