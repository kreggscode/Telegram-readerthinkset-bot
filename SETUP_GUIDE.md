# 🧠 Philosophy Bot - Complete Setup Guide

This guide will walk you through setting up the Telegram Philosophy Bot from scratch.

## 📋 Prerequisites

- Python 3.8 or higher
- A Telegram account
- A GitHub account (for automation)
- Basic command line knowledge

## Part 1: Telegram Setup

### Step 1: Create Your Bot

1. Open Telegram and search for **@BotFather**
2. Send `/newbot` command
3. Follow the prompts:
   - Choose a name (e.g., "Philosophy Wisdom")
   - Choose a username (e.g., "PhilosophyThinkBot")
4. Save the **bot token** you receive (looks like `1234567890:ABCdefGHIjklMNOpqrsTUVwxyz`)

### Step 2: Create Your Channel

1. Create a new Telegram channel (can be public or private)
2. Name it something like "Philosophy & Wisdom" or "Daily Philosophy"
3. Add your bot as an administrator:
   - Go to channel info → Administrators → Add Administrator
   - Search for your bot username
   - Give it "Post Messages" permission

### Step 3: Get Your Channel ID

**Method 1: Using the API**

1. Post any message in your channel
2. Open this URL in your browser (replace `YOUR_BOT_TOKEN`):
   ```
   https://api.telegram.org/botYOUR_BOT_TOKEN/getUpdates
   ```
3. Look for `"chat":{"id":-1001234567890}` in the JSON response
4. The number (including the minus sign) is your `CHAT_ID`

**Method 2: Using @userinfobot**

1. Forward any message from your channel to **@userinfobot**
2. It will reply with the channel ID

**Important**: Channel IDs are negative numbers (e.g., `-1001234567890`)

## Part 2: Local Setup & Testing

### Step 1: Clone the Repository

```bash
git clone https://github.com/kreggscode/Telegram-readerthinkset-bot.git
cd Telegram-readerthinkset-bot
```

### Step 2: Set Up Environment Variables

1. Copy the example file:
   ```bash
   cp .env.example .env
   ```

2. Edit `.env` with your credentials:
   ```
   BOT_TOKEN=1234567890:ABCdefGHIjklMNOpqrsTUVwxyz
   CHAT_ID=-1001234567890
   TIMEZONE_OFFSET_HOURS=5.5
   ```

   **Timezone Examples**:
   - IST (India): `5.5`
   - EST (US East): `-5`
   - PST (US West): `-8`
   - GMT (UK): `0`
   - JST (Japan): `9`

### Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

This installs:
- `requests` - For API calls
- `python-dotenv` - For environment variables

### Step 4: Test the Bot

```bash
python -m src.main
```

You should see:
```
🧠 PHILOSOPHY BOT - Starting
⏰ Current UTC time: 2025-12-07 08:32:01
📝 Decided post type: quote
🤖 Generating quote content...
✅ Content generated successfully!
📤 Sending to Telegram...
✨ Post sent successfully!
```

Check your Telegram channel - you should see a philosophical post! 🎉

## Part 3: GitHub Actions Automation

### Step 1: Create GitHub Repository

