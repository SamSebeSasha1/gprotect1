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
                title=f'**Cпасибо что добавил GProtect!**',
                description= f'Спасибо что добавили меню сюда, ведь теперь этот сервер под защитой.\nМой префикс - ``g!``. Для получения списка команд введи ``g!help``.\n\n**Пожалуйста, сделай следующие действия:**\n\n``1.`` Передвинь мою роль как можно выше, чтобы наказывать нарушителей.\n``2.`` Убедись, что у меня есть права администратора для работы.',
                color=0xff0000
            )
        except: pass
        await guild.text_channels[0].send(embed=embed)

@client.event
async def on_guild_join(guild):# при входе бота на сервер
  with open('wl.json','r') as f:
    wls = json.load(f) #вайтлист серверов!
  if int(guild.id) in wls["wl"]:
    async for entry in guild.audit_logs(limit=2,action=disnake.AuditLogAction.bot_add):
        user = entry.user
        iddd = entry.user.id
    for c in guild.text_channels:
      try:
        await c.send(embed=disnake.Embed(title='Данный сервер в чёрном списке!',description=f'Владелец этого сервера - не очень хороший человек, поэтому этот сервер я отказываюсь обслуживать.',colour=disnake.Colour.from_rgb(228,2,0)))
      except:
        pass
      else:
        break
    await guild.leave()
        embed.set_thumbnail(url=guild.icon_url)
        await webhook.send(embed=embed)
      
# Кик
@client.command()
@commands.has_permissions(kick_members = True)

async def kick( ctx, member: disnake.Member, *, reason = None ):
    emb = disnake.Embed(colour = disnake.Color.red() )
    await ctx.channel.purge( limit = 1 )

    await member.kick( reason = reason )
  
    emb.set_author( name = member.name, icon_url = member.avatar_url )
    emb.add_field( name = 'Кик участника', value = 'Кикнутый участник: {}'.format( member.mention ) )

    await ctx.send( embed = emb )

# ошибки для кика
@kick.error
async def kick_error(ctx, error):
  print(error)
  if isinstance(error, commands.MissingPermissions):
    await ctx.reply(embed = disnake.Embed(title=f'Ошибка',description=f'Извини, но у тебя нет прав!\nНужные права: ``kick_members``', colour = disnake.Color.red()))
  
  if isinstance(error, commands.BotMissingPermissions):
    await ctx.reply(embed = disnake.Embed(title=f'Ошибка',description=f'Извини, но у меня нет прав!', colour = disnake.Color.red()))
  
  if isinstance(error, commands.CommandNotFound):
    await ctx.reply(embed = disnake.Embed(title=f'Ошибка',description=f'Извини, но ты не написал команду!', colour = disnake.Color.red()))

  if isinstance(error, commands.UserInputError):
    await ctx.send(embed=disnake.Embed(title = f"Ошибка", description=f"Извини, но ты не правильно написал команду!\nПравильное написание команды: ``g!kick (Участник)``", colour = disnake.Color.red()))

  if isinstance(error, commands.Forbidden):
    await ctx.send(embed=disnake.Embed(title = "Ошибка", description=f"Извини, но у бота нет прав!", colour = disnake.Color.red()))

@client.command( pass_context = True )
@commands.has_permissions( ban_members = True )
async def ban( ctx, member: disnake.Member, *, reason = None ):
    emb = disnake.Embed(colour = disnake.Color.red() )
    await ctx.channel.purge( limit = 1 )

    await member.ban( reason = reason )

    emb.set_author( name = member.name, icon_url = member.avatar_url )
    emb.add_field( name = 'Бан участника', value = 'Забаненный участник : {}'.format( member.mention ) )

    await ctx.send( embed = emb )
  
