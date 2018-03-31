<template>
  <el-container>
    <el-header>
      <el-row :gutter="8">
      <h1>
        <i class="el-icon-location"></i>
        {{ headTitle }}
      </h1>
      <h5>
        {{ headSubtitle }}
      </h5>
      </el-row>
    </el-header>
    <el-main>
      <el-row :gutter="8">
        <el-col :xs="0" :sm="5" :md="7" :lg="8" :xl="9">
          &nbsp;
        </el-col>
        <el-col :xs="24" :sm="12" :md="8" :lg="6" :xl="4">
          <ComponentUserInput />
        </el-col>
      </el-row>
      <el-row :gutter="8">
        <el-col :xs="24" :sm="12" :md="12" :lg="12" :xl="12">
          <el-card>
            <ComponentNeighbourhoodInfo />
          </el-card>
        </el-col>
        <el-col :xs="24" :sm="12" :md="12" :lg="12" :xl="12">
          <el-card>
            <ComponentNeighbourhoodInfoList />
          </el-card>
        </el-col>
      </el-row>
    </el-main>
  </el-container>
</template>

<script>
import ComponentUserInput from '@/components/ComponentUserInput';
import ComponentNeighbourhoodInfo from '@/components/ComponentNeighbourhoodInfo';
import ComponentNeighbourhoodInfoList from '@/components/ComponentNeighbourhoodInfoList';

export default {
  name: 'PageMain',
  components: { ComponentUserInput, ComponentNeighbourhoodInfo, ComponentNeighbourhoodInfoList },
  data() {
    return {
      headTitle: 'Know Your House',
      headSubtitle: 'Get a comprehensive analysis of your house',
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
  line-height: 10px;
}
.el-main {
  margin-top: 30px;
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
