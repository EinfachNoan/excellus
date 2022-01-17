import discord  # wichtig
import dislash  # wichtig
import schedule  # every day do job
import traceback  # idk was
from discord import Color  # wichtig
from discord.ext import commands, tasks  # wichtig  @tasks.loop()
import datetime  # zeit
import time  # zeit
from discord.utils import get  # get channels user usw
from dislash import *  # import
import asyncio  # sleep
import json  # json
import aiohttp  # session
import random  # zufällig
import youtube_dl  # youtube links zu musik
import os  # file path
from PIL import ImageDraw, ImageFont, Image  # img manipulating
from easy_pil import Canvas, Editor, Font, load_image_async
from io import BytesIO  # img upload
from itertools import cycle  # status = cycle([1, 2, 3])    next(status)   -720 250
from discord import File, Member
import animec
from googletrans import Translator
from discord.ext.commands import has_role
from discord.ext.commands import *
import requests
from pprint import pprint

intents = discord.Intents.all()
intents.members = True

bot = commands.Bot(
    command_prefix="!",
    intents=intents,
    help_command=None
)
inter_client = InteractionClient(bot)
slash = SlashClient(bot)
test_guilds = [881564433439133756]
now = datetime.datetime.now()
get_time = now.strftime("%y-%m-%d %H:%M:%S")


class console_colors:
    HEADER = '\033[95m'
    ok_blue = '\033[94m'
    ok_cyan = '\033[96m'
    ok_green = '\033[92m'
    WARNING = '\033[31;1m'
    FAIL = '\033[91m'
    end_color = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


color_codes = {
    "default": 0,
    "teal": 0x1abc9c,
    "dark_teal": 0x11806a,
    "green": 0x2ecc71,
    "dark_green": 0x1f8b4c,
    "blue": 0x3498db,
    "dark_blue": 0x206694,
    "purple": 0x9b59b6,
    "dark_purple": 0x71368a,
    "magenta": 0xe91e63,
    "dark_magenta": 0xad1457,
    "gold": 0xf1c40f,
    "dark_gold": 0xc27c0e,
    "orange": 0xe67e22,
    "dark_orange": 0xa84300,
    "red": 0xe74c3c,
    "dark_red": 0x992d22,
    "lighter_grey": 0x95a5a6,
    "dark_grey": 0x607d8b,
    "light_grey": 0x979c9f,
    "darker_grey": 0x546e7a,
    "blurple": 0x7289da,
    "greyple": 0x99aab5,
}

page1 = discord.Embed(title="Help-Page 1",
                      description="Navigiere mit den Pfeilbuttons umher.\n Nach *60 Sekunden* wird das Menü **geschlossen**.\n**Achtung:** alles sind /commands!\n\n > *Page 1* - **Index**\n > *Page 2* - **Standard-Befehle**\n > *Page 3* - **Coin-system**\n > *Page 4* - **Admin Commands**\n > *Page 5* - **ContextMenus**\n > *Page 6* - **Musik**\n > *Page 7* - **Infos**\n > *Ticket lösen* - **Für andere Hilfe**",
                      colour=discord.Colour.green())
page1.set_footer(text="Prefix: *")
page2 = discord.Embed(title="Standard",
                      description="Hier findest du alle **Commands** von Excellus\nHier sind alle standard Commands!\n\n > *Help* - **Zeigt dieses Embed an**\n > *Invite* - **Zeigt Invite an**\n > *TicTacToe* - **Spiele TicTacToe**\n > *wasd* - **Spiele ein TEST game**\n > *SchereSteinPapier* - **Spiele ein SchereSteinPapier gegen Member oder Bot**\n > *Slots* - **Spiele ein Slot game**\n > *Get_Welcome* - **Zeigt dir deine Wilkommenskarte an**\n > *8ball* - **Stelle eine JA/NEIN Frage**\n > *Choose* - **Gib 2 möglichkeiten an der Bot entscheidet**\n > *Ping* - **Schaue den Ping von Excellus an**\n > *Color* - **Zeigt Embed Colors an**\n > *Anime* - **Suche nach einem Anime**\n > *Roleinfo* - **Gibt dir informationen über eine Rolle**\n > *Serverinfo* - **Gibt dir informationen über den Server**",
                      colour=discord.Colour.dark_blue())
page2.set_footer(text="Prefix: *")
page3 = discord.Embed(title="Coin",
                      description="Hier findest du alle **Coin-Commands** von Excellus\nAlles mit **Coins!**\n\n > *Coins* - **Zeigt Coins an**\n > *Send* - **Gib jemandem Coins**\n > *Deposit* - **Zahle dein geld in die Bank ein**\n > *Withdraw* - **Lasse dir dein Geld von der Bank auszahlen**\n > *Leaderboard* - **Zeige die top 10 reichsten Member an**",
                      colour=discord.Colour.gold())
page1.set_footer(text="Prefix: *")
page4 = discord.Embed(title="Admin-Commands",
                      description="Hier findest du alle **Admin-Commands** von Excellus\n**Achtung:** diese Commands können nur Teammitglieder benutzen!\n\n > *Clear/Clearall* - **Löscht bestimmte anzahl Nachrichten**\n > *Add* - **Addet jemandem Coins**\n > *Remove* - **Removed jemandem Coins**\n > *Log* - **zeigt den Log an**\n > *Ban* - **bannt ein Member**\n > *Unban* - **unbannt ein Member**\n > *Kick* - **kickt ein Member**\n > *Mute* - **mutet ein Member**\n > *Unmute* - **unmutet ein Member**\n > *Poll* - **startet eine umfrage**\n > *Achtung* - **macht ein Warnungs Embed**\n > *Lock* - **lockt ein channel**\n > *Unlock* - **unlockt ein channel**",
                      colour=discord.Colour.red())
page4.set_footer(text="Prefix: *")
page5 = discord.Embed(title="Context Menu",
                      description="Hier findest du alle **Context Menus** von Excellus\n**Achtung:** Abrufbar durch Rechtsklick auf Member und dann unter Apps!\n\n > *Avatar* - **Gib dir den Avatar von einem Member**\n > *Coins* - **Zeige dir die Coins von dem Member an**\n > *Userinfo* - **Gib dir informationen über den Member**",
                      colour=discord.Colour.orange())
page5.set_footer(text="Prefix: *")
page6 = discord.Embed(title="Musik",
                      description="Hier findest du alle **Musik** von Excellus\n**Achtung:** Joine zuerst in ein Voice channel!\n\n > *Play* - **Spiele ein Lied mit einer Youtube_URL**\n > *Pause* - **Pausiert das gespielte Lied**\n > *Resume* - **Spielt das pausierte spiel weiter**\n > *Stop* - **Stoppt das gespielte lied**\n > *Leave* - **Bot leavt aus den Channel**",
                      colour=discord.Colour.purple())
page6.set_footer(text="Prefix: *")
page7 = discord.Embed(title="Info",
                      description="Hier findest du alle **Infos** von Excellus\nGemacht von **Ξinfach_Ոoan#0001** in zusammenarbeit mit **PandaDΞV#1240**.\n\n > *Library* - **Dislash.py, Discord.py**\n > *Wann* - **Sommer 2021**\n > *Wo* - **Schweiz (Nördlich)**\n > *Noan's Server* - **[Einfach_Noan](https://discord.gg/8dqKZ2RwD5)**\n > *Panda's Server* - **[ᑭ🐼ᑎᗪI᙭](https://discord.gg/5rDh7ubakf)**",
                      colour=discord.Colour.blue())
page7.set_footer(text="Prefix: *")
bot.help_pages = [page1, page2, page3, page4, page5, page6, page7]


async def daly_reward():
    users = await get_bank_data()

    for user in users:
        bank = users[str(user)]["bank"]
        user = bot.get_user(int(user))
        await update_bank(user, 1000, "wallet")
        await update_bank(user, bank / 10000, "bank")


schedule.every().day.at("12:00").do(daly_reward)


@tasks.loop(seconds=1)
async def reward():
    schedule.run_pending()


@bot.event
async def on_ready():
    print("Bot is ready")
    guild = bot.get_guild(881564433439133756)
    channel = bot.get_channel(882648796113281034)
    true_member_count = f"Members: {len([m for m in guild.members if not m.bot])}"
    await channel.edit(name=true_member_count)
    await status_task()


async def status_task():  # discord.ActivityType.listening/watching - discord.game/Streaming
    while True:
        await bot.change_presence(activity=discord.Game("Ξinfach_Ոoan#0001's Bot"))
        await asyncio.sleep(3)
        await bot.change_presence(activity=discord.Game(f'Spezielle features! Auf {len(bot.guilds)} server'))
        await asyncio.sleep(3)
        await bot.change_presence(activity=discord.Game('/commands'))
        await asyncio.sleep(3)


API_KEY_HYPIXEL = "530ea92b-dd20-454a-8df1-da8779e16da2"
API_KEY_WT = "e37fcbfa0c81ade2938c030de2e6a7d5"
key_features = {
    'temp': 'Temperatur:',
    'feels_like': 'Fühlt sich an wie:',
    'temp_min': 'Minimum Temperatur',
    'temp_max': 'Maximal Temperatur'
}


@inter_client.slash_command(name="wetter", guild_ids=test_guilds, description="wetter",
                            options=[Option('land', 'location.', OptionType.STRING, required=True)])
async def hp(inter, land):
    land = land.lower()
    link = f"http://api.openweathermap.org/data/2.5/weather?q={land}&appid={API_KEY_WT}"
    try:
        data = json.loads(requests.get(link).content)
        data = data['main']
        del data['humidity']
        del data['pressure']
        del data['sea_level']
        del data['grnd_level']
        embed = discord.Embed(title=f"Wetter von **{land}**", color=discord.Color.gold())
        for key in data:
            embed.add_field(name=key_features[key], value=str(data[key]), inline=False)
        await inter.reply(embed=embed)
    except KeyError:
        await inter.reply(f"Failed {land} not found")


@inter_client.slash_command(name="abc", guild_ids=test_guilds, description="linked")
async def color(inter):
    profile = await inter.author.profile()
    accounts = profile.connected_accounts
    await inter.reply(accounts)


@inter_client.slash_command(name="color", guild_ids=test_guilds, description="farben liste")
async def color(inter):
    embed = discord.Embed(title="Alle Farb-Codes",
                          description="Für Discord Embed Color 0x vorne dran, z.B. green = 0x3066993.",
                          color=discord.Color.gold())
    for item in color_codes:
        embed.add_field(name=item, value=color_codes[item])
    await inter.reply(embed=embed)


@inter_client.slash_command(name="ping", guild_ids=test_guilds, description="ping")
async def ping(inter):
    ped = discord.Embed(
        title=f"Pong: {bot.latency}ms",
        description=f"Das ist der Ping von: **{bot.user.name}**",
        color=discord.Color.gold())
    await inter.reply(embed=ped)


def convert(time_set):
    pos = ["s", "m", "h", "d"]

    time_dict = {"s": 1, "m": 60, "h": 3600, "d": 3600 * 24}

    unit = time_set[-1]

    if unit not in pos:
        return -1
    try:
        val = int(time_set[:-1])
    except:
        return -2

    return val * time_dict[unit]


@inter_client.slash_command(name="giveaway", guild_ids=test_guilds, description="giveaway",
                            options=[Option('channel', 'Kanal.', OptionType.CHANNEL, required=True),
                                     Option('duration', 'Zeit (s|m|h|d).', OptionType.STRING, required=True),
                                     Option('prize', 'Preis.', OptionType.STRING, required=True)])