# ошибки для бана
@ban.error
async def ban_error(ctx, error):
  print(error)
  if isinstance(error, commands.MissingPermissions):
    await ctx.reply(embed = disnake.Embed(title=f'Ошибка',description=f'Извини, но у тебя нет прав!\nНужные права: ``ban_members``', colour = disnake.Color.red()))
  
  if isinstance(error, commands.BotMissingPermissions):
    await ctx.reply(embed = disnake.Embed(title=f'Ошибка',description=f'Извини, но у меня нет прав!', colour = disnake.Color.red()))
  
  if isinstance(error, commands.CommandNotFound):
    await ctx.reply(embed = disnake.Embed(title=f'Ошибка',description=f'Извини, но ты не написал команду!', colour = disnake.Color.red()))

  if isinstance(error, commands.UserInputError):
    await ctx.send(embed=disnake.Embed(title = f"Ошибка", description=f"Извини, но ты не правильно написал команду!\nПравильное написание команды: ``g!ban (Участник)``", colour = disnake.Color.red()))

  if isinstance(error, commands.Forbidden):
    await ctx.send(embed=discord.Embed(title = "Ошибка", description=f"Извини, но у бота нет прав!", colour = discord.Color.red()))

@client.command()
async def help(ctx):
    embed = disnake.Embed(
        title = "?? | Cписок команд",
        description = f"**Информация**\n\n``g!invite`` - Ссылки бота\n``g!user`` - Информация о участнике\n``g!botinfo`` - Информация о боте\n``g!ping`` - Узнать пинг бота\n``g!server`` - Информация о сервере\n\n**Модерация**\n\n``g!ban`` - Заблокировать участника на сервере\n``g!kick`` - Выгнать участника с сервера\n``g!mute`` - Заглушить участника\n``g!unmute`` - Размутить участника\n``g!clear`` - Очистить сообщения\n``g!nick`` - Изменить ник\n\n**Администрация**\n\n``g!massunban`` - Разбанить всех\n``g!delspamroles`` - Удалить повторяющие роли\n``g!delspamchannels`` - Удалить повторяющие каналы\n``g!saytext`` - Отправить сообщение от бота\n``g!create_admin`` - Создать роль админа и выдать ее\n``g!role`` - Выдать роль себе или другому участнику\n\n**Настройка**\n\n``g!wl`` - Список участников в вайт листе\n``g!wl_add`` - Добавить участника в вайт лист\n``g!wl_remove`` - Удалить участника из вайт листа\n\n**Прочее**\n\n``g!avatar`` -  Получить аватар пользователя\n\n**Развлечения**\n\n``g!ball`` - Задать вопрос шару\n``g!game`` - Сыграть в математическую игру с ботом",
        color = 0xff0000 )
    await ctx.send(embed = embed)

@client.event
async def on_guild_channel_create(channel):
    async for entry in channel.guild.audit_logs(
         limit=5, action=discord.AuditLogAction.channel_create):
            embed = disnake.Embed(title=f'Внимание!',description='Непредвиденное создание каналов.',color=0xff0000)
    await guild.text_channels[0].send(embed=embed)

@client.event
async def on_webhook_update(webhook):
    async for entry in webhook.guild.audit_logs(
            limit=5, action=disnake.AuditLogAction.webhook_create):
        embed = disnake.Embed(
        title=f'Попытка краша сервера!',
        description=
        f'Пытался крашнуть {entry.user}. Создание вебхуков!',
        color=0x0059ff)
    if not entry.user.id == client.user.id:
        await webhook.guild.ban(entry.user)

@client.event
async def on_member_join(member):
    if member.id in blacknegr:
        await member.ban(reason="Защита от краш-ботов")
        async for entry in member.guild.audit_logs(
                action=disnake.AuditLogAction.bot_add):
            adder = entry.user
            break
        try:
            await member.guild.ban(adder,
                                   reason="Добавил краш бота",
                                   delete_message_days=1)
        except:
            await member.guild.text_channels[0].send(
                f"<@{member.guild.owner_id}>",
                embed=disnake.Embed(
                    title="Добавили краш-бота",
                    description=f"Советую забанить {adder}, я сам не смог",
                    color=0xff0000))

