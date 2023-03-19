from email import message
import logging
import time
import disnake as discord
from disnake.ext.commands.core import command
import requests
import json
import time
import random
import os
import asyncio
import fileinput

from disnake.ext import commands
from disnake import Member
from disnake import utils
from disnake.utils import get
from disnake.ext.commands import Bot
from disnake import Embed


from os import system
from config import config

from musicbot.commands.general import General
from musicbot.commands.music import Music




dir_path = os.path.dirname(os.path.realpath(__file__))

class MyCommands(commands.Cog):
    """Набор самописных комманд.

        Аттрибуты:
            bot: бот, который выполняет команды

    """

    def __init__(self, bot):
        self.bot = bot
        self.path = '{}/playlists/playlists.txt'.format(dir_path)
        self.path_PL = '{}/playlists/PL_NAMES.txt'.format(dir_path)
    



    @commands.command(name='cl', description=config.HELP_CLEAR_LONG, help=config.HELP_CLEAR_SHORT) #Очистка канала .cl [количество сообщений] (очистить нужное кол-во сообщений)// !clear (чистит 100 последних сообщений).
    async def _clear(self, ctx, amount = 100):
        await ctx.channel.purge(limit = amount + 1)



    @commands.command(name="help", description=config.HELP_CMD_LONG, help=config.HELP_CMD_SHORT, aliases=['cmd']) #Список всех команд! !commands
    async def _cmd(self, ctx):
        await ctx.channel.purge(limit=1)
        pages = 4

        emb = discord.Embed(colour=0xf57114, title='🔘Основные команды🔘', description=f"*1/{pages}*")
        emb.add_field(name='`!help`', value=config.HELP_CMD_LONG)
        emb.add_field(name='`!suck`', value=config.HELP_SUCK_LONG)
        emb.add_field(name='`!hello`', value=config.HELP_HELLO_LONG)
        emb.add_field(name='`!ping`', value=config.HELP_PING_LONG)
        emb.add_field(name='`!cl`', value=config.HELP_CL_LONG)
        emb.add_field(name='`!roleinfo`', value=config.HELP_ROLEINFO_LONG)
        emb.add_field(name='`!flip`', value=config.HELP_FLIP_LONG)
        emb.add_field(name='`!roll`', value=config.HELP_ROLL_LONG)
        emb.add_field(name='`!dm`', value=config.HELP_DIRECT_LONG)

        emb1 = discord.Embed(colour=0xf57114, title='🔘Основные команды🔘', description=f"*2/{pages}*")
        emb1.add_field(name='!bigletters', value=config.HELP_BL_LONG)
        
        emb2 = discord.Embed(colour=0xf57114, title='🎵Музыка🎵', description=f"*3/{pages}*")
        emb2.add_field(name='`!cc`', value=config.HELP_CHANGECHANNEL_LONG)
        emb2.add_field(name='`!play`', value=config.HELP_YT_LONG)
        emb2.add_field(name='`!pause`', value=config.HELP_PAUSE_LONG)
        emb2.add_field(name='`!resume`', value=config.HELP_RESUME_LONG)
        emb2.add_field(name='`!skip`', value=config.HELP_SKIP_LONG)
        emb2.add_field(name='`!shuffle`', value=config.HELP_SHUFFLE_LONG)
        emb2.add_field(name='`!loop`', value=config.HELP_LOOP_LONG)
        emb2.add_field(name='`!stop`', value=config.HELP_STOP_LONG)
        emb2.add_field(name='`!queue`', value=config.HELP_QUEUE_LONG)

        emb3 = discord.Embed(colour=0xf57114, title='🎵Музыка🎵', description=f"*4/{pages}*")
        emb3.add_field(name='`!songinfo`', value=config.HELP_SONGINFO_LONG)
        emb3.add_field(name='`!clear`', value=config.HELP_CLEAR_LONG)
        emb3.add_field(name='`!history`', value=config.HELP_HISTORY_LONG)
        
        """
        emb3 = discord.Embed(colour=0xf57114, title='Команды', description=f"*4/{pages}*")
        emb3.add_field(name='!lol', value=config.HELP_CMD_SHORT)
        emb3.add_field(name='!lol', value='Пошли кого-то! [!suck @{nickname}]')
        emb3.add_field(name='!lol', value='Поздоровайся с собеседником! !hello @nickname')
        emb3.add_field(name='!ping', value='Проверить пинг')
        emb3.add_field(name='!clear', value='Очистить чат [!clear {количество_сообщений} или !clear]')
        emb3.add_field(name='!roleinfo', value='Выводит информацию о роли [!roleinfo название_роли]')
        emb3.add_field(name='!flip', value='Кидает монетку (Орел или Решка)')
        emb3.add_field(name='!roll', value='Выдает рандомное число [!roll (0-100), !roll {число} (0-{число})]')
        emb3.add_field(name='!dm', value='Написать человеку в ЛС [!dm @nickname {текст сообщения}')

        emb4 = discord.Embed(colour=0xf57114, title='Команды', description=f"*5/{pages}*")
        emb4.add_field(name='!lol', value=config.HELP_CMD_SHORT)
        emb4.add_field(name='!lol', value='Пошли кого-то! [!suck @{nickname}]')
        emb4.add_field(name='!lol', value='Поздоровайся с собеседником! !hello @nickname')
        emb4.add_field(name='!ping', value='Проверить пинг')
        emb4.add_field(name='!clear', value='Очистить чат [!clear {количество_сообщений} или !clear]')
        emb4.add_field(name='!roleinfo', value='Выводит информацию о роли [!roleinfo название_роли]')
        emb4.add_field(name='!flip', value='Кидает монетку (Орел или Решка)')
        emb4.add_field(name='!roll', value='Выдает рандомное число [!roll (0-100), !roll {число} (0-{число})]')
        emb4.add_field(name='!dm', value='Написать человеку в ЛС [!dm @nickname {текст сообщения}')
        """
        contents = [emb, emb1, emb2, emb3]
        cur_page = 0
        msg = await ctx.send(embed=emb)
        await msg.add_reaction('◀️')
        await msg.add_reaction('▶️')

        def check(reaction, user: discord.Member):
            return user == ctx.message.author and str(reaction.emoji) in ['◀️', '▶️']
        
        while True:
            try:
                reaction, user = await self.bot.wait_for('reaction_add', timeout=60, check=check)

                if str(reaction.emoji) == '▶️' and cur_page != pages-1:
                    cur_page += 1
                    await msg.edit(embed=contents[cur_page])
                    await msg.remove_reaction(reaction, user)

                elif str(reaction.emoji) == '◀️' and cur_page > 0:
                    cur_page -= 1
                    await msg.edit(embed=contents[cur_page])
                    await msg.remove_reaction(reaction, user)

                else:
                    await msg.remove_reaction(reaction, user)
                        
            except asyncio.TimeoutError:
                await msg.delete()
                break
            
        
        


    @commands.command()
    async def _check(self, ctx):
        bot_channel = ctx.guild.voice_client.channel
        print(bot_channel)
        author_channel = ctx.author.voice.channel
        print(author_channel)
        author_channel_msg = ctx.message.author.voice
        print(author_channel_msg)



    @commands.command(name='suck', description=config.HELP_SUCK_LONG, help=config.HELP_SUCK_SHORT, aliases=['fuck'])
    async def _suck(self, ctx, member: Member):
        await ctx.channel.purge(limit=1)
        await ctx.send(f'{member.mention}, соси хуй! :middle_finger:', tts=True) 


    @commands.command(name='hello', description=config.HELP_HELLO_LONG, help=config.HELP_HELLO_SHORT, aliases=['hi', 'привет', 'qq']) #Приветствие !hello
    async def _hello(self, ctx, member:Member,):
        await ctx.channel.purge(limit=1)
        author=ctx.message.author
        await ctx.send(f"{member.mention}, Вам привет от {author.mention}! :wave:")


    @commands.command(name='ping', description=config.HELP_PING_LONG, help=config.HELP_PING_SHORT) #Пинг сервера! !ping
    async def _ping(self, ctx):
        await ctx.channel.purge(limit=1)
        author = ctx.message.author
        before = time.monotonic()
        message = await ctx.send("Pong!")
        ping = (time.monotonic() - before) * 10
        if ping < 60:
            await message.edit(content=f"{author.mention}, твой пинг - '{int(ping)}мс' (:green_circle:)")
        else:
            if ping>61 and ping<100:
                await message.edit(content=f"{author.mention}, твой пинг - '{int(ping)}мс' (:yellow_circle:)")
            else:
                await message.edit(content=f"{author.mention}, твой пинг - '{int(ping)}мс' (:red_circle:)")
        print(f'Ping {int(ping)}ms')



    @commands.command(name='flip', description=config.HELP_FLIP_LONG, help=config.HELP_FLIP_SHORT, aliases=['f'])#подкинуть монетку !flip (выпадает Орел или Решка)
    async def _flip(self, ctx):
        await ctx.channel.purge(limit=1)
        author = ctx.message.author
        ch = random.choice(['Орел', 'Решка'])
        
        if ch == 'Решка':
            message = await ctx.send(f"{author.mention}, вам выпадает: ***{ch}***")
            await message.add_reaction('⚫')
        else:
            message = await ctx.send(f"{author.mention}, вам выпадает: ***{ch}***")
            await message.add_reaction('⚪')


    @commands.command(name='roll', description=config.HELP_ROLL_LONG, help=config.HELP_ROLL_SHORT, aliases=['random'])#Выбрать рандомное число !roll (0-100) // !role {число} (0-число)
    async def _roll(self, ctx, limit=100):
        author = ctx.message.author
        x = limit
        r = random.randint(0, x)
        await ctx.send(f"{author.mention}, ваше число: *{r}*")


    @commands.command(name='direct', description=config.HELP_DIRECT_LONG, help=config.HELP_DIRECT_SHORT, aliases=['dm', 'd', 'ls']) #Отправить сообщение в лс !dm @nickname {Сообщение}
    async def _dm(self, ctx, member: Member, *, text):
        msg=text
        await ctx.channel.purge(limit=1)
        author = ctx.message.author
        await member.send(f"*{author.mention} нежно шепнул вам на ушко:* ' {msg} '")


    @commands.command(name='dog', description=' ', brief=' ', aliases=['mem'])
    async def _dog(self, ctx):
        dog = discord.Embed(colour = 0xf57114, title = ':dog:', description = config.MEM_DOG)
        await ctx.send(embed = dog)


    @commands.command()
    async def hack(self, ctx):
        await ctx.channel.purge(limit=1)
        emojis = ['✔', '❌']
        i=0
        hack_agree = discord.Embed(colour = 0xf57114, title='📡HACKING📡', description = "Вы точно хотите взломать данный сервер?")
        mg = await ctx.send(embed=hack_agree)
        await mg.add_reaction('❌')
        await mg.add_reaction('✔')


        def check(reaction, user):
            return user == ctx.message.author and str(reaction.emoji) in emojis

        while True:
            try:
                reaction, user = await self.bot.wait_for('reaction_add', check=check)
                
                if str(reaction.emoji) == '✔':

                    await ctx.channel.purge(limit=1)
                    emb_hack = discord.Embed(colour=0xf57114, title='📡HACKING📡', description=f"Запускается процесс взлома сервера!")
                    msg = await ctx.send(embed=emb_hack)
                    await asyncio.sleep(2)

                    while i < 100:
                        try:
                            i = i + 1
                            
                            if i !=100:
                                hack_embed = discord.Embed(colour=0xf57114, title="📡HACKING📡", description=f"Взлом сервера завершен на **{i}%**")
                                await msg.edit(embed=hack_embed)
                            elif i>100:
                                hack_embed1 = discord.Embed(colour=0xf57114, title="📡HACKING📡", description=f"Взлом сервера завершен на 100%")
                                await msg.edit(embed=hack_embed1)
                            else:
                                await ctx.channel.purge(limit=1)
                                end_emb= discord.Embed(colour=0xf57114, title="📡HACKING📡", description=f"Сервер взломан!")
                                message = await ctx.send(embed=end_emb)
                                await message.add_reaction('🙈')
                                await message.add_reaction('🙉')
                                await message.add_reaction('🙊')

                        except:
                            break
                
                else:
                    await ctx.channel.purge(limit=1)
                    cancel_hack = discord.Embed(colour=0xf57114, title='📡HACKING📡', description='Взлом сервера отменен!')
                    await ctx.send(embed=cancel_hack)
                    break
            except:
                await msg.delete()
                break




    @commands.command(name = 'play', description=config.HELP_YT_LONG, help=config.HELP_YT_SHORT, aliases=['p', 'yt', 'P'])
    async def _play_song_mine(self, ctx, *, track:str):
        track_name=track
        bot_channel = ctx.guild.voice_client.channel
        author_channel = ctx.author.voice.channel
        author_channel_msg = ctx.message.author.voice.channel
        if bot_channel != author_channel:
            await ctx.invoke(self.bot.get_command('changechannel'))
            await ctx.invoke(self.bot.get_command('testplay'), track = track_name)
        elif bot_channel is None:
            await ctx.invoke(self.bot.get_command('connect'))
            await ctx.invoke(self.bot.get_command('testplay'), track = track_name)
        else:
            await ctx.invoke(self.bot.get_command('testplay'), track = track_name)




