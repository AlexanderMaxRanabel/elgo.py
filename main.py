import discord
from discord.ext import commands
import requests
intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix='!', token='token', intents=intents)

@bot.command()
async def filesay(ctx, pastebin_link):
    response = requests.get(pastebin_link)
    if response.status_code == 200:
        await ctx.send(response.text)
    else:
        await ctx.send("Error: Failed to fetch data from the provided Pastebin link.")


@bot.command()
async def urban(ctx, term):
        url = f"https://api.urbandictionary.com/v0/define?term={term}"
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            if len(data['list']) > 0:
                top_definition = data['list'][0]['definition']
                await ctx.send(f"**{term}**: {top_definition}")
            else:
                await ctx.send(f"No definitions found for {term}.")
        else:
            await ctx.send("Error: Failed to fetch data from the Urban Dictionary API.")

#@bot.command()
#async def levget(ctx):

bot.run('token')
