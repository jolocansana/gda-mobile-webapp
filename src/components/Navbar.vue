<template>
  <footer>
    <nav class="d-flex justify-content-evenly">
      <RouterLink to="/car">Car</RouterLink>
      <RouterLink to="/">Map</RouterLink>
      <RouterLink to="/account">Account</RouterLink>
    </nav>
  </footer>
</template>

<script setup>
import {RouterLink} from 'vue-router'
</script>

<style>
  footer {
    background-color: darkgrey;
    height: 10%;
  }
</style>