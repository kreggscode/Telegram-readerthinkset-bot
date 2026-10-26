import json
import requests
from .config import BOT_TOKEN, CHAT_ID
from .formatter import markdown_to_telegram_html, plain_text_fallback_formatter, safe_truncate_html

BASE_URL = f"https://api.telegram.org/bot{BOT_TOKEN}"


def add_social_footer(text: str) -> str:
    """Add sleek social media footer with emojis and hyperlinked channels."""
    if "Connect with kreggscode" in text or "Connect with @kreggscode" in text:
        return text

    footer = """

━━━━━━━━━━━━━━━━━━━━
🚀 **Connect with @kreggscode:**

💬 [Telegram Community](https://t.me/kreggscode) • 📷 [Instagram](https://instagram.com/kreggscode)
✖️ [X / Twitter](https://x.com/kreggscode) • ▶️ [YouTube](https://youtube.com/@kreggscode)
📘 [Facebook](https://www.facebook.com/share/1b95f6Sn3c/) • 🎮 [Play Store Apps](https://play.google.com/store/apps/dev?id=4822923174061161987)
⭐ [GitHub Repositories](https://github.com/kreggscode)
━━━━━━━━━━━━━━━━━━━━"""
    return text.rstrip() + footer


def send_text(text: str, add_footer: bool = True, parse_mode: str = "HTML"):
    """Send text with robust Telegram HTML formatting."""
    if add_footer:
        text = add_social_footer(text)

    if parse_mode == "HTML":
        payload_text = markdown_to_telegram_html(text)
        payload_text = safe_truncate_html(payload_text, max_chars=4000)
    else:
        payload_text = text

    url = f"{BASE_URL}/sendMessage"
    payload = {
        "chat_id": CHAT_ID,
        "text": payload_text,
        "parse_mode": parse_mode,
        "disable_web_page_preview": True
    }
    try:
        resp = requests.post(url, json=payload, timeout=30)
        if resp.status_code != 200:
            print(f"Telegram Error ({resp.status_code}): {resp.text[:200]}")
            if resp.status_code == 400:
                plain_text = plain_text_fallback_formatter(text)
                payload["text"] = plain_text[:3990]
                payload.pop("parse_mode", None)
                resp = requests.post(url, json=payload, timeout=30)
        return resp
    except Exception as e:
        print(f"Telegram Error: {e}")
        return None


def send_photo(image_url: str, caption: str = "", add_footer: bool = True, parse_mode: str = "HTML"):
    if add_footer and caption:
        caption = add_social_footer(caption)

    if parse_mode == "HTML" and caption:
        caption = markdown_to_telegram_html(caption)
        caption = safe_truncate_html(caption, max_chars=1020)

    url = f"{BASE_URL}/sendPhoto"
    payload = {
        "chat_id": CHAT_ID,
        "photo": image_url,
        "caption": caption,
        "parse_mode": parse_mode
    }
    try:
        resp = requests.post(url, json=payload, timeout=30)
        if resp.status_code != 200 and resp.status_code == 400:
            payload["caption"] = plain_text_fallback_formatter(caption)[:1020]
            payload.pop("parse_mode", None)
            resp = requests.post(url, json=payload, timeout=30)
        return resp
    except Exception as e:
        print(f"Photo Error: {e}")
        return None


def send_poll(question: str, options: list[str]):
    safe_q = (question[:295] + "...") if len(question) > 300 else question
    safe_opts = [((o[:95] + "...") if len(o) > 100 else o) for o in options[:10]]
    if len(safe_opts) < 2:
        return None

    url = f"{BASE_URL}/sendPoll"
    payload = {
        "chat_id": CHAT_ID,
        "question": safe_q,
        "options": json.dumps(safe_opts),
        "is_anonymous": True
    }
    try:
        return requests.post(url, json=payload, timeout=30)
    except Exception as e:
        print(f"Poll Error: {e}")
        return None


def send_quiz(question: str, options: list[str], correct_option_id: int, explanation: str = ""):
    safe_q = (question[:295] + "...") if len(question) > 300 else question
    safe_opts = [((o[:95] + "...") if len(o) > 100 else o) for o in options[:10]]
    if len(safe_opts) < 2:
        return None

    safe_correct = max(0, min(correct_option_id, len(safe_opts) - 1))
    safe_expl = ""
    if explanation:
        safe_expl = markdown_to_telegram_html(explanation.strip())
        if len(safe_expl) > 200:
            safe_expl = safe_truncate_html(safe_expl, max_chars=195)

    url = f"{BASE_URL}/sendPoll"
    payload = {
        "chat_id": CHAT_ID,
        "question": safe_q,
        "options": json.dumps(safe_opts),
        "type": "quiz",
        "correct_option_id": safe_correct,
        "explanation": safe_expl,
        "explanation_parse_mode": "HTML",
        "is_anonymous": True
    }
    try:
        resp = requests.post(url, json=payload, timeout=30)
        if resp.status_code != 200 and resp.status_code == 400:
            payload["explanation"] = plain_text_fallback_formatter(explanation)[:195]
            payload.pop("explanation_parse_mode", None)
            resp = requests.post(url, json=payload, timeout=30)
        return resp
    except Exception as e:
        print(f"Quiz Error: {e}")
        return None


def send_thread(messages: list[str]):
    for msg in messages:
        send_text(msg)
