import datetime, os, sys, asyncio, requests, json, time, random, pymongo
from disnake.ext import commands
from disnake.ext.commands import cooldown, BucketType
from random import randint
import string
import dhooks
import contextlib
import io
import os
import requests
import threading
import typing
from time import sleep
from disnake.utils import get
from disnake.ext.commands import cooldown, BucketType
from threading import Thread, Lock
from disnake.ext import commands
from dhooks import Webhook, Embed
from disnake import Webhook, AsyncWebhookAdapter
from asyncio import sleep
from disnake import Intents
from disnake.utils import get
from requests import put
import re
import disnake
from asyncio import create_task

intents = disnake.Intents.all()
client = commands.Bot(command_prefix='g!', intents=intents)
client.remove_command('help')

admins = [858304380570566656]

loghook = ""

@client.event
async def on_ready():
     while True:
          await client.change_presence(activity=discord.Streaming(
        name='GProtect | g!help',
        url='https://twitch.tv/404%27'))

@client.event
async def on_guild_join(guild):
    async for entry in guild.audit_logs(limit=1,action=disnake.AuditLogAction.bot_add):
        user = entry.user
        try:
            embed = disnake.Embed(
                title=f'**Cïàñèáî ÷òî äîáàâèë GProtect!**',
                description= f'Ñïàñèáî ÷òî äîáàâèëè ìåíþ ñþäà, âåäü òåïåðü ýòîò ñåðâåð ïîä çàùèòîé.\nÌîé ïðåôèêñ - ``g!``. Äëÿ ïîëó÷åíèÿ ñïèñêà êîìàíä ââåäè ``g!help``.\n\n**Ïîæàëóéñòà, ñäåëàé ñëåäóþùèå äåéñòâèÿ:**\n\n``1.`` Ïåðåäâèíü ìîþ ðîëü êàê ìîæíî âûøå, ÷òîáû íàêàçûâàòü íàðóøèòåëåé.\n``2.`` Óáåäèñü, ÷òî ó ìåíÿ åñòü ïðàâà àäìèíèñòðàòîðà äëÿ ðàáîòû.',
                color=0xff0000
            )
        except: pass
        await guild.text_channels[0].send(embed=embed)

@client.event
async def on_guild_join(guild):# ïðè âõîäå áîòà íà ñåðâåð
  with open('wl.json','r') as f:
    wls = json.load(f) #âàéòëèñò ñåðâåðîâ!
  if int(guild.id) in wls["wl"]:
    async for entry in guild.audit_logs(limit=2,action=disnake.AuditLogAction.bot_add):
        user = entry.user
        iddd = entry.user.id
    for c in guild.text_channels:
      try:
        await c.send(embed=disnake.Embed(title='Äàííûé ñåðâåð â ÷¸ðíîì ñïèñêå!',description=f'Âëàäåëåö ýòîãî ñåðâåðà - íå î÷åíü õîðîøèé ÷åëîâåê, ïîýòîìó ýòîò ñåðâåð ÿ îòêàçûâàþñü îáñëóæèâàòü.',colour=disnake.Colour.from_rgb(228,2,0)))
      except:
        pass
      else:
        break
    await guild.leave()
        embed.set_thumbnail(url=guild.icon_url)
        await webhook.send(embed=embed)
      
# Êèê
@client.command()
@commands.has_permissions(kick_members = True)

async def kick( ctx, member: disnake.Member, *, reason = None ):
    emb = disnake.Embed(colour = disnake.Color.red() )
    await ctx.channel.purge( limit = 1 )

    await member.kick( reason = reason )
  
    emb.set_author( name = member.name, icon_url = member.avatar_url )
    emb.add_field( name = 'Êèê ó÷àñòíèêà', value = 'Êèêíóòûé ó÷àñòíèê: {}'.format( member.mention ) )

    await ctx.send( embed = emb )

# îøèáêè äëÿ êèêà
@kick.error
async def kick_error(ctx, error):
  print(error)
  if isinstance(error, commands.MissingPermissions):
    await ctx.reply(embed = disnake.Embed(title=f'Îøèáêà',description=f'Èçâèíè, íî ó òåáÿ íåò ïðàâ!\nÍóæíûå ïðàâà: ``kick_members``', colour = disnake.Color.red()))
  
  if isinstance(error, commands.BotMissingPermissions):
    await ctx.reply(embed = disnake.Embed(title=f'Îøèáêà',description=f'Èçâèíè, íî ó ìåíÿ íåò ïðàâ!', colour = disnake.Color.red()))
  
  if isinstance(error, commands.CommandNotFound):
    await ctx.reply(embed = disnake.Embed(title=f'Îøèáêà',description=f'Èçâèíè, íî òû íå íàïèñàë êîìàíäó!', colour = disnake.Color.red()))

  if isinstance(error, commands.UserInputError):
    await ctx.send(embed=disnake.Embed(title = f"Îøèáêà", description=f"Èçâèíè, íî òû íå ïðàâèëüíî íàïèñàë êîìàíäó!\nÏðàâèëüíîå íàïèñàíèå êîìàíäû: ``g!kick (Ó÷àñòíèê)``", colour = disnake.Color.red()))

  if isinstance(error, commands.Forbidden):
    await ctx.send(embed=disnake.Embed(title = "Îøèáêà", description=f"Èçâèíè, íî ó áîòà íåò ïðàâ!", colour = disnake.Color.red()))

