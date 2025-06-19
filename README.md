# Community Swiper

This repository contains a basic skeleton for a Telegram WebApp bot that allows members of a closed community to swipe profiles and see matches. The project uses **FastAPI** for the backend and **PostgreSQL** for persistence.

## Components

- **Backend** (`app/`): FastAPI application with endpoints for authentication, swiping and listing matches.
- **Telegram Bot** (`bot/`): minimal bot that opens the WebApp inside Telegram.
- **WebApp** (`webapp/`): HTML/JavaScript interface for performing swipe actions.

## Quick start

1. Install dependencies (preferably inside a virtual environment):

```bash
pip install -r requirements.txt
```

2. Set the `DATABASE_URL` environment variable pointing to your PostgreSQL instance, e.g.:

```bash
export DATABASE_URL=postgresql://user:password@localhost/swiper
```

3. Run the backend:

```bash
uvicorn app.main:app --reload
```

4. Launch the bot:

```bash
python bot/bot.py
```

5. Open the WebApp link provided by the bot and start swiping.

This is only a starting point and does not implement the full business logic yet. Contributions are welcome.
