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
      <!-- <el-row> -->
      <el-col
        :span="4"
        v-for="(good, index) in goodsList"
        :key="good.src"
        :offset="index > 0 ? 2 : 0"
      >
        <el-card :body-style="{ padding: '1px' }">
          <img
            src="https://shadow.elemecdn.com/app/element/hamburger.9cf7b091-55e9-11e9-a976-7f4d0b07eef6.png"
            class="image"
          />
          <div>
            <div class="name-price">
              <span>{{good.name}}</span>
              <span class="s-price">¥{{good.price}}</span>
            </div>
            <div class="bottom clearfix">
              <time class="time">{{ currentDate|dateFormat('YYYY-MM-DD')}}</time>
              <el-button type="text" class="button">了解更多</el-button>
            </div>
          </div>
        </el-card>
      </el-col>
      <!-- </el-row> -->
    </el-main>
  </el-container>
</template>

<script>
export default {
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
      goodsList: Array(100).fill(goods),
      currentDate: new Date()
    };
  }
};
</script>

<style lang="scss" scoped>
.el-aside {
  color: #333;
  background-color: #ffffff;
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
.name-price {
  padding: 4px;
  // text-align: left;
  display: flex;
  justify-content: space-between;
  .s-price {
    font-weight: 900;
    color: red;
  }
}
.clearfix {
  display: flex;

  justify-content: space-between;
  .time {
    // text-align: left;
    padding: 2px;
  }
  el-button {
    padding: 2px;
    // text-align: right;
  }
}
.clearfix:before,
.clearfix:after {
  display: table;
  content: "";
}

.clearfix:after {
  clear: both;
}
</style>