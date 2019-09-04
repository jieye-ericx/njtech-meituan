<template>
  <div id="app">
    <index></index>
  </div>
</template>

<script>
import index from '@/layout/index.vue'
export default {
  name: 'App',
  components:{
    index
  }
}
</script>

<style>
#app {
  font-family: "Helvetica Neue",Helvetica,"PingFang SC","Hiragino Sans GB","Microsoft YaHei","微软雅黑",Arial,sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}
body{
  margin:0;
}
</style>
