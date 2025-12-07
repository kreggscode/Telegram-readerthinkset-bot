# 🧠 Telegram Philosophy Bot

An automated Telegram bot that posts **philosophical quotes, thinking, and wisdom** from great philosophers around the world. Posts 5 times daily with diverse, educational content powered by AI.

## ✨ Features

- 🎓 **5 Content Types**:
  - Philosophical quotes with deep context
  - Philosopher profiles and biographies  
  - Explanations of philosophical schools of thought
  - Practical philosophical lessons for modern life
  - Philosophical debates exploring different perspectives

- 🌍 **60+ Philosophers** from diverse traditions:
  - Ancient Western (Socrates, Plato, Aristotle, Marcus Aurelius...)
  - Eastern Philosophy (Confucius, Buddha, Laozi, Rumi...)
  - Medieval & Renaissance thinkers
  - Modern & Contemporary philosophers

- 🎲 **Variety System**: Time-seeded randomization prevents repetition
- 🤖 **AI-Powered**: Uses Pollinations.ai (no API key needed)
- ⏰ **Auto-Scheduling**: GitHub Actions posts 5x daily
- 📊 **Dashboard**: Flask web UI for manual posting

## 📅 Posting Schedule (IST)

- **7:00 AM** 🌅 - Philosophical Quote (wisdom to start the day)
- **11:00 AM** 📚 - Philosopher Profile (learn about great thinkers)
- **2:00 PM** 🧠 - Philosophical Thinking (explore schools of thought)
- **6:00 PM** 🌆 - Philosophical Lesson (practical wisdom)
- **9:00 PM** 🌙 - Philosophical Debate (different perspectives)

## 🚀 Setup

### 1. Create Telegram Bot & Channel

1. Talk to **@BotFather** on Telegram:
   - Send `/newbot` → get your `BOT_TOKEN`
2. Create a public or private Telegram channel
3. Add the bot as **Admin** to your channel (with "Post Messages" permission)
4. Get your `CHAT_ID`:
   ```
   https://api.telegram.org/bot<YOUR_BOT_TOKEN>/getUpdates
   ```
   Post a message in your channel, then look for `"chat":{"id": ... }` in the response

### 2. Local Testing

```bash
# Clone this repo
git clone https://github.com/kreggscode/Telegram-readerthinkset-bot.git
cd Telegram-readerthinkset-bot

# Create environment file
cp .env.example .env

# Edit .env with your credentials:
# BOT_TOKEN=your_bot_token_here
# CHAT_ID=your_channel_id_here
# TIMEZONE_OFFSET_HOURS=5.5  # For IST

# Install dependencies
pip install -r requirements.txt

# Test the bot
python -m src.main
```

### 3. Deploy to GitHub Actions

1. Push this repo to GitHub
2. Go to: **Settings → Secrets and variables → Actions**
3. Add these repository secrets:
   - `BOT_TOKEN` - Your bot token from BotFather
   - `CHAT_ID` - Your channel ID
   - `TIMEZONE_OFFSET_HOURS` - Your timezone offset (e.g., `5.5` for IST, `-5` for EST)

The bot will automatically post 5 times daily according to the schedule above! 🎉

### 4. Manual Control (Dashboard)

```bash
cd dashboard
pip install -r requirements.txt
python app.py
```

Open http://127.0.0.1:5000 to manually trigger posts.

## 📁 Project Structure

```
Telegram-readerthinkset-bot/
├── .github/workflows/        # GitHub Actions automation
│   └── auto-post.yml        # 5x daily posting schedule
├── dashboard/                # Flask web UI for manual control
│   ├── app.py
│   ├── templates/
│   └── requirements.txt
├── src/                      # Core bot logic
│   ├── config.py            # Configuration & environment variables
│   ├── telegram_client.py   # Telegram API wrapper
│   ├── pollinations_client.py # AI content generation
│   ├── templates.py         # Philosophical content templates
│   ├── scheduler_logic.py   # Time-based content selection
│   └── main.py              # Main orchestrator
├── index.html               # Optional web mini-app
├── requirements.txt         # Python dependencies
├── .env.example            # Environment variables template
├── README.md               # This file
└── SETUP_GUIDE.md          # Detailed setup instructions
```

## 🎨 Content Examples

**Philosophical Quote** (7 AM):
- Famous quotes with historical context
- Explanation of meaning
- Modern applications

**Philosopher Profile** (11 AM):
- Life and era
- Central ideas
- Famous works
- Lasting impact

**Philosophical Thinking** (2 PM):
- Schools of thought (Stoicism, Existentialism, etc.)
- Core principles
- Key insights

**Philosophical Lesson** (6 PM):
- Real-world challenges
- Philosophical solutions
- Practical applications

**Philosophical Debate** (9 PM):
- Contrasting perspectives
- Different philosophical views
- Critical thinking exercises

## 🔧 Customization

- **Edit content prompts**: Modify `src/templates.py`
- **Change schedule**: Edit `.github/workflows/auto-post.yml` cron times
- **Adjust posting logic**: Modify `src/scheduler_logic.py`
- **Add philosophers**: Update the `PHILOSOPHERS` list in `templates.py`

## 🌟 Why This Bot?

Unlike motivational quote bots, this bot:
- ✅ Provides **deep philosophical education**
- ✅ Explains **historical context** and meaning
- ✅ Covers **diverse philosophical traditions** (Western, Eastern, Ancient, Modern)
- ✅ Makes **philosophy accessible** but not oversimplified
- ✅ Encourages **critical thinking** and reflection
- ✅ Never repeats content (time-seeded randomization)

## 📝 License

MIT License - Feel free to use and modify!

## 🔗 GitHub Repository

https://github.com/kreggscode/Telegram-readerthinkset-bot

---

**Built with 🧠 Powered by Pollinations.ai & Telegram Bot API**

*"The unexamined life is not worth living." - Socrates*
