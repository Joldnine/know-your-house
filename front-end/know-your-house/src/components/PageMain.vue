<template>
  <el-container>
    <el-header>{{ headTitle }}</el-header>
    <el-main>
      <el-row :gutter="10">
        <el-col :xs="24" :sm="12" :md="8" :lg="6" :xl="3">
          <ComponentUserInput />
        </el-col>
      </el-row>
    </el-main>
  </el-container>
</template>

<script>
import ComponentUserInput from '@/components/ComponentUserInput';

export default {
  name: 'PageMain',
  components: { ComponentUserInput },
  data() {
    return {
      headTitle: 'Know Your House',
    };
  },
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.el-header, .el-footer {
  background-color: #ffffff;
  color: #409eff;
  text-align: center;
  line-height: 60px;
}
.el-main {
  background-color: #ffffff;
  color: #409eff;
  text-align: center;
  line-height: 160px;
}
h1, h2 {
  font-weight: normal;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
</style>