async def giveaway(inter, channel, duration, prize):
    await inter.reply(content="Loading", ephemeral=True)

    time_get = convert(duration)
    if time_get == -1:
        await inter.send(f"Benutze (s|m|h|d)!")
        return
    elif time_get == -2:
        await inter.send(
            f"Die Zeit muss nur eine ganze Zahl sein. Bitte geben Sie beim nächsten Mal eine ganze Zahl ein.")
        return

    embed = discord.Embed(title="Giveaway!", description=f"Preis: **{prize}**", color=discord.Color.gold())

    embed.add_field(name="Hosted by:", value=inter.author.mention)

    embed.set_footer(text=f"Endet in {duration} von jetzt!")

    my_msg = await channel.send(embed=embed)

    await my_msg.add_reaction("🎉")

    await asyncio.sleep(time_get)

    new_msg = await channel.fetch_message(my_msg.id)

    users = await new_msg.reactions[0].users().flatten()
    users.pop(users.index(bot.user))

    say_winner = random.choice(users)

    await channel.send(f"Congratulations! **{say_winner.mention}** hat **{prize}** gewonnen!")


@inter_client.slash_command(name="reroll", guild_ids=test_guilds, description="giveaway",
                            options=[Option('channel', 'Kanal.', OptionType.CHANNEL, required=True),
                                     Option('id_', 'Giveaway id', OptionType.STRING, required=True)])
async def reroll(inter, channel, id_):
    await inter.reply(content="Loading", ephemeral=True)

    new_msg = None
    try:
        new_msg = await channel.fetch_message(id_)
    except:
        await inter.send(
            "Die eingegebene ID war falsch. Stellen Sie sicher, dass Sie die richtige Werbegeschenk-ID eingegeben haben")
    users = await new_msg.reactions[0].users().flatten()
    users.pop(users.index(bot.user))

    winner_say = random.choice(users)

    await channel.send(f"Congratulations der neue Gewinner ist: **{winner_say.mention}** wegen reroll.")


@inter_client.slash_command(name="8ball", guild_ids=test_guilds, description="magic 8ball",
                            options=[Option('frage', 'frage.', OptionType.STRING, required=True)])
async def ball(inter, frage):
    responses = ['So, wie ich es sehe, ja.',
                 'Ja.',
                 'Positiv.',
                 'Aus meiner Sicht ja.',
                 'Überzeugt.',
                 'Höchstwahrscheinlich.',
                 'Grosse chance.',
                 'Nein.',
                 'Negativ.',
                 'Nicht überzeugt.',
                 'womöglich.',
                 'Nicht sicher.',
                 'Vielleicht.',
                 'kann ich jetzt nicht vorhersagen.',
                 'Ich bin zu faul vorherzusagen.',
                 'Ich bin müde. *weiter schlafen*']
    response = random.choice(responses)
    embed = discord.Embed(title="Der Magische **8 Ball** hat gesprochen!", color=discord.Color.gold())
    embed.add_field(name='Frage: ', value=f'{frage}', inline=True)
    embed.add_field(name='Antwort: ', value=f'{response}', inline=False)
    await inter.reply(embed=embed)


@inter_client.slash_command(name="choose", guild_ids=test_guilds, description="der bot wählt für dich etwas aus",
                            options=[Option('eins', 'eins.', OptionType.STRING, required=True),
                                     Option('zwei', 'zwei.', OptionType.STRING, required=True)])
async def choose(inter, eins, zwei):
    option = [str(eins), str(zwei)]
    await inter.reply(f"Gewählt: `{random.choice(option)}`")


@inter_client.slash_command(name="create_ticket_msg", guild_ids=test_guilds, description="pausieren")
@dislash.has_permissions(administrator=True)
async def create_ticket_msg(inter):
    if inter.channel.id == 892728308217827389:
        print(f'Ticket wurde in {inter.channel} erstellt von {inter.author}')
        ed = discord.Embed(title="Tickets 🎫", description="Erstelle ein Ticket für Support!",
                           color=discord.Color.gold())
        ed.set_image(url="https://ticketsbot.net/assets/img/logo.png")
        await inter.send(embed=ed, components=[
            ActionRow(Button(style=ButtonStyle.green, label="Create Ticket", emoji="🎫", custom_id="ticket"))])


@bot.event
async def on_button_click(inter):
    category = bot.get_channel(892275808654217237)
    message_content = f"Hallo , {inter.author.mention} unser Team wird sich gleich um dich kümmern! " \
                      f"Bitte beschreibe in der Zwischenzeit dein Problem!"

    if inter.clicked_button.label == "Create Ticket":
        msg = await inter.reply("Ticket System")
        await msg.delete()
        with open("data.json") as f:
            data = json.load(f)
        ticket_number = int(data["ticket-counter"])
        ticket_number += 1
        ticket_channel = await inter.guild.create_text_channel("ticket-{}".format(ticket_number), category=category)
        channel_a = None
        await asyncio.sleep(1)
        print("ticket-{}".format(ticket_number))
        for channel in inter.guild.channels:
            if str(channel.name) == "ticket-{}".format(ticket_number):
                channel_a = channel
        delete_msg = await inter.channel.send(content=f'Du hast ein ticket erstellt {channel_a.mention}')
        await ticket_channel.set_permissions(inter.guild.get_role(inter.guild.id), send_messages=False,
                                             read_messages=False)

        for role_id in data["valid-roles"]:
            role = inter.guild.get_role(role_id)

            await ticket_channel.set_permissions(role, send_messages=True, read_messages=True, add_reactions=True,
                                                 embed_links=True, attach_files=True, read_message_history=True,
                                                 external_emojis=True)

        await ticket_channel.set_permissions(inter.author, send_messages=True, read_messages=True,
                                             add_reactions=True,
                                             embed_links=True, attach_files=True, read_message_history=True,
                                             external_emojis=True)

        em = discord.Embed(title="New ticket from {}".format(inter.author),
                           description="{}".format(message_content), color=discord.Color.gold())

        await ticket_channel.send(embed=em, components=[ActionRow(
            Button(style=ButtonStyle.red, label="Ticket löschen", emoji="✖️", custom_id="ticket-close"),
            Button(style=ButtonStyle.green, label="Transkript", emoji="📰", custom_id="Transkript"))])
        pinged_msg_content = ""
        non_mentionable_roles = []

        if data["pinged-roles"] is not []:

            for role_id in data["pinged-roles"]:
                role = inter.guild.get_role(role_id)

                pinged_msg_content += role.mention
                pinged_msg_content += " "

                if role.mentionable:
                    pass
                else:
                    await role.edit(mentionable=True)
                    non_mentionable_roles.append(role)

            await ticket_channel.send(pinged_msg_content)

            for role in non_mentionable_roles:
                await role.edit(mentionable=False)

        data["ticket-channel-ids"].append(ticket_channel.id)

        data["ticket-counter"] = int(ticket_number)
        with open("data.json", 'w') as f:
            json.dump(data, f)
        await asyncio.sleep(4)
        await delete_msg.delete()

    elif inter.clicked_button.label == "Ticket löschen":
        msg = await inter.reply("Ticket System")
        await msg.delete()
        if not inter.author.guild_permissions.administrator:
            return
        with open('data.json') as f:
            data = json.load(f)
        print(f"{inter.author.display_name} hat versucht das Ticket zu löschen")
        if inter.channel.id in data["ticket-channel-ids"]:
            em = discord.Embed(title="Close Ticket",
                               description="Wenn du das ticket wirklich löschen willst, clicke auf den Button!",
                               color=discord.Color.gold())

            await inter.channel.send(embed=em, components=[
                ActionRow(Button(style=ButtonStyle.red, label="Accept", custom_id="delete"),
                          Button(style=ButtonStyle.red, label="abbrechen", custom_id="abbrechen"))])

    elif inter.clicked_button.label == "Transkript":
        msg = await inter.reply("Ticket System")
        await msg.delete()
        channel = inter.channel
        messages = await inter.channel.history().flatten()
        with open(f"trans/{channel}_messages.txt", "w", encoding="utf-8") as f:
            print(f"\nTranscript Saved by - {inter.author.display_name}.\n\n", file=f)
            for message in messages:
                if len(message.embeds) != 0:
                    embed = message.embeds[0].description
                    print(f"{message.author.name} - {embed}", file=f)
                print(f"{message.author.name} - {message.content}", file=f)
        await inter.channel.send(f"{inter.author.mention}, Transcript saved.")
        history = discord.File(fp=f'trans/{channel}_messages.txt', filename=None)
        await inter.send(file=history)
        inter = bot.get_channel(902944762775089182)
        history = discord.File(fp=f'trans/{channel}_messages.txt', filename=None)
        await inter.send(file=history)

    elif inter.clicked_button.label == "abbrechen" and not inter.clicked_button.custom_id == "ab":
        await inter.message.delete()

    elif inter.clicked_button.label == "Accept":
        if inter.author.bot:
            return
        with open('data.json') as f:
            data = json.load(f)
        if inter.channel_id in data["ticket-channel-ids"]:
            channel_id = inter.channel.id
            data["ticket-channel-ids"].remove(channel_id)
            cids = data["ticket-channel-ids"]
            print(f"Channel: {channel_id} wurde aus List (ticket-channel-ids) entfernt {cids}!")
            channel_id = bot.get_channel(channel_id)
            await channel_id.delete()
            with open('data.json', 'w') as f:
                json.dump(data, f)


@inter_client.slash_command(name="pause", guild_ids=test_guilds, description="pausieren")
async def pause(inter):
    voice = discord.utils.get(bot.voice_clients, guild=inter.guild)
    if voice.is_playing():
        voice.pause()
        await inter.send("Pausiert.")
    else:
        await inter.send("Kein lied läuft gerade.")


@inter_client.slash_command(name="resume", guild_ids=test_guilds, description="resume")
async def resume(inter):
    voice = discord.utils.get(bot.voice_clients, guild=inter.guild)
    if voice.is_paused():
        voice.resume()
        await inter.send("paused.")
    else:
        await inter.send("The audio is not paused.")


@inter_client.slash_command(name="stop", guild_ids=test_guilds, description="pausieren")
async def stop(inter):
    voice = discord.utils.get(bot.voice_clients, guild=inter.guild)
    voice.stop()
    await inter.send("stopped.")


@inter_client.slash_command(name="leave", guild_ids=test_guilds, description="leave")
async def leave(inter):
    voice = discord.utils.get(bot.voice_clients, guild=inter.guild)
    if voice.is_connected():
        await voice.disconnect()
        await inter.send("Left.")
    else:
        await inter.send("The bot is not connected to a voice channel.")


@inter_client.slash_command(name="play", guild_ids=test_guilds, description="Spiele ein lied",
                            options=[Option('url', 'gebe die URL an.', OptionType.STRING, required=True)])
async def play(inter, url):
    with open("log.txt", "a") as log:
        log.write(f"{get_time}, voice with url play!\n")
    log.close()
    msg = await inter.reply("Downloading")
    voice = inter.author.voice
    if voice:
        channel = voice.channel
        if channel:
            songname = f'songs/{inter.guild.id}_current.mp3'
            song_there = os.path.isfile(songname)
            try:
                if song_there:
                    os.remove(songname)
                    print('Removed old song file')
            except PermissionError:
                print('Trying to delete song file, but its being player')
                await inter.send('Error: Music playing')
                return

            voice = await channel.connect()
            ydl_opts = {
                'format': 'bestaudio/best',
                'postprocessors': [{
                    'key': 'FFmpegExtractAudio',
                    'preferredcodec': 'mp3',
                    'preferredquality': '192'
                }]
            }

            with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                print('Downloading audio now\n')
                ydl.download([url])

            for file in os.listdir('./'):
                if file.endswith('.mp3'):
                    print(f'Renamed File: {file}\n')
                    os.rename(file, songname)

            voice.play(discord.FFmpegPCMAudio(songname), after=lambda e: print('Song zu ende.'))
            voice.source = discord.PCMVolumeTransformer(voice.source)

            print('Ok.')
            await msg.delete()
            await inter.reply(content=f"Jetzt spielt {songname}")


@inter_client.slash_command(name="anime", guild_ids=test_guilds, description="search for anime",
                            options=[Option('query', 'query.', OptionType.STRING, required=True)])
