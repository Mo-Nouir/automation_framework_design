import requests
from utils.config import BASE_URL, AUTH_TOKEN

def post_transfer(payload):
    headers = {
        "Authorization": f"Bearer {AUTH_TOKEN}",
        "Content-Type": "application/json"
    }

    response = requests.post(
        f"{BASE_URL}/api/v1/transfers",
        json=payload,
        headers=headers
    )

    return response