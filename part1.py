import numpy as np
import pandas as pd

# --- TODO: Complete the tasks listed in tutorial. Run and verify your results before submission. --- #

'''
Load the datasets
'''
df=pd.read_csv('plant_sensors.csv')
df['timestamp']=pd.to_datetime(df['timestamp'])


'''
Exercise 1.1: Array Basics
'''
moisture_readings=np.array(df['soil_moisture'].str.replace(' %','').astype(float))
calibrated_moisture=moisture_readings-0.5
print("first 5 of calibrated_moisture:",calibrated_moisture[:5])

'''
Exercise 1.2: Array Slicing and Stats
'''
print("50th to 59th soil_moisture:",calibrated_moisture[50:60])
print("Mean:",np.nanmean(calibrated_moisture))
print("Median:",np.nanmedian(calibrated_moisture))
print("Quantiles:",np.nanquantile(calibrated_moisture,[0.25,0.5,0.75]))
print("Standard Deviation:",np.nanstd(calibrated_moisture))


'''
Exercise 1.3: Boolean Indexing and Logic
'''
moisture_status = np.where (calibrated_moisture < 35, 'Dry', np.where(calibrated_moisture <= 70, 'Ok','Wet'))
print("first 10 of moisture_status:",moisture_status[:10])