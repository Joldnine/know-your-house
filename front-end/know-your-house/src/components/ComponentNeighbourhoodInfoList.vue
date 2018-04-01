<template>
  <div class="neighbourhood-info-list">
    <el-table
      :data="nearbyPlaces"
      :default-sort = "{prop: 'distance', order: 'ascending'}"
      style="width: 100%">
      <el-table-column
        prop="name"
        label="Name"
        sortable
        width="180">
      </el-table-column>
      <el-table-column
        prop="distance"
        label="Distance (km)"
        sortable
        width="180">
      </el-table-column>
      <el-table-column
        prop="duration"
        sortable
        label="Walking Time (mins)">
      </el-table-column>
    </el-table>
  </div>
</template>

<script>
export default {
  name: 'ComponentUserInput',
  computed: {
    nearbyPlaces: {
      get() {
        const markers = this.$store.getters.getMapMarkers;
        const places = [];
        markers.forEach((marker) => {
          places.push({
            name: marker.infoText,
            distance: marker.distance,
            duration: marker.duration,
          });
        });
        return places;
      },
    },
  },
};
</script>

<style scoped>
  .neighbourhood-info-list {
    width: 100%;
    height: 454px;
    text-align: left;
    overflow-y: auto;
  }
</style>