async def play(inter, query):
    await inter.reply(content="Loading")
    try:
        anime = animec.Anime(query)
    except animec.errors.NoResultFound:
        await inter.reply(content="No anime found")
        return

    translator = Translator()
    translation = translator.translate(anime.description, dest="de")
    embed = discord.Embed(title=f"Anime **{anime.title_english}**", url=anime.url,
                          description=f"Beschreibung: **{translation.text}**", color=discord.Color.gold())
    embed.add_field(name=f"Episodes:", value=f"{anime.episodes}")
    embed.add_field(name=f"Ausstrahlungs zeit:", value=f"{anime.aired}")
    embed.add_field(name=f"Bewertung:", value=f"{anime.rating}")
    embed.add_field(name=f"Rank:", value=f"{anime.ranked}")
    embed.add_field(name=f"type:", value=f"{anime.type}")
    embed.add_field(name=f"Status:", value=f"{anime.status}")
    embed.add_field(name=f"Popularity:", value=f"{anime.popularity}")
    embed.add_field(name=f"Verfolger:", value=f"{anime.favorites}")
    embed.add_field(name=f"NSFW:", value=f"{str(anime.is_nsfw())}")
    embed.set_thumbnail(url=anime.poster)
    await inter.channel.send(embed=embed)


@inter_client.slash_command(name="achtung", guild_ids=test_guilds, description="gib warnung",
                            options=[Option('text', 'text.', OptionType.STRING, required=True)])
@dislash.has_permissions(administrator=True)
async def play(inter, text):
    embed = discord.Embed(title="<:warningicon:924619447401070622> Wichtige Warnung! <:warningicon:924619447401070622>",
                          description=text, color=discord.Color.gold())
    await inter.reply(embed=embed)


@inter_client.slash_command(name="lock", guild_ids=test_guilds, description="lock channel",
                            options=[Option('channel', 'channel.', OptionType.CHANNEL, required=False)])
@dislash.has_permissions(administrator=True)
async def lock(inter, channel=None):
    if channel is None:
        channel = inter.channel
    guild = bot.get_guild(881564433439133756)
    role = guild.get_role(892130235624079410)
    overwrite = channel.overwrites_for(role)
    overwrite.send_messages = False
    await channel.set_permissions(role, overwrite=overwrite)
    embed = discord.Embed(title="Channel Locked", color=discord.Color.gold())
    await inter.send(embed=embed)


@inter_client.slash_command(name="unlock", guild_ids=test_guilds, description="lock channel",
                            options=[Option('channel', 'channel.', OptionType.CHANNEL, required=False)])
@dislash.has_permissions(administrator=True)
async def lock(inter, channel=None):
    if channel is None:
        channel = inter.channel
    guild = bot.get_guild(881564433439133756)
    role = guild.get_role(892130235624079410)
    overwrite = channel.overwrites_for(role)
    overwrite.send_messages = True
    await channel.set_permissions(role, overwrite=overwrite)
    embed = discord.Embed(title="Channel Unlocked", color=discord.Color.gold())
    await inter.send(embed=embed)


@inter_client.slash_command(name="roleinfo", guild_ids=test_guilds, description="rollen info",
                            options=[Option('role', 'rolle.', OptionType.MENTIONABLE, required=True)])
async def roleinfo(inter, role):
    roles = inter.guild.roles
    embed = discord.Embed(title=f"Infos zu: {role.name}", color=discord.Color.gold())
    embed.add_field(name='Name:', value=f"{role.name}")
    embed.add_field(name='Farbe:', value=f"{role.color}")
    x = 0
    for is_role in roles:
        print(role)
        if is_role == role:
            embed.add_field(name='Position:', value=f"#{len(roles) - x}")
        x += 1
    embed.add_field(name='Created at:', value=f"{role.created_at}")
    embed.add_field(name='id:', value=f"{role.id}")
    embed.add_field(name='Mentionable:', value=f"{str(role.mentionable)}")
    embed.add_field(name='Is role from Bot:', value=f"{str(role.is_bot_managed())}")

    await inter.reply(embed=embed)


@inter_client.slash_command(name="serverinfo", guild_ids=test_guilds, description="server info")
async def serverinfo(inter):
    guild = bot.get_guild(881564433439133756)
    role_count = len(inter.guild.roles)
    list_of_bots = [bote.mention for bote in inter.guild.members if bote.bot]
    allowed = [892133307595235359, 911364890084655124]

    embed2 = discord.Embed(color=discord.Color.gold())
    embed2.add_field(name='Name', value=f"{inter.guild.name}")
    embed2.add_field(name='Owner', value=f"Ξinfach_Ոoan#0001")
    embed2.add_field(name='Verification Level', value=str(inter.guild.verification_level))
    embed2.add_field(name='Highest role', value=inter.guild.roles[-1])
    embed2.add_field(name='Co. Owner/Admin:', value="PandaDΞV#1240")

    for role in inter.guild.roles:
        print(allowed)
        print(role.id)
        if role.id in allowed:
            if role.name == "———————Team———————":
                role.name = "Team"
            print("found")
            members = '\n'.join([member.name for member in role.members]) or "None"
            embed2.add_field(name=role.name, value=members)

    embed2.add_field(name='Number of roles', value=str(role_count))
    embed2.add_field(name='Number Of Members', value=inter.guild.member_count)
    embed2.add_field(name='Text Channels', value=len(inter.guild.text_channels))
    embed2.add_field(name='Voice Channels', value=len(inter.guild.voice_channels))
    embed2.add_field(name='Bots:', value=(', '.join(list_of_bots)))
    embed2.add_field(name='Created At', value=inter.guild.created_at.__format__('%A, %d. %B %Y @ %H:%M:%S'))
    embed2.set_thumbnail(url=inter.guild.icon_url)
    embed2.set_author(name=inter.author.name, icon_url=inter.author.avatar_url)
    embed2.set_footer(text=bot.user.name, icon_url=bot.user.avatar_url)
    embed2.add_field(name=f"Boosts:",
                     value=f"**{guild.premium_subscription_count}** Danke an alle die geboostet haben.")

    await inter.reply(embed=embed2)


@inter_client.slash_command(name="wasd", guild_ids=test_guilds)
async def wasd(inter):
    row = ActionRow(Button(style=ButtonStyle.gray, label="X", disabled=True),
                    Button(style=ButtonStyle.green, label="W"),
                    Button(style=ButtonStyle.gray, label="X", disabled=True))
    row2 = ActionRow(Button(style=ButtonStyle.green, label="A"), Button(style=ButtonStyle.green, label="S"),
                     Button(style=ButtonStyle.green, label="D"))

    pos = [11, 12, 13,
           21, 22, 23,
           31, 32, 33]

    position = 22

    embed = discord.Embed(title="WASD",
                          description=f":red_square::red_square::red_square::red_square::red_square:\n:red_square::white_large_square::white_large_square::white_large_square::red_square:\n:red_square::white_large_square::x::white_large_square::red_square:\n:red_square::white_large_square::white_large_square::white_large_square::red_square:\n:red_square::red_square::red_square::red_square::red_square:",
                          color=discord.Color.green())

    msg = await inter.reply(embed=embed, components=[row, row2])

    while True:
        btn = await msg.wait_for_button_click(check)
        if btn.clicked_button.label == "W":
            position -= 10
            if "0" in str(position):
                position += 10
        if btn.clicked_button.label == "A":
            position -= 1
            if "0" in str(position):
                position += 1
        if btn.clicked_button.label == "S":
            position += 10
            if "0" in str(position):
                position -= 10
        if btn.clicked_button.label == "D":
            position += 1
            if "0" in str(position):
                position -= 1
        if int(position) == int(pos[0]):
            player_pos = ":red_square::red_square::red_square::red_square::red_square:\n:red_square::x::white_large_square::white_large_square::red_square:\n:red_square::white_large_square::white_large_square::white_large_square::red_square:\n:red_square::white_large_square::white_large_square::white_large_square::red_square:\n:red_square::red_square::red_square::red_square::red_square:"
            embed = discord.Embed(title="WASD", description=player_pos,
                                  color=discord.Color.green())
            await btn.respond(type=7, embed=embed, components=[row, row2])
        if int(position) == int(pos[1]):
            player_pos = ":red_square::red_square::red_square::red_square::red_square:\n:red_square::white_large_square::x::white_large_square::red_square:\n:red_square::white_large_square::white_large_square::white_large_square::red_square:\n:red_square::white_large_square::white_large_square::white_large_square::red_square:\n:red_square::red_square::red_square::red_square::red_square:"
            embed = discord.Embed(title="WASD", description=player_pos,
                                  color=discord.Color.green())
            await btn.respond(type=7, embed=embed, components=[row, row2])
        if int(position) == int(pos[2]):
            player_pos = ":red_square::red_square::red_square::red_square::red_square:\n:red_square::white_large_square::white_large_square::x::red_square:\n:red_square::white_large_square::white_large_square::white_large_square::red_square:\n:red_square::white_large_square::white_large_square::white_large_square::red_square:\n:red_square::red_square::red_square::red_square::red_square:"
            embed = discord.Embed(title="WASD", description=player_pos,
                                  color=discord.Color.green())
            await btn.respond(type=7, embed=embed, components=[row, row2])
        if int(position) == int(pos[3]):
            player_pos = ":red_square::red_square::red_square::red_square::red_square:\n:red_square::white_large_square::white_large_square::white_large_square::red_square:\n:red_square::x::white_large_square::white_large_square::red_square:\n:red_square::white_large_square::white_large_square::white_large_square::red_square:\n:red_square::red_square::red_square::red_square::red_square:"
            embed = discord.Embed(title="WASD", description=player_pos,
                                  color=discord.Color.green())
            await btn.respond(type=7, embed=embed, components=[row, row2])
        if int(position) == int(pos[4]):
            player_pos = ":red_square::red_square::red_square::red_square::red_square:\n:red_square::white_large_square::white_large_square::white_large_square::red_square:\n:red_square::white_large_square::x::white_large_square::red_square:\n:red_square::white_large_square::white_large_square::white_large_square::red_square:\n:red_square::red_square::red_square::red_square::red_square:"
            embed = discord.Embed(title="WASD", description=player_pos,
                                  color=discord.Color.green())
            await btn.respond(type=7, embed=embed, components=[row, row2])
        if int(position) == int(pos[5]):
            player_pos = ":red_square::red_square::red_square::red_square::red_square:\n:red_square::white_large_square::white_large_square::white_large_square::red_square:\n:red_square::white_large_square::white_large_square::x::red_square:\n:red_square::white_large_square::white_large_square::white_large_square::red_square:\n:red_square::red_square::red_square::red_square::red_square:"
            embed = discord.Embed(title="WASD", description=player_pos,
                                  color=discord.Color.green())
            await btn.respond(type=7, embed=embed, components=[row, row2])
        if int(position) == int(pos[6]):
            player_pos = ":red_square::red_square::red_square::red_square::red_square:\n:red_square::white_large_square::white_large_square::white_large_square::red_square:\n:red_square::white_large_square::white_large_square::white_large_square::red_square:\n:red_square::x::white_large_square::white_large_square::red_square:\n:red_square::red_square::red_square::red_square::red_square:"
            embed = discord.Embed(title="WASD", description=player_pos,
                                  color=discord.Color.green())
            await btn.respond(type=7, embed=embed, components=[row, row2])
        if int(position) == int(pos[7]):
            player_pos = ":red_square::red_square::red_square::red_square::red_square:\n:red_square::white_large_square::white_large_square::white_large_square::red_square:\n:red_square::white_large_square::white_large_square::white_large_square::red_square:\n:red_square::white_large_square::x::white_large_square::red_square:\n:red_square::red_square::red_square::red_square::red_square:"
            embed = discord.Embed(title="WASD", description=player_pos,
                                  color=discord.Color.green())
            await btn.respond(type=7, embed=embed, components=[row, row2])
        if int(position) == int(pos[8]):
            player_pos = ":red_square::red_square::red_square::red_square::red_square:\n:red_square::white_large_square::white_large_square::white_large_square::red_square:\n:red_square::white_large_square::white_large_square::white_large_square::red_square:\n:red_square::white_large_square::white_large_square::x::red_square:\n:red_square::red_square::red_square::red_square::red_square:"
            embed = discord.Embed(title="WASD", description=player_pos,
                                  color=discord.Color.green())
            await btn.respond(type=7, embed=embed, components=[row, row2])


