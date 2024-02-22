import requests
import random
import string

WEBHOOK_URL = "Your Webhook Here"
ping = 0
ask = 1
while ask:
    ping = str(input("Do you want to enable @everyone pings? y/n"))
    print(ping)
    if ping == "y":       
      pinger = 1
      ask = 0       
    else:
      pinger = 0
      ask = 0

def generate_random_string(length=18):

    return ''.join(random.choices(string.ascii_uppercase + string.ascii_lowercase + string.digits, k=length))

def send_request(code):
    url = f"https://discordapp.com/api/v9/entitlements/gift-codes/{code}?with_application=falsewith_subscription_plan=true"
    response = requests.get(url)
    if response.status_code == 200:
        send_to_discord(code)

def send_to_discord(code):
    if pinger == 1:
        cont = "@everyone"
    else:
        cont = "."
    codec = code
    code = "https://discord.gift/"+ str(code)
    """Send the code through Discord webhook."""
    payload = {
  "content": cont,
  "embeds": [
    {
      "title": "Found a vaild code!",
      "description": "You're Lucky! this has a 1 in 5 **quintillion** chance of happening!",
      "color": 8279176,
      "footer": {
        "text": "Go buy a lottery ticket you're lucky"
      },
      "image": {
        "url": "https://preview.redd.it/4daujeiyitg51.png?width=3840&format=png&auto=webp&s=0a54edb7f7946660e0120881ea81d8483b2e4e8a"
      },
      "author": {
        "name": "WOAH!!!!"
      },
      "fields": [
        {
          "name": "Heres your code:",
          "value": ""    
        },
        {
          "name": "".join(str(codec)),
          "value":  "".join(str(code))
        }
      ]
    }
  ]
 }
    response = requests.post(WEBHOOK_URL, json=payload)
    print(response.status_code)

data = {
  "content": "Running",
  "embeds": [
    {
      "title": "DiscoGen V0.1",
      "description": "Thanks for using [DiscoGen](https://github.com/TunedWolf/DiscoGen) ",
      "url": "https://github.com/TunedWolf/DiscoGen",
      "color": 16749803,
      "image": {
        "url": "https://i0.wp.com/www.techarp.com/wp-content/uploads/2023/05/Discord-Nitro-free-1-month.jpg?fit=900%2C450&ssl=1"
      },
      "footer": {
        "text": "Made By TunedWolf"
      },
      "fields": [
        {
          "name": "What is DiscoGen?",
          "value": "DiscoGen is a nitro code generator thats running on [Python](https://www.python.org/)"
        },
        {
          "name": "How Does It Work?",
          "value": "DiscoGen generates an 18 character alphanumeric string which it then checks if its valid with discords api if it is then its sent to this channel as a link"
        },
        {
          "name": "Why?",
          "value": "I got bored at 3AM one day and decided i wanted to make this."
        }
      ]
    }
  ]
}
reply = requests.post(WEBHOOK_URL, json=data)
print(reply.status_code)
      
while 1:
    if __name__ == "__main__": 
        random_code = generate_random_string()
        send_request(random_code)
