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
        style="height:44px;margin-left:15%;"
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
          <div v-if="this.$store.getters.isLogin&&this.$store.getters.isManager">
            <router-link to="/allusers" tag="div">
              <span>所有用户</span>
            </router-link>
          </div>
          <div v-else>
            <router-link to="/cart" tag="div">
              <span>购物车</span>
            </router-link>
          </div>
        </el-menu-item>
        <el-menu-item index="3">
          <div v-if="this.$store.getters.isLogin&&this.$store.getters.isManager">
            <router-link to="/allorders" tag="div">
              <span>所有订单</span>
            </router-link>
          </div>
          <div v-else>
            <router-link to="/orderlist" tag="div">
              <span>我的订单</span>
            </router-link>
          </div>
        </el-menu-item>
        <el-menu-item index="4">
          <div v-if="this.$store.getters.isLogin&&this.$store.getters.isManager">
            <span @click="AddFoodDialog=true">添加团购</span>
          </div>
        </el-menu-item>
        <el-menu-item index="5">
          <div v-if="this.$store.getters.isLogin&&this.$store.getters.isManager">
            <router-link to="/allcoms" tag="div">
            <span >所有投诉</span>
            </router-link>
          </div>
        </el-menu-item>
        <div v-if="!this.$store.getters.isLogin&&!this.$store.getters.isManager">
          <span class="login-register" @click="dialog1 = true">登录</span>
          <span class="login-register">|</span>
          <span class="login-register" @click="dialog = true">注册</span>
        </div>
        <div v-if="this.$store.getters.isLogin||this.$store.getters.isManager">
          <span class="login-register" @click="quit">退出</span>
        </div>
      </el-menu>
    </el-header>

    <el-drawer
      title="欢迎注册工大美团"
      :visible.sync="dialog"
      direction="rtl"
      custom-class="register-drawer"
      ref="drawer"
    >
      <div class="drawer__content">
        <el-form :model="registerForm">
          <el-form-item label="昵称" :label-width="formLabelWidth">
            <el-input v-model="registerForm.nickName" autocomplete="off"></el-input>
          </el-form-item>
          <el-form-item label="密码" :label-width="formLabelWidth">
            <el-input v-model="registerForm.password" autocomplete="off"></el-input>
          </el-form-item>
          <el-form-item label="性别" :label-width="formLabelWidth">
            <el-radio v-model="registerForm.sex" label="0">男</el-radio>
            <el-radio v-model="registerForm.sex" label="1">女</el-radio>
          </el-form-item>
          <el-form-item label="手机号" :label-width="formLabelWidth">
            <el-input v-model="registerForm.mobilePhone" autocomplete="off"></el-input>
          </el-form-item>
          <el-form-item label="身份证号" :label-width="formLabelWidth">
            <el-input v-model="registerForm.passport" autocomplete="off"></el-input>
          </el-form-item>
        </el-form>
        <div class="drawer__footer">
          <el-button @click="dialog = false">取 消</el-button>
          <el-button
            type="primary"
            @click="pushRegeistr"
          >确 定</el-button>
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
        <el-form :model="loginForm">
          <el-form-item label="手机号" :label-width="formLabelWidth">
            <el-input v-model="loginForm.phone" autocomplete="off"></el-input>
          </el-form-item>
          <el-form-item label="密码" prop="pass" :label-width="formLabelWidth">
            <el-input type="password" v-model="loginForm.password" autocomplete="off"></el-input>
          </el-form-item>
        </el-form>
        <div class="drawer__footer">
          <el-button @click="dialog1 = false">取 消</el-button>
          <el-button type="primary" @click="pushLogin">确定</el-button>
        </div>
      </div>
    </el-drawer>

    <el-drawer
      :open="openAddFoodDrawer"
      title="添加团购"
      :visible.sync="AddFoodDialog"
      direction="ttb"
      custom-class="register-drawer"
      ref="drawer"
      size="80%"
    >
      <div class="drawer__content">
        <el-form :model="newFood">
          <el-form-item>
            <el-upload
              action="http://10.22.252.59:8080/api/upload_pic"
              list-type="picture-card"
              :on-preview="handlePictureCardPreview"
              :on-remove="handleRemove"
              :on-success="uploadSuccess"
            >
              <i class="el-icon-plus"></i>
            </el-upload>
            <el-dialog :visible.sync="dialogVisible">
              <img width="100%" :src="dialogImageUrl" alt />
            </el-dialog>
          </el-form-item>
          <el-form-item label="团购名称" :label-width="formLabelWidth">
            <el-input v-model="newFood.name" autocomplete="off"></el-input>
          </el-form-item>
          <el-form-item label="简介" :label-width="formLabelWidth">
            <el-input v-model="newFood.details" autocomplete="off"></el-input>
          </el-form-item>
          <el-form-item label="价格" :label-width="formLabelWidth">
            <el-input v-model="newFood.price" autocomplete="off"></el-input>
          </el-form-item>
          <el-form-item label="类别" :label-width="formLabelWidth">
            <el-tag
              style="padding:1px;"
              v-for="item in goodsCategorys"
              :key="item.pk"
              type="info"
              :effect="newFood.cateid==item.pk?'dark':'plain'"
              @click="newFood.cateid=item.pk"
            >{{item.fields.name}}</el-tag>
          </el-form-item>
        </el-form>
        <div class="drawer__footer">
          <el-button @click="AddFoodDialog = false">取 消</el-button>
          <el-button type="primary" @click="pushNewFood">提交</el-button>
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
import Cookies from "js-cookie";

