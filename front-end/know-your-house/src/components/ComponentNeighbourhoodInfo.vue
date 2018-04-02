<template>
  <div class="neighbourhood-info">
    <div class="neighbourhood-info-nav">
      <el-tabs v-model="activeTab" @tab-click="handleTabClick">
        <el-tab-pane v-for="(tab, idx) in tabs"
          :key="idx"
          :label="tab.label"
          :name="tab.name"
        ></el-tab-pane>
      </el-tabs>
    </div>
    <div class="neighbourhood-info-section">
      <div class="neighbourhood-map">
        <!-- <div class="neighbourhood-map-loading" v-if="mapLoading">
          <div class="el-icon-loading neighbourhood-map-loading-spinner"></div>
        </div> -->
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
            :position="mapCenter"
            :icon="'http://maps.google.com/mapfiles/ms/icons/blue.png'"
            :clickable="true"
            @click="toggleInfoWindow({
              position: mapCenter,
              infoText: 'Your House'
            }, -1)"
          ></gmap-marker>
          <gmap-marker
            v-for="(m, idx) in mapMarkers"
            :key="idx"
            :position="m.position"
            :icon="m.icon"
            :clickable="true"
            @click="toggleInfoWindow(m, idx)"
          ></gmap-marker>
        </gmap-map>
      </div>
    </div>
  </div>
</template>

<script>
const TAB_NAME_NOT_SELECTED = 'None';

export default {
  name: 'ComponentNeighbourhoodInfo',
  data() {
    return {
      // tabs
      tabs: [
        {
          label: 'Schools',
          name: 'school',
        },
        {
          label: 'Shopping malls',
          name: 'mall',
        },
        {
          label: 'MRT',
          name: 'mrt',
        },
        {
          label: 'Bus Stops',
          name: 'bus stop',
        },
      ],
      activeTab: TAB_NAME_NOT_SELECTED,

      // maps
      // mapLoading: false,
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
        if (TAB_NAME_NOT_SELECTED.localeCompare(this.activeTab)) {
          this.updateNearbyPlaces(this.activeTab, loc);
        }
        return loc;
      },
    },
    mapMarkers: {
      get() {
        return this.$store.getters.getMapMarkers;
      },
    },
  },
  methods: {
    updateNearbyPlaces(type) {
      const markers = [];
      const nearbyPlaces = this.$store.getters.getNearbyPlaces;
      nearbyPlaces.forEach((place) => {
        // console.log(type);
        // console.log(place.type);
        if (type === place.type) {
          const marker = {};
          marker.position = place.location;
          marker.infoText = place.name;
          marker.distance = place.direction.distance.text.replace(' km', '');
          marker.duration = place.direction.duration.text.replace(' mins', '');
          markers.push(marker);
        }
      });
      this.$store.commit('SET_MAP_MARKERS', markers);
    },
    handleTabClick(payload) {
      this.updateNearbyPlaces(payload.name, this.mapCenter);
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
    position: relative;
    width: 100%;
    height: 400px;
  }
  .neighbourhood-map {
    position: relative;
    width: 100%;
    height: 100%;
  }
  /* .neighbourhood-map-loading {
    position: absolute;
    width: 100%;
    height: 100%;
    background-color: rgba(128,128,128,0.5);
    z-index: 10;
  }
  .neighbourhood-map-loading-spinner {
    position:relative;
    top: calc(50% - 1em);
  } */

</style>
