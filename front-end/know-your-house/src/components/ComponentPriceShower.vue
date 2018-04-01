<template>
  <div class="iCountUp">
    <ICountUp
      v-if="addr !== ''"
      :startVal="startVal"
      :endVal="price"
      :decimals="decimals"
      :duration="duration"
      :options="options"
    />
  </div>
</template>

<script>
import ICountUp from 'vue-countup-v2';

export default {
  name: 'demo',
  components: {
    ICountUp,
  },
  data() {
    return {
      startVal: 0,
      decimals: 0,
      duration: 2,
      options: {
        separator: ',',
        prefix: 'SGD ',
      },
    };
  },
  computed: {
    addr: {
      get() {
        return this.$store.getters.getUserInputAddress;
      },
    },
    price: {
      get() {
        return this.$store.getters.getPrice;
      },
    },
  },
};
</script>

<style scoped>
  .iCountUp {
    font-size: 3em;
    margin-top: 1em;
    margin-bottom: 1em;
  }
</style>