export default {
  created() {
    this.getCategorys();
  },
  methods: {
    uploadSuccess(response, file, fileList) {
      console.log(response);
      this.newFood.urls.push(response.path);
    },
    handleSelect(key, keyPath) {
      // console.log(key, keyPath);
    },
    pushRegeistr(done) {
      console.log(987);
      this.$http
        .get(
          "api/register_account?mobile_phone=" +
            this.registerForm.mobilePhone +
            "&sex=" +
            this.registerForm.sex +
            "&nickname=" +
            this.registerForm.nickName +
            "&passport=" +
            this.registerForm.passport +
            "&password=" +
            this.registerForm.password +
            "&avatar=" +
            this.registerForm.avatar
        )
        .then(result => {
          // console.log(result);
          if (result.body.error_num == 0) {
            this.dialog=false
            this.$message({
              duration: 1000,
              type: "info",
              message: "注册成功，请登录"
            });
          } else {
            this.dialog=false
            this.$message({
              duration: 1000,
              type: "error",
              message: "注册不成功，请重试"
            });
          }
        });
    },
    quit() {
      this.$store.commit("loginOut");
    },
    pushLogin(done) {
      // console.log("login");
      this.dialog1 = false;

      this.$http
        .post(
          "api/customer_login",
          {
            userphone: this.loginForm.phone,
            pswd: this.loginForm.password
          },
          { emulateJSON: true }
        )
        .then(result => {
          // console.log(result);
          if (result.body.error_num === 0) {
            this.dialog1 = false;
            var user = {};
            user.uid = result.body.id;
            user.nickName = result.body.name;
            user.sex = result.body.sex;
            user.phone = result.body.phone;
            user.passport = result.body.passport;
            user.isDelete = result.body.isdelete;
            this.$store.commit("loginIn", user);
            this.$message({
              type: "info",
              message: "登陆成功"
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
    handleRemove(file, fileList) {
      console.log(file, fileList);
    },
    handlePictureCardPreview(file) {
      this.dialogImageUrl = file.url;
      this.dialogVisible = true;
    },
    getCategorys() {
      this.$http.get("api/get_all_food_category").then(result => {
        if (result.body.error_num == 0) {
          this.goodsCategorys = result.body.list;
        } else {
          this.$message({
            duration: 1000,
            type: "error",
            message: "获取分类列表不成功，请重试"
          });
        }
      });
    },
    openAddFoodDrawer() {
      this.getCategorys();
    },
    pushNewFood() {
      this.AddFoodDialog = false;
      this.$http.get(
        "api/add_food_variety?category_id=" +
          this.newFood.cateid +
          "&name=" +
          this.newFood.name +
          "&amount_money=" +
          this.newFood.price +
          "&introduction=" +
          this.newFood.details +
          "&add_time=" +
          new Date() +
          "&stop_time=" +
          new Date() +
          "&url1=" +
          this.newFood.urls[0] +
          "&url2=" +
          this.newFood.urls[1] +
          "&url3=" +
          this.newFood.urls[2] +
          "&url4=" +
          this.newFood.urls[3]
      );
    }
  },
  data() {
    return {
      seleteCategoryId: "",
      goodsCategorys: [],
      activeIndex: "1",
      activeIndex2: "1",
      loading: false,
      loading1: false,
      dialog: false,
      dialog1: false,
      AddFoodDialog: false,
      registerForm: {
        nickName: "",
        sex: "",
        mobilePhone: "",
        passport: "",
        password: ""
      },
      loginForm: {
        phone: "",
        password: ""
      },
      newFood: {
        cateid: "",
        name: "",
        details: "",
        price: "",
        urls: []
      },
      formLabelWidth: "70px",
      dialogImageUrl: "",
      dialogVisible: false
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