import Vue from 'vue'
import Vuex from 'vuex'
Vue.use(Vuex)

var store = new Vuex.Store({
  state: {
    // {id},
    token: window.sessionStorage.getItem('token'),
    isLogin: false,
    nowUser: {
      uid: '11',
      nickName: '二丫',
      phone: '19850052217',
      sex: '男'
    },
    cart: []
  },
  mutations: {
    addToCart (state, obj) {
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
        console.log('3231' + result)
        if (result.body.error_num == 0) {
          vueObj.$message({
            type: 'info',
            message: '添加成功'
          })
        } else {
          vueObj.$message({
            type: 'error',
            message: '出错'
          })
        }
      })
      // localStorage.setItem('cart', JSON.stringify(state.cart))
    },
    userStatus (state, flag) {
      state.isLogin = flag
    },
    updateCartNum (state, obj) {
      state.cart.some(item => {
        if (item.id == obj.id) {
          item.count = parseInt(obj.count)
          return true
        }
      })
      localStorage.setItem('cart', JSON.stringify(state.cart))
    },
    removeFromCart (state, i) {
      state.cart.some((item, j) => {
        if (item.id == i) {
          state.cart.splice(j, 1)
          return true
        }
      })
      localStorage.setItem('cart', JSON.stringify(state.cart))
    },
    updateGoodSelected (state, info) {
      state.cart.some(item => {
        if (item.id == info.id) {
          item.selected = info.selected
        }
      })
      localStorage.setItem('cart', JSON.stringify(state.cart))
    }
  },
  getters: {
    isLogin: state => state.isLogin,

    getUserInfo (state) {
      return state.nowUser != null ? state.nowUser : null
    },
    getUserId (state) {
      return state.nowUser != null ? state.nowUser.uid : null
    },
    getAllCountInCart (state) {
      var n = 0
      state.cart.forEach(item => {
        n += item.count
      })
      return n
    },
    getGoodsCount (state) {
      var x = {}
      state.cart.forEach(item => {
        x[item.id] = item.count
      })
      return x
    },
    getGoodsSelected (state) {
      var x = {}
      state.cart.forEach(item => {
        x[item.id] = item.selected
      })
      return x
    },
    getGoodsNumSelected (state) {
      var o = { num: 0, price: 0 }
      state.cart.forEach(item => {
        if (item.selected == true) {
          o.num += item.count
          o.price += item.price * item.count
        }
      })
      return o
    }
  },
  actions: {
    userLogin ({ commit }, flag) {
      commit('userStatus', flag)
    }
  }
})

export default store
