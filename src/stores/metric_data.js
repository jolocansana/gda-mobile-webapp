import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import metric_data from '../data/metrics_data.csv'

export const useMetricStore = defineStore('metrics', () => {
  // const count = ref(0)
  // const doubleCount = computed(() => count.value * 2)
  // function increment() {
  //   count.value++
  // }

  // return { count, doubleCount, increment }

  const all_metrics = ref(metric_data)
  const latest_metric = ref(metric_data.at(-1))
  const sample = ref(1)

  return { all_metrics, latest_metric, sample} 
})
