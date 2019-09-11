<template>
  <div>
    <el-row>
      <el-col :span="16" :offset="5">
        <el-table :data="tableData" stripe style="width: 100%">
          <el-table-column  label="用户名称" width="180">
            <template slot-scope="scope">
              <span style="margin-left: 10px">{{ scope.row.fields.customer_nickname }}</span>
            </template>
          </el-table-column>
          <el-table-column  label="团购名称" width="180">
            <template slot-scope="scope">
              <span style="margin-left: 10px">{{ scope.row.fields.food_name }}</span>
            </template>
          </el-table-column>
          <el-table-column  label="备注" width="140">
            <template slot-scope="scope">
              <span>{{ scope.row.fields.content }}</span>
            </template>
          </el-table-column>
          <el-table-column  label="时间" width="210">
            <template slot-scope="scope">
              <span>{{ scope.row.fields.create_time|dateFormat }}</span>
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
    this.getAllComs();
  },
  data() {
    return {
      tableData: [
      ]
    };
  },
  methods: {
    getAllComs() {
      this.$http.get("api/get_all_complaints").then(result => {
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
