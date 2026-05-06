import requests
import time

BOT_TOKEN = "8648283171:AAHvCySURDBAZlcyozjsuJWhV8KS9"

CHAT_ID = "6026637986"

def send_message(message):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    
    data = {
        "chat_id": CHAT_ID,
        "text": message
    }

    requests.post(url, data=data)

while True:
    signal = "🔥 NIFTY SIGNAL: BUY\nPrice: 24050\nConfidence: 85%"
    
    send_message(signal)

    print("Signal Sent!")

    time.sleep(300)
