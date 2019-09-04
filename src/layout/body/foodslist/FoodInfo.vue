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
        <h1 style="text-align:left;margin-bottom:0;">{{goodInfo.title}}</h1>
        <h2 style="margin-top:5px;">RMB {{goodInfo.price}}</h2>
        <el-tag type="info">{{goodInfo.tag}}</el-tag>
        <div style="margin-top:25px;display:flex;justify-content:space-between;">
          <el-input-number size="mini" v-model="num"></el-input-number>
          <el-button type="primary" plain size="small" style="height:80%;">加入购物袋</el-button>
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
        <el-collapse  >
          <el-collapse-item title="查看详情" name="1">
            <div>与现实生活一致：与现实生活的流程、逻辑保持一致，遵循用户习惯的语言和概念；</div>
            <div>在界面中一致：所有的元素和结构需保持一致，比如：设计样式、图标和文本、元素的位置等。</div>
          </el-collapse-item>
          <el-collapse-item title="评论" name="2">
            <div>控制反馈：通过界面样式和交互动效让用户可以清晰的感知自己的操作；</div>
            <div>页面反馈：操作后，通过页面元素的变化清晰地展现当前状态。</div>
          </el-collapse-item>
          
        </el-collapse>
      </el-col>
    </el-row>
  </div>
</template>

<script>
export default {
  data() {
    return {
      id: this.$route.params.id,
      goodInfo: {
        title: "汉堡汉堡汉堡汉堡汉堡汉堡汉堡汉堡汉堡汉堡汉堡汉堡",
        price: "661",
        tag: "快餐",
        detail:
          "有了这款无线充电盒，只需将 AirPods 放入盒中，然后将充电盒放在兼容 Qi 标准的充电器上，即可轻松充电，易如反掌。充电盒正面的 LED 指示灯能显示 AirPods 的充电状态。如果无线充电器没在身边，你也可以通过闪电端口充电。这款无线充电盒适用于各代 AirPods，并能存储额外电量为耳机充电多次。"
      },
      num: 1
    };
  },
  methods: {
    goBack() {
      console.log("go back");
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