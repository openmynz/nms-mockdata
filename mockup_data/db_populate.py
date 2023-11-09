import pandas as pd
import requests 
import csv

#Note: The data is populated when the server was running locally, change the api if needed
#Note: The data is already pre-processed and check the data availability before running this file

def post_accesspoints():
    
    #Pre-processing
    #preprocess_ap()
    
    accesspoints_file_path = "csv_files/AccessPoints.csv"
    ap_data = pd.read_csv(accesspoints_file_path)
    ap_url = "http://127.0.0.1:8000/api/v1/accesspoints/"

    #Populating the AccessPoints table
    ap_json_data = []
    with open(accesspoints_file_path,'r') as ap_file: 
        ap_reader = csv.DictReader(ap_file)
        for row in ap_reader:
            response = requests.post(ap_url, json=row)
            if response.status_code == 201:
                print("AccessPoints successfully populated")
                print('Response:', response.json())
            else: 
                print("Failed to populate AccessPoints")
                print('Response:', response.text)
            ap_json_data.append(row)

def post_sites():
    
    #Pre-processing
    #preprocess_sites()
    
    sites_file_path = "csv_files/Sites.csv"
    sites_data = pd.read_csv(sites_file_path)
    sites_url = "http://127.0.0.1:8000/api/v1/sites/"
        
    #Populating the Sites table
    sites_json_data = []
    with open(sites_file_path,'r') as sites_file:
        sites_reader = csv.DictReader(sites_file)
        for row in sites_reader:
            
            response = requests.post(sites_url, json=row)
            if response.status_code == 201:
                print("Sites successfully populated")
                print('Response:', response.json())
            else: 
                print("Failed to populate Sites")
                print('Response:', response.text)
            sites_json_data.append(row)

def preprocess_ap():
    ap_data = pd.read_csv("csv_files/AccessPoints.csv")
    ap_data['Activated'] = ap_data["Activated"].fillna("2099-01-01")
    ap_data['Remarks'] = ap_data['Remarks'].fillna("Remarks not available")
    ap_data.to_csv("csv_files/AccessPoints.csv", index=False)

def preprocess_sites():
    sites_data = pd.read_csv("csv_files/Sites.csv")
    sites_data['Name'] = sites_data['Name'].fillna("Name of location not available")
    sites_data['Name'] = sites_data['Name'].replace("0","Name of location not available")
    sites_data.to_csv("csv_files/Sites.csv", index=False)   
    
def populate_db():
    post_accesspoints()
    post_sites()
    
#Main
def main():
    populate_db()
    
if __name__ == "__main__":
    main()