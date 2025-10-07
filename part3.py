# --- TODO: Complete the tasks listed in tutorial. Run and verify your results before submission. --- #
'''
Import necessary libraries here
'''
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

'''
Load the datasets
'''
df=pd.read_csv("avg_soil_moisture_by_sensor.csv")
mdf=pd.read_csv("plant_sensors.csv")

'''
Exercise 3.1: Bar Chart
'''
# fig, ax = plt.subplots(figsize=(8, 5),num="Exercise 3.1: Bar Chart")
# ax.bar(df["sensor_id"],df["avg_soil_moisture"], label='Avg Soil Moisture', color='skyblue')
# # ax.plot(df["sensor_id"], df["avg_soil_moisture"])
# ax.set_title("Average Soil Moisture by Sensor")
# bars = ax.patches
# for bar in bars:
#     # 
#     height = bar.get_height()
#     # 
#     x_pos = bar.get_x() + bar.get_width() / 2
#     # 
#     ax.text(
#         x_pos,          # 
#         height + 0.5,   # 
#         f'{round(height,2)}%',    # 
#         ha='center',    # 
#         va='bottom'     # 
# )

# ax.set_xlabel("Sensor ID")
# ax.set_ylabel("Average Soil Moisture (%)")

# ax.set_ylim(0, 100)

# ax.grid()
# ax.legend()
# plt.show()
'''
Exercise 3.2: Line Plot
'''
# mdf=(mdf.groupby("sensor_id")).get_group("A-1")
# mdf['timestamp']=pd.to_datetime(mdf['timestamp'])
# mdf['soil_moisture']=mdf['soil_moisture'].str.replace(r'\s*%', '', regex=True).astype(float)
# #fill the empty valueS
# mdf['timestamp']=mdf['timestamp'].interpolate(method='linear')
# mdf['soil_moisture']=mdf.groupby(pd.Grouper(key='timestamp', freq='D'))['soil_moisture'].transform(
#     lambda group: group.fillna(group.mean()))
# mdf=mdf.set_index('timestamp')
# print(mdf.head())
# fig,ax=plt.subplots(figsize=(15, 6),num="Exercise 3.2: Line Plot")
# ax.plot(mdf.index,mdf['soil_moisture'], label='Soil Moisture', color='green')
# ax.set_title("Soil Moisture Over Time for Sensor A-1")
# ax.set_xlabel("Time")
# ax.set_ylabel("Soil Moisture (%)")
# ax.set_ylim(0, 100)
# ax.grid()
# ax.legend()
# plt.show()
'''
Exercise 3.3: Subplots and Anomaly Detection
'''
fig,axs=plt.subplots(1,2,figsize=(15, 6),num="Exercise 3.3:Subplots and Anomaly Detection")
axs[0].hist(mdf['temperature_c'].str.replace(r'\s*˚C', '', regex=True).astype(float), bins=40, color='orange', edgecolor='black')
axs[0].set_title("Distribution of All Temperature Readings")
axs[0].set_xlabel("Temperature (˚C)")
axs[0].set_ylabel("Frequency")
axs[0].grid()


axs[1].set_title("Temperature vs. Soil Moisture")
axs[1].scatter(mdf['temperature_c'].str.replace(r'\s*˚C', '', regex=True).astype(float),
               mdf['soil_moisture'].str.replace(r'\s*%', '', regex=True).astype(float),
               alpha=0.1 ,color='purple')
axs[1].set_xlabel("Temperature (˚C)")
axs[1].set_ylabel("Soil Moisture (%)")
axs[1].grid()

plt.show()