<template>
  <div>
    <el-row style="margin-top:25px;">
      <el-col :span="16" :offset="5">
        <el-table :data="tableData" style="width: 100%" :summary-method="getSummaries" show-summary>
          <el-table-column label width="70">
            <template slot-scope="scope">
              <el-switch
                v-model="scope.row.isselected"
                active-color="#13ce66"
                inactive-color="#323232"
              ></el-switch>
            </template>
          </el-table-column>
          <el-table-column label="团购名称" width="180">
            <template slot-scope="scope">
              <i class="el-icon-s-order"></i>
              <span style="margin-left: 10px">{{ scope.row.food_id }}</span>
            </template>
          </el-table-column>
          <el-table-column label width="100">
            <template slot-scope="scope">
              <el-input-number
                style="width:85px;"
                :min="minNum"
                size="mini"
                v-model="scope.row.quantity"
              ></el-input-number>
            </template>
          </el-table-column>
          <el-table-column label="数量" width="60">
            <template slot-scope="scope">
              <span style="margin-left:7px;">{{ scope.row.quantity }}</span>
            </template>
          </el-table-column>
          <el-table-column label="单价" width="70">
            <template slot-scope="scope">
              <el-tag type="info" effect="plain" size="small">{{scope.row.price}}</el-tag>
              <!-- <el-button size="mini" @click="handleEdit(scope.$index, scope.row)">编辑</el-button>
              <el-button size="mini" type="danger" @click="handleDelete(scope.$index, scope.row)">删除</el-button>-->
            </template>
          </el-table-column>
          <el-table-column label="总价" width="70">
            <template slot-scope="scope">
              <span class="price">￥</span>
              <span>{{totalPrice(scope.row)}}</span>
              <!-- <el-button size="mini" @click="handleEdit(scope.$index, scope.row)">编辑</el-button>
              <el-button size="mini" type="danger" @click="handleDelete(scope.$index, scope.row)">删除</el-button>-->
            </template>
          </el-table-column>
          <el-table-column></el-table-column>
        </el-table>
      </el-col>
    </el-row>
    <el-row style="margin-top:25px;margin-bottom:10px;">
      <el-col :span="16" :offset="5" style="text-align:right">
        <el-button
          type="primary"
          plain
          style="width:100px;height:20px;line-height:1px;"
          @click="pushOrder"
        >结算</el-button>
      </el-col>
    </el-row>
  </div>
</template>

<style lang="scss" scoped>
.price {
  margin-left: -5px;
  font-weight: 800;
}
</style>
<script>
export default {
  data() {
    return {
      tableData: [
      ],
      minNum: 1
    };
  },
  created(){
    this.getData()
  },
  computed: {
    totalPrice: function() {
      return function(obj) {
        return obj.quantity * obj.price;
      };
    }
  },
  methods: {
    getSummaries(param) {
      const { columns, data } = param;
      const sums = [];
      // console.log(data);
      sums[0] = "总计";
      sums[4] = " RMB";
      sums[5] = "";
      var sum = 0;
      data.forEach(element => {
        sum += Number(element.quantity * element.price);
      });
      sums[5] += sum.toString();
      return sums;
    },
    pushOrder() {
      var orders = [];
      this.tableData.forEach(element => {
        if (element.isselected == true) {
          orders.push({ element, total: element.quantity * element.price });
          this.$http.get('api/add_purchase_order?food_id='+element.food_id
          +'&customer_id='+this.$store.getters.userInfo.uid
          +"&amount_money="+element.quantity * element.price
          +"&quantity="+element.quantity)
          .then(result=>{
            if(result.body.error_num!=0){
              this.$message({
                  duration: 1000,
                  type: "error",
                  message: "出错"
                });
            }else{
              console.log(1); 
            }
          })
        }
      });
      // console.log(orders);
    },
    getData() {
      this.$http
        .get(
          "api/get_shopping_cart_content?id=" + this.$store.getters.userInfo.uid
        )
        .then(result => {
          if (result.body.error_num === 0) {
            result.body.list.forEach(element => {
              var obj = element.fields;
              obj.id = element.pk;
              this.tableData.push(obj);
            });
          }
        });
    }
  }
};
</script>