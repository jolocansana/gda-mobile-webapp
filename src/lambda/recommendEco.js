const recommendEcoTest = async () => {
  const json_body = {
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
  //
  // COPY AFTER HERE
  //
  //
  let recommedations = []
  
  //
  // Recommendation Logic
  //
  
  // Check if tire pressure is not ideal // FR TO TEST
  if (json_body.FR_tyre_pressure_psi < 32) {
    const obj = {
      "field": "FR_tyre_pressure_psi",
      "title": "Check your tires!",
      "message": "Your left rear tires are in a unsuitable low pressure level. Proceed to the nearest gas station to get your tires pumped.",
      "icon": "fa-solid fa-car-side"
    }
  
    recommedations.push(obj)
  }
  if (json_body.FR_tyre_pressure_psi > 36) {
    const obj = {
      "field": "FR_tyre_pressure_psi",
      "title": "Check your tires!",
      "message": "Your left rear tires are in a unsuitable high pressure level. When safe, try to release some air in the tires",
      "icon": "fa-solid fa-car-side"
    }
  
    recommedations.push(obj)
  }
  
  // Change AC temp based on Outside Temperature
  const https = require('https')
  let recom_temp_c = 0
  let outside_temp_c = 0
  let resp_data = ''
  await new Promise((resolve) => {
      https.get('https://api.openweathermap.org/data/2.5/weather?lat=1.2839934738374048&lon=103.85909576699606&appid=1573c64dacd7de9ad6ccc22cbadbeeda&units=imperial', (resp) => {
      resp.on('data', (data) => {
        resp_data = JSON.parse(data)
        recom_temp_c = (((resp_data.main.temp-20)-32) * 0.5555)
        outside_temp_c = (((resp_data.main.temp)-32) * 0.5555)
        resolve()
      })
    })
  })
  
  if(json_body.carAC_temp_celcius < recom_temp_c) {
    const obj = {
      "field": "carAC_temp_celcius",
      "title": "Bring your temperature above " + Math.floor(recom_temp_c) + "C",
      "message": "Since the outside temperatures are in " + Math.floor(outside_temp_c) + "C, it is advisable to adjust your temperature above to save gas yet remain comfortable.",
      "icon": "fa-solid fa-temperature-arrow-down",
      "data": {
        "recom_temp_c": recom_temp_c
      }
    }
    recommedations.push(obj)
  }
  
  const response = {
    statusCode: 200,
    body: JSON.stringify(recommedations),
  }
  
  //
  //
  // COPY UNTIL HERE
  //
  //
  
  return response
}

recommendEcoTest().then( resp => console.log(JSON.parse(resp.body)))

