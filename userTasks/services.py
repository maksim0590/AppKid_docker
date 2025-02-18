import requests
import datetime

def sendMessage(message):
    TOKEN = "7650515955:AAE1_0NakMldovp-8hlXyOKpwaOo_UY0w_Q"
    chat_id = "731199141"
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={chat_id}&text={message}"
    requests.get(url)  # Эта строка отсылает сообщение

