<template>
  <div>
    <el-container direction="vertical">
      <MainHeader></MainHeader>
      <el-container>
        <Aside></Aside>
        <FoodsList></FoodsList>
      </el-container>
      <Footer></Footer>
    </el-container>
  </div>
</template>

<style lang="scss" scoped>
.el-container {
  height: 500px;
  border: 1px solid #d6d6d6;
}
</style>

<script>
import MainHeader from "@/layout/header/MainHeader.vue";
import Footer from "@/layout/footer/Footer.vue";

export default {
  data() {
    return {};
  },
  components: {
    MainHeader,
    Footer,
  },
  methods: {}
};
</script>