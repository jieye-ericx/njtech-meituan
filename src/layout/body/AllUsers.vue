<template>
  <div>
    <el-row>
      <el-col :span="16" :offset="3">
        <el-table :data="tableData" stripe style="width: 100%">
          <el-table-column prop="name" label="用户名" width="180"></el-table-column>
          <el-table-column prop="phone" label="电话" width="180"></el-table-column>
          <el-table-column prop="sex" label="性别" width="180"></el-table-column>
          <el-table-column prop="passport" label="身份证" width="180"></el-table-column>
          <el-table-column prop="create_time" label="创建时间"></el-table-column>
          <el-table-column label="操作">
            <template slot-scope="scope">
              <el-button size="mini" type="danger" @click="handleDelete(scope.$index, scope.row)">删除</el-button>
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
    this.getAllUsers();
  },
  data() {
    return {
      tableData: [
        {
          id: "",
          name: "",
          phone: "",
          sex: "",
          passport: "",
          create_time: ""
        }
      ]
    };
  },
  methods: {
    getAllUsers() {
      this.$http.get("api/get_all_users").then(result => {
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
    },
    handleDelete(index, row) {
      this.$http
        .get("api/delete_customer?mobile_phone=" + row.phone)
        .then(result => {
          if (result.body.error_num === 0) {
            this.$message({
              duration: 1000,
              type: "info",
              message: "删除成功"
            });
            this.getAllUsers();
            // console.log(result.body);
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
