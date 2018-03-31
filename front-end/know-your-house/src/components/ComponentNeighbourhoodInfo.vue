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
      <div class="neighbourhood-map">
        <div class="neighbourhood-map-loading" v-if="mapLoading">
          <div class="el-icon-loading neighbourhood-map-loading-spinner"></div>
        </div>
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
      mapLoading: false,
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
        const markers = [];
        const loc = this.$store.getters.getUserInputAddressLoc;
        const houseMarker = {};
        houseMarker.position = loc;
        houseMarker.infoText = 'Your House';
        houseMarker.icon = 'http://maps.google.com/mapfiles/ms/icons/blue.png';
        markers.push(houseMarker);
        const nearbyPlaces = this.$store.getters.getNearbyPlaces;
        nearbyPlaces.forEach((place) => {
          const marker = {};
          marker.position = place.location;
          marker.infoText = place.name;
          markers.push(marker);
        });
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
        this.mapLoading = false;
      });
      this.infoWinOpen = false;
      this.mapLoading = true;
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
  .neighbourhood-map-loading {
    position: absolute;
    width: 100%;
    height: 100%;
    background-color: rgba(128,128,128,0.5);
    z-index: 10;
  }
  .neighbourhood-map-loading-spinner {
    position:relative;
    top: calc(50% - 1em);
  }

</style>
