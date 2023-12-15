import requests
import csv

ap_url = "http://192.168.3.55:8080/api/v1/accesspoint/"

with open("csv_files/accesspoint_ver2.csv",'r') as ap_file:
    ap_reader = csv.DictReader(ap_file)
    success = 0
    fail = 0
    for row in ap_reader:
        response = requests.post(ap_url,json=row)
        if response.status_code == 201:
            print("Accesspoint successfully populated")
            print('Response:', response.json())
            success += 1
        else: 
            print("Failed to populate Accesspoint")
            print('Response:', response.text)
            fail += 1
                
    print(success)
    print(fail)
                
print("Program executed successfully")