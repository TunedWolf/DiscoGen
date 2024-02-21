import requests
import random
import string

WEBHOOK_URL = "Your webhook here"

def generate_random_string(length=18):

    return ''.join(random.choices(string.ascii_uppercase + string.ascii_lowercase + string.digits, k=length))

def send_request(code):
    url = f"https://discordapp.com/api/v9/entitlements/gift-codes/{code}?with_application=falsewith_subscription_plan=true"
    response = requests.get(url)
    if response.status_code == 200:
        send_to_discord(code)

def send_to_discord(code):
    """Send the code through Discord webhook."""
    payload = {"content": f"Found one! {code}"}
    response = requests.post(WEBHOOK_URL, json=payload)
    print(response.status_code)

while 1:
    if __name__ == "__main__": 
        random_code = generate_random_string()
        send_request(random_code)
