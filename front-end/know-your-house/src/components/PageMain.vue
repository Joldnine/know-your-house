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
        <el-col :xs="24" :sm="{span:12, offset:5}" :md="{span:8, offset:7}"
                :lg="{span:6, offset:8}" :xl="{span:4, offset:9}">
          <ComponentUserInput />
        </el-col>
      </el-row>
      <div class="house-info-section">
        <div class="page-loading" v-if="pageLoading">
          <div class="el-icon-loading page-loading-spinner"></div>
        </div>
        <div class="house-info-section-content" v-if="!pageLoading">
          <el-row :gutter="8">
            <el-col>
              <ComponentPriceShower />
            </el-col>
          </el-row>
          <el-row :gutter="8" style="margin-bottom:10px">
            <el-col>
              <el-card>
                <div slot="header" class="clearfix">
                  <span>House Resale Price History</span>
                </div>
                <ComponentPriceHistory />
              </el-card>
            </el-col>
          </el-row>
          <el-row :gutter="8" style="margin-bottom:10px">
            <el-col :xs="24" :sm="24" :md="12" :lg="12" :xl="12">
              <el-card>
                <div slot="header" class="clearfix">
                  <span>House Neighbourhood Info</span>
                </div>
                <ComponentNeighbourhoodInfo />
              </el-card>
            </el-col>
            <el-col :xs="24" :sm="24" :md="12" :lg="12" :xl="12">
              <el-card>
                <ComponentNeighbourhoodInfoList />
              </el-card>
            </el-col>
          </el-row>
        </div>
      </div>
    </el-main>
  </el-container>
</template>

<script>
import ComponentUserInput from '@/components/ComponentUserInput';
import ComponentNeighbourhoodInfo from '@/components/ComponentNeighbourhoodInfo';
import ComponentNeighbourhoodInfoList from '@/components/ComponentNeighbourhoodInfoList';
import ComponentPriceShower from '@/components/ComponentPriceShower';
import ComponentPriceHistory from '@/components/ComponentPriceHistory';

export default {
  name: 'PageMain',
  components: {
    ComponentUserInput,
    ComponentNeighbourhoodInfo,
    ComponentNeighbourhoodInfoList,
    ComponentPriceShower,
    ComponentPriceHistory,
  },
  computed: {
    pageLoading: {
      get() {
        return this.$store.getters.getPageLoading;
      },
    },
    pageContentLoaded: {
      get() {
        return this.$store.getters.getPageContentLoaded;
      },
    },
  },
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
.house-info-section {
  position: relative;
  min-height: 200px;
}
.page-loading {
  position: absolute;
  width: 100%;
  height: 100%;
  background-color: white;
  z-index: 10;
}
.page-loading-spinner {
  position: absolute;
  top: calc(50% - 1em);
  color: #409eff;
}
</style>