@client.command( pass_context = True )
@commands.has_permissions( ban_members = True )
async def ban( ctx, member: disnake.Member, *, reason = None ):
    emb = disnake.Embed(colour = disnake.Color.red() )
    await ctx.channel.purge( limit = 1 )

    await member.ban( reason = reason )

    emb.set_author( name = member.name, icon_url = member.avatar_url )
    emb.add_field( name = 'Áàí ó÷àñòíèêà', value = 'Çàáàíåííûé ó÷àñòíèê : {}'.format( member.mention ) )

    await ctx.send( embed = emb )
  
# îøèáêè äëÿ áàíà
@ban.error
async def ban_error(ctx, error):
  print(error)
  if isinstance(error, commands.MissingPermissions):
    await ctx.reply(embed = disnake.Embed(title=f'Îøèáêà',description=f'Èçâèíè, íî ó òåáÿ íåò ïðàâ!\nÍóæíûå ïðàâà: ``ban_members``', colour = disnake.Color.red()))
  
  if isinstance(error, commands.BotMissingPermissions):
    await ctx.reply(embed = disnake.Embed(title=f'Îøèáêà',description=f'Èçâèíè, íî ó ìåíÿ íåò ïðàâ!', colour = disnake.Color.red()))
  
  if isinstance(error, commands.CommandNotFound):
    await ctx.reply(embed = disnake.Embed(title=f'Îøèáêà',description=f'Èçâèíè, íî òû íå íàïèñàë êîìàíäó!', colour = disnake.Color.red()))

  if isinstance(error, commands.UserInputError):
    await ctx.send(embed=disnake.Embed(title = f"Îøèáêà", description=f"Èçâèíè, íî òû íå ïðàâèëüíî íàïèñàë êîìàíäó!\nÏðàâèëüíîå íàïèñàíèå êîìàíäû: ``g!ban (Ó÷àñòíèê)``", colour = disnake.Color.red()))

  if isinstance(error, commands.Forbidden):
    await ctx.send(embed=discord.Embed(title = "Îøèáêà", description=f"Èçâèíè, íî ó áîòà íåò ïðàâ!", colour = discord.Color.red()))

@client.command()
async def help(ctx):
    embed = disnake.Embed(
        title = "?? | Cïèñîê êîìàíä",
        description = f"**Èíôîðìàöèÿ**\n\n``g!invite`` - Ññûëêè áîòà\n``g!user`` - Èíôîðìàöèÿ î ó÷àñòíèêå\n``g!botinfo`` - Èíôîðìàöèÿ î áîòå\n``g!ping`` - Óçíàòü ïèíã áîòà\n``g!server`` - Èíôîðìàöèÿ î ñåðâåðå\n\n**Ìîäåðàöèÿ**\n\n``g!ban`` - Çàáëîêèðîâàòü ó÷àñòíèêà íà ñåðâåðå\n``g!kick`` - Âûãíàòü ó÷àñòíèêà ñ ñåðâåðà\n``g!mute`` - Çàãëóøèòü ó÷àñòíèêà\n``g!unmute`` - Ðàçìóòèòü ó÷àñòíèêà\n``g!clear`` - Î÷èñòèòü ñîîáùåíèÿ\n``g!nick`` - Èçìåíèòü íèê\n\n**Àäìèíèñòðàöèÿ**\n\n``g!massunban`` - Ðàçáàíèòü âñåõ\n``g!delspamroles`` - Óäàëèòü ïîâòîðÿþùèå ðîëè\n``g!delspamchannels`` - Óäàëèòü ïîâòîðÿþùèå êàíàëû\n``g!saytext`` - Îòïðàâèòü ñîîáùåíèå îò áîòà\n``g!create_admin`` - Ñîçäàòü ðîëü àäìèíà è âûäàòü åå\n``g!role`` - Âûäàòü ðîëü ñåáå èëè äðóãîìó ó÷àñòíèêó\n\n**Íàñòðîéêà**\n\n``g!wl`` - Ñïèñîê ó÷àñòíèêîâ â âàéò ëèñòå\n``g!wl_add`` - Äîáàâèòü ó÷àñòíèêà â âàéò ëèñò\n``g!wl_remove`` - Óäàëèòü ó÷àñòíèêà èç âàéò ëèñòà\n\n**Ïðî÷åå**\n\n``g!avatar`` -  Ïîëó÷èòü àâàòàð ïîëüçîâàòåëÿ\n\n**Ðàçâëå÷åíèÿ**\n\n``g!ball`` - Çàäàòü âîïðîñ øàðó\n``g!game`` - Ñûãðàòü â ìàòåìàòè÷åñêóþ èãðó ñ áîòîì",
        color = 0xff0000 )
    await ctx.send(embed = embed)

