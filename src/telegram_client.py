import requests
from .config import BOT_TOKEN, CHAT_ID

BASE_URL = f"https://api.telegram.org/bot{BOT_TOKEN}"


def send_text(text: str):
    """Send a text message to Telegram channel with proper error handling."""
    url = f"{BASE_URL}/sendMessage"
    data = {
        "chat_id": CHAT_ID,
        "text": text,
        "parse_mode": "Markdown"
    }
    
    try:
        resp = requests.post(url, data=data, timeout=30)
        resp_json = resp.json()
        
        # Check if the request was successful
        if not resp_json.get("ok"):
            error_msg = resp_json.get("description", "Unknown error")
            raise RuntimeError(f"Telegram API error: {error_msg}")
        
        print(f"✅ Message sent successfully! Message ID: {resp_json['result']['message_id']}")
        return resp
        
    except requests.exceptions.RequestException as e:
        raise RuntimeError(f"Failed to send message to Telegram: {str(e)}")


def send_photo(image_url: str, caption: str = ""):
    """Send a photo to Telegram channel with proper error handling."""
    url = f"{BASE_URL}/sendPhoto"
    data = {
        "chat_id": CHAT_ID,
        "photo": image_url,
        "caption": caption,
        "parse_mode": "Markdown"
    }
    
    try:
        resp = requests.post(url, data=data, timeout=30)
        resp_json = resp.json()
        
        if not resp_json.get("ok"):
            error_msg = resp_json.get("description", "Unknown error")
            raise RuntimeError(f"Telegram API error: {error_msg}")
        
        print(f"✅ Photo sent successfully!")
        return resp
        
    except requests.exceptions.RequestException as e:
        raise RuntimeError(f"Failed to send photo to Telegram: {str(e)}")


def send_poll(question: str, options: list[str]):
    """Send a poll to Telegram channel with proper error handling."""
    import json
    url = f"{BASE_URL}/sendPoll"
    data = {
        "chat_id": CHAT_ID,
        "question": question,
        "options": json.dumps(options),
        "is_anonymous": False
    }
    
    try:
        resp = requests.post(url, data=data, timeout=30)
        resp_json = resp.json()
        
        if not resp_json.get("ok"):
            error_msg = resp_json.get("description", "Unknown error")
            raise RuntimeError(f"Telegram API error: {error_msg}")
        
        print(f"✅ Poll sent successfully!")
        return resp
        
    except requests.exceptions.RequestException as e:
        raise RuntimeError(f"Failed to send poll to Telegram: {str(e)}")


def send_thread(messages: list[str]):
    """Send multiple messages as a thread."""
    for msg in messages:
        send_text(msg)
