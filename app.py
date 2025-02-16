from flask import Flask, request
import requests
import os

app = Flask(__name__)

# Get the Telegram bot token from environment variables
TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
TELEGRAM_API_URL = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}"

@app.route('/webhook', methods=['POST'])
def webhook():
    # Parse incoming message from Telegram
    update = request.get_json()
    chat_id = update['message']['chat']['id']
    text = update['message']['text']

    # Simple echo response
    response_text = f"You said: {text}"
    send_message(chat_id, response_text)

    return '', 200

def send_message(chat_id, text):
    # Send a message back to the user
    url = f"{TELEGRAM_API_URL}/sendMessage"
    payload = {
        "chat_id": chat_id,
        "text": text
    }
    requests.post(url, json=payload)

if __name__ == '__main__':
    app.run(debug=True)