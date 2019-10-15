<template>
  <div>
    <el-row style="margin-top:25px;">
      <el-col :span="16" :offset="4">
        <el-table :data="tableData" stripe style="width: 100%">
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
          <el-table-column  label="备注" width="180">
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
          <el-table-column label="操作" width="180">
            <template slot-scope="scope">
              <div>
                <el-button size="mini" @click="sendComplaint(scope.$index, scope.row)">投诉</el-button>
              </div>
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
  created() {
    this.getOrders();
  },
  data() {
    return {
      tableData: [],
      dialogFormVisible: false,
      formLabelWidth: "120px",
      form: {
        content: "",
        purchase_order_id: "",
        uid:''
      }
    };
  },
  computed: {
    isLogin: function() {
      return this.$store.getters.isLogin;
    },
    isManager: function() {
      return this.$store.getters.isManager;
    }
  },
  methods: {
    sendComplaint(index, row) {
      this.dialogFormVisible = true;
      this.form.purchase_order_id = row.pk;
    },
    clickOk() {
      this.dialogFormVisible = false;
      this.form.uid=this.$store.getters.userInfo.uid
      this.$http
        .get(
          "api/add_complaints?purchase_order_id=" +
            this.form.purchase_order_id +
            "&customer_id=" +
            this.form.uid +
            "&content=" +
            this.form.content
        )
        .then(result => {
          console.log(result);
          
          if (result.body.error_num == 0) {
            this.$message({
              duration: 1000,
              type: "info",
              message: "投诉成功"
            });
          } else {
            this.$message({
              duration: 1000,
              type: "error",
              message: "出错"
            });
          }
        });
    },
    getOrders() {
      this.$http
        .get("api/get_customer_order?id=" + this.$store.getters.userInfo.uid)
        .then(result => {
          if (result.body.error_num === 0) {
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
