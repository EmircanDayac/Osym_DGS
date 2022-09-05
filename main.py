
from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl
import discord

context = ssl._create_unverified_context()
res = urlopen("https://www.osym.gov.tr/TR,23771/2022.html",
              context=context)
soup = BeautifulSoup(res, "html.parser")
data = soup.findAll("table", "table")

token = "TOKEN GİRİN"
client = discord.Client(intents=discord.Intents.default())


@client.event
async def on_ready():
    print(f"Bot logged in as {client.user}")


@client.event
async def on_message(msg):
    if msg.author != client.user:
        if msg.content.lower().startswith("?yeter"):
            for i in range(len(data)):
                await msg.channel.send(f"yeterse yeter lan\n  {data[i].text.strip().replace('  ', '')}")


client.run(token)
