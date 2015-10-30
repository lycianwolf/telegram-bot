#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  main.py
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
#  
import telegram


botkey = ''
broadcastid = 0

def main():
	bot = telegram.Bot(token=botkey)
	while 1:
		raw_input("Bitte Enter Drücken")
		bot.sendChatAction(chat_id=broadcastid, action=telegram.ChatAction.TYPING) 
		msg = raw_input("Nachricht: ")
		if msg=="poo":
			msg=telegram.Emoji.PILE_OF_POO
		if msg=="exit":
			break
		bot.sendMessage(chat_id=broadcastid, text=msg, parse_mode=telegram.ParseMode.MARKDOWN)
	
if __name__ == '__main__':
	main()

