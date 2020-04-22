import discord

 
client = discord.Client()
 
@client.event
async def on_ready():
    print('BOT ONLINE - OLÁ MUNDO')
    print(client.user.name)
    print(client.user.id)
    print('-----PR------')
 
 
@client.event
async def on_message(message):
    message.content = message.content.lower()
    if message.author == client.user:
        return
    if message.content.startswith("pergunta"):
        await message.channel.send("resposta!!!")
 







client.run('token')