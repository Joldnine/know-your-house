<template>
  <div class="chart-section">
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
</style>
