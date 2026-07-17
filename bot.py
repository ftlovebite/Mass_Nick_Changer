import discord
from discord.ext import commands

# ==============================
# USER INPUT
# ==============================

TOKEN = input("Enter your Discord Bot Token: ").strip()

if not TOKEN:
    print("Bot token cannot be empty!")
    exit()

TAG = input("Enter the tag (Example: FK): ").strip()

if not TAG:
    print("Tag cannot be empty!")
    exit()

PREFIX = f"{TAG} | "

# ==============================
# BOT SETUP
# ==============================

intents = discord.Intents.default()
intents.members = True
intents.message_content = True

bot = commands.Bot(
    command_prefix="!",
    intents=intents,
    help_command=None
)

# ==============================
# EVENTS
# ==============================

@bot.event
async def on_ready():
    print("=" * 40)
    print(f"Logged in as {bot.user}")
    print(f"Using Tag: {PREFIX}")
    print("Bot is Online!")
    print("=" * 40)

# ==============================
# HELP
# ==============================

@bot.command()
async def help(ctx):
    embed = discord.Embed(
        title="Nickname Renamer",
        description="Bulk renames every member.",
        color=0x5865F2
    )

    embed.add_field(
        name="Command",
        value="`!renameall`",
        inline=False
    )

    await ctx.send(embed=embed)

# ==============================
# RENAME ALL
# ==============================

@bot.command()
@commands.has_permissions(administrator=True)
async def renameall(ctx):

    await ctx.send(f"Renaming everyone to `{PREFIX}Username`...")

    success = 0
    failed = 0

    me = ctx.guild.me

    for member in ctx.guild.members:

        if member.bot:
            continue

        if member == ctx.guild.owner:
            failed += 1
            continue

        if member.top_role >= me.top_role:
            failed += 1
            continue

        nickname = f"{PREFIX}{member.name}"

        if len(nickname) > 32:
            nickname = nickname[:32]

        try:
            await member.edit(nick=nickname)
            success += 1

        except Exception as e:
            print(f"Failed: {member} -> {e}")
            failed += 1

    embed = discord.Embed(
        title="Rename Finished",
        color=0x57F287
    )

    embed.add_field(name="Renamed", value=success)
    embed.add_field(name="Failed", value=failed)

    await ctx.send(embed=embed)

# ==============================
# ERRORS
# ==============================

@renameall.error
async def rename_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send("Administrator permission required.")
    else:
        await ctx.send(f"Error: {error}")

# ==============================
# START BOT
# ==============================

try:
    bot.run(TOKEN)

except discord.LoginFailure:
    print("Invalid bot token.")

except Exception as e:
    print(e)
