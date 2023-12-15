import pandas as pd 
from geopy.geocoders import Nominatim
import random
#Already mocked, check before running 
df = pd.read_csv('csv_files/AccessPoints.csv')

geolocator = Nominatim(user_agent="Mock_data_generator")

def get_location_details(row):
    location = geolocator.reverse((row['Latitude'], row['Longitude']))
    print(location.address)
    return location.address if location else None
print("Before get_location")
df['Location'] = df.apply(get_location_details, axis=1)
print("After get_location")
df['Status'] = [random.choice(['Fine','Not_Fine']) for _ in range(len(df))]

new_df = df[['OBJECTID','Borough','Latitude','Longitude','Location','Status']]
new_df = new_df.rename(columns={'OBJECTID': 'Ap_id'})

new_df.to_csv('csv_files/accesspoint_ver2.csv',index=False)
print("Finished")