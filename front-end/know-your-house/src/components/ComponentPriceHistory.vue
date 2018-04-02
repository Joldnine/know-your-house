<template>
  <div class="chart-section">
    <canvas id="mycanvas" count="1" style="height:100%, width:100%"></canvas>
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
      target="mycanvas"
    ></chartjs-line>
  </div>
</template>

<script>
export default {
  name: 'ComponentPriceHistory',
  data() {
    return {
      data: ['10000', '15000', '20000'],
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
</style>