async def check_button(inter, label: str):
    if inter.clicked_button.label == label:
        print(inter)
        return True, label


@inter_client.slash_command(name="select", description="test", guild_ids=test_guilds)
async def select(inter):
    row = ActionRow(Button(style=ButtonStyle.green, label="Alter"), Button(style=ButtonStyle.green, label="Games"),
                    Button(style=ButtonStyle.green, label="land"))
    # "<:coin:924619447367512094>"
    embed = discord.Embed(title=f"Wähle Selfroles:", color=discord.Color.green())

    await inter.respond(embed=embed, components=[row])


@slash.event
async def on_button_click(selfrole):
    d_row_g = ActionRow(Button(style=ButtonStyle.green, label="Minecraft", disabled=True),
                        Button(style=ButtonStyle.green, label="Rocket League", disabled=True),
                        Button(style=ButtonStyle.green, label="Fortnite", disabled=True))
    d_row_a = ActionRow(Button(style=ButtonStyle.green, label="10-14 Jahre", disabled=True),
                        Button(style=ButtonStyle.green, label="15-18 Jahre", disabled=True),
                        Button(style=ButtonStyle.green, label="18+", disabled=True))
    d_row_l = ActionRow(Button(style=ButtonStyle.green, label="Deutschland", disabled=True),
                        Button(style=ButtonStyle.green, label="Schweiz", disabled=True),
                        Button(style=ButtonStyle.green, label="England", disabled=True))
    if selfrole.clicked_button.label == "Alter":
        row = ActionRow(Button(style=ButtonStyle.green, label="10-14 Jahre"),
                        Button(style=ButtonStyle.green, label="15-18 Jahre"),
                        Button(style=ButtonStyle.green, label="18+"))
        embed = discord.Embed(title=f"Wähle dein Alter:", color=discord.Color.green())
        msg = await selfrole.reply(embed=embed, components=[row], ephemeral=True)
        inter = await msg.wait_for_button_click(check)
        embed = discord.Embed(title=f"Alter = {inter.clicked_button.label}", color=discord.Color.green())
        await inter.respond(type=7, embed=embed, components=[d_row_a])
    if selfrole.clicked_button.label == "Games":
        row = ActionRow(Button(style=ButtonStyle.green, label="Minecraft"),
                        Button(style=ButtonStyle.green, label="Rocket League"),
                        Button(style=ButtonStyle.green, label="Fortnite"))
        embed = discord.Embed(title=f"Wähle deine Games:", color=discord.Color.green())
        msg = await selfrole.reply(embed=embed, components=[row], ephemeral=True)
        inter = await msg.wait_for_button_click(check)
        embed = discord.Embed(title=f"Game = {inter.clicked_button.label}", color=discord.Color.green())
        await inter.respond(type=7, embed=embed, components=[d_row_g])
    if selfrole.clicked_button.label == "land":
        row = ActionRow(Button(style=ButtonStyle.green, label="Deutschland"),
                        Button(style=ButtonStyle.green, label="Schweiz"),
                        Button(style=ButtonStyle.green, label="England"))
        embed = discord.Embed(title=f"Wähle dein Land", color=discord.Color.green())
        msg = await selfrole.reply(embed=embed, components=[row], ephemeral=True)
        inter = await msg.wait_for_button_click(check)
        embed = discord.Embed(title=f"Land = {inter.clicked_button.label}", color=discord.Color.green())
        await inter.respond(type=7, embed=embed, components=[d_row_l])


@inter_client.user_command(name="Coins", guild_ids=test_guilds)
async def balance(inter):
    member = inter.target

    await open_account(member)

    users = await get_bank_data()

    user = member

    geld = users[str(user.id)]["wallet"]
    bank = users[str(user.id)]["bank"]
    total = str(bank + geld)

    embed = discord.Embed(title=f"<:coin:924619447367512094> {user.display_name}'s Geld:",
                          description=f"> **{geld}** in Bar.\n > **{bank}** auf der Bank\n > **{total}** im total",
                          color=discord.Color.gold())
    await inter.reply(embed=embed)


@inter_client.slash_command(
    name="invite",
    description="invite den bot"
)
@dislash.has_permissions(administrator=True)
async def invite(inter):
    emb = discord.Embed(title="Invite Excellus auf deinen Server!",
                        description=f"{bot.user.mention}: [INVITE](https://discord.com/oauth2/authorize?client_id={bot.user.id}&permissions=8&scope=bot%20applications.commands)",
                        color=Color.gold())
    emb.timestamp = datetime.datetime.now()
    await inter.respond(embed=emb)


@inter_client.slash_command(name="coins", guild_ids=test_guilds, description="Zeigt dir die Coins an",
                            options=[Option('member', 'gebe den member an.', OptionType.USER, required=False)])
async def coins(inter, member=None):
    if member is None:
        member = inter.author

    await open_account(member)

    users = await get_bank_data()

    user = member

    geld = users[str(user.id)]["wallet"]
    bank = users[str(user.id)]["bank"]
    total = bank + geld

    embed = discord.Embed(title=f"<:coin:924619447367512094> {user.display_name}'s Geld:",
                          description=f"> **{geld}** in Bar.\n > **{bank}** auf der Bank\n > **{total}** im total",
                          color=discord.Color.gold())
    await inter.reply(embed=embed)


@inter_client.slash_command(name="leaderboard",
                            description="Top 10 reichste personen. IMAGE mit zufälliger Farbe. (/lb für EMBED)",
                            guild_ids=test_guilds)
async def lb(inter):
    await inter.reply("**Leaderboard:**")
    users = await get_bank_data()
    color_random = ["blue", "cyan", "green", "pink", "purple", "red", "yellow"]
    bg = Image.open(f"./Assets/global_{random.choice(color_random)}.png")
    font_big = ImageFont.truetype("./Assets/bahnschrift.ttf", size=25)

    x, x1, y, y_ = 90, 400, 90, 66
    leader_board = {}
    total = []
    for user in users:
        name = int(user)
        total_amount = users[user]["wallet"] + users[user]["bank"]
        leader_board[total_amount] = name
        total.append(total_amount)

    total = sorted(total, reverse=True)

    draw = ImageDraw.Draw(bg)

    counter = 10
    for i in total:
        mem = await bot.fetch_user(int(leader_board[i]))
        name = f"{mem}"
        draw.text((x, y), name, fill=(255, 255, 255), font=font_big)  # <:coin:924619447367512094>
        draw.text((x1, y), f"{str(i)}", fill=(255, 255, 255), font=font_big)
        y += y_
        counter -= 1
        if counter == 0:
            break
    while counter > 0:
        draw.text((x, y), "    -    ", fill=(255, 255, 255))
        draw.text((x1, y), "    -    ", fill=(255, 255, 255))
        y += y_
        counter -= 1

    with BytesIO() as a:
        bg.save(a, 'PNG')
        a.seek(0)
        await inter.channel.send(file=discord.File(a, filename="leader.png"), content="")


@inter_client.slash_command(name="poll", description="willkommen", guild_ids=test_guilds,
                            options=[Option('frage', 'gebe die Frage ein.', OptionType.STRING, required=True)])
@dislash.has_permissions(administrator=True)
async def get_welcome(inter, frage):
    clicked = {}
    v1 = 0
    v2 = 0
    embed = discord.Embed(title=f"Poll: vote für 👍 oder 👎", description=frage, color=discord.Color.gold())
    embed.add_field(name="👍", value=v1)
    embed.add_field(name="👎", value=v2)
    row = ActionRow(Button(style=ButtonStyle.green, emoji="👍", label="Ja"),
                    Button(style=ButtonStyle.red, emoji="👎", label="Nein"),
                    Button(style=ButtonStyle.red, label="abbrechen", custom_id="ab"),
                    )
    msg = await inter.reply(embed=embed, components=[row])
    while True:
        knopf = await msg.wait_for_button_click(check)
        try:
            if clicked[str(knopf.author.id)] == "ja" or "nein" or "abbrechen":
                pass
        except:
            clicked[str(knopf.author.id)] = "None"
        if knopf.clicked_button.label == 'Ja':
            if clicked[str(knopf.author.id)] != "ja":
                if clicked[str(knopf.author.id)] == "nein":
                    v2 -= 1
                v1 += 1
                embed = discord.Embed(title=f"Poll: vote für 👍 oder 👎", description=frage, color=discord.Color.gold())
                embed.add_field(name="👍", value=v1)
                embed.add_field(name="👎", value=v2)
                await knopf.respond(type=7, embed=embed)
                clicked[str(knopf.author.id)] = "ja"
            else:
                await knopf.reply("du hast das schon geklickt")
        if knopf.clicked_button.label == 'Nein':
            if clicked[str(knopf.author.id)] != "nein":
                if clicked[str(knopf.author.id)] == "ja":
                    v1 -= 1
                v2 += 1
                embed = discord.Embed(title=f"Poll: vote für 👍 oder 👎", description=frage,
                                      color=discord.Color.gold())
                embed.add_field(name="👍", value=v1)
                embed.add_field(name="👎", value=v2)
                await knopf.respond(type=7, embed=embed)
                clicked[str(knopf.author.id)] = "nein"
            else:
                await knopf.reply("du hast das schon geklickt")
        if knopf.clicked_button.custom_id == 'ab':
            perm = knopf.author.guild_permissions.administrator
            if perm is True:
                disabled_row = ActionRow(Button(style=ButtonStyle.green, emoji="👍", label="Ja", disabled=True),
                                         Button(style=ButtonStyle.red, emoji="👎", label="Nein", disabled=True))
                embed = discord.Embed(title=f"Poll: **ENDET**", description=frage,
                                      color=discord.Color.gold())
                embed.add_field(name="👍", value=v1)
                embed.add_field(name="👎", value=v2)
                await msg.edit(components=[disabled_row], embed=embed)
                await knopf.reply("You stopped the Poll", ephemeral=True)
                return
            await knopf.reply("Du hast keine permissions", ephemeral=True)


@inter_client.slash_command(name="get_welcome", description="willkommen", guild_ids=test_guilds,
                            options=[Option('member', 'gebe den member ein.', OptionType.USER, required=False)])
async def get_welcome(inter, member=None):
    if member is None:
        member = inter.author
    await inter.reply(f"Willkommen Karte von {member.name}.")
    file = await welcome_img(member)
    await inter.channel.send(file=file)


async def welcome_img(inter):
    if inter == "Ξinfach_Ոoan#0001":
        inter.name = "Einfach_Noan"
    text = f"{inter.name}#{inter.discriminator}"
    size = 45
    height = 280
    if len(text) > 14:
        text = f"{inter.name}"
        if len(text) > 14:
            text = f"{text[0:13]}" + "..."

    font_big = ImageFont.truetype("./Assets/bahnschrift.ttf", size=size)
    font_big2 = ImageFont.truetype("./Assets/bahnschrift.ttf", size=25)

    background = Editor("Assets/welcome.png")
    profile = await load_image_async(str(inter.avatar_url))
    profile2 = await load_image_async(str(bot.user.avatar_url))

    profile = Editor(profile).resize((252, 252)).circle_image()
    profile2 = Editor(profile2).resize((40, 40)).circle_image()

    background.paste(profile.image, (50, 91))
    background.paste(profile2.image, (630, 395))

    background.text((340, height), text, font=font_big, color="white")
    background.text((680, 406), "Excellus", font=font_big2, color="white")

    file = File(fp=background.image_bytes, filename="card.png")
    return file


@inter_client.slash_command(name="lb", description="Top 10 reichste personen. Als Embed (/leaderboard für IMAGE)",
                            guild_ids=test_guilds)