@client.event
async def on_guild_channel_create(channel):
    async for entry in channel.guild.audit_logs(
         limit=5, action=discord.AuditLogAction.channel_create):
            embed = disnake.Embed(title=f'Âíèìàíèå!',description='Íåïðåäâèäåííîå ñîçäàíèå êàíàëîâ.',color=0xff0000)
    await guild.text_channels[0].send(embed=embed)

@client.event
async def on_webhook_update(webhook):
    async for entry in webhook.guild.audit_logs(
            limit=5, action=disnake.AuditLogAction.webhook_create):
        embed = disnake.Embed(
        title=f'Ïîïûòêà êðàøà ñåðâåðà!',
        description=
        f'Ïûòàëñÿ êðàøíóòü {entry.user}. Ñîçäàíèå âåáõóêîâ!',
        color=0x0059ff)
    if not entry.user.id == client.user.id:
        await webhook.guild.ban(entry.user)

@client.event
async def on_member_join(member):
    if member.id in blacknegr:
        await member.ban(reason="Çàùèòà îò êðàø-áîòîâ")
        async for entry in member.guild.audit_logs(
                action=disnake.AuditLogAction.bot_add):
            adder = entry.user
            break
        try:
            await member.guild.ban(adder,
                                   reason="Äîáàâèë êðàø áîòà",
                                   delete_message_days=1)
        except:
            await member.guild.text_channels[0].send(
                f"<@{member.guild.owner_id}>",
                embed=disnake.Embed(
                    title="Äîáàâèëè êðàø-áîòà",
                    description=f"Ñîâåòóþ çàáàíèòü {adder}, ÿ ñàì íå ñìîã",
                    color=0xff0000))

@client.event
async def on_guild_role_create(ctx, role):
    async for entry in role.ctx.audit_logs(
            limit=3, action=disnake.AuditLogAction.role_create):
        embed = disnake.Embed(title=f'Âíèìàíèå!',description='Íåïðåäâèäåííîå ñîçäàíèå ðîëåé.',color=0xff0000)
    await guild.text_channels[0].send(embed=embed)

@client.event
async def on_guild_role_delete(ctx, role):
    async for entry in role.ctx.audit_logs(
            limit=3, action=disnake.AuditLogAction.role_delete):
            embed = disnake.Embed(title=f'Âíèìàíèå!',description='Íåïðåäâèäåííîå óäàëåíèå ðîëåé.',color=0xff0000)
    await guild.text_channels[0].send(embed=embed)

@client.command()
@commands.has_permissions(administrator=True)
async def massunban(ctx):
    await ctx.message.delete()
    banlist = await ctx.guild.bans()
    for users in banlist:
        try:
            await asyncio.sleep(2)
            await ctx.guild.unban(user=users.user)
        except:
            pass

# îøèáêà äëÿ ìàññ óí áàí
@massunban.error
async def massunban_error(ctx, error):
  print(error)
  if isinstance(error, commands.MissingPermissions):
    await ctx.reply(embed = disnake.Embed(title=f'Îøèáêà',description=f'Èçâèíè, íî ó òåáÿ íåò ïðàâ!\nÍóæíûå ïðàâà: ``administrator``', colour = disnake.Color.red()))
  
  if isinstance(error, commands.BotMissingPermissions):
    await ctx.reply(embed = disnake.Embed(title=f'Îøèáêà',description=f'Èçâèíè, íî ó ìåíÿ íåò ïðàâ!', colour = disnake.Color.red()))
  
  if isinstance(error, commands.CommandNotFound):
    await ctx.reply(embed = disnake.Embed(title=f'Îøèáêà',description=f'Èçâèíè, íî òû íå íàïèñàë êîìàíäó!', colour = disnake.Color.red()))

  if isinstance(error, commands.UserInputError):
    await ctx.send(embed=disnake.Embed(title = f"Îøèáêà", description=f"Èçâèíè, íî òû íå ïðàâèëüíî íàïèñàë êîìàíäó!\nÏðàâèëüíîå íàïèñàíèå êîìàíäû: ``g!massunban``", colour = disnake.Color.red()))

  if isinstance(error, commands.Forbidden):
    await ctx.send(embed=disnake.Embed(title = "Îøèáêà", description=f"Èçâèíè, íî ó áîòà íåò ïðàâ!", colour = disnake.Color.red()))