1. Go to [GitHub](https://github.com)
2. Create a new repository (can be public or private)
3. Name it `Telegram-readerthinkset-bot` or similar

### Step 2: Push Your Code

```bash
git init
git add .
git commit -m "Initial commit: Philosophy Bot"
git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPO.git
git branch -M main
git push -u origin main
```

**IMPORTANT**: Make sure `.env` is in `.gitignore` (it already is). Never commit your `.env` file!

### Step 3: Add GitHub Secrets

1. Go to your repository on GitHub
2. Click **Settings** → **Secrets and variables** → **Actions**
3. Click **New repository secret**
4. Add three secrets:

   - **Secret 1**:
     - Name: `BOT_TOKEN`
     - Value: Your bot token (e.g., `1234567890:ABCdefGHI...`)

   - **Secret 2**:
     - Name: `CHAT_ID`
     - Value: Your channel ID (e.g., `-1001234567890`)

   - **Secret 3**:
     - Name: `TIMEZONE_OFFSET_HOURS`
     - Value: Your timezone offset (e.g., `5.5`)

### Step 4: Verify Workflow File

The workflow file at `.github/workflows/auto-post.yml` should already exist with this schedule:

- 7:00 AM - Philosophical Quote
- 11:00 AM - Philosopher Profile
- 2:00 PM - Philosophical Thinking
- 6:00 PM - Philosophical Lesson
- 9:00 PM - Philosophical Debate

### Step 5: Enable GitHub Actions

1. Go to the **Actions** tab in your repository
2. If prompted, click "I understand my workflows, go ahead and enable them"
3. You should see "Philosophy Bot Auto-Poster" workflow

### Step 6: Test Manual Run

1. Go to **Actions** tab
2. Click "Philosophy Bot Auto-Poster" on the left
3. Click "Run workflow" dropdown on the right
4. Click the green "Run workflow" button
5. Wait 15-30 seconds and refresh
6. Check your Telegram channel for a new post!

### Step 7: Monitor Automated Posts

- GitHub Actions will now run automatically 5 times per day
- To check logs:
  1. Go to **Actions** tab
  2. Click on any workflow run
  3. Click "post-philosophy" job
  4. Expand steps to see detailed logs

## Part 4: Dashboard (Optional)

The dashboard allows you to manually trigger posts outside the schedule.

### Step 1: Navigate to Dashboard

```bash
cd dashboard
```

### Step 2: Install Dashboard Dependencies

```bash
pip install -r requirements.txt
```

### Step 3: Run Dashboard

```bash
python app.py
```

### Step 4: Access Dashboard

Open your browser to: http://127.0.0.1:5000

You can now manually trigger:
- Philosophical quotes
- Philosopher profiles
- Philosophical thinking posts
- Philosophical lessons
- Philosophical debates

## 🔧 Customization Guide

### Change Posting Times

Edit `.github/workflows/auto-post.yml`:

```yaml
schedule:
  # Format: 'minute hour * * *'
  # Example: '0 12 * * *' = 12:00 PM UTC daily
  - cron: '30 1 * * *'   # 7:00 AM IST
  - cron: '30 5 * * *'   # 11:00 AM IST
  # Add or modify times as needed
```

**Cron Time Calculator**: https://crontab.guru/

### Add More Philosophers

Edit `src/templates.py` and add to the `PHILOSOPHERS` list:

```python
PHILOSOPHERS = [
    # Add your philosophers here
    "Your Philosopher Name",
    "Another Philosopher",
    # ... existing ones
]
```

### Customize Content Templates

Edit the prompt functions in `src/templates.py`:
- `get_philosophical_quote_prompt()` - Modify quote format
- `get_philosopher_profile_prompt()` - Change profile structure
- etc.

### Adjust Timezone

Update the `TIMEZONE_OFFSET_HOURS` secret in GitHub:
1. Settings → Secrets and variables → Actions
2. Click `TIMEZONE_OFFSET_HOURS`
3. Click "Update secret"
4. Enter new value

## 🐛 Troubleshooting

### Bot doesn't post

**Check 1**: Verify bot is channel admin
- Go to channel → Administrators
- Make sure your bot is listed with "Post Messages" permission

**Check 2**: Verify CHAT_ID is correct
- Run: `https://api.telegram.org/botYOUR_TOKEN/getUpdates`
- Confirm the ID matches (including minus sign for channels)

**Check 3**: Check GitHub Actions logs
- Actions tab → click workflow run → view logs
- Look for error messages

### Posts are at wrong times

**Issue**: Timezone offset is incorrect

**Fix**: 
1. Calculate correct offset from UTC
2. Update `TIMEZONE_OFFSET_HOURS` secret in GitHub
3. Update `.env` file for local testing

### "API rate limit" errors

**Issue**: Posting too frequently

**Fix**: 
- Pollinations.ai has rate limits
- Ensure schedule doesn't post more than once per hour
- Add delays in code if needed

### Content is repetitive

**Issue**: Seed randomization not working

**Fix**:
- Check that `datetime` is working correctly
- Verify timezone settings
- Each hour should produce different content

## 📊 Monitoring Your Bot

### GitHub Actions Dashboard

- Go to **Actions** tab
- Green checkmark ✅ = successful post
- Red X ❌ = failed post (click to see why)

### Telegram Channel

- Monitor engagement (views, shares)
- Read comments/reactions
- Adjust content based on audience feedback

### Usage Limits

**GitHub Actions**:
- Free tier: 2,000 minutes/month
- This bot uses ~5 minutes/day = 150 minutes/month
- Well within free limits! ✅

**Pollinations.ai**:
- Free API with fair use limits
- Our posting frequency (5x/day) is well within limits

## 🚀 Next Steps

1. ✅ Test locally
2. ✅ Set up GitHub Actions
3. ✅ Monitor first week of posts
4. ✅ Customize content to your audience
5. ✅ Share your channel!

## 💡 Pro Tips

- **Morning quotes** tend to get the most engagement
- **Evening debates** encourage discussion
- **Vary philosophers** between Western and Eastern traditions
- **Check spelling** of philosopher names before adding
- **Keep .env private** - never commit it!

## 📞 Support

If you encounter issues:
1. Check this guide again carefully
2. Review GitHub Actions logs
3. Test locally first before debugging automation
4. Check Telegram bot permissions

---

**Happy philosophizing! 🧠✨**

*"We are what we repeatedly do. Excellence, then, is not an act, but a habit." - Aristotle*
