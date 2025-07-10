import requests
from config import MERCHANT_ID, CALLBACK_URL

def create_payment(amount, description):
    data = {
        "merchant_id": MERCHANT_ID,
        "amount": amount,
        "callback_url": CALLBACK_URL,
        "description": description
    }
    res = requests.post("https://api.zarinpal.com/pg/v4/payment/request.json", json=data)
    return f"https://www.zarinpal.com/pg/StartPay/{res.json()['data']['authority']}"
