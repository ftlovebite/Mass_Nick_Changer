import os
import discord
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("TOKEN")
PREFIX = os.getenv("PREFIX", "FK | ")

intents = discord.Intents.default()
intents.members = True
intents.guilds = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")

@bot.command()
@commands.has_permissions(administrator=True)
async def renameall(ctx):
    await ctx.send("Starting nickname update...")

    success = 0
    failed = 0

    for member in ctx.guild.members:
        if member.bot:
            continue

        try:
            if member.top_role >= ctx.guild.me.top_role:
                failed += 1
                continue

            base_name = member.nick if member.nick else member.name
            new_name = f"{PREFIX}{base_name}"

            if len(new_name) > 32:
                new_name = new_name[:32]

            await member.edit(nick=new_name)
            success += 1

        except Exception:
            failed += 1

    await ctx.send(
        f"Done!\n"
        f"✅ Renamed: {success}\n"
        f"❌ Failed: {failed}"
    )

bot.run(TOKEN)
