import discord
from google import genai

# Gemini client
client = genai.Client(api_key="Key")

# Discord intents
intents = discord.Intents.default()
intents.message_content = True

bot = discord.Client(intents=intents)


@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")


@bot.event
async def on_message(message):
    if message.author.bot:
        return

    if bot.user in message.mentions:
        prompt = message.content.replace(
            f"<@{bot.user.id}>",
            ""
        ).strip()

        try:
            response = client.models.generate_content(
                model="gemini-3.5-flash",
                contents=prompt
            )

            await message.channel.send(response.text)

        except Exception as e:
            await message.channel.send(f"Error: {e}")

bot.run("Key2")