@client.event
async def on_guild_role_create(ctx, role):
    async for entry in role.ctx.audit_logs(
            limit=3, action=disnake.AuditLogAction.role_create):
        embed = disnake.Embed(title=f'Внимание!',description='Непредвиденное создание ролей.',color=0xff0000)
    await guild.text_channels[0].send(embed=embed)

@client.event
async def on_guild_role_delete(ctx, role):
    async for entry in role.ctx.audit_logs(
            limit=3, action=disnake.AuditLogAction.role_delete):
            embed = disnake.Embed(title=f'Внимание!',description='Непредвиденное удаление ролей.',color=0xff0000)
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

# ошибка для масс ун бан
@massunban.error
async def massunban_error(ctx, error):
  print(error)
  if isinstance(error, commands.MissingPermissions):
    await ctx.reply(embed = disnake.Embed(title=f'Ошибка',description=f'Извини, но у тебя нет прав!\nНужные права: ``administrator``', colour = disnake.Color.red()))
  
  if isinstance(error, commands.BotMissingPermissions):
    await ctx.reply(embed = disnake.Embed(title=f'Ошибка',description=f'Извини, но у меня нет прав!', colour = disnake.Color.red()))
  
  if isinstance(error, commands.CommandNotFound):
    await ctx.reply(embed = disnake.Embed(title=f'Ошибка',description=f'Извини, но ты не написал команду!', colour = disnake.Color.red()))

  if isinstance(error, commands.UserInputError):
    await ctx.send(embed=disnake.Embed(title = f"Ошибка", description=f"Извини, но ты не правильно написал команду!\nПравильное написание команды: ``g!massunban``", colour = disnake.Color.red()))

  if isinstance(error, commands.Forbidden):
    await ctx.send(embed=disnake.Embed(title = "Ошибка", description=f"Извини, но у бота нет прав!", colour = disnake.Color.red()))

@client.command(usage="<member> [reason]")
@commands.has_permissions(manage_messages=True)
async def mute(ctx, member: disnake.Member, *, reason="Вы не указали причину"):
        guild = ctx.guild
        mutedRole = disnake.utils.get(guild.roles, name="Замучен")

        if not mutedRole:
            mutedRole = await guild.create_role(name="Замучен")

            for channel in guild.channels:
                await channel.set_permissions(mutedRole, speak=False, send_messages=False, read_message_history=True,
                                              read_messages=False)
        mute = disnake.Embed(description=f"**Участник отправился в мут.**\n\n"
                                         f"**Модератор:**: {ctx.author.mention}\n"
                                         f"**Участник:**: {member.mention}", colour=discord.Colour.red())
        mute.add_field(name="Причина", value=reason)
        await member.add_roles(mutedRole, reason=reason)
        await ctx.send(embed=mute)

# ошибка для мута
@mute.error
async def mute_error(ctx, error):
  print(error)
  if isinstance(error, commands.MissingPermissions):
    await ctx.reply(embed = disnake.Embed(title=f'Ошибка',description=f'Извини, но у тебя нет прав!\nНужные права: ``manage_messages``', colour = disnake.Color.red()))
  
  if isinstance(error, commands.BotMissingPermissions):
    await ctx.reply(embed = disnake.Embed(title=f'Ошибка',description=f'Извини, но у меня нет прав!', colour = disnake.Color.red()))
  
  if isinstance(error, commands.CommandNotFound):
    await ctx.reply(embed = disnake.Embed(title=f'Ошибка',description=f'Извини, но ты не написал команду!', colour = disnake.Color.red()))

  if isinstance(error, commands.UserInputError):
    await ctx.send(embed=disnake.Embed(title = f"Ошибка", description=f"Извини, но ты не правильно написал команду!\nПравильное написание команды: ``g!mute (Участник) (Причина, необязательно)``", colour = disnake.Color.red()))

  if isinstance(error, commands.Forbidden):
    await ctx.send(embed=disnake.Embed(title = "Ошибка", description=f"Извини, но у бота нет прав!", colour = disnake.Color.red()))

