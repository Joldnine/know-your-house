<template>
  <div class="chart-section">
    <chartjs-line
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
      class="chartjs-line"
    ></chartjs-line>
  </div>
</template>

<script>
export default {
  name: 'ComponentPriceHistory',
  data() {
    return {
      data: ['10000', '15000', '20001'],
      labels: ['2015', '2016', '2017'],
    };
  },
};
</script>

<style scoped>
  .chart-section {
    max-width: 768px;
    height: 300px;
    margin: auto;
  }
  .chartjs-line {
    position: relative;
    height: 100%;
    width:100%;
  }
</style>
