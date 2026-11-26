# Discord Bot

A Python-based Discord bot with web scraping and content summarization capabilities. The bot can collect information from web sources, summarize content, and deliver results directly through Discord.

## Features

- **Discord Integration** – Interact with the bot through Discord commands.
- **Web Scraping** – Extract information from web pages.
- **Content Summarization** – Generate concise summaries of scraped content.
- **Command Handling** – Process custom commands and user messages.

## Tech Stack

- Python
- discord.py
- BeautifulSoup
- Requests
- Python-dotenv

## Project Structure

```text
discord_bot_code/
│
├── bot.py
├── main.py
├── scraper.py
├── summarizer.py
├── .gitignore
├── .env.example
└── README.md
```

## Installation

1. Clone the repository:

```bash
git clone YOUR_REPOSITORY_URL
cd discord_bot_code
```

2. Create a virtual environment:

```bash
python -m venv .venv
```

3. Activate the virtual environment:

**Windows:**
```powershell
.venv\Scripts\Activate.ps1
```

4. Install dependencies:

```bash
pip install -r requirements.txt
```

5. Create a `.env` file in the project root:

```env
DISCORD_TOKEN=your_discord_bot_token
```

6. Run the bot:

```bash
python main.py
```

## Configuration

Before running the bot, make sure to:

- Create a Discord application in the [Discord Developer Portal](https://discord.com/developers/applications).
- Enable the required Gateway Intents, including Message Content Intent.
- Add your bot token to the `.env` file.

## Security

Never share your Discord bot token or commit your `.env` file to GitHub.

## License

This project is available for educational and personal use.
