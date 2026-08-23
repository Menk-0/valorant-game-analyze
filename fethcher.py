import requests
import json
from config import NAME, TAG, REGION,URL


from dotenv import load_dotenv
load_dotenv()

import os
key=os.getenv("apikey")

wallet={"Authorization":key}

response=requests.get(URL,headers=wallet)

if response.status_code == 200:
    match_data = response.json()
    with open('my_matches.json', 'w') as file:
        json.dump(match_data, file, indent=4)
    print("\nExtraction is comeplete")
else:
    print(f"Failed to connect, Error code: {response.status_code}")