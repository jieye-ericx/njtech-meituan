<template>
  <div>
    <el-row>
      <el-col :span="16" :offset="4">
        <el-form class="form" ref="form" :model="form" label-width="80px">
          <el-form-item label="用户名">
            <el-input type="textarea" v-model="form.name"></el-input>
          </el-form-item>
          <el-form-item label="密码">
            <el-input type="password" v-model="form.password"></el-input>
          </el-form-item>
          <el-form-item>
            <el-button type="primary" @click="login">登录</el-button>
            <el-button @click="cancel">取消</el-button>
          </el-form-item>
        </el-form>
      </el-col>
    </el-row>
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
      this.$http
        .post(
          "api/admin_login",
          {
            name: this.form.name,
            pswd: this.form.password
          },
          { emulateJSON: true }
        )
        .then(result => {
          console.log(result);

          if (result.body.error_num === 0) {
            this.$store.commit("managerLogin");
            this.$message({
              type: "info",
              message: "管理员登陆成功"
            });
          } else {
            this.dialog1 = false;
            this.$message({
              type: "error",
              message: "登陆失败"
            });
          }
        });
    },
    cancel(){
      this.$router.go('/foodslist')
    }
  }
};
</script>

<style scoped lang="scss">
.form {
  margin-top: 30px;
}
.el-input,
.el-form-item {
  width: 300px;
  height: 50%;
}
</style>
