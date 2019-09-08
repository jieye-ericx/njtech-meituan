<template>
  <div>
    <el-row>
      <el-col :span="16" :offset="3">
        <!-- <h1 style="text-align:left;margin-bottom:0;">团购详情</h1> -->
        <el-page-header @back="goBack" content="团购详情" style="margin-top:30px;"></el-page-header>
        <el-divider content-position="left">工大美团</el-divider>
      </el-col>
    </el-row>
    <el-row>
      <el-col :span="8" :offset="3" style="text-align:left">
        <h1 style="text-align:left;margin-bottom:0;">{{foodInfo.name}}</h1>
        <h2 style="margin-top:5px;">RMB {{foodInfo.amount_money}}</h2>
        <el-tag type="info">{{foodInfo.category_id}}</el-tag>
        <div style="margin-top:25px;display:flex;justify-content:space-between;">
          <el-input-number size="mini" v-model="num" :min="1"></el-input-number>
          <el-button type="primary" plain size="small" style="height:80%;" @click="addToCart">加入购物袋</el-button>
        </div>
      </el-col>
      <el-col :span="12" :push="3">
        <el-carousel :interval="4000" type="card" height="200px" arrow="never">
          <el-carousel-item v-for="item in 4" :key="item">
            <img
              src="https://shadow.elemecdn.com/app/element/hamburger.9cf7b091-55e9-11e9-a976-7f4d0b07eef6.png"
              alt
            />
          </el-carousel-item>
        </el-carousel>
      </el-col>
    </el-row>
    <el-row>
      <el-col :span="20" :offset="3" style="margin-top:80px;">
        <el-collapse>
          <el-collapse-item title="查看详情" name="1">
            <div>{{foodInfo.introduction}}</div>

          </el-collapse-item>
          <el-collapse-item title="评论" name="2">

          </el-collapse-item>
        </el-collapse>
      </el-col>
    </el-row>
  </div>
</template>

<script>
export default {
  created() {
    this.$http.get("api/get_food_info?id=" + this.$route.params.id).then(result => {
              console.log(result.body);

      if (result.body.error_num == 0) {
        console.log(result.body);
        
        this.foodInfo = result.body.list[0].fields;
      } else {
        this.$message({
          duration:1000,
          type: "error",
          message: "出错"
        });
      }
    });
  },
  data() {
    return {
      foodInfo: {},
      num: 1
    };
  },
  methods: {
    goBack() {
      console.log("go back");
      this.$router.go(-1);
    },
    addToCart() {
      var user =
        this.$store.getters.getUserInfo != null
          ? this.$store.getters.getUserInfo
          : null;
      if (null == user) {
        console.log("未登录需要登陆");
        return;
      }
      // console.log(user);

      var cartRecord = {
        uid: user.uid,
        id: this.$route.params.id,
        isSelected: true,
        quantity: this.num,
        price: this.foodInfo.amount_money,
        time: new Date()
      };
      this.$store.commit("addToCart", cartRecord);
    }
  }
};
</script>

<style lang="scss" scoped>
.el-carousel {
  width: 480px;
  //   .el-carousel-item {
  //     height: 200px;
  //     width: 200px;
  //   }
}
// .el-carousel__item h3 {
//   color: #475669;
//   font-size: 14px;
//   opacity: 0.75;
//   line-height: 200px;
//   margin: 0;
// }

// .el-carousel__item:nth-child(2n) {
//   background-color: #99a9bf;
// }

// .el-carousel__item:nth-child(2n + 1) {
//   background-color: #d3dce6;
// }
</style>