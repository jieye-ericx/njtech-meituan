<template>
  <el-container>
    <el-aside width="200px">
      <el-menu>
        <el-menu-item index="-1">
          <i class="el-icon-s-fold"></i>浏览所有
        </el-menu-item>
        <el-menu-item
          v-for="(item,i) in goodsCategorys"
          :key="item.pk"
          :index="i.toString()"
        >{{item.fields.name}}</el-menu-item>
      </el-menu>
    </el-aside>
    <el-main>
      <router-link :to="'/foodinfo/'+good.id" tag="div" v-for="(good) in foodsList" :key="good.id">
        <el-card :body-style="{ padding: '1px' }">
          <img :src="good.picUrl1" class="image" />
          <div>
            <div class="name-price">
              <span class="s-name">{{good.name}}</span>
              <span class="s-price">¥{{good.amount_money}}</span>
            </div>
            <div class="category-more">
              <span class="s-category">{{good.category_id}}</span>
              <el-button type="text" class="button">了解更多</el-button>
            </div>
          </div>
        </el-card>
      </router-link>
      <el-pagination layout="prev, pager, next" page-size="20"></el-pagination>
    </el-main>
  </el-container>
</template>

<script>
export default {
  created() {
    // for (var i = 0; i < 100; i++) {
    //   var good = {
    //     img:
    //       "https://shadow.elemecdn.com/app/element/hamburger.9cf7b091-55e9-11e9-a976-7f4d0b07eef6.png",
    //     name: "汉堡",
    //     category: "快餐",
    //     price: "100",
    //     id: i
    //   };
    //   this.foodsList.push(good);
    // }
    this.$http.get("api/get_all_food_category").then(result => {
      if (result.body.error_num == 0) {
        this.goodsCategorys = result.body.list;
      } else {
        this.$message({
          type: "error",
          message: "获取分类列表不成功，请重试"
        });
      }
    });

    this.getAllFoods();
    console.log(this.foodsList);
  },
  data() {
    return {
      foodsList: [],
      currentDate: new Date(),
      goodsCategorys: [],
      page: 1
    };
  },
  methods: {
    getAllFoods() {
      this.$http.get("api/get_page_food?page=" + this.page).then(result => {
        this.foodsList = [];
        result.body.list.forEach(element => {
          var obj = element.fields;
          obj.id = element.pk;
          this.foodsList.push(obj);
        });
      });
    }
  }
};
</script>

<style lang="scss" scoped>
.el-container {
  margin-top: 25px;
  margin-right: 10%;
  margin-left: 10%;
}
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
    // border: 0.1px solid #ccc;
    box-shadow: 0 2px 12px 0 rgba(0, 0, 0, 0.1);
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