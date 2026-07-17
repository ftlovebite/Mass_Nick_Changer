# FK Renamer Bot

A simple Discord bot that adds a prefix to all members' server nicknames.

## Requirements

- Python 3.10+
- A Discord Bot
- Administrator permission
- "Manage Nicknames" permission
- Server Members Intent enabled

## Installation

1. Install Python.
2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Create a `.env` file:

```env
TOKEN=YOUR_BOT_TOKEN
PREFIX=FK |
```

4. Enable **Server Members Intent** in the Discord Developer Portal.

5. Invite the bot with:
- Manage Nicknames
- Read Messages
- Send Messages

6. Start the bot:

```bash
python bot.py
```

## Usage

```
!renameall
```

The bot will rename every member it has permission to manage.

## Notes

- The bot cannot rename the server owner.
- The bot cannot rename members whose highest role is equal to or above the bot's highest role.
- Discord nickname limit is 32 characters.