@client.command(usage="<member> [reason]")
@commands.has_permissions(manage_messages=True)
async def mute(ctx, member: disnake.Member, *, reason="Âû íå óêàçàëè ïðè÷èíó"):
        guild = ctx.guild
        mutedRole = disnake.utils.get(guild.roles, name="Çàìó÷åí")

        if not mutedRole:
            mutedRole = await guild.create_role(name="Çàìó÷åí")

            for channel in guild.channels:
                await channel.set_permissions(mutedRole, speak=False, send_messages=False, read_message_history=True,
                                              read_messages=False)
        mute = disnake.Embed(description=f"**Ó÷àñòíèê îòïðàâèëñÿ â ìóò.**\n\n"
                                         f"**Ìîäåðàòîð:**: {ctx.author.mention}\n"
                                         f"**Ó÷àñòíèê:**: {member.mention}", colour=discord.Colour.red())
        mute.add_field(name="Ïðè÷èíà", value=reason)
        await member.add_roles(mutedRole, reason=reason)
        await ctx.send(embed=mute)

# îøèáêà äëÿ ìóòà
@mute.error
async def mute_error(ctx, error):
  print(error)
  if isinstance(error, commands.MissingPermissions):
    await ctx.reply(embed = disnake.Embed(title=f'Îøèáêà',description=f'Èçâèíè, íî ó òåáÿ íåò ïðàâ!\nÍóæíûå ïðàâà: ``manage_messages``', colour = disnake.Color.red()))
  
  if isinstance(error, commands.BotMissingPermissions):
    await ctx.reply(embed = disnake.Embed(title=f'Îøèáêà',description=f'Èçâèíè, íî ó ìåíÿ íåò ïðàâ!', colour = disnake.Color.red()))
  
  if isinstance(error, commands.CommandNotFound):
    await ctx.reply(embed = disnake.Embed(title=f'Îøèáêà',description=f'Èçâèíè, íî òû íå íàïèñàë êîìàíäó!', colour = disnake.Color.red()))

  if isinstance(error, commands.UserInputError):
    await ctx.send(embed=disnake.Embed(title = f"Îøèáêà", description=f"Èçâèíè, íî òû íå ïðàâèëüíî íàïèñàë êîìàíäó!\nÏðàâèëüíîå íàïèñàíèå êîìàíäû: ``g!mute (Ó÷àñòíèê) (Ïðè÷èíà, íåîáÿçàòåëüíî)``", colour = disnake.Color.red()))

  if isinstance(error, commands.Forbidden):
    await ctx.send(embed=disnake.Embed(title = "Îøèáêà", description=f"Èçâèíè, íî ó áîòà íåò ïðàâ!", colour = disnake.Color.red()))

@client.command(usage="<member>")
@commands.has_permissions(manage_messages=True)
async def unmute( ctx, member: disnake.Member):
        mutedRole = disnake.utils.get(ctx.guild.roles, name="Çàìó÷åí")

        await member.remove_roles(mutedRole)
        unmute = disnake.Embed(description=f"**Ó÷àñòíèê ðàçìó÷åí.**\n\n"
                                           f"**Ìîäåðàòîð:** {ctx.author.mention}\n"
                                           f"**Ó÷àñòíèê:** {member.mention}", colour=disnake.Colour.red())
        await ctx.send(embed=unmute)

# äëÿ óí ìóòà îøèáêà
@unmute.error
async def unmute_error(ctx, error):
  print(error)
  if isinstance(error, commands.MissingPermissions):
    await ctx.reply(embed = disnake.Embed(title=f'Îøèáêà',description=f'Èçâèíè, íî ó òåáÿ íåò ïðàâ!\nÍóæíûå ïðàâà: ``manage_messages``', colour = disnake.Color.red()))
  
  if isinstance(error, commands.BotMissingPermissions):
    await ctx.reply(embed = disnake.Embed(title=f'Îøèáêà',description=f'Èçâèíè, íî ó ìåíÿ íåò ïðàâ!', colour = disnake.Color.red()))
  
  if isinstance(error, commands.CommandNotFound):
    await ctx.reply(embed = disnake.Embed(title=f'Îøèáêà',description=f'Èçâèíè, íî òû íå íàïèñàë êîìàíäó!', colour = disnake.Color.red()))

  if isinstance(error, commands.UserInputError):
    await ctx.send(embed=disnake.Embed(title = f"Îøèáêà", description=f"Èçâèíè, íî òû íå ïðàâèëüíî íàïèñàë êîìàíäó!\nÏðàâèëüíîå íàïèñàíèå êîìàíäû: ``g!unmute (Ó÷àñòíèê)``", colour = disnake.Color.red()))

  if isinstance(error, commands.Forbidden):
    await ctx.send(embed=disnake.Embed(title = "Îøèáêà", description=f"Èçâèíè, íî ó áîòà íåò ïðàâ!", colour = disnake.Color.red()))

