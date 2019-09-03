<template>
  <div>
    <el-header>
      <el-menu
        :default-active="activeIndex2"
        class="el-menu-demo"
        mode="horizontal"
        @select="handleSelect"
        background-color="#323232"
        text-color="#fff"
        active-text-color="#ffd04b"
      >
        <el-menu-item index="1">
          <router-link tag="div" to="/foodslist">
            <span>美食团购</span>
          </router-link>
        </el-menu-item>
        <el-menu-item index="2">
          <router-link to="/" tag="div">
            <span>未命名</span>
          </router-link>
        </el-menu-item>
        <el-menu-item index="3">
          <router-link to="/cart" tag="div">
            <span>购物车</span>
          </router-link>
        </el-menu-item>
        <el-menu-item index="4">
          <router-link to="/orderlist" tag="div">
            <span>我的订单</span>
          </router-link>
        </el-menu-item>
        <span class="login-regiest">登陆</span>
        <span class="login-regiest">|</span>
        <span class="login-regiest">注册</span>
      </el-menu>
    </el-header>
    <transition>
      <router-view></router-view>
    </transition>
  </div>
</template>

<script>
export default {
  methods: {
    handleSelect(key, keyPath) {
      console.log(key, keyPath);
    }
  },
  data() {
    return {
      activeIndex: "1",
      activeIndex2: "1"
    };
  }
};
</script>

<style lang="scss" scoped>
.el-header {
  height: 60px;
  padding: 0 0px;
  background-color: #323232;
  color: #333;
  line-height: 60px;
  margin: -1px;
  span{
    font-size: 18px;
  }
  .login-regiest {
    color: #f3f3f3;
    float: right;
    margin-right: 10px;
    line-height: 60px;
  }
}
.v-enter {
  opacity: 0;
  transform: translateX(100%);
}
.v-leave-to {
  opacity: 0;
  transform: translateX(-100%);
  position: absolute;
}
.v-enter-active,
.v-leave-active {
  transition: all 0.5s ease;
}
</style>