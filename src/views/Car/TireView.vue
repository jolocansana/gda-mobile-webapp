<template>
  <div class="d-flex flex-column container">
    <div class="d-flex justify-content-center align-items-center">
      <div id="car-container" class="image-container">
        <img src="/../src/assets/car/tires.png" alt="car" id="car-image" />
      </div>
    </div>
    <div class="">
      <h1>My Car</h1>
      <h4>Some Car, Some Model</h4>
    </div>
    <div class="mt-3">
      <h1>Tire Status</h1>

      <table class="table">
        <thead>
          <tr>
            <th scope="col">Tire</th>
            <th scope="col">Pressure in PSI</th>
            <th scope="col">Status</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td>Front Left</td>
            <td>{{ FLpsi }} psi</td>
            <td>Good</td>
          </tr>
          <tr>
            <td>Front Right</td>
            <td>{{ FRpsi }} psi</td>
            <td>Good</td>
          </tr>
          <tr>
            <td>Rear Left</td>
            <td>{{ RLpsi }} psi</td>
            <td>Good</td>
          </tr>
          <tr>
            <td>Rear Right</td>
            <td>{{ RRpsi }} psi</td>
            <td>Good</td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
</template>

<script setup>
import { useMetricStore } from "../../stores/metric_data";
import { storeToRefs } from "pinia";
import { onMounted, ref } from "vue";

const FLpsi = ref(0)
const FRpsi = ref(0)
const RLpsi = ref(0)
const RRpsi = ref(0)

onMounted(() => {
  const metric_store = useMetricStore();
  const { all_metrics, latest_metric } = storeToRefs(metric_store);

  FLpsi.value = latest_metric.value.FL_tyre_pressure_psi
  FRpsi.value = latest_metric.value.FR_tyre_pressure_psi
  RLpsi.value = latest_metric.value.RL_tyre_pressure_psi
  RRpsi.value = latest_metric.value.RR_tyre_pressure_psi
  
});
</script>