@client.command(usage="<member>")
@commands.has_permissions(manage_messages=True)
async def unmute( ctx, member: disnake.Member):
        mutedRole = disnake.utils.get(ctx.guild.roles, name="Замучен")

        await member.remove_roles(mutedRole)
        unmute = disnake.Embed(description=f"**Участник размучен.**\n\n"
                                           f"**Модератор:** {ctx.author.mention}\n"
                                           f"**Участник:** {member.mention}", colour=disnake.Colour.red())
        await ctx.send(embed=unmute)

# для ун мута ошибка
@unmute.error
async def unmute_error(ctx, error):
  print(error)
  if isinstance(error, commands.MissingPermissions):
    await ctx.reply(embed = disnake.Embed(title=f'Ошибка',description=f'Извини, но у тебя нет прав!\nНужные права: ``manage_messages``', colour = disnake.Color.red()))
  
  if isinstance(error, commands.BotMissingPermissions):
    await ctx.reply(embed = disnake.Embed(title=f'Ошибка',description=f'Извини, но у меня нет прав!', colour = disnake.Color.red()))
  
  if isinstance(error, commands.CommandNotFound):
    await ctx.reply(embed = disnake.Embed(title=f'Ошибка',description=f'Извини, но ты не написал команду!', colour = disnake.Color.red()))

  if isinstance(error, commands.UserInputError):
    await ctx.send(embed=disnake.Embed(title = f"Ошибка", description=f"Извини, но ты не правильно написал команду!\nПравильное написание команды: ``g!unmute (Участник)``", colour = disnake.Color.red()))

  if isinstance(error, commands.Forbidden):
    await ctx.send(embed=disnake.Embed(title = "Ошибка", description=f"Извини, но у бота нет прав!", colour = disnake.Color.red()))

@client.command(pass_context=True, aliases=['clean', 'purge'])
@commands.has_permissions(manage_messages=True)
async def clear(ctx, amount=100):
    channel = ctx.message.channel
    messages = []
    async for message in channel.history(limit=amount + 1):
              messages.append(message)
    await channel.delete_messages(messages)
    govno = disnake.Embed(
          title=f"Очищено {amount} сообщений",
          description=f"**Модератор:** {ctx.author.mention}\n", colour=disnake.Colour.red())
    await ctx.send(embed=govno)

# очистить ошибка
@clear.error
async def clear_error(ctx, error):
  print(error)
  if isinstance(error, commands.MissingPermissions):
    await ctx.reply(embed = disnake.Embed(title=f'Ошибка',description=f'Извини, но у тебя нет прав!\nНужные права: ``manage_messages``', colour = disnake.Color.red()))
  
  if isinstance(error, commands.BotMissingPermissions):
    await ctx.reply(embed = disnake.Embed(title=f'Ошибка',description=f'Извини, но у меня нет прав!', colour = disnake.Color.red()))
  
  if isinstance(error, commands.CommandNotFound):
    await ctx.reply(embed = disnake.Embed(title=f'Ошибка',description=f'Извини, но ты не написал команду!', colour = disnake.Color.red()))

  if isinstance(error, commands.UserInputError):
    await ctx.send(embed=disnake.Embed(title = f"Ошибка", description=f"Извини, но ты не правильно написал команду!\nПравильное написание команды: ``g!clear (Колличество)``", colour = disnake.Color.red()))

  if isinstance(error, commands.Forbidden):
    await ctx.send(embed=disnake.Embed(title = "Ошибка", description=f"Извини, но у бота нет прав!", colour = disnake.Color.red()))

@client.command(pass_context=True)
@commands.has_permissions(manage_nicknames=True)
async def nick(ctx, member: disnake.Member, nick):
    await member.edit(nick=nick)
    govno1 = disnake.Embed(
          title=f"Успех!",
          description=f"Ник {member} успешно изменен на **{nick}** ?\n", colour=disnake.Colour.red())
    await ctx.send(embed=govno1)

