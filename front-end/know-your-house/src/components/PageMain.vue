<template>
  <el-container>
    <el-header>
      <i class="el-icon-location"></i>
      {{ headTitle }}
    </el-header>
    <el-main>
      <el-row :gutter="10">
        <el-col :xs="0" :sm="5" :md="7" :lg="8" :xl="9">
          &nbsp;
        </el-col>
        <el-col :xs="24" :sm="12" :md="8" :lg="6" :xl="4">
          <ComponentUserInput />
        </el-col>
      </el-row>
      <el-row>
        <el-col :xs="24" :sm="12" :md="12" :lg="12" :xl="12">
          <ComponentNeighbourhoodInfo />
        </el-col>
      </el-row>
    </el-main>
  </el-container>
</template>

<script>
import ComponentUserInput from '@/components/ComponentUserInput';
import ComponentNeighbourhoodInfo from '@/components/ComponentNeighbourhoodInfo';

export default {
  name: 'PageMain',
  components: { ComponentUserInput, ComponentNeighbourhoodInfo },
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
