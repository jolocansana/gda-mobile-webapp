<template>
  <div class="modal" tabindex="-1" id="myModal">
    <div class="modal-dialog modal-dialog-centered">
      <div class="modal-content">
        <div class="modal-body d-flex flex-column text-center">
          <button
            type="button"
            class="btn-close"
            data-bs-dismiss="modal"
            aria-label="Close"
          ></button>
          <i class="fa-solid fa-car-side" style="font-size: 7rem;"></i>
          <h1 class="mt-2">Pump your tires!</h1>
          <p>Your left rear tires are in a unsuitable pressure level. Proceed to the nearest gas station to get your tires pumped.</p>
        </div>
      </div>
    </div>
  </div>


  <div class="d-flex flex-column container">
    <div class="d-flex justify-content-center align-items-center">
      <div id="car-container" class="image-container">
        <img src="src\assets\car\full-orientation.png" alt="car" id="car-image">
      </div>
    </div>
    <div class="">
      <h1>My Car</h1>
      <h4>Some Car, Some Model</h4>
    </div>
    <div class="mt-3">
      <h1>Car Status</h1>

      <div class="d-flex flex-wrap w-100 text-center">

        <RouterLink to="car/tires" class="status-grid d-flex flex-column flex-grow-1">
          <b class="status text-success">Good</b>
          <span>Tire Pressure</span>
        </RouterLink>

        <RouterLink to="car/ac" class="status-grid d-flex flex-column flex-grow-1">
          <b class="status text-warning">Ok</b>
          <span>AC Temperature</span>
        </RouterLink>

        <RouterLink to="car/engine" class="status-grid d-flex flex-column flex-grow-1">
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
  var myModal = new bootstrap.Modal(document.getElementById("myModal"));
  myModal.toggle();
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