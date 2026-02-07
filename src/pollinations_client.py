import urllib.parse
import requests
import random
import time
from datetime import datetime


from .config import POLLINATIONS_API_KEY, AI_MODEL


def generate_text(prompt: str) -> str:
    """Generate text using paid Pollinations.ai API."""
    seed = random.randint(1000, 999999)
    date_str = datetime.now().strftime("%Y-%m-%d")
    
    # Enhance prompt with context
    enhanced_prompt = f"{prompt}\n\nIMPORTANT: Make this unique and different. Today's date: {date_str}. Seed: {seed}"
    
    url = "https://gen.pollinations.ai/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {POLLINATIONS_API_KEY}",
        "Content-Type": "application/json"
    }
    payload = {
        "model": AI_MODEL,
        "messages": [
            {"role": "system", "content": "You are a helpful assistant that generates engaging content for a Telegram channel."},
            {"role": "user", "content": enhanced_prompt}
        ],
        "seed": seed
    }
    
    try:
        resp = requests.post(url, headers=headers, json=payload, timeout=60)
        if resp.status_code == 200:
            data = resp.json()
            return data['choices'][0]['message']['content'].strip()
        else:
            print(f"Error from Pollinations: {resp.status_code} - {resp.text}")
    except Exception as e:
        print(f"Exception during text generation: {e}")
        
    return "AI generation failed. Please try again."


def image_url(prompt: str) -> str:
    """Return an image URL from Pollinations with paid access via API key query param."""
    seed = random.randint(1000, 999999)
    encoded = urllib.parse.quote(prompt)
    # Using 'key' query param so Telegram servers can fetch the image without needing headers
    return f"https://gen.pollinations.ai/image/{encoded}?model=flux&seed={seed}&width=1024&height=1024&nologo=true&key={POLLINATIONS_API_KEY}"
