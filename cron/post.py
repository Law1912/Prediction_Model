import requests
import os
import json
import pandas as pd

# API URL (adjust if hosted on a different domain)
API_URL = "https://coolfi-ai.vercel.app/api/crypto-prediction"

# Fetch token from environment variables
AUTH_TOKEN = os.getenv("AUTH_TOKEN")

if not AUTH_TOKEN:
    print("Error: AUTH_TOKEN is not set in environment variables.")
    exit(1)

# Example prediction data for 4 days
df = pd.read_csv("predicted_returns.csv")

df["Predicted"] = df["Predicted"].astype(float)

# Convert DataFrame into dictionary format
data_dict = df.pivot(index="Date", columns="Crypto", values="Predicted").to_dict("list")

print(data_dict)

# Headers for authentication
headers = {
    "Authorization": f"Bearer {AUTH_TOKEN}",
    "Content-Type": "application/json"
}

# Send request
response = requests.post(API_URL, headers=headers, data=json.dumps(data_dict))

# Print response
print(response.status_code, response.json())
