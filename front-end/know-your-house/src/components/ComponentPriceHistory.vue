<template>
  <chartjs-line
    :data="data"
    :labels="labels"
    :datalabel="'Price'"
    :bordercolor="'#409eff'"
    :pointborderwidth="4"
    :pointbordercolor="'#f35009'"
    :option="{
      responsive:true,
      maintainAspectRatio:true,
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
