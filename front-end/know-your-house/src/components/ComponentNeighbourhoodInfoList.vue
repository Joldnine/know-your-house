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
  data() {
    return {
      tableData: [{
        date: '2016-05-03',
        name: 'Tom',
        address: 'No. 189, Grove St, Los Angeles',
      }],
    };
  },
  computed: {
    nearbyPlaces: {
      get() {
        const nearbyPlaces = this.$store.getters.getNearbyPlaces;
        const places = [];
        nearbyPlaces.forEach((e) => {
          console.log(places);
          places.push({
            name: e.name,
            distance: e.direction.distance.text.replace(' km', ''),
            duration: e.direction.duration.text.replace(' mins', ''),
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
    overflow-y: scroll;
  }
</style>
