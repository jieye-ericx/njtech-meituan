<template>
  <div>
    <el-form ref="form" :model="form" label-width="80px">
      <el-form-item label="管理员"></el-form-item>
      <el-form-item label="用户名">
        <el-input type="textarea" v-model="form.name"></el-input>
      </el-form-item>
      <el-form-item label="密码">
        <el-input type="textarea" v-model="form.password"></el-input>
      </el-form-item>
      <el-form-item>
        <el-button type="primary" @click="login">登录</el-button>
        <router-link tag="div" to="/foodslist">
          <el-button>取消</el-button>
        </router-link>
      </el-form-item>
    </el-form>
  </div>
</template>

<script>
export default {
  props: {},
  data() {
    return {
      form: {
        name: "",
        password: ""
      }
    };
  },
  methods: {
    login() {
        this.$store.commit('managerLogin');
    }
  }
};
</script>

<style scoped lang="scss">
.el-input,
.el-form-item {
  width: 500px;
}
</style>
