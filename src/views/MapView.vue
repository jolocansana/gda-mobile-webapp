<template>
<div class="modal" tabindex="-1" id="myModal">
  <div class="modal-dialog modal-dialog-centered">
    <div class="modal-content">
      <div class="modal-header">
        <h5 class="modal-title">Sample Alert Notifcation</h5>
        <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
      </div>
      <div class="modal-body">
        <p>Alert Notification Body</p>
      </div>
    </div>
  </div>
</div>
</template>

<script setup>
import { onMounted } from 'vue';

onMounted(() => {
    var myModal = new bootstrap.Modal(document.getElementById('myModal'))

    myModal.toggle();
})
</script>