<template>
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
            <span style="margin-left: 10px">{{ scope.row.name }}</span>
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
            <span>{{scope.row.totalPrice}}</span>
            <!-- <el-button size="mini" @click="handleEdit(scope.$index, scope.row)">编辑</el-button>
            <el-button size="mini" type="danger" @click="handleDelete(scope.$index, scope.row)">删除</el-button>-->
          </template>
        </el-table-column>
        <el-table-column></el-table-column>
      </el-table>
    </el-col>
  </el-row>
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
        {
          date: "2016-05-02",
          name: "大保健套餐",
          quantity: "2",
          price: "100",
          totalPrice: "200",
          isselected: "0"
        },
        {
          date: "2016-05-02",
          name: "大保健套餐",
          quantity: "2",
          price: "100",
          totalPrice: "200",
          isselected: "0"
        },
        {
          date: "2016-05-02",
          name: "大保健套餐",
          quantity: "2",
          price: "100",
          totalPrice: "200",
          isselected: "0"
        },
        {
          date: "2016-05-02",
          name: "大保健套餐",
          quantity: "2",
          price: "100",
          totalPrice: "200",
          isselected: "0"
        }
      ],
      minNum: 1
    };
  },
  methods: {
    getSummaries(param) {
      const { columns, data } = param;
      const sums = [];
      console.log(data);
      sums[0]='总计'
      sums[5]='';
      var sum=0
      data.forEach(element => {
        sum+=Number(element.totalPrice)
      });
      sums[5]+=sum.toString()
      // columns.forEach((column, index) => {
      //   if (index === 0) {
      //     sums[index] = "总价";
      //     return;
      //   }
        // if (index === 5) {
        //   const values = data.map(item => Number(item[column.property]));
        //   if (!values.every(value => isNaN(value))) {
        //     sums[index] = values.reduce((prev, curr) => {
        //       const value = Number(curr);
        //       if (!isNaN(value)) {
        //         return prev + curr;
        //       } else {
        //         return prev;
        //       }
        //     }, 0);
        //     sums[index] += " 元";
        //   } else {
        //     sums[index] = "";
        //   }
        // }
      // });

      return sums;
    }
  }
};
</script>