from dotenv import load_dotenv
import requests as r
import os

load_dotenv()

token = os.getenv("ACCESS_TOKEN")
url = os.getenv("URL")

header = {
    "Authorization": f"Bearer {token}",
    "Content-Type": "application/json",
}

response = r.get(f"{url}", headers=header)

print(response.json())