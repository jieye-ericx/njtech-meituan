<template>
  <div>
    <el-row>
      <el-col :span="16" :offset="5">
        <el-table :data="tableData" stripe style="width: 100%">
          <el-table-column label="用户名" width="180">
            <template slot-scope="scope">
              <span>{{ scope.row.fields.nickname }}</span>
            </template>
          </el-table-column>
          <el-table-column label="电话" width="100">
            <template slot-scope="scope">
              <span>{{ scope.row.fields.mobile_phone }}</span>
            </template>
          </el-table-column>
          <el-table-column label="性别" width="60">
            <template slot-scope="scope">
              <span>{{ scope.row.fields.sex==1? "男":"女" }}</span>
            </template>
          </el-table-column>
          <el-table-column label="身份证" width="180">
            <template slot-scope="scope">
              <span>{{ scope.row.fields.passport }}</span>
            </template>
          </el-table-column>
          <el-table-column label="创建时间">
            <template slot-scope="scope">
              <span>{{ scope.row.fields.create_time|dateFormat }}</span>
            </template>
          </el-table-column>
          <el-table-column label="状态">
            <template slot-scope="scope">
              <span>{{ scope.row.fields.isdeleted==1? "已删除":"正常"}}</span>
            </template>
          </el-table-column>
          <el-table-column label="操作">
            <template slot-scope="scope">
              <el-button :disabled="scope.row.fields.isdeleted==1" size="mini" type="danger" @click="handleDelete(scope.$index, scope.row)">删除</el-button>
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
          create_time: "",
          isdelete: ""
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
      console.log(row);
      this.$http
        .get("api/delete_customer?mobile_phone=" + row.fields.mobile_phone)
        .then(result => {
          console.log(result);
          
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