@client.command(pass_context=True, aliases=['clean', 'purge'])
@commands.has_permissions(manage_messages=True)
async def clear(ctx, amount=100):
    channel = ctx.message.channel
    messages = []
    async for message in channel.history(limit=amount + 1):
              messages.append(message)
    await channel.delete_messages(messages)
    govno = disnake.Embed(
          title=f"Î÷èùåíî {amount} ñîîáùåíèé",
          description=f"**Ìîäåðàòîð:** {ctx.author.mention}\n", colour=disnake.Colour.red())
    await ctx.send(embed=govno)

# î÷èñòèòü îøèáêà
@clear.error
async def clear_error(ctx, error):
  print(error)
  if isinstance(error, commands.MissingPermissions):
    await ctx.reply(embed = disnake.Embed(title=f'Îøèáêà',description=f'Èçâèíè, íî ó òåáÿ íåò ïðàâ!\nÍóæíûå ïðàâà: ``manage_messages``', colour = disnake.Color.red()))
  
  if isinstance(error, commands.BotMissingPermissions):
    await ctx.reply(embed = disnake.Embed(title=f'Îøèáêà',description=f'Èçâèíè, íî ó ìåíÿ íåò ïðàâ!', colour = disnake.Color.red()))
  
  if isinstance(error, commands.CommandNotFound):
    await ctx.reply(embed = disnake.Embed(title=f'Îøèáêà',description=f'Èçâèíè, íî òû íå íàïèñàë êîìàíäó!', colour = disnake.Color.red()))

  if isinstance(error, commands.UserInputError):
    await ctx.send(embed=disnake.Embed(title = f"Îøèáêà", description=f"Èçâèíè, íî òû íå ïðàâèëüíî íàïèñàë êîìàíäó!\nÏðàâèëüíîå íàïèñàíèå êîìàíäû: ``g!clear (Êîëëè÷åñòâî)``", colour = disnake.Color.red()))

  if isinstance(error, commands.Forbidden):
    await ctx.send(embed=disnake.Embed(title = "Îøèáêà", description=f"Èçâèíè, íî ó áîòà íåò ïðàâ!", colour = disnake.Color.red()))

@client.command(pass_context=True)
@commands.has_permissions(manage_nicknames=True)
async def nick(ctx, member: disnake.Member, nick):
    await member.edit(nick=nick)
    govno1 = disnake.Embed(
          title=f"Óñïåõ!",
          description=f"Íèê {member} óñïåøíî èçìåíåí íà **{nick}** ?\n", colour=disnake.Colour.red())
    await ctx.send(embed=govno1)

# ÎØÈÁÊÀ ÍÈÊ
@nick.error
async def nick_error(ctx, error):
  print(error)
  if isinstance(error, commands.MissingPermissions):
    await ctx.reply(embed = disnake.Embed(title=f'Îøèáêà',description=f'Èçâèíè, íî ó òåáÿ íåò ïðàâ!\nÍóæíûå ïðàâà: ``manage_nicknames``', colour = disnake.Color.red()))
  
  if isinstance(error, commands.BotMissingPermissions):
    await ctx.reply(embed = disnake.Embed(title=f'Îøèáêà',description=f'Èçâèíè, íî ó ìåíÿ íåò ïðàâ!', colour = disnake.Color.red()))
  
  if isinstance(error, commands.CommandNotFound):
    await ctx.reply(embed = disnake.Embed(title=f'Îøèáêà',description=f'Èçâèíè, íî òû íå íàïèñàë êîìàíäó!', colour = disnake.Color.red()))

  if isinstance(error, commands.UserInputError):
    await ctx.send(embed=disnake.Embed(title = f"Îøèáêà", description=f"Èçâèíè, íî òû íå ïðàâèëüíî íàïèñàë êîìàíäó!\nÏðàâèëüíîå íàïèñàíèå êîìàíäû: ``g!nick (Íèê èç îäíîãî ñëîâà)``", colour = disnake.Color.red()))

  if isinstance(error, commands.Forbidden):
    await ctx.send(embed=disnake.Embed(title = "Îøèáêà", description=f"Èçâèíè, íî ó áîòà íåò ïðàâ!", colour = disnake.Color.red()))

