import requests
from .config import BOT_TOKEN, CHAT_ID

BASE_URL = f"https://api.telegram.org/bot{BOT_TOKEN}"


def send_text(text: str):
    url = f"{BASE_URL}/sendMessage"
    data = {
        "chat_id": CHAT_ID,
        "text": text,
        "parse_mode": "Markdown"
    }
    resp = requests.post(url, data=data)
    if resp.ok:
        msg_id = resp.json().get("result", {}).get("message_id")
        print(f"✅ Message sent successfully! Message ID: {msg_id}")
    else:
        error_msg = resp.json().get("description", "Unknown error")
        print(f"❌ Telegram API Error (send_text): {error_msg}")
    return resp


def send_photo(image_url: str, caption: str = ""):
    """
    Downloads the image from image_url and uploads it to Telegram.
    This is much more reliable than sending the URL to Telegram.
    Returns response on success, None on failure (does NOT crash).
    """
    try:
        # 1. Download the image first
        print(f"📥 Downloading image from AI: {image_url[:50]}...")
        img_resp = requests.get(image_url, timeout=60)
        img_resp.raise_for_status()
        
        # 2. Upload to Telegram
        url = f"{BASE_URL}/sendPhoto"
        files = {
            "photo": ("image.jpg", img_resp.content, "image/jpeg")
        }
        data = {
            "chat_id": CHAT_ID,
            "caption": caption,
            "parse_mode": "Markdown"
        }
        
        print("📤 Uploading image to Telegram...")
        resp = requests.post(url, data=data, files=files)
        
        if not resp.ok:
            error_data = resp.json()
            error_msg = error_data.get("description", "Unknown error")
            print(f"❌ Telegram API error sending photo: {error_msg}")
            return None
            
        print(f"✨ Photo sent successfully! Message ID: {resp.json().get('result', {}).get('message_id')}")
        return resp
        
    except Exception as e:
        print(f"❌ Failed to send photo (non-fatal): {e}")
        return None


def send_poll(question: str, options: list[str]):
    import json
    url = f"{BASE_URL}/sendPoll"
    data = {
        "chat_id": CHAT_ID,
        "question": question,
        "options": json.dumps(options),
        "is_anonymous": False
    }
    resp = requests.post(url, data=data)
    return resp


def send_thread(messages: list[str]):
    for msg in messages:
        send_text(msg)
