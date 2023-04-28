<template>
  <div class="modal" tabindex="-1" id="myModal">
    <div class="modal-dialog modal-dialog-centered">
      <div class="modal-content">
        <div class="modal-body d-flex flex-column text-center">
          <button
            type="button"
            class="btn-close"
            @click="closeModal"
            aria-label="Close"
          ></button>
          <i :class="icon" style="font-size: 7rem;"></i>
          <h1 class="mt-2">{{ title }}</h1>
          <p>{{ message }}</p>
        </div>
      </div>
    </div>
  </div>

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
import axios from 'axios';

//
// Variable and Config Declaration
//

let car_data_array = ref([])
let data_counter = ref(1)
let data_counter_max = 12
var is_generate_data = true

var myModal
const notifications = ref([])
const icon = ref('')
const title = ref('')
const message = ref('')
const isModalActive = ref(false)

let CAR_ID = 'TA001'
let test_agg_data = {
    "metrics_id": " IKcf4sILbHQT",
    "car_id": "TA001",
    "time_of_record": "2023-04-25T14:24:09.663Z",
    "carAC_temp_celcius": 15,
    "engine_temp_celcius": 86,
    "FL_tyre_pressure_psi": 35,
    "FR_tyre_pressure_psi": 30,
    "RL_tyre_pressure_psi": 35,
    "RR_tyre_pressure_psi": 34,
    "speed_kmh": 7,
    "engine_speed_rpm": 0,
    "air_flow_gs": 4,
    "MAP_inHg": 8,
    "mileage_km": 2132,
    "is_vehicle_moving": true
}

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
  // console.log(Math.round(avg))
  return Math.round(avg)
}

function renderNotifications() {
  if(notifications.value.length > 0 && !isModalActive.value) {
    var latest_notif = notifications.value.pop()
    console.log(latest_notif)
    icon.value = latest_notif.icon
    title.value = latest_notif.title
    message.value = latest_notif.message
    isModalActive.value = true
    myModal.show()
  }
  console.log('NOTIF: ', notifications.value)
}


function closeModal(){
  myModal.hide()
  isModalActive.value = false
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

    console.log('NEW VALUES SPEED: ', curr_speed, 'TYRE: ', curr_FR_tyre_pressure)

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

    console.log('DATA_GEN: ', car_data_array.value, '\nARRAY LENGTH: ', car_data_array.value.length, '\nCOUNT: ', data_counter.value)
  }
}

const sendDataToAWS = () => {
  const startIndex = (car_data_array.value.length < 15 ? 0 : 12)
  data_counter.value = 1
  averageFieldName(car_data_array.value.slice(startIndex, startIndex+11), 'speed_kmh')
  
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

  // const agg_data = test_agg_data
  // console.log('AVG DATA:', agg_data)


  let string_data = JSON.stringify(agg_data)

  // Push data to RDS
  axios.post('https://abs0mxhj35.execute-api.ap-southeast-1.amazonaws.com/prod/pushRDS', string_data).then(resp => {
    console.log(resp)
  }).catch(err => console.log(err))

  // Process data for recommendations
  axios.post('https://voj3iwpcb7.execute-api.ap-southeast-1.amazonaws.com/prod/recommendeco', string_data).then(resp => {
    for (var item of resp.data) notifications.value.push(item)
    console.log(resp)
  }).catch(err => console.log(err))

}

//
// 10s Loop
//

setInterval(() => {
  generate_data(is_generate_data)
  renderNotifications()
}, 10000)

// sendDataToAWS()

onMounted(() => {
  myModal = new bootstrap.Modal(document.getElementById("myModal"));
})
</script>

<style>
</style>