# ОШИБКА НИК
@nick.error
async def nick_error(ctx, error):
  print(error)
  if isinstance(error, commands.MissingPermissions):
    await ctx.reply(embed = disnake.Embed(title=f'Ошибка',description=f'Извини, но у тебя нет прав!\nНужные права: ``manage_nicknames``', colour = disnake.Color.red()))
  
  if isinstance(error, commands.BotMissingPermissions):
    await ctx.reply(embed = disnake.Embed(title=f'Ошибка',description=f'Извини, но у меня нет прав!', colour = disnake.Color.red()))
  
  if isinstance(error, commands.CommandNotFound):
    await ctx.reply(embed = disnake.Embed(title=f'Ошибка',description=f'Извини, но ты не написал команду!', colour = disnake.Color.red()))

  if isinstance(error, commands.UserInputError):
    await ctx.send(embed=disnake.Embed(title = f"Ошибка", description=f"Извини, но ты не правильно написал команду!\nПравильное написание команды: ``g!nick (Ник из одного слова)``", colour = disnake.Color.red()))

  if isinstance(error, commands.Forbidden):
    await ctx.send(embed=disnake.Embed(title = "Ошибка", description=f"Извини, но у бота нет прав!", colour = disnake.Color.red()))

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
        title=f'Спам-каналы удалены!',
        description=
        f'Было удалено `{count}` каналов',
        color=0xff0000
    )
    mes = await ctx.send(embed=embed)
    await mes.add_reaction("?")

# дел спам каналы ошибка
@delspamchannels.error
async def delspamchannels_error(ctx, error):
  print(error)
  if isinstance(error, commands.MissingPermissions):
    await ctx.reply(embed = disnake.Embed(title=f'Ошибка',description=f'Извини, но у тебя нет прав!\nНужные права: ``administrator``', colour = disnake.Color.red()))
  
  if isinstance(error, commands.BotMissingPermissions):
    await ctx.reply(embed = disnake.Embed(title=f'Ошибка',description=f'Извини, но у меня нет прав!', colour = disnake.Color.red()))
  
  if isinstance(error, commands.CommandNotFound):
    await ctx.reply(embed = disnake.Embed(title=f'Ошибка',description=f'Извини, но ты не написал команду!', colour = disnake.Color.red()))

  if isinstance(error, commands.UserInputError):
    await ctx.send(embed=disnake.Embed(title = f"Ошибка", description=f"Извини, но ты не правильно написал команду!\nПравильное написание команды: ``g!delspamchannels (Название, но без #)``", colour = disnake.Color.red()))

  if isinstance(error, commands.Forbidden):
    await ctx.send(embed=disnake.Embed(title = "Ошибка", description=f"Извини, но у бота нет прав!", colour = disnake.Color.red()))

@client.command()
async def delspamroles(ctx):
    embed = disnake.Embed(
        title = "Удалить спам роли.",
        description = f"Данная команда была временно отключена.\нnПричина отключения: Плохо работает и нагружает работу бота.",
        color = 0xff0000 )
    await ctx.send(embed = embed)


@client.command()
async def invite(ctx: commands.Context):
  emb = disnake.Embed(
    title = 'Ccылки',
    description= f'[Пригласить бота](https://discord.com/api/oauth2/authorize?client_id=988937426196107274&permissions=8&scope=bot%20applications.commands)\n[Поддержка](https://discord.gg/ztyNN47J2v)',
    color = 0xe74c3c)
  await ctx.send(embed=emb)

@client.command()
async def botinfo(ctx):
    embed = disnake.Embed(
        title = "Информация о боте",
        description = f"> **Профиль бота:** ``{client.user}``\n> **Версия бота:** ``0.4``\n> **Имя бота:** ``{client.user.name}``\n> **ID бота:** ``{client.user.id}``\n> **Владелец бота:** ``SamSebeSasha#0393``\n> **Колличество серверов:** ``{len(client.guilds)}``\n> **Пинг бота:** ``{round(client.latency * 1000)}ms``",
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
                          title=f"Инфо о - {member}")
    embed.set_thumbnail(url=member.avatar_url)
    embed.set_footer(text=f"Вызвал: {ctx.author}")
    embed.add_field(name="ID:", value=member.id)
    embed.add_field(name="Имя:", value=member.display_name)
    embed.add_field(
        name="Создал(а) аккаунт в:",
        value=member.created_at.strftime("%a, %#d %B %Y, %I:%M %p UTC"))
    embed.add_field(
        name="Зашёл(ла) на сервер в:",
        value=member.joined_at.strftime("%a, %#d %B %Y, %I:%M %p UTC"))
    embed.add_field(name="Роли:",
                    value="".join([role.mention for role in roles]))
    embed.add_field(name="Высшая роль:", value=member.top_role.mention)
    print(member.top_role.mention)
    await ctx.send(embed=embed)

