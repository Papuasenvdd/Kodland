from discord import member

from settings import settings
import discord
from bot_logic import gen_pass, gen_emodji, flip_coin

# Переменная intents - хранит привилегии бота
intents = discord.Intents.default()
# Включаем привелегию на чтение сообщений
intents.message_content = True
# Создаем бота в переменной client и передаем все привелегии
client = discord.Client(intents=intents)


@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')


@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('$hello'):
        await message.channel.send("Здравствуй,мой ужин!")
    elif message.content.startswith('$bye'):
        await message.channel.send("Ты можешь бегать, но не сможешь от меня убежать, потому что я пудж!")
    elif message.content.startswith('$smile'):
        await message.channel.send(gen_emodji())
    elif message.content.startswith('$coin'):
        await message.channel.send(flip_coin())
    elif message.content.startswith('$pass'):
        await message.channel.send(gen_pass(10))
    else:
        await message.channel.send("Я не понимаю такую команду!")

        async def on_member_join():
            channel = client.get.channel(1108776196067561562)
            role = discord.utils.get(member.guild.roles, id=1108776196067561562)
            await member.add_roles(role)
            await channel.send(embed=discord.Embed(description=f'Пользователь``{member.name}``, присоединился к нам!',
                                                   color=0x0c0c0c))


client.run("MTEwNDM5OTQwNzIwMzUwNDE3OA.GaqETe.1l2yXb8Z919fsUWMO1cuyYjcOH9njQ4JpvqQEM")