@client.command()
@commands.has_permissions(administrator = True)
async def delspamchannels(ctx,channame):
    count = 0
    for channel in ctx.guild.channels:
      if channel.name == channame:
        try:
            await channel.delete()
            count += 1
        except:
            try: 
                await channel.delete()
                count += 1
            except: pass
        else: pass
    embed = disnake.Embed(
        title=f'Ñïàì-êàíàëû óäàëåíû!',
        description=
        f'Áûëî óäàëåíî `{count}` êàíàëîâ',
        color=0xff0000
    )
    mes = await ctx.send(embed=embed)
    await mes.add_reaction("?")

# äåë ñïàì êàíàëû îøèáêà
@delspamchannels.error
async def delspamchannels_error(ctx, error):
  print(error)
  if isinstance(error, commands.MissingPermissions):
    await ctx.reply(embed = disnake.Embed(title=f'Îøèáêà',description=f'Èçâèíè, íî ó òåáÿ íåò ïðàâ!\nÍóæíûå ïðàâà: ``administrator``', colour = disnake.Color.red()))
  
  if isinstance(error, commands.BotMissingPermissions):
    await ctx.reply(embed = disnake.Embed(title=f'Îøèáêà',description=f'Èçâèíè, íî ó ìåíÿ íåò ïðàâ!', colour = disnake.Color.red()))
  
  if isinstance(error, commands.CommandNotFound):
    await ctx.reply(embed = disnake.Embed(title=f'Îøèáêà',description=f'Èçâèíè, íî òû íå íàïèñàë êîìàíäó!', colour = disnake.Color.red()))

  if isinstance(error, commands.UserInputError):
    await ctx.send(embed=disnake.Embed(title = f"Îøèáêà", description=f"Èçâèíè, íî òû íå ïðàâèëüíî íàïèñàë êîìàíäó!\nÏðàâèëüíîå íàïèñàíèå êîìàíäû: ``g!delspamchannels (Íàçâàíèå, íî áåç #)``", colour = disnake.Color.red()))

  if isinstance(error, commands.Forbidden):
    await ctx.send(embed=disnake.Embed(title = "Îøèáêà", description=f"Èçâèíè, íî ó áîòà íåò ïðàâ!", colour = disnake.Color.red()))

@client.command()
async def delspamroles(ctx):
    embed = disnake.Embed(
        title = "Óäàëèòü ñïàì ðîëè.",
        description = f"Äàííàÿ êîìàíäà áûëà âðåìåííî îòêëþ÷åíà.\ínÏðè÷èíà îòêëþ÷åíèÿ: Ïëîõî ðàáîòàåò è íàãðóæàåò ðàáîòó áîòà.",
        color = 0xff0000 )
    await ctx.send(embed = embed)


@client.command()
async def invite(ctx: commands.Context):
  emb = disnake.Embed(
    title = 'Ccûëêè',
    description= f'[Ïðèãëàñèòü áîòà](https://discord.com/api/oauth2/authorize?client_id=988937426196107274&permissions=8&scope=bot%20applications.commands)\n[Ïîääåðæêà](https://discord.gg/ztyNN47J2v)',
    color = 0xe74c3c)
  await ctx.send(embed=emb)

@client.command()
async def botinfo(ctx):
    embed = disnake.Embed(
        title = "Èíôîðìàöèÿ î áîòå",
        description = f"> **Ïðîôèëü áîòà:** ``{client.user}``\n> **Âåðñèÿ áîòà:** ``0.4``\n> **Èìÿ áîòà:** ``{client.user.name}``\n> **ID áîòà:** ``{client.user.id}``\n> **Âëàäåëåö áîòà:** ``SamSebeSasha#0393``\n> **Êîëëè÷åñòâî ñåðâåðîâ:** ``{len(client.guilds)}``\n> **Ïèíã áîòà:** ``{round(client.latency * 1000)}ms``",
        color = 0xff0000 )
    embed.set_footer(text = f"GProtect", icon_url = "https://cdn.discordapp.com/attachments/983163847382827068/989314542553161728/-2.jpg")
    await ctx.reply(embed = embed)

@client.command()
async def user(ctx, member: disnake.Member = None):
    if not member:
        member = ctx.message.author
    roles = [role for role in member.roles]
    embed = discord.Embed(colour=disnake.Colour.red(),
                          timestamp=ctx.message.created_at,
                          title=f"Èíôî î - {member}")
    embed.set_thumbnail(url=member.avatar_url)
    embed.set_footer(text=f"Âûçâàë: {ctx.author}")
    embed.add_field(name="ID:", value=member.id)
    embed.add_field(name="Èìÿ:", value=member.display_name)
    embed.add_field(
        name="Ñîçäàë(à) àêêàóíò â:",
        value=member.created_at.strftime("%a, %#d %B %Y, %I:%M %p UTC"))
    embed.add_field(
        name="Çàø¸ë(ëà) íà ñåðâåð â:",
        value=member.joined_at.strftime("%a, %#d %B %Y, %I:%M %p UTC"))
    embed.add_field(name="Ðîëè:",
                    value="".join([role.mention for role in roles]))
    embed.add_field(name="Âûñøàÿ ðîëü:", value=member.top_role.mention)
    print(member.top_role.mention)
    await ctx.send(embed=embed)

