<template>
  <div class="m-0 d-flex flex-column">
    <div class="">
      <RouterView />
    </div>
  </div>
  <Navbar />
</template>

<script setup>
import {RouterView} from 'vue-router'
import Navbar from './components/Navbar.vue'
</script>

<style>
</style>