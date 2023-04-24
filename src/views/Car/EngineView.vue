<template>
  <div class="d-flex flex-column">
    <div class="d-flex justify-content-center align-items-center">
      <div id="car-container" class="image-container">
        <img src="/../src/assets/car/engine.png" alt="car" id="car-image" />
      </div>
    </div>
    <div class="">
      <h1>My Car</h1>
      <h4>Some Car, Some Model</h4>
    </div>
    <div class="mt-3">
      <h1>Engine Status</h1>

      Engine Temperature: {{ engineTemp }} C
    </div>
  </div>
</template>

<script setup>
import { useMetricStore } from "../../stores/metric_data";
import { storeToRefs } from "pinia";
import { onMounted, ref } from "vue";

const engineTemp = ref(0)

onMounted(() => {
  const metric_store = useMetricStore();
  const { all_metrics, latest_metric } = storeToRefs(metric_store);

  engineTemp.value = latest_metric.value.engine_temp_celcius
  
});
</script>