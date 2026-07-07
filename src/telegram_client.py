import requests
import re
from .config import BOT_TOKEN, CHAT_ID

BASE_URL = f"https://api.telegram.org/bot{BOT_TOKEN}"


def markdown_to_html(text: str) -> str:
    """
    Converts basic Markdown (Bold, Code, Links) to Telegram-flavor HTML.
    This is much more robust than MarkdownV1/V2 for generated content.
    """
    if not text:
        return ""

    # 1. Escape HTML special characters (CRITICAL first step)
    html = text.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')

    # 2. Convert Code blocks (```...```)
    # Use a placeholder system to avoid messing with content inside code blocks
    code_blocks = []
    def save_code(match):
        content = match.group(1).strip()
        code_blocks.append(content)
        return f"___CODEBLOCK_{len(code_blocks)-1}___"
    
    html = re.sub(r'```(?:[\w]*\n)?([\s\S]*?)```', save_code, html)

    # 3. Convert Inline code (`...`)
    html = re.sub(r'`([^`]+)`', r'<code>\1</code>', html)

    # 4. Convert Bold (**...**)
    html = re.sub(r'\*\*(.*?)\*\*', r'<b>\1</b>', html)

    # 5. Convert Links ([text](url))
    html = re.sub(r'\[(.*?)\]\((.*?)\)', r'<a href="\2">\1</a>', html)

    # 6. Restore code blocks with <pre>
    for i, block in enumerate(code_blocks):
        html = html.replace(f"___CODEBLOCK_{i}___", f"<pre>{block}</pre>")

    return html


def send_text(text: str, parse_mode: str = "HTML"):
    """Send text with robust HTML formatting and plain-text fallback."""
    if parse_mode == "HTML":
        text = markdown_to_html(text)
    
    # Safety truncation for Telegram limits
    if len(text) > 4000:
        text = text[:3800] + "\n\n...(truncated)"

    url = f"{BASE_URL}/sendMessage"
    payload = {
        "chat_id": CHAT_ID,
        "text": text,
        "parse_mode": parse_mode
    }

    try:
        resp = requests.post(url, json=payload, timeout=30)
        if resp.status_code != 200:
            print(f"Telegram HTML Failure: {resp.text}")
            # Final fallback: Send as plain text if HTML is somehow broken
            payload.pop("parse_mode", None)
            payload["text"] = text.replace('&lt;', '<').replace('&gt;', '>').replace('&amp;', '&') # Clean for plain text
            resp = requests.post(url, json=payload, timeout=30)
        
        if resp.ok:
            msg_id = resp.json().get("result", {}).get("message_id")
            print(f"✅ Message sent successfully! Message ID: {msg_id}")
        else:
            error_msg = resp.json().get("description", "Unknown error")
            print(f"❌ Telegram API Error (send_text): {error_msg}")
        return resp
    except Exception as e:
        print(f"Telegram Connection Error: {e}")
        return None


def send_photo(image_url: str, caption: str = "", parse_mode: str = "HTML"):
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
        
        # Convert Markdown to HTML if parse_mode is HTML
        if parse_mode == "HTML" and caption:
            caption = markdown_to_html(caption)
            
        if caption and len(caption) > 1000:
            caption = caption[:950] + "..."
            
        data = {
            "chat_id": CHAT_ID,
            "caption": caption,
            "parse_mode": parse_mode
        }
        
        print("📤 Uploading image to Telegram...")
        resp = requests.post(url, data=data, files=files)
        
        if not resp.ok:
            print(f"❌ Telegram API error sending photo (HTML): {resp.text}")
            # Fallback to plain text caption
            data.pop("parse_mode", None)
            # Restore caption symbols for plain text
            if caption:
                data["caption"] = caption.replace('&lt;', '<').replace('&gt;', '>').replace('&amp;', '&')
            resp = requests.post(url, data=data, files=files)
            
        if resp.ok:
            print(f"✨ Photo sent successfully! Message ID: {resp.json().get('result', {}).get('message_id')}")
        else:
            print(f"❌ Telegram API error sending photo (Fallback): {resp.text}")
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

