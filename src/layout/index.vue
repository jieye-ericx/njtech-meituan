<template>
  <div>
    <div>
      <MainHeader></MainHeader>
      <Footer></Footer>
    </div>
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