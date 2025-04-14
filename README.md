# 📜 Hadith Verification Telegram Bot

A simple yet powerful Telegram bot for verifying Hadiths using their numbers — designed to provide authentic references quickly and effortlessly.

---

## ✨ Features

- 🔍 **Hadith Lookup** — Send a Hadith number, get its text and reference.
- 📚 **Authentic Sources** — Uses trusted Hadith collection source sunnah.com.
- 🤖 **Minimal Setup** — Just update your API key and you're good to go.

---

## 🚀 Getting Started

### Prerequisites

- Python 3.6+
- A Telegram bot token from [BotFather](https://t.me/BotFather).

---

### Installation

1. **Clone this repository**

   ```bash
   git clone https://github.com/abdulmuizz0903/Hadith-Verification-TG-Bot.git
   cd Hadith-Verification-TG-Bot
   ```

2. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

3. **Configure your API Key**

   Open `hadith_bot.py` and replace:

   ```python
   API_KEY = "YOUR_TELEGRAM_BOT_API_KEY"
   ```

   with your actual bot token.

4. **Run the bot**

   ```bash
   python hadith_bot.py
   ```

---

## 💡 Usage

- Open Telegram and start a conversation with your bot.
- Send a Hadith number (example: `Sahih Bukhari 1234`).
- The bot will reply with the corresponding Hadith text and reference.

---

## 🗂️ Project Structure

```
├── hadith_bot.py         # Main bot script
├── HadithScraper/        # Separate folder for the people who just want to access the Hadith Scraper.
├── requirements.txt      # Dependency list
└── README.md             # Project info
```

---

## 🤝 Contributing

Pull requests are welcome! Fork the repository, make your changes, and submit a PR.

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).

---

## 📬 Contact

Have questions or feedback?  
Open an issue here: [GitHub Issues](https://github.com/abdulmuizz0903/Hadith-Verification-TG-Bot/issues)

