import discord

# Переменная intents - хранит привилегии бота
intents = discord.Intents.all()
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
        await message.channel.send("Привет, мой ужин!")
    elif message.content.startswith('$bye'):
        await message.channel.send("ты можешь бегать но не сможешь от меня убежать потому что я пудж пудж")
    else:
        await message.channel.send(message.content)

        import random


def gen_pass(pass_length):
    elements = "+-/*!&$#?=@<>"
    password = ""

    for i in range(pass_length):
        password += random.choice(elements)

    return password


def gen_emodji():
    emodji = ["\U0001f600", "\U0001f642", "\U0001F606", "\U0001F923"]
    return random.choice(emodji)


client.run("MTEwNDM5OTQwNzIwMzUwNDE3OA.GaqETe.1l2yXb8Z919fsUWMO1cuyYjcOH9njQ4JpvqQEM")


