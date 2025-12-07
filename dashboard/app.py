import os
from flask import Flask, render_template, redirect, url_for, flash
from dotenv import load_dotenv

# Allow dashboard to use same bot config
load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), "..", ".env"), override=False)

import sys
sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from src import telegram_client as tg
from src import pollinations_client as ai
from src.templates import TEXT_TEMPLATES

app = Flask(__name__)
app.secret_key = os.getenv("FLASK_SECRET_KEY", "philosophy-secret-key-2025")


@app.route("/")
def index():
    return render_template("dashboard.html")


@app.route("/send/quote")
def send_quote():
    """Send a philosophical quote with context."""
    try:
        prompt = TEXT_TEMPLATES["quote"]()
        text = ai.generate_text(prompt)
        tg.send_text(text)
        flash("📜 Philosophical quote sent successfully!", "success")
    except Exception as e:
        flash(f"❌ Error sending quote: {str(e)}", "error")
    return redirect(url_for("index"))


@app.route("/send/profile")
def send_profile():
    """Send a philosopher profile."""
    try:
        prompt = TEXT_TEMPLATES["profile"]()
        text = ai.generate_text(prompt)
        tg.send_text(text)
        flash("👤 Philosopher profile sent successfully!", "success")
    except Exception as e:
        flash(f"❌ Error sending profile: {str(e)}", "error")
    return redirect(url_for("index"))


@app.route("/send/thinking")
def send_thinking():
    """Send philosophical school of thought explanation."""
    try:
        prompt = TEXT_TEMPLATES["thinking"]()
        text = ai.generate_text(prompt)
        tg.send_text(text)
        flash("🧠 Philosophical thinking post sent successfully!", "success")
    except Exception as e:
        flash(f"❌ Error sending thinking post: {str(e)}", "error")
    return redirect(url_for("index"))


@app.route("/send/lesson")
def send_lesson():
    """Send practical philosophical lesson."""
    try:
        prompt = TEXT_TEMPLATES["lesson"]()
        text = ai.generate_text(prompt)
        tg.send_text(text)
        flash("🌟 Philosophical lesson sent successfully!", "success")
    except Exception as e:
        flash(f"❌ Error sending lesson: {str(e)}", "error")
    return redirect(url_for("index"))


@app.route("/send/debate")
def send_debate():
    """Send philosophical debate/perspectives post."""
    try:
        prompt = TEXT_TEMPLATES["debate"]()
        text = ai.generate_text(prompt)
        tg.send_text(text)
        flash("⚖️ Philosophical debate sent successfully!", "success")
    except Exception as e:
        flash(f"❌ Error sending debate: {str(e)}", "error")
    return redirect(url_for("index"))


@app.route("/test")
def test_connection():
    """Test Telegram connection."""
    try:
        tg.send_text("🧠 Philosophy Bot Dashboard - Test message sent successfully!")
        flash("✅ Test message sent! Check your Telegram channel.", "success")
    except Exception as e:
        flash(f"❌ Connection failed: {str(e)}", "error")
    return redirect(url_for("index"))


if __name__ == "__main__":
    print("=" * 60)
    print("🧠 Philosophy Bot Dashboard Starting...")
    print("📊 Open http://127.0.0.1:5000 in your browser")
    print("=" * 60)
    app.run(debug=True)
