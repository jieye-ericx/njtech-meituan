import Vue from 'vue'
import Router from 'vue-router'
import index from '@/layout/index'
import CartList from '@/layout/body/Cart.vue'
import OrderList from '@/layout/body/OrderList.vue'
import FoodsList from '@/layout/body/foodslist/FoodsList.vue'
import FoodInfo from '@/layout/body/foodslist/FoodInfo.vue'
Vue.use(Router)

export default new Router({
  routes: [
    { path: '/', redirect: '/index' },
    { path: '/index', component: index },
    { path: '/cart', component: CartList },
    { path: '/orderlist', component: OrderList },
    { path: '/foodslist', component: FoodsList },
    { path: '/foodinfo/:id', component: FoodInfo }

  ]
})
