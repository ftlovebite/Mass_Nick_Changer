# Light Renamer Bot

A lightweight Discord bot written in Python that bulk renames server members by adding a custom tag before their username.

Example:

Before:
```
Light
John
Emily
```

After:
```
FK | Light
FK | John
FK | Emily
```

---

## Features

- Bulk rename all members with one command
- Custom tag entered when the bot starts
- Skips bots automatically
- Skips the server owner
- Respects Discord role hierarchy
- Built with Python using discord.py
- Easy to run locally

---

## Requirements

- Python 3.10 or newer
- discord.py

Install the required package:

```bash
pip install -U discord.py
```

---

## Setup

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/FK-Renamer-Bot.git
```

### 2. Open the project folder

```bash
cd FK-Renamer-Bot
```

### 3. Run the bot

```bash
python bot.py
```

---

## Startup

When the bot starts it will ask for:

```
Enter your Discord Bot Token:
```

Paste your bot token.

Then:

```
Enter the tag (Example: FK):
```

Enter any tag you want.

Example:

```
FK
```

The bot will then use:

```
FK | Username
```

---

## Commands

### Rename every member

```
!renameall
```

Example result:

```
Light
```

becomes

```
FK | Light
```

---

## Required Permissions

The bot needs:

- Manage Nicknames
- Read Messages
- Send Messages

The bot's role must be above the members it should rename.

---

## Required Intents

Enable these in the Discord Developer Portal:

- Server Members Intent
- Message Content Intent

---

## Limitations

The bot cannot rename:

- The server owner
- Members with roles higher than or equal to the bot's role
- Members whose nicknames Discord does not allow the bot to edit

---

## Built With

- Python
- discord.py

---

## License

All Rights Reserved.

Copyright © 2026 Light.

This project may not be copied, modified, redistributed, or used without explicit permission from the copyright holder.
