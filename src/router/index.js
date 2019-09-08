import Vue from 'vue'
import Router from 'vue-router'
import index from '@/layout/index'
import CartList from '@/layout/body/Cart.vue'
import OrderList from '@/layout/body/OrderList.vue'
import FoodsList from '@/layout/body/foodslist/FoodsList.vue'
import FoodInfo from '@/layout/body/foodslist/FoodInfo.vue'
import ManagerLogin from '@/layout/body/ManagerLogin.vue'
import Allusers from '@/layout/body/Allusers.vue'
Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/', redirect: '/foodslist',
      meta: {
        needLogin: false
      }
    },
    {
      path: '/index', component: index, meta: {
        needLogin: false
      }
    },
    {
      path: '/cart', component: CartList, meta: {
        needLogin: true
      }
    },
    { path: '/orderlist', component: OrderList, meta: { needLogin: true } },
    {
      path: '/foodslist', component: FoodsList, meta: {
        needLogin: false
      }
    },
    {
      path: '/foodinfo/:id', component: FoodInfo, meta: {
        needLogin: false
      }
    },
    {
      path: '/manager', component: ManagerLogin, meta: {
        needLogin: false
      }
    },
    {
      path: '/allusers', component: Allusers, meta: {
        needLogin: true
      }
    }

  ]
})