async def leaderboard(inter):
    users = await get_bank_data()
    leader_board = {}
    total = []
    for user in users:
        name = int(user)
        total_amount = users[user]["wallet"] + users[user]["bank"]
        leader_board[total_amount] = name
        total.append(total_amount)

    total = sorted(total, reverse=True)
    print(leader_board)
    print(total)

    embed = discord.Embed(title="Top 10 reichste personen auf dem Server!", color=discord.Color.green())
    index = 1
    for amt in total:
        mem = await bot.fetch_user(int(leader_board[amt]))
        print(int(leader_board[amt]))
        print(mem)
        name = mem
        if index == 1:
            rank = "<:1:924619447392694282>"
        elif index == 2:
            rank = "<:2_:924619447195562027>"
        elif index == 3:
            rank = "<:3_:924619446990037043>"
        else:
            rank = f"{index}" + "."
        embed.add_field(name=f"{rank} {name}", value=f"{amt} <:coin:924619447367512094>", inline=False)
        if index == 10:
            break
        else:
            index += 1

    await inter.reply(embed=embed)


@inter_client.slash_command(name="withdraw", description="abheben", guild_ids=test_guilds,
                            options=[Option('amount', 'gebe den amount ein.', OptionType.STRING, required=True)])
async def withdraw(inter, amount):
    error = discord.Embed(title="Error:", color=discord.Color.red())
    await open_account(inter.author)

    bal = await update_bank(inter.author)

    amount = int(amount)

    if amount > bal[1]:
        error.add_field(name="Betrag auf der Bank zu niedrig",
                        value="Bitte gib ein Betrag an den du auf der bank hast!")
        await inter.reply(embed=error)
        return
    if 0 > amount:
        error.add_field(name="Betrag negativ", value="Bitte gib ein positiven Betrag an!")
        await inter.reply(embed=error)
        return

    embed = discord.Embed(title="Geld von der Bank abgehoben.",
                          description=f"Du hast **{amount}** <:coin:924619447367512094> von der Bank abgehoben.",
                          color=discord.Color.gold())
    await inter.reply(embed=embed)

    await update_bank(inter.author, amount)
    await update_bank(inter.author, -1 * amount, "bank")


@inter_client.slash_command(name="deposit", description="einzahlen", guild_ids=test_guilds,
                            options=[Option('amount', 'gebe den amount ein.', OptionType.INTEGER, required=True)])
async def deposit(inter, amount):
    error = discord.Embed(title="Error:", color=discord.Color.red())
    await open_account(inter.author)

    bal = await update_bank(inter.author)

    amount = int(amount)

    if amount > bal[0]:
        error.add_field(name="Betrag in Bar zu niedrig", value="Bitte gib ein Betrag an den du gerade in Bar hast!")
        await inter.reply(embed=error)
        return
    if 0 >= amount:
        error.add_field(name="Betrag zu niedrig", value="Bitte gib ein größeren Betrag an!")
        await inter.reply(embed=error)
        return

    embed = discord.Embed(title="Geld in der Bank gesichert.",
                          description=f"Du hast **{amount}** <:coin:924619447367512094> in die Bank gegeben.",
                          color=discord.Color.gold())
    await inter.reply(embed=embed)

    await update_bank(inter.author, -1 * amount)
    await update_bank(inter.author, amount, "bank")


@inter_client.slash_command(name="send", description="geld weggeben", guild_ids=test_guilds,
                            options=[Option('member', 'gebe den member an.', OptionType.USER, required=True),
                                     Option('amount', 'gebe den amount ein.', OptionType.INTEGER, required=True)])
async def send(inter, member, amount):
    error = discord.Embed(title="Error:", color=discord.Color.red())
    await open_account(inter.author)
    await open_account(member)

    bal = await update_bank(inter.author)

    amount = int(amount)

    if amount > bal[0]:
        error.add_field(name="Betrag in Bar zu niedrig", value="Bitte gib ein Betrag an den du gerade in Bar hast!")
        await inter.reply(embed=error)
        return
    if 0 >= amount:
        error.add_field(name="Betrag zu niedrig", value="Bitte gib ein größeren Betrag an!")
        await inter.reply(embed=error)
        return

    embed = discord.Embed(title="Geld gegeben.",
                          description=f"Du hast **{amount}** <:coin:924619447367512094> an **{member}** gegeben.",
                          color=discord.Color.gold())
    await inter.reply(embed=embed)

    await update_bank(inter.author, -1 * amount, "wallet")
    await update_bank(member, amount, "wallet")


@inter_client.slash_command(name="shop", guild_ids=test_guilds, description="shop")
async def shop(inter):
    with open("shop.json") as f:
        mainshop = json.load(f)
    em = discord.Embed(title="Shop", color=discord.Color.gold())
    for item in mainshop:
        print(item)
        name = item["name"]
        price = str(item["price"])
        des = item["description"]
        em.add_field(name=f"{name} - **{price}** <:coin:924619447367512094>", value=des, inline=False)
    await inter.reply(embed=em)


@inter_client.slash_command(name="kick", guild_ids=test_guilds, description="Geld Hinzufügen",
                            options=[Option('member', 'gebe den member an.', OptionType.USER, required=True),
                                     Option('reason', 'grund.', OptionType.STRING, required=True)])
@dislash.has_permissions(administrator=True)
async def kick(inter, member, reason):
    await inter.reply(f"**{member}** wurde wegen {reason} gekickt!")
    await member.send(f"Du wurdest wegen {reason} gekickt!")
    await member.kick(reason=reason)


@inter_client.slash_command(name="mute", guild_ids=test_guilds, description="muten",
                            options=[Option('member', 'gebe den member an.', OptionType.USER, required=True),
                                     Option('reason', 'grund.', OptionType.STRING, required=True)])
@dislash.has_permissions(administrator=True)
async def mute(inter, member, reason):
    guild = bot.get_guild(881564433439133756)
    role = get(guild.roles, id=928314516612186143)
    await member.add_roles(role)
    await inter.reply(f"**{member}** wurde wegen {reason} gemutet!")
    await member.send(f"Du wurdest wegen **{reason}** gemutet!")


@inter_client.slash_command(name="unmute", guild_ids=test_guilds, description="unmute",
                            options=[Option('member', 'gebe den member an.', OptionType.USER, required=True)])
@dislash.has_permissions(administrator=True)
async def mute(inter, member):
    guild = bot.get_guild(881564433439133756)
    role = get(guild.roles, id=928314516612186143)
    if role in member.roles:
        await member.remove_roles(role)
        await inter.reply(f"**{member}** wurde geunmutet!")
        await member.send(f"Du wurdest geunmutet!")
    else:
        await inter.reply(f"**{member}** ist nicht gemutet!")


@inter_client.slash_command(name="ban", guild_ids=test_guilds, description="banne member",
                            options=[Option('member', 'gebe den member an.', OptionType.USER, required=True),
                                     Option('reason', 'grund.', OptionType.STRING, required=True)])
@dislash.has_permissions(administrator=True)
async def ban(inter, member, reason):
    await inter.reply(f"**{member}** wurde wegen {reason} gebannt!")
    await member.send(f"Du wurdest wegen **{reason}** gebannt!")
    await member.ban(reason=reason)


@inter_client.slash_command(name="unban", guild_ids=test_guilds, description="Geld Hinzufügen",
                            options=[Option('member', 'gebe den member an.', OptionType.USER, required=True)])
@dislash.has_permissions(administrator=True)
async def unban(inter, member):
    await inter.reply(f"**{member}** wurde entbannt!")
    banned_users = await inter.guild.bans()
    name = f"{member.name}#{member.discriminator}"
    print(name)
    member_name, member_disc = name.split('#')

    for banned_entry in banned_users:
        user = banned_entry.user

        if (user.name, user.discriminator) == (member_name, member_disc):
            await inter.guild.unban(user)
            return
    await inter.reply(f"**{member}** wurde nicht gefunden!")


@inter_client.slash_command(name="add", guild_ids=test_guilds, description="Geld Hinzufügen",
                            options=[Option('member', 'gebe den member an.', OptionType.USER, required=True),
                                     Option('amount', 'gebe den amount ein.', OptionType.INTEGER, required=True)])
@dislash.has_permissions(administrator=True)
async def add(inter, member, amount):
    error = discord.Embed(title="Error:", color=discord.Color.red())
    await open_account(member)

    amount = int(amount)

    if 0 >= amount:
        error.add_field(name="Betrag zu niedrig", value="Bitte gib ein größeren Betrag an!")
        await inter.reply(embed=error)
        return

    embed = discord.Embed(title="Geld geaddet.",
                          description=f"Du hast **{amount}** <:coin:924619447367512094> an **{member}** gegeben.",
                          color=discord.Color.gold())
    await inter.reply(embed=embed)

    await update_bank(member, amount, "wallet")


@inter_client.slash_command(name="set", guild_ids=test_guilds, description="Set",
                            options=[Option('member', 'gebe den member an.', OptionType.USER, required=True),
                                     Option('amount', 'gebe den amount ein.', OptionType.INTEGER, required=True),
                                     Option("where", description="Wallet or Bank",
                                            type=OptionType.STRING,
                                            required=True,
                                            choices=[
                                                OptionChoice("Bank", "bank"),
                                                OptionChoice("Wallet", "wallet")
                                            ])
                                     ])
@dislash.has_permissions(administrator=True)
async def set(inter, member, amount, where):
    error = discord.Embed(title="Error:", color=discord.Color.red())
    await open_account(member)

    amount = int(amount)

    if 0 >= amount:
        error.add_field(name="Betrag zu niedrig", value="Bitte gib ein größeren Betrag an!")
        await inter.reply(embed=error)
        return

    await set_bank(member, amount, "wallet")

    embed = discord.Embed(title="Geld gesetzt.",
                          description=f"Du hast von **{member}** **{where}** auf **{amount}** <:coin:924619447367512094> gesetzt.",
                          color=discord.Color.gold())
    await inter.reply(embed=embed)


@inter_client.slash_command(name="reset", guild_ids=test_guilds, description="Member coin reset",
                            options=[Option('member', 'gebe den member an.', OptionType.USER, required=True)])
@dislash.has_permissions(administrator=True)
async def reset(inter, member):
    await close_account(member)
    embed = discord.Embed(title="Geld reset.",
                          description=f"Du hast **{member}**'s account zurückgesetzt.",
                          color=discord.Color.gold())
    await inter.reply(embed=embed)


@inter_client.slash_command(name="remove", guild_ids=test_guilds, description="Geld wegnehmen",
                            options=[Option('member', 'gebe den member an.', OptionType.USER, required=True),
                                     Option('amount', 'gebe den amount ein.', OptionType.INTEGER, required=True)])
@dislash.has_permissions(administrator=True)
async def remove(inter, member, amount):
    error = discord.Embed(title="Error:", color=discord.Color.red())
    await open_account(member)

    amount = int(amount)

    if 0 >= amount:
        error.add_field(name="Betrag zu niedrig", value="Bitte gib ein größeren Betrag an!")
        await inter.reply(embed=error)
        return

    embed = discord.Embed(title="Geld removed.",
                          description=f"Du hast **{amount}** <:coin:924619447367512094> von **{member}** genommen.",
                          color=discord.Color.gold())
    await inter.reply(embed=embed)

    await update_bank(member, -1 * amount, "wallet")


async def open_account(user):
    users = await get_bank_data()

    if str(user.id) in users:
        return False
    else:
        users[str(user.id)] = {}
        users[str(user.id)]["wallet"] = 1000
        users[str(user.id)]["bank"] = 0

    with open("mainbank.json", "w") as f:
        json.dump(users, f)
    return True


async def close_account(user):
    users = await get_bank_data()

    if str(user.id) in users:
        users[str(user.id)] = {}
        users[str(user.id)]["wallet"] = 1000
        users[str(user.id)]["bank"] = 0
    else:
        users[str(user.id)] = {}
        users[str(user.id)]["wallet"] = 1000
        users[str(user.id)]["bank"] = 0

    with open("mainbank.json", "w") as f:
        json.dump(users, f)
    return True


