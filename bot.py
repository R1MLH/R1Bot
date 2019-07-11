# -*- coding: utf-8 -*-

import asyncio
import aiohttp
import json
import discord
import yaml
import time
import datetime
import requests
import pickle
import regex as re
from pytz import timezone
from discord import Game
from discord.ext.commands import Bot

BOT_PREFIX = ("|")
TOKEN = ""

client = Bot(command_prefix=BOT_PREFIX)
r1 = "<:R1:428141251120857109>"

subregex = r"\/?\/[a-zA-Z]{2,20}\/?"


@client.listen()
async def on_message(message):
    if message.author.bot: return
    if message.content.find('http://') is not -1 or message.content.find('https://') is not -1: return

    for subreddit in re.findall(subregex, message.content):
        processedSub = subreddit.replace("/", "")[1:]
        await client.send_message(message.channel,
                                  r1 + ' https://old.reddit.com/r/'
                                  + processedSub + '/top/?sort=top&t=all '
                                  + r1)

    if message.content.startswith("!pirate"):
        await client.send_file(message.channel,
                               "/server/discord/R1Bot/pirate.png")

    if message.content.startswith("!heure"):
        clem = datetime.datetime.now(timezone('America/Montreal'))
        france = datetime.datetime.now(timezone('Europe/Paris'))
        suede = datetime.datetime.now(timezone('Europe/Stockholm'))
        embed = discord.Embed(title="Heure", color=0xdf0000)
        embed.add_field(name="France", value=france.strftime('%H:%M'),
                        inline=True)
        embed.add_field(name="Québec", value=clem.strftime('%H:%M'),
                        inline=True)
        embed.add_field(name="Suède", value=suede.strftime('%H:%M'),
                        inline=True)
        await client.send_message(message.channel, embed=embed)

    if message.content.startswith("!monnaie ") or message.content.startswith("!mon ") or message.content.startswith("!m ") or message.content.startswith("!écus ") or message.content.startswith("!ecus ") or message.content.startswith("!avoir ") or message.content.startswith("!bourse ") or message.content.startswith("!finance ") or message.content.startswith("!fonds ") or message.content.startswith("!galette ") or message.content.startswith("!pognon ") or message.content.startswith("!billet ") or message.content.startswith("!capital ") or message.content.startswith("!finances ") or message.content.startswith("!fortune ") or message.content.startswith("!recette ") or message.content.startswith("!blé ") or message.content.startswith("!espèces ") or message.content.startswith("!espèce ") or message.content.startswith("!flouze ") or message.content.startswith("!fric ") or message.content.startswith("!papier-monnaie ") or message.content.startswith("!trésor ") or message.content.startswith("!moneyzzz ") or message.content.startswith("!cash ") or message.content.startswith("!mitraille ") or message.content.startswith("!pèze ") or message.content.startswith("!radis ") or message.content.startswith("!grisbi ") or message.content.startswith("!pécule ") or message.content.startswith("!somme ") or message.content.startswith("!buck ") or message.content.startswith("!currency ") or message.content.startswith("!cabbage ") or message.content.startswith("!cheddar ") or message.content.startswith("!clams ") or message.content.startswith("!coins ") or message.content.startswith("!coin ") or message.content.startswith("!bucks ") or message.content.startswith("!bucks ") or message.content.startswith("!cheddar ") or message.content.startswith("!dime ") or message.content.startswith("!dough ") or message.content.startswith("!ducats ") or message.content.startswith("!fins ") or message.content.startswith("!greenbacks ") or message.content.startswith("!lettuce ") or message.content.startswith("!loot ") or message.content.startswith("!lucre ") or message.content.startswith("!moola ") or message.content.startswith("!nickel ") or message.content.startswith("!quarter ") or message.content.startswith("!sawbucks ") or message.content.startswith("!scratch ") or message.content.startswith("!shekels ") or message.content.startswith("!simoleons ") or message.content.startswith("!skrilla ") or message.content.startswith("!smackers ") or message.content.startswith("!spondulix ") or message.content.startswith("!stacks ") or message.content.startswith("!tenners ") or message.content.startswith("!wad ") or message.content.startswith("!wampum ") or message.content.startswith("!avoine ") or message.content.startswith("!artiche ") or message.content.startswith("!balles ") or message.content.startswith("!beurre ") or message.content.startswith("!bifton ") or message.content.startswith("!biftons ") or message.content.startswith("!grisbi ") or message.content.startswith("!carbure ") or message.content.startswith("!douille ") or message.content.startswith("!faf ") or message.content.startswith("!fafiots ") or message.content.startswith("!fourrage ") or message.content.startswith("!maille ") or message.content.startswith("!osier ") or message.content.startswith("!patate ") or message.content.startswith("!ronds ") or message.content.startswith("!thune ") or message.content.startswith("!talbin ") or message.content.startswith("!doublons ") or message.content.startswith("!doublon ") or message.content.startswith("!pépettes ") or message.content.startswith("!pépette ") or message.content.startswith("!green ") or message.content.startswith("!sou ") or message.content.startswith("!sous ") or message.content.startswith("!oseille ") or message.content.startswith("!pécune "):
        dataCanada = requests.get(url='http://free.currencyconverterapi.com/api/v5/convert?q=EUR_CAD&compact=y').json()
        dataSuede = requests.get(url='http://free.currencyconverterapi.com/api/v5/convert?q=EUR_SEK&compact=y').json()
        mCanada = dataCanada["EUR_CAD"]["val"]
        mSuede = dataSuede["EUR_SEK"]["val"]
        if message.content == "!monnaie":
            embed = discord.Embed(title="Valeur des monnaies (1 Euro =)", color=0xdf0000)
            embed.add_field(name="Dollars canadiens", value=mCanada, inline=True)
            embed.add_field(name="Couronnes suédoises", value=mSuede, inline=True)
            await client.send_message(message.channel, embed=embed)
        else:
            mes = message.content.split()
            if len(mes) < 3:
                f1 = mes[1] + " " + "SEK"
                f2 = str(float(mes[1]) / mSuede) + " EUR"
                embed = discord.Embed(title="Conversion", color=0xdf0000)
                embed.add_field(name=f1, value=f2, inline=False)
                await client.send_message(message.channel, embed=embed)
            elif len(mes) < 4:
                dataMonnaie = requests.get(url='http://free.currencyconverterapi.com/api/v5/convert?q=EUR_{}&compact=y'.format(mes[2])).json()
                if dataMonnaie:
                    f1 = mes[1] + " " + mes[2].upper()
                    f2 = str(float(mes[1]) / dataMonnaie["EUR_{}".format(mes[2].upper())]["val"]) + " EUR"
                    embed = discord.Embed(title="Conversion", color=0xdf0000)
                    embed.add_field(name=f1, value=f2, inline=False)
                    await client.send_message(message.channel, embed=embed)
                else:
                    await client.send_message(message.channel, "Monnaie {} invalide".format(mes[2].upper()))
            else:
                dataMonnaie = requests.get(url='http://free.currencyconverterapi.com/api/v5/convert?q={a}_{b}&compact=y'.format(a=mes[3], b=mes[2])).json()
                if dataMonnaie:
                    f1 = mes[1] + " " + mes[2].upper()
                    f2 = str(float(mes[1]) / dataMonnaie["{a}_{b}".format(a=mes[3].upper(), b=mes[2].upper())]["val"]) + " {}".format(mes[3].upper())
                    embed = discord.Embed(title="Conversion", color=0xdf0000)
                    embed.add_field(name=f1, value=f2, inline=False)
                    await client.send_message(message.channel, embed=embed)
                else:
                    await client.send_message(message.channel, "Monnaie {b} ou {b} invalide".format(a=mes[2].upper(), b=mes[3].upper()))

    if message.content.startswith("!hype"):
        embed = discord.Embed(title="Dates à venir", color=0xff1111, url="http://www.jeuxvideo.com/news/1025856/e3-2019-dates-horaires-toutes-les-infos-sur-les-conferences.htm")
        with open('/server/discord/R1Bot/hype.yaml', 'r') as f:
            hypester = yaml.load(f, Loader=yaml.FullLoader)
        for hype in hypester:
            embed.add_field(name=hype['name'], value=datetime.datetime(*hype['date']) - datetime.datetime.now(), inline=True)
        await client.send_message(message.channel, embed=embed)

    if "🦏" in message.content and "🐦" in message.content and "⚡" in message.content and "🐸" in message.content:
        await client.send_file(message.channel, "/server/discord/R1Bot/boys.jpg")


@client.event
async def on_ready():
    await client.change_presence(game=Game(name="Half Life 3"))
    print("Prêt.")


client.run(TOKEN)
