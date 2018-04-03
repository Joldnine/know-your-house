<template>
  <div class="chart-section">
    <div class="no-data-view" v-if="noData">
      <div class="info-text">No data is available</div>
    </div>
    <div v-if="!noData">
      <div class="chart-y-label">
        Resale Price (SGD/m<span class="text-sup">2</span>)
      </div>
      <chartjs-line
        class="chartjs-line"
        :data="data"
        :labels="labels"
        :datalabel="'Price'"
        :bordercolor="'#409eff'"
        :pointborderwidth="4"
        :pointbordercolor="'#f35009'"
        :option="{
          responsive:true,
          maintainAspectRatio:false,
          legend: {
            display:false,
          },
          scales: {
            yAxes: [{
              display: true,
              ticks: {
                beginAtZero:true,
              },
            }],
          },
        }"
      ></chartjs-line>
    </div>
  </div>
</template>

<script>
export default {
  name: 'ComponentPriceHistory',
  data() {
    return {
      data: [],
      labels: ['2015', '2016', '2017'],
    };
  },
  computed: {
    noData: {
      get() {
        return this.data.length === 0;
      },
    },
  },
};
</script>

<style scoped>
  .chart-section {
    position: relative;
    max-width: 768px;
    min-height: 50px;
    margin: auto;
  }
  .chart-y-label {
    text-align: left;
  }
  .chartjs-line {
    position: relative;
    height: 300px;
    width: 100%;
  }
  .text-sup {
    font-size: small;
    vertical-align: super;
  }
  .no-data-view {
    position: absolute;
    width: 100%;
    height: 100%;
    z-index: 10;
  }
  .no-data-view .info-text {
    left: 50%;
    line-height: 50px;
    color: gray;
  }

</style>
