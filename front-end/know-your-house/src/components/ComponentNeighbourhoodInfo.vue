<template>
  <div class="neighbourhood-info">
    <div class="neighbourhood-info-nav">
      <el-tabs @tab-click="handleTabClick">
        <el-tab-pane v-for="(tab, idx) in tabs"
          :key="idx"
          :label="tab.label"
          :name="tab.name"
          style="height:100%;width:100%;"
        ></el-tab-pane>
      </el-tabs>
    </div>
    <div class="neighbourhood-info-section">
        <gmap-map
          :center="mapCenter"
          :zoom="mapZoom"
          style="height:100%;width:100%;"
        >
          <gmap-info-window
            :options="infoOptions"
            :position="infoWindowPos"
            :opened="infoWinOpen"
            @closeclick="infoWinOpen=false">
            {{infoContent}}
          </gmap-info-window>
          <gmap-marker
            v-for="(m, idx) in mapMarkers"
            :key="idx"
            :position="m.position"
            :clickable="true"
            @click="toggleInfoWindow(m, idx)"
          ></gmap-marker>
        </gmap-map>
    </div>
  </div>
</template>

<script>
export default {
  name: 'ComponentNeighbourhoodInfo',
  data() {
    return {
      // tabs
      tabs: [
        {
          label: 'Schools',
          name: 'schools',
        },
        {
          label: 'Shopping malls',
          name: 'malls',
        },
        {
          label: 'Sports facilities',
          name: 'sports',
        },
        {
          label: 'Transport',
          name: 'transport',
        },
      ],

      // maps
      mapZoom: 14,
      infoContent: '',
      infoWindowPos: {
        lat: 0,
        lng: 0,
      },
      infoWinOpen: false,
      currentMidx: null,
      // optional: offset infowindow so it visually sits nicely on top of our marker
      infoOptions: {
        pixelOffset: {
          width: 0,
          height: -35,
        },
      },
    };
  },
  computed: {
    mapCenter: {
      get() {
        const loc = this.$store.getters.getUserInputAddressLoc;
        return loc;
      },
    },
    mapMarkers: {
      get() {
        const markers = this.$store.getters.getMapMarkers;
        return markers;
      },
    },
  },
  methods: {
    handleTabClick(payload) {
      this.$store.dispatch('requestNearbyPlaces', {
        type: payload.name,
        loc: this.mapCenter,
      }).then(() => {
        // this.loading = false
      }).catch(() => {
        // this.loading = false
      });
      this.infoWinOpen = false;
    },
    toggleInfoWindow(marker, idx) {
      this.infoWindowPos = marker.position;
      this.infoContent = marker.infoText;

      if (this.currentMidx === idx) {
        this.infoWinOpen = !this.infoWinOpen;
      } else {
        this.infoWinOpen = true;
        this.currentMidx = idx;
      }
    },
  },
};
</script>

<style scoped>
  .neighbourhood-info-section {
    width: 100%;
    height: 400px;
  }
</style>