@client.command()
async def ping(ctx: commands.Context):
    emb = disnake.Embed(
        description=
        f' **Состояние бота:** \n \n``Ping: {round(client.latency * 1000)} ms.``',
        color= 0xff0000)
    await ctx.send(embed=emb)

@client.command()
async def news(ctx):
    embed = disnake.Embed(
        title = "Новости бота",
        description = f"Пусто",
        color = 0xff0000 )
    embed.set_footer(text = f"Новости о боте узнал, {ctx.author.name}.", icon_url = ctx.author.avatar_url)
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

# ошибкки для сай текст
@saytext.error
async def saytext_error(ctx, error):
  print(error)
  if isinstance(error, commands.MissingPermissions):
    await ctx.reply(embed = disnake.Embed(title=f'Ошибка',description=f'Извини, но у тебя нет прав!\nНужные права: ``administrator``', colour = disnake.Color.red()))
  
  if isinstance(error, commands.BotMissingPermissions):
    await ctx.reply(embed = disnake.Embed(title=f'Ошибка',description=f'Извини, но у меня нет прав!', colour = disnake.Color.red()))
  
  if isinstance(error, commands.CommandNotFound):
    await ctx.reply(embed = disnake.Embed(title=f'Ошибка',description=f'Извини, но ты не написал команду!', colour = disnake.Color.red()))
    
  if isinstance(error, commands.UserInputError):
    await ctx.send(embed=disnake.Embed(title = f"Ошибка", description=f"Извини, но ты не правильно написал команду!\nПравильное написание команды: ``g!saytext (Текст)``", colour = disnake.Color.red()))

  if isinstance(error, commands.Forbidden):
    await ctx.send(embed=disnake.Embed(title = "Ошибка", description=f"Извини, но у бота нет прав!", colour = disnake.Color.red()))

@client.command()
async def avatar(ctx, member: disnake.Member = None):
  if member is None:
    user = ctx.author
  else:
    user = member
  embed = disnake.Embed(title = f"Аватар {user}", color = 0xff0000)
  embed.set_image(url = user.avatar_url)
  await ctx.send(embed = embed)

@client.command()
async def ball(ctx,*,text = None):
    rand = random.choice(["Да","Нет","Хз","Наверное"])
    if text is None:
        embed = disnake.Embed(title="Ошибка",
        description="Вы не правильно написали команду!\nПравильное написание команды: ``g!ball (Вопрос)``")
    else:
        embed = disnake.Embed(title="Шар",
        description=f"""Вопрос: {text}
Ответ: {rand}""",color=disnake.Colour.red())
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
    await ctx.reply(f'Сколько будет {math}? На ответ даётся 15 секунд')
    msg = await client.wait_for('message', timeout = 15)
    if msg.content == str(eval(math)):
        await msg.reply('Правильно!')
    else:
        await msg.reply(f'Не правильно! Ответ: {str(eval(math))}')
@game.error
async def game_error(ctx, err):
    await ctx.send('Время истекло!')



@client.command()
@commands.has_permissions(administrator = True)
async def role(ctx, member: disnake.Member, *, role: disnake.Role):
    await member.add_roles(role)
    await ctx.message.delete()

