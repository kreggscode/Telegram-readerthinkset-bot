from . import pollinations_client as ai
from . import telegram_client as tg
from . import scheduler_logic as sched
from .templates import TEXT_TEMPLATES, HASHTAGS
import random

CURRENT_POST_TYPE = None

# Wrap tg.send_text to automatically append hashtags based on CURRENT_POST_TYPE
_original_send_text = tg.send_text
def custom_send_text(text):
    global CURRENT_POST_TYPE
    if CURRENT_POST_TYPE:
        tags = HASHTAGS.get(CURRENT_POST_TYPE, "")
        text = text + tags
    return _original_send_text(text)
tg.send_text = custom_send_text
from datetime import datetime


def post_philosophical_content():
    """
    Posts philosophical content based on the current time.
    Content types: quotes, profiles, thinking, lessons, debates
    """
    global CURRENT_POST_TYPE
    post_type = sched.decide_post_type()
    print(f"📝 Decided post type: {post_type}")
    CURRENT_POST_TYPE = post_type
    
    try:
        # Get the appropriate prompt templates
        if post_type in TEXT_TEMPLATES:
            templates = TEXT_TEMPLATES[post_type]()
            text_prompt = templates["text"]
            img_prompt = templates["image"]
            
            print(f"🤖 Generating {post_type} content...")
            
            # Generate content using AI
            content = ai.generate_text(text_prompt)
            
            # Generate image URL
            img_url = ai.image_url(img_prompt)
            
            print(f"✅ Content and image URL generated!")
            print(f"📤 Sending to Telegram...")
            
            # Send photo first — if it fails, we still send the text content
            try:
                tg.send_photo(img_url, caption=f"🧠 **{post_type.capitalize()} of the Day**")
                print(f"✨ Photo sent successfully!")
            except Exception as e:
                print(f"⚠️ Photo failed to send, but continuing with text: {e}")
            
            # Always send the text content regardless of photo success
            tg.send_text(content)
            
            print(f"✨ Post sent successfully!")
            
        else:
            error_msg = f"⚠️ Unknown post type: {post_type}"
            print(error_msg)
            tg.send_text(error_msg)
            
    except Exception as e:
        error_msg = f"❌ Error posting {post_type} content: {str(e)}"
        print(error_msg)
        # Send error notification
        tg.send_text(f"⚠️ Bot Error: Failed to post {post_type} content. Please check logs.")
        raise


def main():
    """Main entry point for the bot."""
    print("=" * 60)
    print("🧠 PHILOSOPHY BOT - Starting")
    print(f"⏰ Current UTC time: {datetime.utcnow()}")
    print("=" * 60)
    
    post_philosophical_content()
    
    print("=" * 60)
    print("✅ Philosophy Bot execution completed")
    print("=" * 60)


if __name__ == "__main__":
    main()
