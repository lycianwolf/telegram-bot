#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  bot.py
#  
#  Copyright 2015 Adrian Pauli <lycian@thuringiafurs.de>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#
#  Base for Telegram Connection from:
#  Simple Bot to reply Telegram messages
#  Copyright (C) 2015 Leandro Toledo de Souza <leandrotoeldodesouza@gmail.com>
#  
#  Daemon Copyright by Sander Marechal:
#  http://www.jejik.com/articles/2007/02/a_simple_unix_linux_daemon_in_python/
#  


import logging
import telegram
import datetime
import sys, time
from daemon import Daemon


LAST_UPDATE_ID = None

class MyDaemon(Daemon):
	def run(self):
			main()

def main():
	botkey = ''
	ownerid = 0
	broadcastid = 0
	
    global LAST_UPDATE_ID
    logging.basicConfig(
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    bot = telegram.Bot(botkey)

    # This will be our global variable to keep the latest update_id when requesting
    # for updates. It starts with the latest update_id if available.
    try:
        LAST_UPDATE_ID = bot.getUpdates()[-1].update_id
    except IndexError:
        LAST_UPDATE_ID = None

    while True:
        echo(bot)

def stammi():
	d=datetime.date.today()
	a=d-datetime.timedelta(days=d.day-1)
	if(a.weekday<=5):
		a=a+datetime.timedelta(weeks=3)+datetime.timedelta(days=5-a.weekday())
	if(a.weekday>5):
		a=a+datetime.timedelta(weeks=3)-datetime.timedelta(days=1)
	if(a<d):
		d=d.replace(month=d.month+1)
		a=d-datetime.timedelta(days=d.day-1)
		if(a.weekday<=5):
			a=a+datetime.timedelta(weeks=3)+datetime.timedelta(days=5-a.weekday())
		if(a.weekday>5):
			a=a+datetime.timedelta(weeks=3)-datetime.timedelta(days=1)
			
	return a

def echo(bot):
    global LAST_UPDATE_ID

    # Request updates after the last updated_id
    for update in bot.getUpdates(offset=LAST_UPDATE_ID, timeout=10):
        # chat_id is required to reply any message
        chat_id = update.message.chat_id
        user = update.message.from_user.username
        message = update.message.text.encode('utf-8')
        if (message):
			if (chat_id == ownerid):
				if (message.startswith("echo")):
					bot.sendMessage(chat_id=,text=message[4:])
				if (message.find("stammi_send")!=-1):
					s_date = stammi()
					message = "Hallo thüringer Fussel.\nDer nächste Stammi ist am "+str(s_date.day)+"."+str(s_date.month)+"."+str(s_date.year)+" ab 14:00"
					bot.sendMessage(chat_id=broadcastid,text=message)
				if (message.find("stammi")!=-1):
					s_date = stammi()
					message = "Hallo thüringer Fussels.\nDer nächste Stammi ist am "+str(s_date.day)+"."+str(s_date.month)+"."+str(s_date.year)+" ab 14:00"
					bot.sendMessage(chat_id=chat_id,text=message)
			if (message.find("mehrstammi")!=-1):
				message = "Der Stammi findet immer im Krautspace, den Vereinsräumen des Hackspace Jena e.V. statt. Wie du da hin kommst findest du [hier](https://kraut.space/raum)"
				bot.sendMessage(chat_id=chat_id,text=message,parse_mode=telegram.ParseMode.MARKDOWN)
			if (message.find("stammi")!=-1):
				s_date = stammi()
				message = "Hallo "+str(user)+".\nDer nächste Stammi ist am "+str(s_date.day)+"."+str(s_date.month)+"."+str(s_date.year)+" ab 14:00"
				bot.sendMessage(chat_id=chat_id,text=message)
			if (message.find("zeit")!=-1):
				message = "Bissu blöde? Schau oben auf die Uhr alter!"
				bot.sendMessage(chat_id=chat_id,text=message)
			# Updates global offset to get the new updates
			print chat_id+" "+message
			LAST_UPDATE_ID = update.update_id + 1


if __name__ == "__main__":
	daemon = MyDaemon('/tmp/echobot.pid')
	if len(sys.argv) == 2:
		if 'start' == sys.argv[1]:
			daemon.start()
		elif 'stop' == sys.argv[1]:
			daemon.stop()
		elif 'restart' == sys.argv[1]:
			daemon.restart()
		else:
			print "Unknown command"
			sys.exit(2)
		sys.exit(0)
        else:
			print "usage: %s start|stop|restart" % sys.argv[0]
			sys.exit(2)
