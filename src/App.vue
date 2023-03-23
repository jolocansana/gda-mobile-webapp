<template>
  <div class="vh-100 d-flex flex-column">
    <div class="flex-fill">
      <RouterView />
    </div>
    <Navbar />
  </div>
</template>

<script setup>
import {RouterView} from 'vue-router'
import Navbar from './components/Navbar.vue'
</script>

<style>
</style>