async def get_bank_data():
    with open("mainbank.json", "r") as f:
        users = json.load(f)
    return users


async def update_bank(user, change=0, mode="wallet"):
    users = await get_bank_data()

    users[str(user.id)][mode] += change

    with open("mainbank.json", "w") as f:
        json.dump(users, f)

    bal = [users[str(user.id)]["wallet"], users[str(user.id)]["bank"]]

    return bal


async def set_bank(user, change=0, mode="wallet"):
    users = await get_bank_data()

    users[str(user.id)][mode] = change

    with open("mainbank.json", "w") as f:
        json.dump(users, f)

    bal = [users[str(user.id)]["wallet"], users[str(user.id)]["bank"]]

    return bal


@inter_client.user_command(name="Userinfo", guild_ids=test_guilds)
async def userinfo(inter):
    used = discord.Embed(colour=inter.target.color)
    used.timestamp = datetime.datetime.now()
    used.set_author(name=f"User Info - {inter.target}")
    used.set_thumbnail(url=inter.target.avatar_url)
    used.set_footer(text=f"Angefordert von: {inter.target}")
    used.add_field(name=f"ID: ", value=inter.target.id)
    used.add_field(name=f"Servername: ", value=inter.target.display_name)
    used.add_field(name='Account Created', value=inter.target.created_at.__format__('%A, %d. %B %Y @ %H:%M:%S'))
    used.add_field(name='Join Date', value=inter.target.joined_at.__format__('%A, %d. %B %Y @ %H:%M:%S'), inline=True)
    used.add_field(name=f"Oberste Rolle: ", value=inter.target.top_role.mention)
    used.add_field(name='Status:', value=inter.target.status)
    await inter.reply(embed=used)


@inter_client.slash_command(name="userinfo", description="userinfo", guild_ids=test_guilds,
                            options=[
                                Option('member', 'member.', OptionType.USER, required=False)])
async def userinfo(inter, member=None):
    msg = inter
    if member is None:
        member = inter.author
    inter = member
    used = discord.Embed(colour=inter.color)
    used.timestamp = datetime.datetime.now()
    used.set_author(name=f"User Info - {inter}")
    used.set_thumbnail(url=inter.avatar_url)
    used.set_footer(text=f"Angefordert von: {inter}")
    used.add_field(name=f"ID: ", value=inter.id)
    used.add_field(name=f"Servername: ", value=inter.display_name)
    used.add_field(name='Account Created', value=inter.created_at.__format__('%A, %d. %B %Y @ %H:%M:%S'))
    used.add_field(name='Join Date', value=inter.joined_at.__format__('%A, %d. %B %Y @ %H:%M:%S'), inline=True)
    used.add_field(name=f"Oberste Rolle: ", value=inter.top_role.mention)
    used.add_field(name='Status:', value=inter.status)
    await msg.reply(embed=used)


@inter_client.user_command(name="Profile Card", guild_ids=test_guilds)
async def userinfo(inter):
    member = inter.target
    name = member.name
    if name == "PandaDΞV":
        name = "PandaDEV"
    if name == "Ξinfach_Ոoan":
        name = "Einfach_Noan"
    await inter.reply("Loading")
    canvas = Canvas((400, 500), color="black")  # 1920 x 1080

    poppins = Font.poppins(size=16)
    poppins_large = Font.poppins(size=20)

    users = await get_bank_data()

    geld = users[str(member.id)]["wallet"]
    bank = users[str(member.id)]["bank"]
    total = str(bank + geld)

    image = await load_image_async(str(member.avatar_url))

    editor = Editor(canvas).rounded_corners(10)
    bg = Editor("Assets/img.png").resize((400, 230)).rounded_corners(10)
    profile = Editor(image).resize((100, 100)).circle_image()
    editor.rectangle((10, 10), 20, 20, "black")
    editor.paste(bg, (0, 0))
    editor.rectangle((2, 210), width=396, height=40, fill="#000")
    editor.rectangle((30, 190), width=320, height=40, fill="#494b4f", radius=20)
    editor.paste(profile, (20, 155))
    editor.text((150, 10), "Von Einfach_Noan's Server", color="#cc0a0b", font=poppins)
    editor.text((320, 475), "Excellus", font=poppins, color="white")
    editor.text((40, 283), 'Coins', font=poppins_large, color="white")
    editor.text((120, 290), '-', font=poppins_large, color="white")
    editor.text((145, 283), total + " in total", font=poppins_large, color="white")
    editor.text((40, 333), 'UserID', font=poppins_large, color="white")
    editor.text((120, 340), '-', font=poppins_large, color="white")
    editor.text((145, 333), str(member.id), font=poppins_large, color="white")
    editor.text((40, 383), 'Joined', font=poppins_large, color="white")
    editor.text((120, 390), '-', font=poppins_large, color="white")
    # inter.target.joined_at.__format__('%d. %b %Y %H:%M:%S')
    editor.text((145, 383), member.joined_at.__format__('%d. %b %Y %H:%M:%S'), font=poppins_large, color="white")
    editor.text((40, 433), 'Level', font=poppins_large, color="white")
    editor.text((120, 440), '-', font=poppins_large, color="white")
    editor.text((145, 433), "Nicht vorhanden", font=poppins_large, color="white")
    editor.text((130, 204), f"{name}#{member.discriminator}", font=poppins, color="white")
    editor.rectangle((20, 270), 360, 40, outline="white", radius=6, stroke_width=3)
    editor.rectangle((20, 320), 360, 40, outline="white", radius=6, stroke_width=3)
    editor.rectangle((20, 370), 360, 40, outline="white", radius=6, stroke_width=3)
    editor.rectangle((20, 420), 360, 40, outline="white", radius=6, stroke_width=3)
    file = File(fp=editor.image_bytes, filename='profile.png')

    await inter.channel.send(file=file)


@inter_client.slash_command(name="profile", description="Profil", guild_ids=test_guilds,
                            options=[
                                Option('member', 'member.', OptionType.USER, required=False)])
async def userinfo(inter, member=None):
    if member is None:
        member = inter.author
    name = member.name
    if name == "PandaDΞV":
        name = "PandaDEV"
    if name == "Ξinfach_Ոoan":
        name = "Einfach_Noan"
    await inter.reply("Loading")
    canvas = Canvas((400, 500), color="black")  # 1920 x 1080

    poppins = Font.poppins(size=16)
    poppins_large = Font.poppins(size=20)

    users = await get_bank_data()

    geld = users[str(member.id)]["wallet"]
    bank = users[str(member.id)]["bank"]
    total = str(bank + geld)

    image = await load_image_async(str(member.avatar_url))

    editor = Editor(canvas).rounded_corners(10)
    bg = Editor("Assets/img.png").resize((400, 230)).rounded_corners(10)
    profile = Editor(image).resize((100, 100)).circle_image()
    editor.rectangle((10, 10), 20, 20, "black")
    editor.paste(bg, (0, 0))
    editor.rectangle((2, 210), width=396, height=40, fill="#000")
    editor.rectangle((30, 190), width=320, height=40, fill="#494b4f", radius=20)
    editor.paste(profile, (20, 155))
    editor.text((150, 10), "Von Einfach_Noan's Server", color="#cc0a0b", font=poppins)
    editor.text((320, 475), "Excellus", font=poppins, color="white")
    editor.text((40, 283), 'Coins', font=poppins_large, color="white")
    editor.text((120, 290), '-', font=poppins_large, color="white")
    editor.text((145, 283), total + " in total", font=poppins_large, color="white")
    editor.text((40, 333), 'UserID', font=poppins_large, color="white")
    editor.text((120, 340), '-', font=poppins_large, color="white")
    editor.text((145, 333), str(member.id), font=poppins_large, color="white")
    editor.text((40, 383), 'Joined', font=poppins_large, color="white")
    editor.text((120, 390), '-', font=poppins_large, color="white")
    # inter.target.joined_at.__format__('%d. %b %Y %H:%M:%S')
    editor.text((145, 383), member.joined_at.__format__('%d. %b %Y %H:%M:%S'), font=poppins_large, color="white")
    editor.text((40, 433), 'Level', font=poppins_large, color="white")
    editor.text((120, 440), '-', font=poppins_large, color="white")
    editor.text((145, 433), "Nicht vorhanden", font=poppins_large, color="white")
    editor.text((130, 204), f"{name}#{member.discriminator}", font=poppins, color="white")
    editor.rectangle((20, 270), 360, 40, outline="white", radius=6, stroke_width=3)
    editor.rectangle((20, 320), 360, 40, outline="white", radius=6, stroke_width=3)
    editor.rectangle((20, 370), 360, 40, outline="white", radius=6, stroke_width=3)
    editor.rectangle((20, 420), 360, 40, outline="white", radius=6, stroke_width=3)
    file = File(fp=editor.image_bytes, filename='profile.png')

    await inter.channel.send(file=file)


@inter_client.user_command(name="Avatar", guild_ids=test_guilds)
async def avatar(inter):
    emb = discord.Embed(title=f"{inter.target}'s avatar")
    emb.set_image(url=inter.target.avatar_url)
    await inter.reply(embed=emb)


@inter_client.message_command(name="repeat", guild_ids=test_guilds)
async def repeat(inter):
    if len(inter.target.content) == 0:
        await inter.reply(f"Es können keine Embeds wiederholt werden!")
    else:
        await inter.reply(f"{inter.target.content}")


@bot.event
async def on_member_join(member: discord.Member):
    print("joined")
    guild = bot.get_guild(881564433439133756)
    if member.guild == guild:
        role_id = 892130235624079410
        role = get(guild.roles, id=role_id)
        print(role)
        welcome2 = bot.get_channel(896059062536523807)
        file = await welcome_img(member)
        regeln = bot.get_channel(892422512078622770)
        welcomed = discord.Embed(title=f"Willkommen **{member.display_name}** auf {guild.name}",
                                 description=f"Bitte lese dir {regeln.mention} __gut__ durch und akzeptiere sie um die {role.mention} Rolle zu bekommen",
                                 color=Color.gold())
        await welcome2.send(embed=welcomed)
        await welcome2.send(file=file)
        channel = bot.get_channel(894674818346127401)
        await channel.send(f"{member.mention} joined the **PARTY**")
        await update_member_count()
    else:
        print(member.guild)
        print(guild)
        return


async def update_member_count():
    guild = bot.get_guild(881564433439133756)
    true_member_count = f"Members: {len([m for m in guild.members if not m.bot])}"
    channel = bot.get_channel(882648796113281034)
    await channel.edit(name=f"{true_member_count}")


@bot.event
async def on_member_remove(member):
    with open("log.txt", "a") as log:
        log.write(f"{get_time}, member left: {member}!\n")
    log.close()
    guild = bot.get_guild(881564433439133756)
    if member.guild == guild:
        await update_member_count()
        channel = bot.get_channel(894674818346127401)
        await channel.send(f"{member.mention} left the **PARTY**")
    else:
        return


@inter_client.slash_command(name="clear", description="clear", guild_ids=test_guilds,
                            options=[
                                Option('amount', 'gebe die anzahl nachrichten an.', OptionType.INTEGER, required=True)])
@dislash.has_permissions(administrator=True)
async def clear(inter, amount):
    embed = discord.Embed(title=f"{amount} Nachrichten gelöscht")
    await inter.reply(embed=embed, ephemeral=True)
    await inter.channel.purge(limit=amount)


@inter_client.slash_command(name="clearall", description="clearall", guild_ids=test_guilds)
@dislash.has_permissions(administrator=True)
async def clearall(inter):
    embed = discord.Embed(title=f"Alle Nachrichten gelöscht")
    await inter.channel.purge()
    await inter.reply(embed=embed, ephemeral=True)


@inter_client.slash_command(name="log", description="get_log", guild_ids=test_guilds)
@dislash.has_permissions(administrator=True)
async def get_log(inter):
    await inter.reply("**Log.txt**")
    await inter.channel.send(file=discord.File("log.txt"))


