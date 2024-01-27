import discord
from discord.ext import commands
import requests
from dtoken import TOKEN


# Define intents
intents = discord.Intents.default()
intents.messages = True
intents.message_content = True  # Enable the privileged message content intent

bot = commands.Bot(command_prefix='$', intents=intents)

def get_btc_price():
    print("[BTCPricer]")
    response = requests.get('https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd')
    data = response.json()
    return data['bitcoin']['usd']

@bot.command()
async def BTC(ctx, btc_amount: float):
    btc_price_usd = get_btc_price()
    btc_value_usd = btc_amount * btc_price_usd
    satoshis = btc_amount * 100000000
    await ctx.send(embed=discord.Embed(
        description=f"{btc_amount} BTC is ${btc_value_usd:.2f} USD & {int(satoshis):,} Satoshis",
        color=discord.Color.blue()
    ))

@bot.command()
async def USD(ctx, usd_amount: float):
    btc_price_usd = get_btc_price()
    btc_amount = usd_amount / btc_price_usd
    satoshis = btc_amount * 100000000
    await ctx.send(embed=discord.Embed(
        description=f"${usd_amount} USD is {btc_amount:.8f} BTC & {int(satoshis):,} Satoshis",
        color=discord.Color.green()
    ))

bot.run(TOKEN)
