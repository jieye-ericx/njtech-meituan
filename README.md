# **基于web的美食团购网站**

+ 包括三大类用户：游客、注册用户和管理员

+ 用户可以按类别浏览美食信息并且可以查看最新以及往期的团购信息；

+ 用户可以在线注册，注册成功并登录后方进行美食团购；

+ 注册后的用户可以对商家进行投诉或提建议；

+ 注册后的用户可以对自己的购物车进行操作，可以查看自己的订单明细；

+ 管理员可以添加和修改管理员账户，并且可以查看用户信息和投诉信息；

+ 管理员可以对美食信息以及用户的订单信息进行操作。

|       功能       | 游客 | 注册用户 | 管理员 |
| :--------------: | :--: | :------: | :----: |
|     浏览美食     |  有  |    有    |   有   |
| 将美食加入购物车 |      |    有    |        |
|     购买美食     |      |    有    |        |
|     新增美食     |      |          |   有   |
|     查看订单     |      |    有    |   有   |
|     删除订单     |      |          |   有   |
|     投诉订单     |      |    有    |        |
|     查看投诉     |      |          |   有   |
|     删除用户     |      |          |   有   |
|     删除美食     |      |          |   有   |

#### 浏览美食页面

![屏幕快照 2019-09-11 下午10.28.28](https://github.com/radoapx/njtechmeituan/blob/master/images/屏幕快照%202019-09-11%20下午10.28.28.png)

#### 购物车页面

![屏幕快照 2019-09-11 下午10.31.10](https://github.com/radoapx/njtechmeituan/blob/master/images/屏幕快照%202019-09-11%20下午10.31.10-1568217886375.png)

#### 商品详情

![屏幕快照 2019-09-11 下午10.28.55](https://github.com/radoapx/njtechmeituan/blob/master/images/屏幕快照%202019-09-11%20下午10.28.55-1568217927616.png)

#### 查看订单

![屏幕快照 2019-09-11 下午10.31.44](https://github.com/radoapx/njtechmeituan/blob/master/images/屏幕快照%202019-09-11%20下午10.31.44.png)

#### 管理用户![屏幕快照 2019-09-11 下午10.32.34](https://github.com/radoapx/njtechmeituan/blob/master/images/屏幕快照%202019-09-11%20下午10.32.34.png)

#### 添加美食

 图片加载为添加美食图片（演示用的随便点的图片

![屏幕快照 2019-09-11 下午10.33.44](https://github.com/radoapx/njtechmeituan/blob/master/images/屏幕快照%202019-09-11%20下午10.33.44.png)

#### 查看投诉

![屏幕快照 2019-09-11 下午10.34.00](https://github.com/radoapx/njtechmeituan/blob/master/images/屏幕快照%202019-09-11%20下午10.34.00.png)

#### vue组件示意

app.vue 根页面

> index.vue 主页
>
> > header 导航栏
> >
> > > 登录
> > >
> > > 注册
> >
> > 路由装载
> >
> > > 美食列表
> > >
> > > 美食详细信息
> > >
> > > 购物车
> > >
> > > 订单
> > >
> > > 添加美食
> > >
> > > 管理用户
> > >
> > > 管理订单
> > >
> > > 管理员登录

## Build Setup

```
# enter project
cd njtechmeituan

# install dependencies
npm install

# serve with hot reload at localhost:8080
npm run dev

# build for production with minification
npm run build

# build for production and view the bundle analyzer report
npm run build --report

# run unit tests
npm run unit

# run e2e tests
npm run e2e

# run all tests
npm test
```
