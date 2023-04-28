import sys
import logging
import pymysql
import json

# rds settings
rds_host  = "gda-metrics-data.ckux9o2yliq3.ap-southeast-1.rds.amazonaws.com"
user_name = "admin"
password = "password"
db_name = "MetricsDB"

logger = logging.getLogger()
logger.setLevel(logging.INFO)

# create the database connection outside of the handler to allow connections to be
# re-used by subsequent function invocations.
try:
    conn = pymysql.connect(host=rds_host, user=user_name, passwd=password, db=db_name, connect_timeout=5)
except pymysql.MySQLError as e:
    logger.error("ERROR: Unexpected error: Could not connect to MySQL instance.")
    logger.error(e)
    sys.exit()

logger.info("SUCCESS: Connection to RDS MySQL instance succeeded")

def lambda_handler(event, context):
    """
    This function creates a new RDS database table and writes records to it
    """
    message = event['Records'][0]['body']
    data = json.loads(message)
    metrics_id = data['metrics_id']
    car_id = data['car_id']
    time_of_record = data['time_of_record']
    env_temp_celcius = data['env_temp_celcius']
    carAC_temp_celcius = data['carAC_temp_celcius']
    engine_temp_celcius = data['engine_temp_celcius']
    FL_tyre_pressure_psi = data['FL_tyre_pressure_psi']
    FR_tyre_pressure_psi = data['FR_tyre_pressure_psi']
    RL_tyre_pressure_psi = data['RL_tyre_pressure_psi']
    RR_tyre_pressure_psi = data['RR_tyre_pressure_psi']
    speed_kmh = data['speed_kmh']
    engine_speed_rpm = data['engine_speed_rpm']
    air_flow_gs = data['air_flow_gs']
    MAP_inHg = data['MAP_inHg']
    mileage_km = data['mileage_km']
    is_vehicle_moving = data['is_vehicle_moving']

    item_count = 0
    sql_string = f"insert into Metrics (metrics_id,car_id,time_of_record,env_temp_celcius,carAC_temp_celcius,engine_temp_celcius,FL_tyre_pressure_psi,FR_tyre_pressure_psi,RL_tyre_pressure_psi,RR_tyre_pressure_psi,speed_kmh,engine_speed_rpm,air_flow_gs,MAP_inHg,mileage_km,is_vehicle_moving) values('{metrics_id}', '{car_id}','{time_of_record}',{env_temp_celcius},{carAC_temp_celcius},{engine_temp_celcius},{FL_tyre_pressure_psi},{FR_tyre_pressure_psi},{RL_tyre_pressure_psi},{RR_tyre_pressure_psi},{speed_kmh},{engine_speed_rpm},{air_flow_gs},{MAP_inHg},{mileage_km},{is_vehicle_moving})"

    with conn.cursor() as cur:
        cur.execute("create table if not exists Metrics ( metrics_id varchar(255) NOT NULL,car_id varchar(255) NOT NULL,time_of_record varchar(255),env_temp_celcius int,carAC_temp_celcius int ,engine_temp_celcius int,FL_tyre_pressure_psi int,FR_tyre_pressure_psi int,RL_tyre_pressure_psi int,RR_tyre_pressure_psi int,speed_kmh int,engine_speed_rpm int,air_flow_gs float,MAP_inHg int,mileage_km int,is_vehicle_moving bool, PRIMARY KEY(metrics_id))")
        cur.execute(sql_string)
        conn.commit()
        cur.execute("select * from Metrics")
        logger.info("The following items have been added to the database:")
        for row in cur:
            item_count += 1
            logger.info(row)
    conn.commit()

    return "Added %d items to RDS MySQL table" %(item_count)
    