### БОЛЬШИЕ БУКВЫ ###

    @commands.command(name = 'bigletters', description = config.HELP_BL_SHORT, help = config.HELP_BL_LONG, aliases=['bl', 'big', 'biglet'])
    async def _big_letters(self, ctx, *, text):
        dic = {'A':':regional_indicator_a:', 'a':':regional_indicator_a:', 'B':':regional_indicator_b:', 'b':':regional_indicator_b:', 'C':':regional_indicator_c:', 'c':':regional_indicator_c:',
            'D':':regional_indicator_d:', 'd':':regional_indicator_d:', 'E':':regional_indicator_e:', 'e':':regional_indicator_e:', 'F':':regional_indicator_f:', 'f':':regional_indicator_f:',
            'G':':regional_indicator_g:', 'g':':regional_indicator_g:', 'H':':regional_indicator_h:', 'h':':regional_indicator_h:', 'I':':regional_indicator_i:', 'i':':regional_indicator_i:',
            'J':':regional_indicator_j:', 'j':':regional_indicator_j:', 'K':':regional_indicator_k:', 'k':':regional_indicator_k:', 'L':':regional_indicator_l:', 'l':':regional_indicator_l:',
            'M':':regional_indicator_m:', 'm':':regional_indicator_m:', 'N':':regional_indicator_n:', 'n':':regional_indicator_n:', 'O':':regional_indicator_o:', 'o':':regional_indicator_o:',
            'P':':regional_indicator_p:', 'p':':regional_indicator_p:', 'Q':':regional_indicator_q:', 'q':':regional_indicator_q:', 'R':':regional_indicator_r:', 'r':':regional_indicator_r:',
            'S':':regional_indicator_s:', 's':':regional_indicator_s:', 'T':':regional_indicator_t:', 't':':regional_indicator_t:', 'U':':regional_indicator_u:', 'u':':regional_indicator_u:',
            'V':':regional_indicator_v:', 'v':':regional_indicator_v:', 'W':':regional_indicator_w:', 'w':':regional_indicator_w:', 'X':':regional_indicator_x:', 'x':':regional_indicator_x:',
            'Y':':regional_indicator_y:', 'y':':regional_indicator_y:', 'Z':':regional_indicator_z:', 'z':':regional_indicator_z:',
            '0':':zero:', '1':':one:', '2':':two:', '3':':three:', '4':':four:', '5':':five:', '6':':six:', '7':':seven:', '8':':eight:', '9':':nine:', ' ':'  '}
    
        alphabet = ['A', 'a', 'B', 'b', 'C', 'c', 'D', 'd', 'E', 'e', 'F', 'f', 'G', 'g', 'H', 'h', 'I', 'i', 'J', 'j', 
                    'K', 'k', 'L', 'l', 'M', 'm', 'N', 'n', 'O', 'o', 'P', 'p', 'Q', 'q', 'R', 'r', 'S', 's', 'T', 't', 'U', 'u', 
                    'V', 'v', 'W', 'w', 'X', 'x', 'Y', 'y', 'Z', 'z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', ' ']

        await ctx.channel.purge(limit=1)
        st = str(text)
        result = str()

        len_st = len(st)
        for i in range(0, len_st):
            if st[i] in alphabet:
                simb = dic[st[i]]
            else:
                simb = st[i]
            result = result + simb
        await ctx.send(result)

