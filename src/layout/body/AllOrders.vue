<template>
  <div>
    <el-row>
      <el-col :span="16" :offset="3">
        <el-table :data="tableData" stripe style="width: 100%">
          <el-table-column prop="user" label="用户名" width="180"></el-table-column>
          <el-table-column prop="purchase_name" label="购买美食名称" width="180"></el-table-column>
          <el-table-column prop="content" label="内容" width="180"></el-table-column>
          <el-table-column prop="create_time" label="投诉时间" width="180"></el-table-column>
        </el-table>
      </el-col>
    </el-row>
  </div>
</template>

<script>
export default {
  props: {},
  created() {
    this.getAllComplaint();
  },
  data() {
    return {
      tableData: [
        {
          id: "",
          purchase_name: "",
          user: "", //用户的用户名
          content: "",
          create_time: ""
        }
      ]
    };
  },
  methods: {
    getAllComplaint() {
      this.$http.get("api/get_all_complaint").then(result => {
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
