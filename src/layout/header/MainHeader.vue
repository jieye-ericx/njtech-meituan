<template>
  <div>
    <el-header height="44px">
      <el-menu
        :default-active="activeIndex2"
        class="el-menu-demo"
        mode="horizontal"
        @select="handleSelect"
        background-color="#323232"
        text-color="#fff"
        active-text-color="rgb(181,181,181)"
        style="height:44px;margin-left:20%;"
      >
        <el-menu-item index="0">
          <router-link to="/foodslist" tag="div">
            <i class="el-icon-platform-eleme" style="color:#fff;"></i>
          </router-link>
        </el-menu-item>
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
        <div v-if="!this.$store.getters.isLogin">
          <span class="login-register" @click="dialog1 = true">登陆</span>
          <span class="login-register">|</span>
          <span class="login-register" @click="dialog = true">注册</span>
        </div>
        <div v-if="this.$store.getters.isLogin">
          <span class="login-register" @click="quit">退出</span>
        </div>
      </el-menu>
    </el-header>

    <el-drawer
      title="欢迎注册工大美团"
      :before-close="pushRegeistr"
      :visible.sync="dialog"
      direction="rtl"
      custom-class="register-drawer"
      ref="drawer"
    >
      <div class="drawer__content">
        <el-form :model="form">
          <el-form-item label="昵称" :label-width="formLabelWidth">
            <el-input v-model="form.nickName" autocomplete="off"></el-input>
          </el-form-item>
          <el-form-item label="密码" :label-width="formLabelWidth">
            <el-input v-model="form.password" autocomplete="off"></el-input>
          </el-form-item>
          <el-form-item label="性别" :label-width="formLabelWidth">
            <el-radio v-model="form.sex" label="0">男</el-radio>
            <el-radio v-model="form.sex" label="1">女</el-radio>
          </el-form-item>
          <el-form-item label="手机号" :label-width="formLabelWidth">
            <el-input v-model="form.mobilePhone" autocomplete="off"></el-input>
          </el-form-item>
          <el-form-item label="身份证号" :label-width="formLabelWidth">
            <el-input v-model="form.passport" autocomplete="off"></el-input>
          </el-form-item>
        </el-form>
        <div class="drawer__footer">
          <el-button @click="dialog = false">取 消</el-button>
          <el-button
            type="primary"
            @click="$refs.drawer.closeDrawer()"
            :loading="loading"
          >{{ loading ? '提交中 ...' : '确 定' }}</el-button>
        </div>
      </div>
    </el-drawer>

    <el-drawer
      title="欢迎登录工大美团"
      :before-close="pushLogin"
      :visible.sync="dialog1"
      direction="rtl"
      custom-class="register-drawer"
      ref="drawer"
    >
      <div class="drawer__content">
        <el-form :model="form">
          <el-form-item label="手机号" :label-width="formLabelWidth">
            <el-input v-model="form.nickName" autocomplete="off"></el-input>
          </el-form-item>
          <el-form-item label="密码" :label-width="formLabelWidth">
            <el-input v-model="form.password" autocomplete="off"></el-input>
          </el-form-item>
        </el-form>
        <div class="drawer__footer">
          <el-button @click="dialog1 = false">取 消</el-button>
          <el-button
            type="primary"
            @click="$refs.drawer.closeDrawer()"
            :loading="loading1"
          >{{ loading ? '提交中 ...' : '确 定' }}</el-button>
        </div>
      </div>
    </el-drawer>

    <transition>
      <router-view></router-view>
    </transition>
  </div>
</template>

<script>
import { log } from "util";
export default {
  methods: {
    handleSelect(key, keyPath) {
      // console.log(key, keyPath);
    },
    pushRegeistr(done) {
      this.$confirm("确定要提交表单吗？")
        .then(_ => {
          this.loading = true;
          this.$http
            .get(
              "api/register_account?mobile_phone=" +
                this.form.mobilePhone +
                "&sex=" +
                this.form.sex +
                "&nickname=" +
                this.form.nickName +
                "&passport=" +
                this.form.passport +
                "&password=" +
                this.form.password +
                "&avatar=" +
                this.form.avatar
            )
            .then(result => {
              // console.log(result);
              if (result.body.error_num == 0) {
                this.loading = false;
                this.$message({
                  type: "info",
                  message: "注册成功，请登录"
                });
              } else {
                this.loading = false;
                this.$message({
                  type: "info",
                  message: "注册不成功，请重试"
                });
              }
            });
        })
        .catch(_ => {
          this.dialog = false;
          this.$message({
            type: "info",
            message: "已取消注册"
          });
        });
    },
    quit() {
      this.$store.dispatch("userLogin", false);
      localStorage.setItem("Flag", "notLogin");
    },
    pushLogin(done) {
      // this.$confirm("确定要登陆吗？")
      // .then(_ => {
      //   this.loading1 = true;
      //   this.$http
      //     .get(
      //       "api/register_account?mobile_phone=" +
      //         this.form.mobilePhone +
      //         "&sex=" +
      //         this.form.sex +
      //         "&nickname=" +
      //         this.form.nickName +
      //         "&passport=" +
      //         this.form.passport +
      //         "&password=" +
      //         this.form.password +
      //         "&avatar=" +
      //         this.form.avatar
      //     )
      //     .then(result => {
      //       // console.log(result);
      //       if (result.body.error_num == 0) {
      //         this.$store.dispatch("userLogin", true);
      //         localStorage.setItem("Flag", "isLogin");
      //         this.loading = false;
      //         this.$message({
      //           type: "info",
      //           message: "登陆成功"
      //         });
      //       } else {
      //         this.loading = false;
      //         this.$message({
      //           type: "error",
      //           message: "登陆失败"
      //         });
      //       }
      //     });
      // })
      // .catch(_ => {
      //   this.dialog = false;
      //   this.$message({
      //     type: "info",
      //     message: "已取消注册"
      //   });
      // });
      this.dialog1 = false;
      this.$store.dispatch("userLogin", true);
      localStorage.setItem("Flag", "isLogin");
      this.loading1 = false;
    }
  },
  data() {
    return {
      activeIndex: "1",
      activeIndex2: "1",
      loading: false,
      loading1: false,
      dialog: false,
      dialog1: false,
      form: {
        avatar: "1",
        nickName: "",
        sex: "",
        mobilePhone: "",
        passport: "",
        password: ""
      },
      formLabelWidth: "70px"
    };
  }
};
</script>

<style lang="scss" scoped>
.drawer__footer {
  display: flex;
  justify-content: center;
}
.el-header {
  padding: 0 0px;
  background-color: #323232;
  color: #333;
  line-height: 44px;
  margin: -1px;
  .el-menu-item {
    height: 44px;
    text-align: center;
    line-height: 44px;
  }
  span {
    font-size: 14px;
  }
  .login-register {
    color: #f3f3f3;
    float: right;
    margin-right: 10px;
    line-height: 44px;
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