from . import pollinations_client as ai
from . import telegram_client as tg
from . import scheduler_logic as sched
from .templates import TEXT_TEMPLATES
import random
from datetime import datetime


def post_philosophical_content():
    """
    Posts philosophical content based on the current time.
    Content types: quotes, profiles, thinking, lessons, debates
    """
    post_type = sched.decide_post_type()
    print(f"📝 Decided post type: {post_type}")
    
    try:
        # Get the appropriate prompt template
        if post_type in TEXT_TEMPLATES:
            prompt_func = TEXT_TEMPLATES[post_type]
            prompt = prompt_func()
            
            print(f"🤖 Generating {post_type} content...")
            print(f"📋 Prompt preview: {prompt[:150]}...")
            
            # Generate content using AI
            content = ai.generate_text(prompt)
            
            print(f"✅ Content generated successfully!")
            print(f"📤 Sending to Telegram...")
            
            # Send to Telegram
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
