#metric_id
# for i in range(1,1001):
#     if i < 10:
#         print("MID00" + str(i))
#     elif i < 100:
#         print("MID0" + str(i))
#     elif i < 1000:
#         print("MID" + str(i))
#     elif i == 1000:
#         print("MID1000")

#car_id
# for i in range(1,201):
#     print("TA001")

# for i in range(1,201):
#     print("TA002")

# for i in range(1,201):
#     print("TA003")

# for i in range(1,201):
#     print("TA004")

# for i in range(1,201):
#     print("TA005")

#carAC_temp_celcius
# def carAC_temp_celcius(record_size, temp):
#     if record_size == 20:
#         for i in range(record_size):
#             print(temp)
#     elif record_size == 30 or record_size == 40:
#         for i in range(record_size):
#             if i > 19:
#                 print(temp+1)
#             else:
#                 print(temp)
#     elif record_size == 50:
#         for i in range(record_size):
#             if i > 19 and i < 40:
#                 print(temp+1)
#             else:
#                 print(temp)

# carAC_temp_celcius(30, 19)
# carAC_temp_celcius(30, 20)
# carAC_temp_celcius(30, 21)
# carAC_temp_celcius(20, 20)
# carAC_temp_celcius(40, 22)
# carAC_temp_celcius(50, 25)
# carAC_temp_celcius(50, 22)
# carAC_temp_celcius(50, 25)
# carAC_temp_celcius(50, 23)

#engine_temp_celcius
# def engine_temp_celcius(record_size, temp):
#     counter = 0
#     for i in range(record_size):
#         if counter%6==0:
#             temp += 1
#         counter+=1
#         print(temp)

# engine_temp_celcius(30, 84)
# engine_temp_celcius(30, 81)
# engine_temp_celcius(30, 82)
# engine_temp_celcius(20, 80)
# engine_temp_celcius(40, 84)
# engine_temp_celcius(50, 85)
# engine_temp_celcius(50, 87)
# engine_temp_celcius(50, 84)
# engine_temp_celcius(50, 89)


#tyre_pressure_psi - FL, FR, RL, RR
# def tyre_pressure_psi(record_size, psi):
#     counter = 0
#     for i in range(record_size):
#         if counter%110==0:
#             psi -= 1
#         counter+=1
#         print(psi)

# tyre_pressure_psi(200, 35)

#speed_kmh
# def speed_kmh(record_size, speed):
#     counter = 0
#     for i in range(record_size):
#         speed += 2
#         if counter%10==0:
#             speed-=20
#         counter += 1
#         print(speed)

# speed_kmh(30, 69)
# speed_kmh(30, 71)
# speed_kmh(30, 75)
# speed_kmh(20, 84)
# speed_kmh(40, 79)
# speed_kmh(50, 79)
# speed_kmh(50, 74)
# speed_kmh(50, 79)
# speed_kmh(50, 80)

#engine_speed_rpm
#2900/90 * speed

#air_flow_gs
#scaled_value = (value - min_value) * (scaled_max - scaled_min) / (max_value - min_value) + scaled_min
#min_value = 1500
#max_value = 2900
#scaled_max = 25
#scaled_min = 15

#MAP_inHg
# def MAP_inHg(record_size, map):
#     counter = 0
#     for i in range(record_size):
#         if counter%100==0:
#             map += 1
#         counter+=1
#         print(map)

# MAP_inHg(200, 6)

#mileage_km
# def mileage_km(record_size, mileage):
#     for i in range(record_size):
#         print(mileage)
#         mileage += 1

# mileage_km(200, 8388)

#is_vehicle_moving
#if speed > 0, TRUE else FALSE