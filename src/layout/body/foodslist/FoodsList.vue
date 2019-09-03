<template>
  <el-container>
    <el-aside width="200px">
      <el-menu :default-openeds="['1', '3']">
        <el-submenu index="1">
          <template slot="title">
            <i class="el-icon-message"></i>导航一
          </template>
          <el-menu-item-group>
            <template slot="title">分组一</template>
            <el-menu-item index="1-1">选项1</el-menu-item>
            <el-menu-item index="1-2">选项2</el-menu-item>
          </el-menu-item-group>
          <el-menu-item-group title="分组2">
            <el-menu-item index="1-3">选项3</el-menu-item>
          </el-menu-item-group>
          <el-submenu index="1-4">
            <template slot="title">选项4</template>
            <el-menu-item index="1-4-1">选项4-1</el-menu-item>
          </el-submenu>
        </el-submenu>
        <el-submenu index="2">
          <template slot="title">
            <i class="el-icon-menu"></i>导航二
          </template>
          <el-menu-item-group>
            <template slot="title">分组一</template>
            <el-menu-item index="2-1">选项1</el-menu-item>
            <el-menu-item index="2-2">选项2</el-menu-item>
          </el-menu-item-group>
          <el-menu-item-group title="分组2">
            <el-menu-item index="2-3">选项3</el-menu-item>
          </el-menu-item-group>
          <el-submenu index="2-4">
            <template slot="title">选项4</template>
            <el-menu-item index="2-4-1">选项4-1</el-menu-item>
          </el-submenu>
        </el-submenu>
        <el-submenu index="3">
          <template slot="title">
            <i class="el-icon-setting"></i>导航三
          </template>
          <el-menu-item-group>
            <template slot="title">分组一</template>
            <el-menu-item index="3-1">选项1</el-menu-item>
            <el-menu-item index="3-2">选项2</el-menu-item>
          </el-menu-item-group>
          <el-menu-item-group title="分组2">
            <el-menu-item index="3-3">选项3</el-menu-item>
          </el-menu-item-group>
          <el-submenu index="3-4">
            <template slot="title">选项4</template>
            <el-menu-item index="3-4-1">选项4-1</el-menu-item>
          </el-submenu>
        </el-submenu>
      </el-menu>
    </el-aside>
    <el-main>
      <router-link :to="'/foodinfo/'+good.id" tag="div" v-for="(good) in goodsList" :key="good.id">
        <el-card :body-style="{ padding: '1px' }">
          <img :src="good.img" class="image" />
          <div>
            <div class="name-price">
              <span class="s-name">{{good.name}}+{{good.id}}</span>
              <span class="s-price">¥{{good.price}}</span>
            </div>
            <div class="category-more">
              <span class="s-category">{{good.category}}</span>
              <el-button type="text" class="button">了解更多</el-button>
            </div>
          </div>
        </el-card>
      </router-link>
    </el-main>
  </el-container>
</template>

<script>
export default {
  created() {
    for (var i = 0; i < 100; i++) {
      var good = {
        img:
          "https://shadow.elemecdn.com/app/element/hamburger.9cf7b091-55e9-11e9-a976-7f4d0b07eef6.png",
        name: "汉堡",
        category: "快餐",
        price: "100",
        id: i
      };
      this.goodsList.push(good);
    }
  },
  data() {
    const item = {
      date: "2016-05-02",
      name: "王小虎",
      address: "上海市普陀区金沙江路 1518 弄"
    };
    const goods = {
      img:
        "https://shadow.elemecdn.com/app/element/hamburger.9cf7b091-55e9-11e9-a976-7f4d0b07eef6.png",
      name: "汉堡",
      category: "快餐",
      price: "100"
    };
    return {
      tableData: Array(20).fill(item),
      goodsList: [],
      currentDate: new Date()
    };
  }
};
</script>

<style lang="scss" scoped>
.el-aside {
  color: #333;
  background-color: #ffffff;
  // .el-menu {
  //   border: 0.1px solid #ccc;
  //   box-shadow: 0 0 8px #ccc;
  //   border-radius: 4%;
  // }
}
.time {
  font-size: 15px;
  color: #999;
}

.bottom {
  margin-top: 13px;
  line-height: 12px;
}

.button {
  padding: 0;
  float: right;
}

.image {
  width: 100%;
  display: block;
}
.el-main {
  flex-wrap: wrap;
  padding: 7px;
  justify-content: space-between;
  display: flex;

  .el-card {
    border: 0.1px solid #ccc;
    box-shadow: 0 0 8px #ccc;
    border-radius: 4%;
    margin: 5px;
    width: 220px;
    height: 290px;
    flex-direction: column;
    justify-content: space-between;
    .name-price {
      display: flex;
      justify-content: space-between;
      .s-name {
        font-size: 18px;
      }

      .s-price {
        padding-top: 24px;
        color: red;
        font-weight: bold;
        font-size: 20px;
      }
    }
    .category-more {
      margin: 0;
      display: flex;
      justify-content: space-between;
      .s-category {
        font-size: 12px;
      }
      .el-button {
      }
    }
  }
}

// .clearfix:before,
// .clearfix:after {
//   display: table;
//   content: "";
// }

// .clearfix:after {
//   clear: both;
// }
</style>