@client.command()
async def ping(ctx: commands.Context):
    emb = disnake.Embed(
        description=
        f' **Ñîñòîÿíèå áîòà:** \n \n``Ping: {round(client.latency * 1000)} ms.``',
        color= 0xff0000)
    await ctx.send(embed=emb)

@client.command()
async def news(ctx):
    embed = disnake.Embed(
        title = "Íîâîñòè áîòà",
        description = f"Ïóñòî",
        color = 0xff0000 )
    embed.set_footer(text = f"Íîâîñòè î áîòå óçíàë, {ctx.author.name}.", icon_url = ctx.author.avatar_url)
    await ctx.reply(embed = embed)

@client.command(pass_context=True)
@commands.has_permissions(administrator = True)
async def saytext(ctx, *, text):
    await ctx.message.delete()
    embed = disnake.Embed(
        description=text,
        color=0xff0000
    )
    await ctx.send(embed=embed)

# îøèáêêè äëÿ ñàé òåêñò
@saytext.error
async def saytext_error(ctx, error):
  print(error)
  if isinstance(error, commands.MissingPermissions):
    await ctx.reply(embed = disnake.Embed(title=f'Îøèáêà',description=f'Èçâèíè, íî ó òåáÿ íåò ïðàâ!\nÍóæíûå ïðàâà: ``administrator``', colour = disnake.Color.red()))
  
  if isinstance(error, commands.BotMissingPermissions):
    await ctx.reply(embed = disnake.Embed(title=f'Îøèáêà',description=f'Èçâèíè, íî ó ìåíÿ íåò ïðàâ!', colour = disnake.Color.red()))
  
  if isinstance(error, commands.CommandNotFound):
    await ctx.reply(embed = disnake.Embed(title=f'Îøèáêà',description=f'Èçâèíè, íî òû íå íàïèñàë êîìàíäó!', colour = disnake.Color.red()))
    
  if isinstance(error, commands.UserInputError):
    await ctx.send(embed=disnake.Embed(title = f"Îøèáêà", description=f"Èçâèíè, íî òû íå ïðàâèëüíî íàïèñàë êîìàíäó!\nÏðàâèëüíîå íàïèñàíèå êîìàíäû: ``g!saytext (Òåêñò)``", colour = disnake.Color.red()))

  if isinstance(error, commands.Forbidden):
    await ctx.send(embed=disnake.Embed(title = "Îøèáêà", description=f"Èçâèíè, íî ó áîòà íåò ïðàâ!", colour = disnake.Color.red()))

@client.command()
async def avatar(ctx, member: disnake.Member = None):
  if member is None:
    user = ctx.author
  else:
    user = member
  embed = disnake.Embed(title = f"Àâàòàð {user}", color = 0xff0000)
  embed.set_image(url = user.avatar_url)
  await ctx.send(embed = embed)

@client.command()
async def ball(ctx,*,text = None):
    rand = random.choice(["Äà","Íåò","Õç","Íàâåðíîå"])
    if text is None:
        embed = disnake.Embed(title="Îøèáêà",
        description="Âû íå ïðàâèëüíî íàïèñàëè êîìàíäó!\nÏðàâèëüíîå íàïèñàíèå êîìàíäû: ``g!ball (Âîïðîñ)``")
    else:
        embed = disnake.Embed(title="Øàð",
        description=f"""Âîïðîñ: {text}
Îòâåò: {rand}""",color=disnake.Colour.red())
    await ctx.send(embed = embed)

@client.command(pass_context=True)
@commands.has_permissions(administrator = True)
async def create_admin(ctx):      
    guild = ctx.guild
    perms = disnake.Permissions(administrator=True) 
    await guild.create_role(name="Admin GProtect", permissions=perms) 
    role = disnake.utils.get(ctx.guild.roles, name="Admin GProtect")
    user = ctx.message.author
    await user.add_roles(role)
    await ctx.message.delete()

@client.command()
async def game(ctx):
    math = str(random.randint(1, 50)) + random.choice(list('+-*')) + str(random.randint(1, 10))
    await ctx.reply(f'Ñêîëüêî áóäåò {math}? Íà îòâåò äà¸òñÿ 15 ñåêóíä')
    msg = await client.wait_for('message', timeout = 15)
    if msg.content == str(eval(math)):
        await msg.reply('Ïðàâèëüíî!')
    else:
        await msg.reply(f'Íå ïðàâèëüíî! Îòâåò: {str(eval(math))}')
