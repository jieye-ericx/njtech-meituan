<template>
  <div>
    <el-row>
      <el-col :span="16" :offset="5">
        <el-table :data="tableData" stripe style="width: 100%">
          <el-table-column  label="用户名称" width="180">
            <template slot-scope="scope">
              <span style="margin-left: 10px">{{ scope.row.fields.customername }}</span>
            </template>
          </el-table-column>
          <el-table-column  label="团购名称" width="180">
            <template slot-scope="scope">
              <span style="margin-left: 10px">{{ scope.row.fields.foodname }}</span>
            </template>
          </el-table-column>
          <el-table-column  label="数量" width="60">
            <template slot-scope="scope">
              <span>{{ scope.row.fields.quantity }}</span>
            </template>
          </el-table-column>
          <el-table-column  label="备注" width="140">
            <template slot-scope="scope">
              <span>{{ scope.row.fields.remarks }}</span>
            </template>
          </el-table-column>
          <el-table-column  label="金额 RMB" width="110">
            <template slot-scope="scope">
              <span>{{ scope.row.fields.amount_money }}</span>
            </template>
          </el-table-column>
          <el-table-column  label="时间" width="210">
            <template slot-scope="scope">
              <span>{{ scope.row.fields.order_time|dateFormat }}</span>
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
  created() {
    this.getAllOrders();
  },
  data() {
    return {
      tableData: [
      ]
    };
  },
  methods: {
    getAllOrders() {
      this.$http.get("api/get_all_order").then(result => {
        // console.log(result.body)
        if (result.body.error_num === 0) {
          // console.log(result.body);
          this.tableData = result.body.list;
        } else {
          this.$message({
            duration: 1000,
            type: "error",
            message: "出错"
          });
        }
      });
    }
  }
};
</script>

<style scoped lang="scss">
</style>
