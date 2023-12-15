import pandas as pd
import requests
from faker import Faker
fake = Faker()

df = pd.read_csv('csv_files/accesspoint_ver2.csv')
ap_id = df['ap_id']

eth1 = 0
eth1_fail = 0
eth2 = 0
eth2_fail = 0
wl1 = 0
wl1_fail = 0
wl2 = 0
wl2_fail = 0
usb1 = 0
usb1_fail = 0
bss1 = 0 
bss1_fail = 0
bss2 = 0 
bss2_fail = 0
bss3 = 0
bss3_fail = 0

interface_url = 'http://192.168.3.55:8080/api/v1/interface/' 
mock_interface_3_list = []
mock_interface_4_list = []

for ap in ap_id:
    mock_interface_1 = {
        "interface_id" : f'Eth{ap}_1',
        "interface_name" : "Power_Over_Internet",
        "interface_type" : "Ethernet",
        "ap_id" : ap,
        "tx_bytes": fake.random_number(digits=8),
        "rx_bytes": fake.random_number(digits=8),
        "tx_errors": fake.random_number(digits=2),
        "rx_errors": fake.random_number(digits=2)
    }
    response = requests.post(interface_url, json=mock_interface_1)
    if response.status_code == 201:
        print("Mock Ethernet 1 posted successfully")
        eth1 += 1
    else:
        print("Failed to post mock Ethernet 1")
        eth1_fail += 1
        print(response.text)
    
    mock_interface_2 = {
        "interface_id" : f'Eth{ap}_2',
        "interface_name" : "Ethernet_SFP",
        "interface_type" : "Ethernet",
        "ap_id" : ap,
        "tx_bytes": fake.random_number(digits=8),
        "rx_bytes": fake.random_number(digits=8),
        "tx_errors": fake.random_number(digits=2),
        "rx_errors": fake.random_number(digits=2)    
    }
    response = requests.post(interface_url, json=mock_interface_2)
    if response.status_code == 201:
        print("Mock Ethernet 2 posted successfully")
        eth2 += 1
    else:
        print("Failed to post mock Ethernet 2")
        eth2_fail += 1
        print(response.text)
    
    mock_interface_3 = {
        "interface_id" : f'Wl{ap}_1',
        "interface_name" : "802.11ac",
        "interface_type" : "Wireless",
        "ap_id" : ap,
        "tx_bytes": fake.random_number(digits=8),
        "rx_bytes": fake.random_number(digits=8),
        "tx_errors": fake.random_number(digits=2),
        "rx_errors": fake.random_number(digits=2)
    }
    response = requests.post(interface_url, json=mock_interface_3)
    if response.status_code == 201:
        print("Mock Wireless 1 posted successfully")
        wl1 += 1
    else:
        print("Failed to post mock Wireless 1")
        wl1_fail += 1
        print(response.text)
    mock_interface_3_list.append(mock_interface_3)
    
    mock_interface_4 = {
        "interface_id" : f'Wl{ap}_2',
        "interface_name" : "802.11ax",
        "interface_type" : "Wireless",
        "ap_id" : ap,
        "tx_bytes": fake.random_number(digits=8),
        "rx_bytes": fake.random_number(digits=8),
        "tx_errors": fake.random_number(digits=2),
        "rx_errors": fake.random_number(digits=2)
    }
    response = requests.post(interface_url, json=mock_interface_4)
    if response.status_code == 201:
        print("Mock Wireless 2 posted successfully")
        wl2 += 1
    else:
        print("Failed to post mock Wireless 2")
        wl2_fail += 1
        print(response.text)
    mock_interface_4_list.append(mock_interface_4)
    
    mock_interface_5 = {
        "interface_id" : f'Usb{ap}_1',
        "interface_name" : "USB3.0",
        "interface_type" : "USB",
        "ap_id" : ap,
        "tx_bytes": fake.random_number(digits=8),
        "rx_bytes": fake.random_number(digits=8),
        "tx_errors": fake.random_number(digits=2),
        "rx_errors": fake.random_number(digits=2)
    }  
    response = requests.post(interface_url, json=mock_interface_5)
    if response.status_code == 201:
        print("Mock USB 1 posted successfully")
        usb1 += 1
    else:
        print("Failed to post mock USB 1")
        usb1_fail += 1
        print(response.text)    
    
bss_url = 'http://192.168.3.55:8080/api/v1/bss/'
    