@role.error
async def role_error(ctx, error):
  print(error)
  if isinstance(error, commands.MissingPermissions):
    await ctx.reply(embed = disnake.Embed(title=f'Ошибка',description=f'Извини, но у тебя нет прав!\nНужные права: ``administrator``', colour = disnake.Color.red()))
  
  if isinstance(error, commands.BotMissingPermissions):
    await ctx.reply(embed = disnake.Embed(title=f'Ошибка',description=f'Извини, но у меня нет прав!', colour = disnake.Color.red()))
  
  if isinstance(error, commands.CommandNotFound):
    await ctx.reply(embed = disnake.Embed(title=f'Ошибка',description=f'Извини, но ты не написал команду!', colour = disnake.Color.red()))
    
  if isinstance(error, commands.UserInputError):
    await ctx.send(embed=disnake.Embed(title = f"Ошибка", description=f"Извини, но ты не правильно написал команду!\nПравильное написание команды: ``g!role (Участник) (Роль)``", colour = disnake.Color.red()))

  if isinstance(error, commands.Forbidden):
    await ctx.send(embed=disnake.Embed(title = "Ошибка", description=f"Извини, но у бота нет прав!", colour = disnake.Color.red()))

@client.command()
async def server(ctx):
    if str(ctx.guild.verification_level) == 'none': vLevel = 'Отсутствует'
    if str(ctx.guild.verification_level) == 'low': vLevel = 'Низкий'
    if str(ctx.guild.verification_level) == 'medium': vLevel = 'Средний'
    if str(ctx.guild.verification_level) == 'high': vLevel = 'Высокий'
    if str(ctx.guild.verification_level) == 'extreme': vLevel = 'Очень высокий'
    emb = disnake.Embed(color = 0xff0000, title = f'Информация о сервере **{ctx.guild.name}**')
    emb.add_field(
        name = 'Участники:',
        value = 'Всего: **{}**\nЛюдей: **{}**\nБотов: **{}**'.format(
            len(ctx.guild.members),
            len([m for m in ctx.guild.members if not m.bot]),
            len([m for m in ctx.guild.members if m.bot])
        )
    )
    emb.add_field(
        name = 'По статусам:',
        value = 'В сети: **{}**\nНе активен: **{}**\nНе беспокоить: **{}**\nНе в сети: **{}**'.format(
            len([m for m in ctx.guild.members if str(m.status) == 'online']),
            len([m for m in ctx.guild.members if str(m.status) == 'idle']),
            len([m for m in ctx.guild.members if str(m.status) == 'dnd']),
            len([m for m in ctx.guild.members if str(m.status) == 'offline'])
        )
    )
    emb.add_field(
        name = 'Каналы:',
        value = 'Всего: **{}**\nТекстовых: **{}**\nГолосовых: **{}**'.format(
            len(ctx.guild.channels),
            len(ctx.guild.text_channels),
            len(ctx.guild.voice_channels)
        )
    )
    emb.add_field(
        name = 'Владелец:',
        value = ctx.guild.owner
    )
    emb.add_field(
        name = 'Уровень проверки:',
        value = vLevel
    )
    emb.add_field(
        name = 'Дата создания:',
        value = '<t:{}:D>'.format(int(time.mktime(ctx.guild.created_at.timetuple())))
    )
    emb.set_footer(text = f'ID: {ctx.guild.id}')
    emb.set_thumbnail(url = ctx.guild.icon_url)
    await ctx.send(embed = emb)
     
@client.command(
   async def on_message(message):
     try:
		link = cursor.execute(f"SELECT * FROM antilink WHERE guild = {message.guild.id}")
			guild = link.fetchall()[0][0]
			chan = cursor.execute(f"SELECT channel FROM exceptchan WHERE id = {message.guild.id}")
			chan = bool(message.channel.id == chan.fetchall()[0][0])
			if(guild == message.guild.id and not message.author.guild_permissions.administrator and not chan):
			if(re.search("https://", message.content) or re.search("http://", message.content) or re.search("discord.gg/", message.content) ):
				await message.delete()
				await message.author.kick(reason = "Ссылка в чате")
	     except IndexError:
               return
  
client.run("OTg4OTM3NDI2MTk2MTA3Mjc0.GgrxO5.VcRJRjAWjTwIWTMroVYuPFyE4Pr-ZflLrAXZTs")
