<template>
  <div class="d-flex flex-column">
    <div class="d-flex justify-content-center align-items-center">
      <div id="car-container" class="image-container">
        <!-- <img src="src\assets\car.png" alt="car" id="car-image" usemap="#carMap"> -->
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
import * as THREE from 'three';
import { OBJLoader } from 'three/addons/loaders/OBJLoader.js';

const scene = new THREE.Scene();
const camera = new THREE.PerspectiveCamera( 
  75, 
  window.innerWidth / window.innerHeight, 
  0.1, 
  10000
);
const loader = new OBJLoader();

// load a resource
loader.load(
  // resource URL
  'src/assets/mercedes-and-nissan-cars-3d-model/Nissan_skyline/Nissan_skyline.obj',
  // called when resource is loaded
  function ( object ) {

    scene.add( object );

  },
  // called when loading is in progresses
  function ( xhr ) {

    console.log( ( xhr.loaded / xhr.total * 100 ) + '% loaded' );

  },
  // called when loading has errors
  function ( error ) {

    console.log( error );

  }
);

const renderer = new THREE.WebGLRenderer();
renderer.setSize( window.innerWidth, window.innerHeight/2);

function animate() {
	requestAnimationFrame( animate );

	renderer.render( scene, camera );
}


onMounted(() => {
  document.getElementById('car-container').appendChild( renderer.domElement );
  animate();
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