from datetime import datetime, timedelta
from . import config

def decide_post_type() -> str:
    """
    Decides what type of philosophical content to post based on time of day.
    We post 5 times a day with different content types.
    
    Schedule (IST - adjust based on your timezone):
    - Morning (7 AM): Philosophical Quote - Start the day with wisdom
    - Late Morning (11 AM): Philosopher Profile - Learn about great thinkers
    - Afternoon (2 PM): Philosophical Thinking - Deep dive into concepts
    - Evening (6 PM): Philosophical Lesson - Practical wisdom
    - Night (9 PM): Philosophical Debate - Explore different perspectives
    """
    
    # Get current hour in the configured timezone
    offset_hours = config.TIMEZONE_OFFSET_HOURS
    utc_now = datetime.utcnow()
    local_now = utc_now + timedelta(hours=offset_hours)
    current_hour = local_now.hour
    
    print(f"Current UTC time: {utc_now}")
    print(f"Current local time (offset +{offset_hours}h): {local_now}")
    print(f"Current hour: {current_hour}")
    
    # Determine post type based on hour
    if 6 <= current_hour < 9:
        return "quote"  # 7 AM posting
    elif 10 <= current_hour < 12:
        return "profile"  # 11 AM posting
    elif 13 <= current_hour < 15:
        return "thinking"  # 2 PM posting
    elif 17 <= current_hour < 19:
        return "lesson"  # 6 PM posting
    elif 20 <= current_hour < 22:
        return "debate"  # 9 PM posting
    else:
        # Default fallback - post a quote
        print(f"Outside scheduled hours, defaulting to quote")
        return "quote"


def get_schedule_description() -> str:
    """Returns a human-readable description of the posting schedule."""
    return """
📅 **Posting Schedule (5 times daily):**

🌅 7:00 AM - Philosophical Quote
   Deep wisdom to start your day

📚 11:00 AM - Philosopher Profile  
   Learn about great thinkers

🧠 2:00 PM - Philosophical Thinking
   Explore schools of thought

🌆 6:00 PM - Philosophical Lesson
   Practical wisdom for life

🌙 9:00 PM - Philosophical Debate
   Different perspectives to ponder
"""
