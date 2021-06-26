import discord
import os
import time

runned = False

client = discord.Client()

token = "ODUzNDExNTM4ODIyODg5NTIy.YMU_bg.jGdR6tJVCUx5DfSrBbmSTMqXms4"

@client.event
async def on_ready():
    print("letssss goooo")

@client.event
async def on_message(msg):
    runned = False
    if msg.author == client.user:
        return
    if msg.content.startswith('£wassup'):
        await msg.channel.send('wassup!')
    if msg.content.startswith('£run'):
        channel = msg.channel
        os.startfile("executor.bat")
        while runned == False:
            with open("run.txt", "r") as running:
                if running.read() == "done":
                    runned = True
                    print(runned)
        with open("results.txt", "r") as file_end:
            r = file_end.read()
            print(r)
        await channel.send(r)
        await channel.send(file=discord.File('result.png'))

client.run(token)
