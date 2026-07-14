<img width="1011" height="272" alt="image" src="https://github.com/user-attachments/assets/28a09e31-567b-4a05-945e-dd1ae37bb317" />
As You Can See it communcaition
# Discord AI Bot

A Discord chatbot built with Python that uses the Google Gemini API to generate AI responses. The bot listens for mentions in a Discord server and replies with natural language responses.

## Features

- Responds when mentioned in a Discord server
- Generates AI responses using the Gemini API
- Built using Python and discord.py
- Simple and easy to customize
- Designed to be extended with additional features

## Technologies

- Python
- discord.py
- Google Gemini API
- python-dotenv

## Project Structure

```
Discord-Voice-bot/
│── bot.py
│── requirements.txt
│── README.md
│── images/
```

## Installation

Clone the repository:

```bash
git clone https://github.com/HackerBoyHub/Discord-Voice-bot.git
```

Move into the project directory:

```bash
cd Discord-Voice-bot
```

Install the required packages:

```bash
pip install -r requirements.txt
```

Create a `.env` file and add your credentials:

```text
DISCORD_TOKEN=YOUR_DISCORD_TOKEN
GEMINI_API_KEY=YOUR_GEMINI_API_KEY
```

Run the bot:

```bash
python bot.py
```

## Usage

Start the bot and invite it to your Discord server.

Mention the bot in any text channel:

```
@BotName Hello
```

The bot will reply with an AI-generated response.

## Screenshots

Add screenshots inside the `images` folder.

Example:

```markdown
![Discord Chat](images/chat.png)
```

## Future Improvements

- Voice channel support
- Speech-to-text
- Text-to-speech
- Conversation history
- Slash commands
- PDF question answering
- Web search integration

## License

This project is available under the MIT License.
