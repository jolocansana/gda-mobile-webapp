<template>
  <footer>
    <nav class="d-flex justify-content-evenly h-100 align-items-center">
      <RouterLink to="/car">
        <div class="d-flex flex-column text-center">
          <i class="fa-solid fa-car"></i>
          <span class="navbar-sub">Car</span>
        </div>
      </RouterLink>
      <RouterLink to="/">
        <div class="d-flex flex-column text-center">
          <i class="fa-solid fa-map-location"></i>
          <span class="navbar-sub">Map</span>
        </div>
      </RouterLink>
      <RouterLink to="/account">
        <div class="d-flex flex-column text-center">
          <i class="fa-solid fa-user"></i>
          <span class="navbar-sub">Account</span>
        </div>
      </RouterLink>
    </nav>
  </footer>
</template>

<script setup>
import {RouterLink} from 'vue-router'
</script>

<style>
  footer {
    background-color: darkgrey;
    height: 5rem;
    font-size: 2rem;
    color: black;
  }

  a {
    text-decoration: none;
    color: black;
  }

  a:hover{
    color: green;
  }

  .navbar-sub {
    font-size: 0.5em;
  }
</style>