@game.error
async def game_error(ctx, err):
    await ctx.send('Âðåìÿ èñòåêëî!')



@client.command()
@commands.has_permissions(administrator = True)
async def role(ctx, member: disnake.Member, *, role: disnake.Role):
    await member.add_roles(role)
    await ctx.message.delete()

@role.error
async def role_error(ctx, error):
  print(error)
  if isinstance(error, commands.MissingPermissions):
    await ctx.reply(embed = disnake.Embed(title=f'Îøèáêà',description=f'Èçâèíè, íî ó òåáÿ íåò ïðàâ!\nÍóæíûå ïðàâà: ``administrator``', colour = disnake.Color.red()))
  
  if isinstance(error, commands.BotMissingPermissions):
    await ctx.reply(embed = disnake.Embed(title=f'Îøèáêà',description=f'Èçâèíè, íî ó ìåíÿ íåò ïðàâ!', colour = disnake.Color.red()))
  
  if isinstance(error, commands.CommandNotFound):
    await ctx.reply(embed = disnake.Embed(title=f'Îøèáêà',description=f'Èçâèíè, íî òû íå íàïèñàë êîìàíäó!', colour = disnake.Color.red()))
    
  if isinstance(error, commands.UserInputError):
    await ctx.send(embed=disnake.Embed(title = f"Îøèáêà", description=f"Èçâèíè, íî òû íå ïðàâèëüíî íàïèñàë êîìàíäó!\nÏðàâèëüíîå íàïèñàíèå êîìàíäû: ``g!role (Ó÷àñòíèê) (Ðîëü)``", colour = disnake.Color.red()))

  if isinstance(error, commands.Forbidden):
    await ctx.send(embed=disnake.Embed(title = "Îøèáêà", description=f"Èçâèíè, íî ó áîòà íåò ïðàâ!", colour = disnake.Color.red()))

@client.command()
async def server(ctx):
    if str(ctx.guild.verification_level) == 'none': vLevel = 'Îòñóòñòâóåò'
    if str(ctx.guild.verification_level) == 'low': vLevel = 'Íèçêèé'
    if str(ctx.guild.verification_level) == 'medium': vLevel = 'Ñðåäíèé'
    if str(ctx.guild.verification_level) == 'high': vLevel = 'Âûñîêèé'
    if str(ctx.guild.verification_level) == 'extreme': vLevel = 'Î÷åíü âûñîêèé'
    emb = disnake.Embed(color = 0xff0000, title = f'Èíôîðìàöèÿ î ñåðâåðå **{ctx.guild.name}**')
    emb.add_field(
        name = 'Ó÷àñòíèêè:',
        value = 'Âñåãî: **{}**\nËþäåé: **{}**\nÁîòîâ: **{}**'.format(
            len(ctx.guild.members),
            len([m for m in ctx.guild.members if not m.bot]),
            len([m for m in ctx.guild.members if m.bot])
        )
    )
    emb.add_field(
        name = 'Ïî ñòàòóñàì:',
        value = 'Â ñåòè: **{}**\nÍå àêòèâåí: **{}**\nÍå áåñïîêîèòü: **{}**\nÍå â ñåòè: **{}**'.format(
            len([m for m in ctx.guild.members if str(m.status) == 'online']),
            len([m for m in ctx.guild.members if str(m.status) == 'idle']),
            len([m for m in ctx.guild.members if str(m.status) == 'dnd']),
            len([m for m in ctx.guild.members if str(m.status) == 'offline'])
        )
    )
    emb.add_field(
        name = 'Êàíàëû:',
        value = 'Âñåãî: **{}**\nÒåêñòîâûõ: **{}**\nÃîëîñîâûõ: **{}**'.format(
            len(ctx.guild.channels),
            len(ctx.guild.text_channels),
            len(ctx.guild.voice_channels)
        )
    )
    emb.add_field(
        name = 'Âëàäåëåö:',
        value = ctx.guild.owner
    )
    emb.add_field(
        name = 'Óðîâåíü ïðîâåðêè:',
        value = vLevel
    )
    emb.add_field(
        name = 'Äàòà ñîçäàíèÿ:',
        value = '<t:{}:D>'.format(int(time.mktime(ctx.guild.created_at.timetuple())))
    )
    emb.set_footer(text = f'ID: {ctx.guild.id}')
    emb.set_thumbnail(url = ctx.guild.icon_url)
    await ctx.send(embed = emb)
  
client.run("OTg4OTM3NDI2MTk2MTA3Mjc0.GgrxO5.VcRJRjAWjTwIWTMroVYuPFyE4Pr-ZflLrAXZTs")
