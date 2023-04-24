<template>
  <div id="map"></div>
</template>

<script setup>
import { onMounted, ref } from "vue";

onMounted(() => {
  var map = L.map("map").setView([51.505, -0.09], 13);

  L.tileLayer("https://tile.openstreetmap.org/{z}/{x}/{y}.png", {
    maxZoom: 19,
    attribution:
      '&copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a>',
  }).addTo(map);

});
</script>

<style>
#map {
  height: 100vh;
  z-index: -1;
}
</style>
