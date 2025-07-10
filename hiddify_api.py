import requests
from config import HIDDIFY_API_URL, HIDDIFY_TOKEN

headers = {
    "Authorization": f"Bearer {HIDDIFY_TOKEN}",
    "Content-Type": "application/json"
}

def create_profile(name, volume, duration):
    data = {
        "name": name,
        "limit": volume,
        "expiry_days": duration,
        "protocol": "vless"
    }
    res = requests.post(f"{HIDDIFY_API_URL}/profiles", headers=headers, json=data)
    return res.json().get("link")
