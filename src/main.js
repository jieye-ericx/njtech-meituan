// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
import router from './router'
import store from './vuex/index.js'

router.beforeEach((to, from, next) => {

  // 获取用户登录成功后储存的登录标志
  // let getFlag = localStorage.getItem("Flag");
  store.commit('syncLoginState')

  if (!store.getters.offLine) {//登录
    next()
  }else{
    if (to.meta.needLogin) {
      const vueObj = new Vue()
      vueObj.$message({
        duration:1000,

        type: 'error',
        message: '请先登录'
      })
      next({
        path: '/foodslist',
      }) 
    } else {
      next()
    }
  }
  // else {
  //   const vueObj = new Vue()
  //   vueObj.$message({
  //     type: "info",
  //     message: "请先登录"
  //   });
  //用户想进入需要登录的页面，则定向回登录界面
  
})
import ElementUI from 'element-ui';
import 'element-ui/lib/theme-chalk/index.css';
Vue.use(ElementUI);
Vue.config.productionTip = false

import VueResource from 'vue-resource'
Vue.use(VueResource)
Vue.http.options.root = 'http://10.22.252.59:8080'

import moment from 'moment'
Vue.filter('dateFormat', function (dataStr, pattern = 'YYYY-MM-DD HH:mm:ss') {
  return moment(dataStr).format(pattern)
})

/* eslint-disable no-new */
new Vue({
  el: '#app',
  store,
  router,
  components: { App },
  template: '<App/>'
})
