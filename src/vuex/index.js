import Vue from 'vue'
import Vuex from 'vuex'
import * as Cookies from "js-cookie"
Vue.use(Vuex)

var store = new Vuex.Store({
  state: {
    isManager: false,
    isLogin: false,
    cart: [],
    loginState: {
      loginIn: false,
      user: null
    }
  },
  mutations: {
    addToCart(state, obj) {
      var flag = true
      var newObj = obj
      state.cart.forEach(item => {
        if (item.id == obj.id) {
          item.quantity += parseInt(obj.quantity)
          flag = false
          newObj = item
          return true
        }
      })
      if (flag) {
        state.cart.push(newObj)
      }
      const vueObj = new Vue()
      vueObj.$http.get('api/add_shopping_cart_content?customer_id=' +
        newObj.uid +
        '&food_id=' +
        newObj.id +
        '&quantity=' +
        newObj.quantity +
        '&amount_money=' +
        newObj.price
      ).then(result => {
        console.log('添加购物车时发送的请求' + result)
        if (result.body.error_num == 0) {
          vueObj.$message({
            duration: 1000,
            type: 'info',
            message: '添加成功'
          })
        } else {
          vueObj.$message({
            duration: 1000,
            type: 'error',
            message: '出错'
          })
        }
      })
      // localStorage.setItem('cart', JSON.stringify(state.cart))
    },
    // 登入状态
    loginIn(state, user) {
      state.loginState.loginIn = true
      state.loginState.user = user
      state.isLogin = true
      Cookies.set('loginState', state.loginState, { expires: 2 })
    },
    // 登出状态
    loginOut(state) {
      state.loginState.loginIn = false
      state.loginState.user = {}
      state.isLogin = false
      state.isManager = false

      Cookies.remove('loginState')
    },
    syncLoginState(state) {
      let cookieState = Cookies.getJSON('loginState')
      if (cookieState) {
        console.log(cookieState);
        
        state.loginState = cookieState
        state.isLogin = true
      }
    },
    managerLogin(state) {
      state.isManager = true
      state.loginState.loginIn = true
      state.loginState.user = {}
      state.isLogin = true
      Cookies.remove('loginState')
    }
  },
  getters: {
    isLogin: state => state.isLogin,
    isManager: state => state.isManager,
    offLine: (state, getters, rootState) => {
      return !state.loginState.loginIn
    },
    userInfo:(state)=>{
      if(state.loginState.user!=null){
        return state.loginState.user
      }else{
        return -1
      }
    }
  },
  actions: {
  }
})

export default store
