# --- TODO: Complete the tasks listed in tutorial. Run and verify your results before submission. --- #
'''
Import necessary libraries here
'''
import numpy as np
import pandas as pd


'''
Load the datasets
'''
df=pd.read_csv("plant_sensors.csv")
print("File head:\n",df.head())
print("\nthe shape of dataframe:",df.shape,"\n")
print(df.info())


'''
Exercise 2.1: Initial Inspection & Cleaning
'''
df['timestamp']=pd.to_datetime(df['timestamp'])
# print(df['timestamp'].dt.year)
temperature_f=df['temperature_c'].str.replace(r'\s*˚C', '', regex=True).astype(float)*9/5+32
print("first 5 of temperature_f:\n",temperature_f.head())

'''
Exercise 2.2: Missing Data & Filtering
'''
nullsum=(df['soil_moisture'].str.replace(r'\s*%', '', regex=True).astype(float)).isnull().sum()
df['soil_moisture'] = df['soil_moisture'].str.replace(r'\s*%', '', regex=True).astype(float)

# n=pd.DataFrame()
# n["timestamp_unix"]= df['timestamp'].astype('int64')  # 转换为数值型
# n['timestamp_unix'] = n['timestamp_unix'].interpolate(method='time')
# df['timestamp'] = pd.to_datetime(n['timestamp_unix'], unit='ns')
df['timestamp']=df['timestamp'].interpolate(method='linear')
df['soil_moisture'] = df.groupby('timestamp')['soil_moisture'].transform(
    lambda group: group.fillna(group.mean()))
print("number of missing ",nullsum,"\n\n")
patio_high_light=df["light_level"].str.replace(r'\s*lx', '', regex=True).astype(float)
patio_high_light=patio_high_light[patio_high_light>1200]
print("first 5 of patio_high_light ",patio_high_light.head(),"\n\n")


# df.to_csv('plant_sensors_cleaned.csv', index=False)

'''
Exercise 2.3: Grouping and Aggregation
'''
soil_moisture_avg=df.groupby('sensor_id')['soil_moisture'].mean()
pump_activation_counts=df.groupby('plant_type')['pump_active'].sum()
df['temperature_c']=df['temperature_c'].str.replace(r'\s*˚C', '', regex=True).astype(float)

highest_temp=df.groupby('location')['temperature_c']
highest_temp=highest_temp.max()

print("soil_moisture_avg:\n",soil_moisture_avg,"\n")
print("pump_activation_counts:\n",pump_activation_counts,"\n")
print("highest_temp(˚C):\n",highest_temp,"\n")

soil_csv=soil_moisture_avg.reset_index()
soil_csv.columns=['sensor_id','avg_soil_moisture']
soil_csv.to_csv('avg_soil_moisture_by_sensor.csv', index=False)
