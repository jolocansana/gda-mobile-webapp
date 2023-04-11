<template>
  <div class="d-flex flex-column">
    <div class="d-flex justify-content-center align-items-center">
      <div class="image-container">
        <img src="src\assets\car.png" alt="car" id="car-image" usemap="#carMap">
      </div>
    </div>
    <div class="">
      <h1>My Car</h1>
      <h4>Some Car, Some Model</h4>
    </div>
    <div class="mt-3">
      <h1>Car Status</h1>

      <div class="d-flex flex-wrap vw-100">

        <RouterLink to="car/tires" class="status-grid d-flex flex-column">
          <b class="status text-success">Good</b>
          <span>Tire Pressure</span>
        </RouterLink>

        <div class="status-grid d-flex flex-column">
          <b class="status text-warning">Ok</b>
          <span>Oil Levels</span>
        </div>

        <RouterLink to="car/engine" class="status-grid d-flex flex-column">
          <b class="status text-danger">Check</b>
          <span>Engine Temperature</span>
        </RouterLink>
        
      </div>  
    </div>
  </div>
</template>

<script setup>
import { onMounted } from 'vue';

onMounted(() => {
  // run code once page has been mounted
})
</script>

<style>
#car-image {
  width: 80vw;
}

.image-container {
  position: relative;
}

.status {
  font-size: 5vh;
}

.status-grid {
  padding: 1vh 2vw;
  margin: 1vw;
  border-style: solid;
  border-color: black;
  border-width: 1px;
}
</style>