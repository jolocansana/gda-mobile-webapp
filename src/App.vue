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
import { onMounted, ref } from 'vue';

//
// Variable and Config Declaration
//

let car_data_array = ref([])
let data_counter = ref(1)
let data_counter_max = 12
var is_generate_data = true

let CAR_ID = 'TA001'

//
// Helper Functions
//

const characters ='ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789';

function generateString(length) {
    let result = ' ';
    const charactersLength = characters.length;
    for ( let i = 0; i < length; i++ ) {
        result += characters.charAt(Math.floor(Math.random() * charactersLength));
    }

    return result;
}

function averageFieldName(arr, key_name) {
  var key_arr = arr.map((item) => {return item[key_name]})
  var avg = key_arr.reduce((a, b) => a + b, 0) / key_arr.length
  console.log(Math.round(avg))
  return Math.round(avg)
}

//
// Start Data
//

let start_car_data = {
  metrics_id: generateString(12),
  car_id: CAR_ID,
  time_of_record: new Date(),
  carAC_temp_celcius: 25,
  engine_temp_celcius: 86,
  FL_tyre_pressure_psi: 35,
  FR_tyre_pressure_psi: 35,
  RL_tyre_pressure_psi: 35,
  RR_tyre_pressure_psi: 34,
  speed_kmh: 0,
  engine_speed_rpm: 0,
  air_flow_gs: 4.29,
  MAP_inHg: 8,
  mileage_km: 2132,
  is_vehicle_moving: false
}

car_data_array.value.push(start_car_data)

//
// Data Randomizers
//

const changeSpeed = (previous_speed) => {
  var curr_speed = 0
  let isRunning = (Math.random() < 0.7 ? true : false)
  if(isRunning) {
    let isConstant = (Math.random() < 0.5 ? true : false)
    if(isConstant && previous_speed > 20) {
      curr_speed = previous_speed + (Math.random() < 0.5 ? -1 : 1)
    } 
    else {
      curr_speed = previous_speed + (Math.random() < 0.5 ? -25 : 25)
    }
    
    if (curr_speed < 0) return 0
    else return curr_speed
  } else {
    return 0
  }
}

//
// Generate Data Functions
//

const generate_data = (is_generate_data) => {
  if(is_generate_data) {

    // NEW VALUES
    var latest_metric = car_data_array.value[car_data_array.value.length-1]
    var curr_speed = changeSpeed(latest_metric.speed_kmh)
    var curr_FR_tyre_pressure = latest_metric.FR_tyre_pressure_psi + (Math.random() < 0.2 && latest_metric.FR_tyre_pressure_psi > 30 ? -5 : 0)

    console.log('NEW VALUES', curr_speed, curr_FR_tyre_pressure)

    var car_data = {
      metrics_id: generateString(12),
      car_id: CAR_ID,
      time_of_record: new Date(),
      carAC_temp_celcius: 25,
      engine_temp_celcius: 86,
      FL_tyre_pressure_psi: 35,
      FR_tyre_pressure_psi: curr_FR_tyre_pressure,
      RL_tyre_pressure_psi: 35,
      RR_tyre_pressure_psi: 34,
      speed_kmh: curr_speed,
      engine_speed_rpm: 0,
      air_flow_gs: 4.29,
      MAP_inHg: 8,
      mileage_km: 2132,
      is_vehicle_moving: (curr_speed == 0 ? false : true)
    }

    car_data_array.value.push(car_data)

    // Store only 4 minutes worth of 10s data
    if(car_data_array.value.length >= 24) car_data_array.value.shift()

    // Every 2 minutes, aggregate and send data to AWS
    if(data_counter.value == data_counter_max) sendDataToAWS()
    else data_counter.value++

    console.log('DATA_GEN: ', car_data_array.value, car_data_array.value.length, data_counter.value)
  }
}

const sendDataToAWS = () => {
  const startIndex = (car_data_array.value.length < 15 ? 0 : 12)
  data_counter.value = 1
  // averageFieldName(car_data_array.value.slice(startIndex, startIndex+11), 'speed_kmh')
  
  // Average Data
  const agg_data = {
    metrics_id: generateString(12),
    car_id: CAR_ID,
    time_of_record: new Date(),
    carAC_temp_celcius: averageFieldName(car_data_array.value.slice(startIndex, startIndex+11), 'carAC_temp_celcius'),
    engine_temp_celcius: averageFieldName(car_data_array.value.slice(startIndex, startIndex+11), 'engine_temp_celcius'),
    FL_tyre_pressure_psi: averageFieldName(car_data_array.value.slice(startIndex, startIndex+11), 'FL_tyre_pressure_psi'),
    FR_tyre_pressure_psi: averageFieldName(car_data_array.value.slice(startIndex, startIndex+11), 'FR_tyre_pressure_psi'),
    RL_tyre_pressure_psi: averageFieldName(car_data_array.value.slice(startIndex, startIndex+11), 'RL_tyre_pressure_psi'),
    RR_tyre_pressure_psi: averageFieldName(car_data_array.value.slice(startIndex, startIndex+11), 'RR_tyre_pressure_psi'),
    speed_kmh: averageFieldName(car_data_array.value.slice(startIndex, startIndex+11), 'speed_kmh'),
    engine_speed_rpm: averageFieldName(car_data_array.value.slice(startIndex, startIndex+11), 'engine_speed_rpm'),
    air_flow_gs: averageFieldName(car_data_array.value.slice(startIndex, startIndex+11), 'air_flow_gs'),
    MAP_inHg: averageFieldName(car_data_array.value.slice(startIndex, startIndex+11), 'MAP_inHg'),
    mileage_km: averageFieldName(car_data_array.value.slice(startIndex, startIndex+11), 'mileage_km'),
    is_vehicle_moving: true
  }

  console.log('AVG DATA:', agg_data)

}

//
// 10s Loop
//

setInterval(() => {
  generate_data(is_generate_data)
}, 10000)

// const sample_arr = [
//   {one: 1, two: 2, three: 3},
//   {one: 10, two: 2, three: 6},
//   {one: 1, two: 5, three: 5},
// ]

// const sample_key = 'one'
// console.log(sample_arr.map(item=>{return item[sample_key]}))


</script>

<style>
</style>