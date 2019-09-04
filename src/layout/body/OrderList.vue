<template>
  <div>
    <el-row style="margin-top:25px;">
      <el-col :span="16" :offset="5">
        <el-table :data="tableData" stripe style="width: 100%">
          <el-table-column prop="name" label="团购名称" width="180"></el-table-column>
          <el-table-column prop="num" label="数量" width="60"></el-table-column>
          <el-table-column prop="date" label="时间" width="180"></el-table-column>
          <el-table-column prop="remark" label="备注" width="180"></el-table-column>
          <el-table-column prop="total" label="金额 RMB" width="110"></el-table-column>
          <el-table-column  width="180">
            <template slot-scope="scope">
              <el-button size="mini" @click="sendComplaint(scope.$index, scope.row)">投诉</el-button>
            </template>
          </el-table-column>
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
        {
          date: "2016-05-02 13:22",
          name: "大保健套餐",
          num: "2",
          total: "1000",
          remark: "要开发票"
        }
      ]
    };
  },
  methods: {
    sendComplaint(index, row) {
      // console.log(index, row);
    }
  }
};
</script>

<style scoped lang="scss">
</style>
