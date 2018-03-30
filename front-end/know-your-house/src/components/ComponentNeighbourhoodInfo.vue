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
          :draggable="true"
          @click="toggleInfoWindow(m, idx)"
          title="aaaa"
          ></gmap-marker>
        </gmap-map>
    </div>
  </div>
</template>

<script>
import { getNearbyPlaces } from '@/api';

const SINGAPORE = { lat: 1.3521, lng: 103.8198 };

const QUERIES = {
  schools: {
    types: [
      {
        name: 'school',
        keyword: 'school',
      },
    ],
  },
  malls: {
    types: [
      {
        name: 'mall',
        keyword: 'mall',
      },
    ],
  },
  sports: {
    types: [
      {
        name: 'sports',
        keyword: 'sports',
      },
    ],
  },
  transport: {
    types: [
      {
        name: 'mrt',
        keyword: 'mrt',
      },
      {
        name: 'bus',
        keyword: 'bus',
      },
    ],
  },
};

const QUERY_DEFAULT_SEARCH_DISTANCE = 1000;

const QUERY_DEFAULT_NEED_WALKING_DISTANCE = false;

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
      mapCenter: JSON.parse(JSON.stringify(SINGAPORE)),
      mapZoom: 11,
      mapMarkers: [
        {
          position: JSON.parse(JSON.stringify(SINGAPORE)),
          infoText: 'Singapore',
        },
      ],
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
  methods: {
    handleNearbyPlaces(result) {
      let markers = [];
      const resultObj = JSON.parse(result.body);
      resultObj.forEach(resultByType => {
        resultByType.places.forEach(place => {
          let marker = {};
          marker.position = place.location;
          marker.infoText = place.name;
          markers.push(marker);
        });
      });
      this.mapMarkers = markers;
      this.infoWinOpen = false;
    },
    handleTabClick(payload) {
      const query = JSON.parse(JSON.stringify(QUERIES[payload.name]));
      query.location = JSON.parse(JSON.stringify(this.mapCenter));
      query.radius = QUERY_DEFAULT_SEARCH_DISTANCE;
      query.need_distance = QUERY_DEFAULT_NEED_WALKING_DISTANCE;
      getNearbyPlaces(query).then(result => this.handleNearbyPlaces(result));
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