### ПОЦЕЛУЙ ###

    @commands.command(name = 'kiss', desription = config.HELP_KISS_SHORT, help = config.HELP_KISS_LONG, aliases = ['kisses', 'cmok', 'цомк', 'целую', 'поцеловать'])
    async def _kiss(self, ctx, member: Member):

        state_imgs = [
        "https://i.gifer.com/1JN.gif",
        "https://i.gifer.com/1Ve.gif",
        "https://i.gifer.com/Aq.gif",
        "https://i.gifer.com/T0lE.gif",
        "https://i.gifer.com/PCUi.gif",
        "https://i.gifer.com/2uEt.gif",
        "https://i.gifer.com/2lte.gif",
        "https://i.gifer.com/T0lE.gif",
        "https://i.gifer.com/XrqL.gif",
        "https://i.gifer.com/gZ2.gif",
        "https://i.gifer.com/55UX.gif",
        "https://i.gifer.com/24jg.gif",
        "https://i.gifer.com/3h0f.gif",
        "https://i.gifer.com/FChS.gif",
        "https://i.gifer.com/36KV.gif",
        "https://cdn.weeb.sh/images/rJ6PWohA-.gif",
        "https://i.gifer.com/9Gd2.gif"
        ]

        imgs = []
        
        await ctx.channel.purge(limit=1)
        author = ctx.message.author

        print ("Список imgs: ")
        print (imgs)
        print ("Список state_imgs: ")
        print (state_imgs)

        imgs.extend(state_imgs)
        print ("Список imgs после добавления: ")
        print (imgs)

        elements_in_imgs = len(imgs)
        print (f"Количество элементов в списке imgs = {elements_in_imgs}")

        if elements_in_imgs > 0:

            print("количество элеметов > 0")

            if author == member:
                img_url = random.choice(imgs)
                emb = discord.Embed(colour=0xf57114, description=f"**{author.mention}** поцеловал сам себя! Каков эгоист😏")
                emb.set_image(url = img_url)
                imgs.remove(img_url)
                await ctx.send(embed = emb)
            else:
                img_url = random.choice(imgs)
                emb = discord.Embed(colour=0xf57114, description=f"**{author.mention}** целует **{member.mention}**")
                emb.set_image(url = img_url)
                imgs.remove(img_url)
                await ctx.send(embed = emb)
        else:
            print ("Количество элементов = 0")
            imgs.extend(state_imgs)
            print (f"список imgs после функции Else: {imgs}")