for interface in mock_interface_3_list:
    ap_id = interface["ap_id"]
    interface_id = interface["interface_id"]
    ssid_name = fake.user_name()
    passphrase = fake.password()
    security_mode = fake.random_element(elements=('WEP', 'WPA', 'WPA2', 'WPA3'))
    
    mockup_bss_1 = {
        "bss_id": f'Bss{ap_id}_1_1',
        "ssid_name": f'{ssid_name}_2.4GHz',
        "passphrase": passphrase,
        "security_mode": security_mode,
        "status": fake.random_element(elements=('active', 'inactive')),
        "num_clients": fake.random_int(min=0, max=100),
        "tx_bytes": fake.random_number(digits=8),
        "rx_bytes": fake.random_number(digits=8),
        "tx_errors": fake.random_int(min=0, max=10),
        "rx_errors": fake.random_int(min=0, max=5),
        "interface_id": interface_id
    }
    response = requests.post(bss_url, json=mockup_bss_1)
    if response.status_code == 201:
        print("Mock Bss 2.4GHz for Interface 1 posted successfully")
        bss1 += 1
    else:
        print("Failed to post mock Bss 2.4GHz for Interface 1")
        bss1_fail += 1
        print(response.text)
    
    mockup_bss_2 = {
        "bss_id": f'Bss{ap_id}_1_2',
        "ssid_name": f'{ssid_name}_5GHz',
        "passphrase": passphrase,
        "security_mode": security_mode,
        "status": fake.random_element(elements=('active', 'inactive')),
        "num_clients": fake.random_int(min=0, max=100),
        "tx_bytes": fake.random_number(digits=8),
        "rx_bytes": fake.random_number(digits=8),
        "tx_errors": fake.random_int(min=0, max=10),
        "rx_errors": fake.random_int(min=0, max=5),
        "interface_id": interface_id
    }
    response = requests.post(bss_url, json=mockup_bss_2)
    if response.status_code == 201:
        print("Mock Bss 5GHz for Interface 1 posted successfully")
        bss2 += 1
    else:
        print("Failed to post mock Bss 5GHz for Interface 1")
        bss2_fail += 1
        print(response.text)
        
    mockup_bss_3 = {
        "bss_id": f'Bss{ap_id}_1_3',
        "ssid_name": f'{ssid_name}_6GHz',
        "passphrase": passphrase,
        "security_mode": security_mode,
        "status": fake.random_element(elements=('active', 'inactive')),
        "num_clients": fake.random_int(min=0, max=100),
        "tx_bytes": fake.random_number(digits=8),
        "rx_bytes": fake.random_number(digits=8),
        "tx_errors": fake.random_int(min=0, max=10),
        "rx_errors": fake.random_int(min=0, max=5),
        "interface_id": interface_id
    }
    response = requests.post(bss_url, json=mockup_bss_3)
    if response.status_code == 201:
        print("Mock Bss 6GHz for Interface 1 posted successfully")
        bss3 += 1
    else:
        print("Failed to post mock Bss 6GHz for Interface 1")
        bss3_fail += 1
        print(response.text)
    
for interface in mock_interface_4_list:
    ap_id = interface["ap_id"]
    interface_id = interface["interface_id"]
    ssid_name = fake.user_name()
    passphrase = fake.password()
    security_mode = fake.random_element(elements=('WEP', 'WPA', 'WPA2', 'WPA3'))
    
    mockup_bss_1 = {
        "bss_id": f'Bss{ap_id}_2_1',
        "ssid_name": f'{ssid_name}_2.4GHz',
        "passphrase": passphrase,
        "security_mode": security_mode,
        "status": fake.random_element(elements=('active', 'inactive')),
        "num_clients": fake.random_int(min=0, max=100),
        "tx_bytes": fake.random_number(digits=8),
        "rx_bytes": fake.random_number(digits=8),
        "tx_errors": fake.random_int(min=0, max=10),
        "rx_errors": fake.random_int(min=0, max=5),
        "interface_id": interface_id
    }
    response = requests.post(bss_url, json=mockup_bss_1)
    if response.status_code == 201:
        print("Mock Bss 2.4GHz for Interface 2 posted successfully")
        bss1 += 1
    else:
        print("Failed to post mock Bss 2.4GHz for Interface 2")
        bss1_fail += 1
        print(response.text)
    
    mockup_bss_2 = {
        "bss_id": f'Bss{ap_id}_2_2',
        "ssid_name": f'{ssid_name}_5GHz',
        "passphrase": passphrase,
        "security_mode": security_mode,
        "status": fake.random_element(elements=('active', 'inactive')),
        "num_clients": fake.random_int(min=0, max=100),
        "tx_bytes": fake.random_number(digits=8),
        "rx_bytes": fake.random_number(digits=8),
        "tx_errors": fake.random_int(min=0, max=10),
        "rx_errors": fake.random_int(min=0, max=5),
        "interface_id": interface_id
    }
    response = requests.post(bss_url, json=mockup_bss_2)
    if response.status_code == 201:
        print("Mock Bss 5GHz for Interface 2 posted successfully")
        bss2 += 1
    else:
        print("Failed to post mock Bss 5GHz for Interface 2")
        bss2_fail += 1
        print(response.text)    
    
    mockup_bss_3 = {
        "bss_id": f'Bss{ap_id}_2_3',
        "ssid_name": f'{ssid_name}_6GHz',
        "passphrase": passphrase,
        "security_mode": security_mode,
        "status": fake.random_element(elements=('active', 'inactive')),
        "num_clients": fake.random_int(min=0, max=100),
        "tx_bytes": fake.random_number(digits=8),
        "rx_bytes": fake.random_number(digits=8),
        "tx_errors": fake.random_int(min=0, max=10),
        "rx_errors": fake.random_int(min=0, max=5),
        "interface_id": interface_id
    }
    response = requests.post(bss_url, json=mockup_bss_3)
    if response.status_code == 201:
        print("Mock Bss 6GHz for Interface 2 posted successfully")
        bss3 += 1
    else:
        print("Failed to post mock Bss 6GHz for Interface 2")
        bss3_fail += 1
        print(response.text)
  
print(f'"Eth1": {eth1}')
print(f'"Eth1_fail": {eth1_fail}')
print(f'"Eth2": {eth2}')
print(f'"Eth2_fail": {eth2_fail}')

print(f'"Wl1": {wl1}')
print(f'"Wl1_fail": {wl1_fail}')
print(f'"Wl2": {wl2}')
print(f'"Wl2_fail": {wl2_fail}')

print(f'"Usb1": {usb1}')
print(f'"Usb1_fail: {usb1_fail}')

print(f'"Bss1": {bss1}')
print(f'"Bss1_fail: {bss1_fail}')
print(f'"Bss2": {bss2}')
print(f'"Bss2_fail: {bss2_fail}')
print(f'"Bss3": {bss3}')
print(f'"Bss3_fail: {bss3_fail}')