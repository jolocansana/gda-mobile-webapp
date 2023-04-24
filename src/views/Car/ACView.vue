<template>
  <div class="d-flex flex-column">
    <div class="d-flex justify-content-center align-items-center">
      <div id="car-container" class="image-container">
        <div class="d-flex flex-column text-center">
          <i class="weather-icon fa-solid fa-sun"></i>
          <span class="weather-sub">Sunny</span>
        </div>
      </div>
    </div>
    <div class="">
      <h1>Weather Info</h1>
      <h4>Temperature: 30C</h4>
    </div>
    <div class="mt-3">
      <h1>Air Conditioning Status</h1>

      AC Temperature: 23C
    </div>
  </div>
</template>

<script setup></script>

<style>
.weather-icon {
    font-size: 10em;
  }

.weather-sub {
  font-size: 3rem;
}
</style>