"""
    @commands.Cog.listener()
    async def on_raw_reaction_add(self, payload):

        Channel = self.bot.get_channel(payload.channel_id)
        message = await Channel.fetch_message(payload.message_id)
        x = self.bot.get_channel(837800327990214666)
        guild = self.bot.get_guild(payload.guild_id)
        reaction = discord.utils.get(message.reactions, emoji=payload.emoji.name)
        New = discord.utils.get(guild.roles, id = 838180435929727024)
        Meeting_chat = self.bot.get_channel(837801306721747015)

        if x != Channel:
            print("wrong channel")
            return

        #мужчины
        elif payload.emoji.name == "🕺":
            Man = discord.utils.get(guild.roles, name = 'Мужчины')
            await payload.member.add_roles(Man)
            print("Выдана роль:")
            print(Man)
            await payload.member.remove_roles(New)
            print("Удалена роль:")
            print(New)

        #Девушки
        elif payload.emoji.name == "💃":
            Woman = discord.utils.get(guild.roles, name  = 'Девушки')
            await payload.member.add_roles(Woman)
            print("Выдана роль:")
            print(Woman)
            await payload.member.remove_roles(New)
            print("Удалена роль:")
            print(New)
            #await Meeting_chat.send(config.MEETING_CHANNEL_PHRASE + f"**{payload.member}**")

        #пользовательская реакция
        else:
            await reaction.remove(payload.member)
            print("Пользовательская реакция удалена")
            return

"""
"""
    @commands.command()
    async def _meeting(self, ctx):
        Channel = self.bot.get_channel(837800327990214666)
        Text = discord.Embed(color=0xf57114, title='**Добро пожаловать домой!**', description=f'Рады видеть тебя у нас дома!\n\nЗдесь мы:\n:thought_balloon: | Общаемся\n:video_game: | Играем в игры\n:film_frames: | Смотрим видео\n:microphone2: | Стримим\n:headphones: | Слушаем музыку\n\nВ общем, весело проводим время.\n\nПрежде, чем начать общение укажи свой пол!\n\n:man_dancing: - Мужчина\n:dancer: - Девушка\n\n*(Нажми на реакцию)*')
        Moji = await ctx.send(embed = Text)
        await Moji.add_reaction('🕺')
        await Moji.add_reaction('💃')
"""

"""
    @commands.command(pass_context=True)
    async def get_roles(ctx):
        all_roles = []
        for role in ctx.guild.roles:
            all_roles.append(role.name)
        all_roles.reverse()# to make it higher first 
        print(all_roles)
"""


def setup(bot):
    bot.add_cog(MyCommands(bot))

