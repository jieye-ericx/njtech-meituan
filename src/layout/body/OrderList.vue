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
          <el-table-column width="180">
            <template slot-scope="scope">
              <el-button size="mini" @click="sendComplaint(scope.$index, scope.row)">投诉</el-button>
            </template>
          </el-table-column>
        </el-table>
      </el-col>
    </el-row>

    <el-dialog title="投诉" :visible.sync="dialogFormVisible">
      <el-form :model="form">
        <el-form-item label="投诉内容：" :label-width="formLabelWidth">
          <el-input v-model="form.content" autocomplete="off"></el-input>
        </el-form-item>
      </el-form>
      <div slot="footer" class="dialog-footer">
        <el-button @click="dialogFormVisible = false">取 消</el-button>
        <el-button type="primary" @click="clickOk">确 定</el-button>
      </div>
    </el-dialog>
  </div>
</template>

<script>
export default {
  props: {},
  data() {
    return {
      tableData: [
        {
          id: "2",
          date: "2016-05-02 13:22",
          name: "大保健套餐",
          num: "2",
          total: "1000",
          remark: "要开发票"
        }
      ],
      dialogFormVisible: false,
      formLabelWidth: '120px',
      form: {
        content: "",
        uid:this.$store.getters.getUserId,
        purchase_order_id:''
      }
    };
  },
  methods: {
    sendComplaint(index, row) {
      this.dialogFormVisible = true;
      // console.log(index, row);
      this.form.purchase_order_id=row.id
    },
    clickOk() {
      this.dialogFormVisible = false;
      this.$http
        .get(
          "api/add_complaints?purchase_order_id=" +
            this.form.purchase_order_id +
            "&customer_id=" +
             this.form.uid+
            "&content=" +
            this.form.content
        )
        .then(result => {
          if (result.body.error_num == 0) {
            this.$message({
              type: "info",
              message: "添加成功"
            });
          } else {
            this.$message({
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