@inter_client.slash_command(name="dm", description="dm jemand", guild_ids=test_guilds,
                            options=[Option('user', 'gebe den member an.', OptionType.USER, required=True),
                                     Option('args', 'gebe die nachricht ein', OptionType.STRING, required=True)])
@dislash.has_permissions(administrator=True)
async def dm(inter, user, args):
    user = user.id
    target = await bot.fetch_user(user)
    await inter.reply("'" + args + "' gesendet zu: " + target.name)
    await target.send(args)


@inter_client.slash_command(name="help", description="Zeig dir hilfe an", guild_ids=test_guilds)
async def help(inter):
    row = ActionRow(
        Button(
            style=ButtonStyle.green,
            label="<<",
            custom_id="start"
        ),
        Button(
            style=ButtonStyle.green,
            label="<",
            custom_id="back"
        ),
        Button(
            style=ButtonStyle.green,
            label=">",
            custom_id="vor"
        ),
        Button(
            style=ButtonStyle.green,
            label=">>",
            custom_id="end"
        ),
    )
    disabled_row = ActionRow(
        Button(
            style=ButtonStyle.green,
            label="<<",
            disabled=True
        ),
        Button(
            style=ButtonStyle.green,
            label="<",
            disabled=True
        ),
        Button(
            style=ButtonStyle.green,
            label=">",
            disabled=True
        ),
        Button(
            style=ButtonStyle.green,
            label=">>",
            disabled=True
        ),
    )
    current = 0
    msg = await inter.reply(embed=bot.help_pages[current], components=[row])
    print(current)
    while True:
        try:
            button_interaction = await msg.wait_for_button_click(check, timeout=20.0)
        except asyncio.TimeoutError:
            await msg.edit(components=[disabled_row])
            return print(f"Das Embed von: '{inter.author.display_name}' wurde beendet!")
        else:
            if button_interaction.clicked_button.custom_id == "start":
                current = 0
                await button_interaction.respond(type=7, embed=bot.help_pages[current], components=[row])
            if button_interaction.clicked_button.custom_id == "back":
                if current > 0:
                    current -= 1
                await button_interaction.respond(type=7, embed=bot.help_pages[current], components=[row])
            if button_interaction.clicked_button.custom_id == "vor":
                if current < len(bot.help_pages) - 1:
                    current += 1
                await button_interaction.respond(type=7, embed=bot.help_pages[current], components=[row])
            if button_interaction.clicked_button.custom_id == "end":
                current = len(bot.help_pages) - 1
                await button_interaction.respond(type=7, embed=bot.help_pages[current], components=[row])


def checkForWin(board):
    win = (
            board[0] == board[1] and board[1] == board[2]
            or board[3] == board[4] and board[4] == board[5]
            or board[6] == board[7] and board[7] == board[8]
            or board[0] == board[4] and board[4] == board[8]
            or board[2] == board[4] and board[4] == board[6]
            or board[0] == board[3] and board[3] == board[6]
            or board[1] == board[4] and board[4] == board[7]
            or board[2] == board[5] and board[5] == board[8]
    )
    if not any(i.isdigit() for i in board) and not win:
        return 2
    else:
        return win


@inter_client.slash_command(name="tictactoe", description="tictactoe", guild_ids=test_guilds,
                            options=[Option('member', 'vordere jemanden heraus.', OptionType.USER, required=True)])
async def ttt(inter, member):
    if inter.author == member:
        await inter.send(f"{inter.author.mention} Du kannst nicht gegen dich spielen.!")
        return
    if member.bot:
        await inter.send(f"{inter.author.mention} Ich glaub nicht das bots tic-tac-toe spielen können...")
        return
    row = [ActionRow(
        Button(
            style=ButtonStyle.gray,
            label="1",
            custom_id="1"
        ),
        Button(
            style=ButtonStyle.gray,
            label="2",
            custom_id="2"
        ),
        Button(
            style=ButtonStyle.gray,
            label="3",
            custom_id="3"
        ),
    ), ActionRow(
        Button(
            style=ButtonStyle.gray,
            label="4",
            custom_id="4"
        ),
        Button(
            style=ButtonStyle.gray,
            label="5",
            custom_id="5"
        ),
        Button(
            style=ButtonStyle.gray,
            label="6",
            custom_id="6"
        ),
    ), ActionRow(
        Button(
            style=ButtonStyle.gray,
            label="7",
            custom_id="7"
        ),
        Button(
            style=ButtonStyle.gray,
            label="8",
            custom_id="8"
        ),
        Button(
            style=ButtonStyle.gray,
            label="9",
            custom_id="9"
        )
    )]
    embed = discord.Embed(title=f"{inter.author.name} fordert {member.name} für ein TicTacToe Game heraus.",
                          description=f"Will {member.name} mitmachen?", color=discord.Color.gold())
    ja = ActionRow(Button(style=ButtonStyle.green, label="Ja ich will."),
                   Button(style=ButtonStyle.red, label="Nein kein Bock."))
    msg = await inter.reply(embed=embed, components=[ja])
    while True:
        knopf = await msg.wait_for_button_click(check)
        if member == knopf.author:
            if knopf.clicked_button.label == 'Ja ich will.':
                embed = discord.Embed(title=f"Spiel Abgebrochen", color=discord.Color.red())
                await knopf.respond(type=7, embed=embed, components=[])
                break
            else:
                embed = discord.Embed(title=f"Spiel Abgebrochen", color=discord.Color.green())
                await knopf.respond(type=7, embed=embed, components=[])
                return False
    embed = discord.Embed(title=f"{member.name} und {inter.author.name}'s TicTacToe Game.",
                          description=f"Es ist {member.mention}'s Zug", color=discord.Color.gold())
    msg = await inter.reply(embed=embed, components=row)

    turn = 'X'
    players = {
        'X': member,
        'O': inter.author
    }

    clicked = {
        1: 1,
        2: 2,
        3: 3,
        4: 4,
        5: 5,
        6: 6,
        7: 7,
        8: 8,
        9: 9
    }

    activated = {
        1: False,
        2: False,
        3: False,
        4: False,
        5: False,
        6: False,
        7: False,
        8: False,
        9: False
    }

    was = {
        "1": "1",
        "2": "2",
        "3": "3",
        "4": "4",
        "5": "5",
        "6": "6",
        "7": "7",
        "8": "8",
        "9": "9"
    }

    color_style = {
        "O": ButtonStyle.green,
        "X": ButtonStyle.blurple
    }

    gelegt = []

    while True:
        btn = await msg.wait_for_button_click(check)
        print(f"{players[turn]} - {btn.author} Ist das gleiche oder?")
        if players[turn] == btn.author:
            if btn.clicked_button.label != 'X' or '0':
                gelegt.append(btn.clicked_button.label)
                clicked[int(btn.clicked_button.label)] = turn
                activated[int(btn.clicked_button.label)] = True
                was[str(btn.clicked_button.label)] = turn
                eins = ButtonStyle.gray
                zwei = ButtonStyle.gray
                drei = ButtonStyle.gray
                vier = ButtonStyle.gray
                fun = ButtonStyle.gray
                sechs = ButtonStyle.gray
                sieben = ButtonStyle.gray
                acht = ButtonStyle.gray
                neun = ButtonStyle.gray
                if activated[1] is True:
                    eins = color_style[was["1"]]
                if activated[2] is True:
                    zwei = color_style[was["2"]]
                if activated[3] is True:
                    drei = color_style[was["3"]]
                if activated[4] is True:
                    vier = color_style[was["4"]]
                if activated[5] is True:
                    fun = color_style[was["5"]]
                if activated[6] is True:
                    sechs = color_style[was["6"]]
                if activated[7] is True:
                    sieben = color_style[was["7"]]
                if activated[8] is True:
                    acht = color_style[was["8"]]
                if activated[9] is True:
                    neun = color_style[was["9"]]
                row = [ActionRow(
                    Button(
                        style=eins,
                        label=str(clicked[1]),
                        custom_id="1"
                    ),
                    Button(
                        style=zwei,
                        label=str(clicked[2]),
                        custom_id="2"
                    ),
                    Button(
                        style=drei,
                        label=str(clicked[3]),
                        custom_id="3"
                    ),
                ), ActionRow(
                    Button(
                        style=vier,
                        label=str(clicked[4]),
                        custom_id="4"
                    ),
                    Button(
                        style=fun,
                        label=str(clicked[5]),
                        custom_id="5"
                    ),
                    Button(
                        style=sechs,
                        label=str(clicked[6]),
                        custom_id="6"
                    ),
                ), ActionRow(
                    Button(
                        style=sieben,
                        label=str(clicked[7]),
                        custom_id="7"
                    ),
                    Button(
                        style=acht,
                        label=str(clicked[8]),
                        custom_id="8"
                    ),
                    Button(
                        style=neun,
                        label=str(clicked[9]),
                        custom_id="9"
                    ),
                )]
            aList = []
            print(was)
            for i in was:
                aList.append(was[i])
            board = aList
            print(board)
            gameWon = checkForWin(board)
            print(gameWon)

            if gameWon is True or gameWon == 2:
                eins = ButtonStyle.gray
                zwei = ButtonStyle.gray
                drei = ButtonStyle.gray
                vier = ButtonStyle.gray
                fun = ButtonStyle.gray
                sechs = ButtonStyle.gray
                sieben = ButtonStyle.gray
                acht = ButtonStyle.gray
                neun = ButtonStyle.gray
                if activated[1] is True:
                    eins = color_style[was["1"]]
                if activated[2] is True:
                    zwei = color_style[was["2"]]
                if activated[3] is True:
                    drei = color_style[was["3"]]
                if activated[4] is True:
                    vier = color_style[was["4"]]
                if activated[5] is True:
                    fun = color_style[was["5"]]
                if activated[6] is True:
                    sechs = color_style[was["6"]]
                if activated[7] is True:
                    sieben = color_style[was["7"]]
                if activated[8] is True:
                    acht = color_style[was["8"]]
                if activated[9] is True:
                    neun = color_style[was["9"]]
                lose_row = [ActionRow(
                    Button(
                        style=eins,
                        label=str(clicked[1]),
                        custom_id="1",
                        disabled=True
                    ),
                    Button(
                        style=zwei,
                        label=str(clicked[2]),
                        custom_id="2",
                        disabled=True
                    ),
                    Button(
                        style=drei,
                        label=str(clicked[3]),
                        custom_id="3",
                        disabled=True
                    ),
                ), ActionRow(
                    Button(
                        style=vier,
                        label=str(clicked[4]),
                        custom_id="4",
                        disabled=True
                    ),
                    Button(
                        style=fun,
                        label=str(clicked[5]),
                        custom_id="5",
                        disabled=True
                    ),
                    Button(
                        style=sechs,
                        label=str(clicked[6]),
                        custom_id="6",
                        disabled=True
                    ),
                ), ActionRow(
                    Button(
                        style=sieben,
                        label=str(clicked[7]),
                        custom_id="7",
                        disabled=True
                    ),
                    Button(
                        style=acht,
                        label=str(clicked[8]),
                        custom_id="8",
                        disabled=True
                    ),
                    Button(
                        style=neun,
                        label=str(clicked[9]),
                        custom_id="9",
                        disabled=True
                    ),
                )]
                if gameWon == 2:
                    print("tie")
                    embed = discord.Embed(title=f"{member.name} und {inter.author.name}'s TicTacToe Game.",
                                          description=f"Game Over! Unentschieden!",
                                          color=discord.Color.gold())
                    await btn.respond(type=7, embed=embed, components=lose_row)
                else:
                    print("won")
                    embed = discord.Embed(title=f"{member.name} und {inter.author.name}'s TicTacToe Game.",
                                          description=f"Game Over! **{players[turn].mention}** hat gewonnen! Du bekommst von deinem Gegner 100 <:coin:924619447367512094>",
                                          color=discord.Color.gold())
                    await btn.respond(type=7, embed=embed, components=lose_row)
                    if players[turn].name == member.name:
                        await winner(inter.author, member, 100)
                    else:
                        await winner(member, inter.author, 100)
                break
            turn = 'O' if turn == 'X' else 'X'
            embed = discord.Embed(title=f"{member.name} und {inter.author.name}'s TicTacToe Game.",
                                  description=f"Es ist {players[turn].mention}'s Zug", color=discord.Color.gold())
            await btn.respond(type=7, embed=embed, components=row)
        else:
            if btn.author == players['X'] or players['O']:
                await btn.reply("Du bist nicht Dran.", ephemeral=True)
            else:
                await btn.reply("Du spielst nicht mit.", ephemeral=True)


