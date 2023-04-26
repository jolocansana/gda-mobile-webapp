<template>
  <div class="d-flex justify-content-center align-items-center w-100 text-center flex-column mt-5">
    <img src="../assets/charles-leclerc-ferrari-1.jpg" alt="photo" width="250" class="rounded-circle mb-3">
    <h2>Charles Leclerc</h2>
    <h4>Singapore, Singapore</h4>
  </div>

  <div class="container mt-3">
    <h2>Personal Details</h2>
    
    <table class="w-100">
      <tbody>
        <tr>
          <td><b>Birthdate</b></td>
          <td>January 1, 1999</td>
        </tr>
        <tr>
          <td><b>Sex</b></td>
          <td>Male</td>
        </tr>
      </tbody>
    </table>
  </div>

  <div class="container mt-3">
    <h2>Car Details</h2>
    
    <table class="w-100">
      <tbody>
        <tr>
          <td><b>Make</b></td>
          <td>Ferrari</td>
        </tr>
        <tr>
          <td><b>Model</b></td>
          <td>SF23</td>
        </tr>
        <tr>
          <td><b>Year</b></td>
          <td>2023</td>
        </tr>
      </tbody>
    </table>
  </div>

</template>

<script setup>
import { useUserStore } from "../stores/user_data";
import { storeToRefs } from "pinia";
import { onMounted, ref } from "vue";
import axios from 'axios';

const alert_body = ref('')

onMounted(() => {
  const user_store = useUserStore();
  const { all_users } = storeToRefs(user_store);

  console.log(all_users.value)

  // var myModal = new bootstrap.Modal(document.getElementById("myModal"));
  // myModal.toggle();
  // axios.get('https://4rmmyhvha9.execute-api.ap-southeast-1.amazonaws.com/testFunc').then((response) => {
  //   alert_body.value = response.data
  //   myModal.toggle();
  // })
  
});
</script>
