# created by Short-round
# Work with Python 3.6
import discord, os
import datetime
import math

s3 = os.environ['TOKEN']


client = discord.Client()

@client.event
async def on_message(message):
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return

    if message.content.startswith('Hi'):
        msg = 'Fuck you, Dad! I do what I want!'
        await client.send_message(message.channel, msg)
    if message.content.startswith('!ice') or message.content.startswith('!Ice'):
        img = "https://i.imgur.com/2URY60H.jpg"
        await client.send_message(message.channel, img) 
    if message.content.starswith('!test'):
        msg = 'It worked'
        await client.send_message(message.channel, msg)
    
    if message.content.startswith('!fired'):
        msg = incrementFiringCounter()
        await client.send_message(message.channel, msg)
    
    if message.content.startswith('!unfired'):
        msg = decrementFiringCounter()
        await client.send_message(message.channel, msg)

def incrementFiringCounter():
    DATE_FORMAT = '%B %d, %Y at %I:%M%p'
    DATE_START = 'October 12, 2018'

    f = open('cypressCounter','r')
    firedCounter = int(f.readline())
    firedDate = datetime.datetime.strptime(f.readline(),DATE_FORMAT)
    f.close()
    
    newCounter = firedCounter + 1
    newDate = datetime.datetime.now()

    f = open('cypressCounter','w')
    f.write(str(newCounter) + '\n')
    f.write(newDate.strftime(DATE_FORMAT))
    f.close()

    timediff = newDate - firedDate
    days = divmod(timediff.total_seconds(),86400)
    hours = divmod(days[1],3600)
    minutes = divmod(hours[1],60)
    seconds = minutes[1]

    msg = 'Again? Really? That makes {count} people fired since I started counting on {date}\n'.format(count=newCounter,date=DATE_START)
    msg = msg + 'It had been {d} days, {h} hours, {m} minutes, and {s} seconds since the last firing. Oh well.'.format(
        d=math.floor(days[0]),h=math.floor(hours[0]),m=math.floor(minutes[0]),s=math.floor(seconds))
    return msg

def decrementFiringCounter():
    DATE_FORMAT = '%B %d, %Y at %I:%M%p'
    DATE_START = 'October 12, 2018'

    f = open('cypressCounter','r')
    firedCounter = int(f.readline())
    firedDate = datetime.datetime.strptime(f.readline(),DATE_FORMAT)
    f.close()
    
    newCounter = firedCounter - 1
    newDate = datetime.datetime.now()

    f = open('cypressCounter','w')
    f.write(str(newCounter) + '\n')
    f.write(newDate.strftime(DATE_FORMAT))
    f.close()

    msg = 'Wait, what? You rehired someone you fired before? What could possibly go wrong...\n'
    msg = msg + 'I guess there have only been {count} firings since {date} now. Technically.'.format(count=newCounter,date=DATE_START)
    return msg


@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run(s3)