async def winner(inter, member, amount):
    await open_account(inter)
    await open_account(member)

    await update_bank(inter)

    amount = int(amount)

    await update_bank(inter, -1 * amount, "wallet")
    await update_bank(member, amount, "wallet")


@inter_client.slash_command(description="slots", guild_ids=test_guilds)
async def slots(inter):
    slot = ["X", "O", "I"]
    round = 0
    lose = 0
    wine = 0
    row = ActionRow(Button(style=ButtonStyle.green, label="drehen"), Button(style=ButtonStyle.red, label="abbrechen"))
    d_row = ActionRow(Button(style=ButtonStyle.green, label="drehen", disabled=True),
                      Button(style=ButtonStyle.red, label="abbrechen", disabled=True))
    embed = discord.Embed(title="Slot Maschine", description=f"|X|X|X|", color=discord.Color.gold())
    msg = await inter.reply(embed=embed, components=[row], ephemeral=True)
    win = {"1": "", "2": "", "3": ""}
    while True:
        btn = await msg.wait_for_button_click(check)
        if btn.clicked_button.label == "drehen":
            round += 1
            win["1"] = random.choice(slot)
            win["2"] = random.choice(slot)
            win["3"] = random.choice(slot)
            if win["1"] == win["2"] and win["2"] == win["3"]:
                wine += 800
                await slot_a(btn.author, wine)
            else:
                lose += 100
                await slot_a(btn.author, -lose)
            embed = discord.Embed(title="Slot Maschine", description=f'|{win["1"]}|{win["2"]}|{win["3"]}|',
                                  color=discord.Color.gold())
            embed.add_field(name="Round", value=f"{round}", inline=False)
            embed.add_field(name="Wins", value=f"{wine} <:coin:924619447367512094>", inline=False)
            embed.add_field(name="Lose", value=f"{lose} <:coin:924619447367512094>", inline=False)
            await btn.respond(type=7, embed=embed, components=[row])
        if btn.clicked_button.label == "abbrechen":
            embed = discord.Embed(title="Slot Maschine", description=f'CANCELED',
                                  color=discord.Color.gold())
            embed.add_field(name="Rounds", value=f"{round}", inline=False)
            embed.add_field(name="Wins", value=f"{wine} <:coin:924619447367512094>", inline=False)
            embed.add_field(name="Lose", value=f"{lose} <:coin:924619447367512094>", inline=False)
            await btn.respond(type=7, embed=embed, components=[d_row])
            return


async def slot_a(member, amount):
    await open_account(member)

    amount = int(amount)

    await update_bank(member, amount, "wallet")


@inter_client.slash_command(name="schersteinpapier", description="tictactoe", guild_ids=test_guilds,
                            options=[Option('member', 'vordere jemanden heraus.', OptionType.USER, required=False)])
async def ssp(inter, member=None):
    is_bot = False
    if inter.author == member:
        await inter.send(f"{inter.author.mention} Du kannst nicht gegen dich spielen.!")
        return
    try:
        if member.bot:
            await inter.send(f"{inter.author.mention} Du kannst nicht einen Bot spielen.!")
    except:
        if member is None:
            is_bot = True
            member = bot.user
    if member is not bot.user:
        embed = discord.Embed(title=f"{inter.author.name} fordert {member.name} für ein ScherSteinPapier Game heraus.",
                              description=f"Will {member.name} mitmachen?", color=discord.Color.gold())
        ja = ActionRow(Button(style=ButtonStyle.green, label="Ja ich will."),
                       Button(style=ButtonStyle.red, label="Nein kein Bock."))
        msg = await inter.reply(embed=embed, components=[ja])
        while True:
            knopf = await msg.wait_for_button_click(check)
            if member == knopf.author:
                if knopf.clicked_button.label == 'Ja ich will.':
                    embed = discord.Embed(title=f"Spiel Abgebrochen", color=discord.Color.red())
                    await knopf.respond(type=7, embed=embed, components=[])
                    break
                else:
                    embed = discord.Embed(title=f"Spiel Abgebrochen", color=discord.Color.green())
                    await knopf.respond(type=7, embed=embed, components=[])
                    return False
    row = ActionRow(
        Button(
            style=ButtonStyle.gray,
            label="Schere",
            emoji="✂"
        ),
        Button(
            style=ButtonStyle.green,
            label="Stein",
            emoji="<:stone:925406142098710568>"
        ),
        Button(
            style=ButtonStyle.blurple,
            label="Papier",
            emoji="📰"
        ),

    )

    ran = ["Schere", "Stein", "Papier"]

    player = {
        "p1": "",
        "p2": "" if is_bot is not True else f"{random.choice(ran)}"
    }

    emoji = {
        "Schere": "✂",
        "Papier": "📰",
        "Stein": "<:stone:925406142098710568>"
    }

    embed = discord.Embed(title=f"{member.name} und {inter.author.name}'s Game", color=discord.Color.gold())

    msg = await inter.reply(embed=embed, components=[row])

    while True:
        btn = await msg.wait_for_button_click(check)
        print(player)
        if inter.author or member == btn.author:
            if btn.clicked_button.label == 'Schere':
                if btn.author == inter.author:
                    if player["p1"] == "":
                        player["p1"] = btn.clicked_button.label
                        await btn.reply(f"**{btn.clicked_button.label}** Hast du gewählt", ephemeral=True)
                    else:
                        await btn.reply("Du hast schon gewählt!", ephemeral=True)
                elif btn.author == member:
                    if player["p2"] == "":
                        player["p2"] = btn.clicked_button.label
                        await btn.reply(f"**{btn.clicked_button.label}** Hast du gewählt", ephemeral=True)
                    else:
                        await btn.reply("Du hast schon gewählt!", ephemeral=True)
            if btn.clicked_button.label == 'Stein':
                if btn.author == inter.author:
                    if player["p1"] == "":
                        player["p1"] = btn.clicked_button.label
                        await btn.reply(f"**{btn.clicked_button.label}** Hast du gewählt", ephemeral=True)
                    else:
                        await btn.reply("Du hast schon gewählt!", ephemeral=True)
                elif btn.author == member:
                    if player["p2"] == "":
                        player["p2"] = btn.clicked_button.label
                        await btn.reply(f"**{btn.clicked_button.label}** Hast du gewählt", ephemeral=True)
                    else:
                        await btn.reply("Du hast schon gewählt!", ephemeral=True)
            if btn.clicked_button.label == 'Papier':
                if btn.author == inter.author:
                    if player["p1"] == "":
                        player["p1"] = btn.clicked_button.label
                        await btn.reply(f"**{btn.clicked_button.label}** Hast du gewählt", ephemeral=True)
                    else:
                        await btn.reply("Du hast schon gewählt!", ephemeral=True)
                elif btn.author == member:
                    if player["p1"] == "":
                        player["p2"] = btn.clicked_button.label
                        await btn.reply(f"**{btn.clicked_button.label}** Hast du gewählt", ephemeral=True)
                    else:
                        await btn.reply("Du hast schon gewählt!", ephemeral=True)
            row_disabled = ActionRow(
                Button(
                    style=ButtonStyle.gray,
                    label="Schere",
                    emoji="✂",
                    disabled=True
                ),
                Button(
                    style=ButtonStyle.green,
                    label="Stein",
                    emoji="<:stone:925406142098710568>",
                    disabled=True
                ),
                Button(
                    style=ButtonStyle.blurple,
                    label="Papier",
                    emoji="📰",
                    disabled=True
                ),
            )
            if player["p1"] == player["p2"]:
                print(f"Unentschieden: {player['p1']} - {player['p2']}")
                embed = discord.Embed(title=f"{member.name} und {inter.author.name}'s Game",
                                      description=f"Unentschieden: {emoji[player['p1']]} **{player['p1']} - {emoji[player['p1']]} {player['p2']}**",
                                      color=discord.Color.gold())
                await msg.edit(type=7, embed=embed, components=[row_disabled])
                break
            if player["p1"] == "Schere" and player["p2"] == "Papier":
                print(f"Gewonnen hat {inter.author} mit {player['p1']} - {player['p2']}")
                embed = discord.Embed(title=f"{member.name} und {inter.author.name}'s Game",
                                      description=f"Gewonnen hat *{inter.author}* mit ✂ **{player['p1']} - 📰 {player['p2']}**",
                                      color=discord.Color.gold())
                await msg.edit(type=7, embed=embed, components=[row_disabled])
                break
            if player["p1"] == "Papier" and player["p2"] == "Stein":
                print(f"Gewonnen hat {inter.author} mit {player['p1']} - {player['p2']}")
                embed = discord.Embed(title=f"{member.name} und {inter.author.name}'s Game",
                                      description=f"Gewonnen hat *{inter.author}* mit 📰 **{player['p1']} - <:stone:925406142098710568> {player['p2']}**",
                                      color=discord.Color.gold())
                await msg.edit(type=7, embed=embed, components=[row_disabled])
                break
            if player["p1"] == "Stein" and player["p2"] == "Schere":
                print(f"Gewonnen hat {inter.author} mit {player['p1']} - {player['p2']}")
                embed = discord.Embed(title=f"{member.name} und {inter.author.name}'s Game",
                                      description=f"Gewonnen hat *{inter.author}* mit <:stone:925406142098710568> **{player['p1']} - ✂ {player['p2']}**",
                                      color=discord.Color.gold())
                await msg.edit(type=7, embed=embed, components=[row_disabled])
                break
            if player["p2"] == "Schere" and player["p1"] == "Papier":
                print(f"Gewonnen hat {member} mit {player['p1']} - {player['p2']}")
                embed = discord.Embed(title=f"{member.name} und {inter.author.name}'s Game",
                                      description=f"Gewonnen hat *{member}* mit ✂ **{player['p1']} - 📰 {player['p2']}**",
                                      color=discord.Color.gold())
                await msg.edit(type=7, embed=embed, components=[row_disabled])
                break
            if player["p2"] == "Papier" and player["p1"] == "Stein":
                print(f"Gewonnen hat {member} mit {player['p1']} - {player['p2']}")
                embed = discord.Embed(title=f"{member.name} und {inter.author.name}'s Game",
                                      description=f"Gewonnen hat *{member}* mit 📰 **{player['p1']} - <:stone:925406142098710568> {player['p2']}**",
                                      color=discord.Color.gold())
                await msg.edit(type=7, embed=embed, components=[row_disabled])
                break
            if player["p2"] == "Stein" and player["p1"] == "Schere":
                print(f"Gewonnen hat {member} mit {player['p1']} - {player['p2']}")
                embed = discord.Embed(title=f"{member.name} und {inter.author.name}'s Game",
                                      description=f"Gewonnen hat *{member}* mit <:stone:925406142098710568> **{player['p1']} - ✂ {player['p2']}**",
                                      color=discord.Color.gold())
                await msg.edit(type=7, embed=embed, components=[row_disabled])
                break
        else:
            await btn.reply("Du machst nicht mit!")


@bot.event
async def on_raw_reaction_add(payload):
    if payload.member.bot:
        return
    if payload.channel_id == 892422512078622770:
        if payload.message_id == 896708283778367538:
            guild: discord.Guild = bot.get_guild(881564433439133756)
            role: discord.Role = guild.get_role(892130235624079410)
            await payload.member.add_roles(role, reason="Rollenvergabe: Member")


bot.run("TOKEN")
