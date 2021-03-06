#!/usr/bin/env python
"""
seen.py - Phenny Seen Module
Copyright 2008, Sean B. Palmer, inamidst.com
Licensed under the Eiffel Forum License 2.

http://inamidst.com/phenny/
"""

#from relativeDates import *
import time

def f_seen(bot, input): 
   """.seen <nick> - Reports when <nick> was last seen."""
   if input.sender == '#talis': return
   if not input.group(2):
      return bot.reply('Harp darp. You homunculus troglodyte, the syntax is: .seen <nick>')
   nick = input.group(2).lower()
   if not hasattr(bot, 'seen'): 
      return bot.reply('?')
   if bot.seen.has_key(nick): 
      channel, t = bot.seen[nick]
      t = time.strftime('%H:%M %d/%m/%Y', time.localtime(t))

      msg = "I last saw %s at %s on %s" % (input.group(2), t, channel)
#      msg = "%s last seen %s" % (input.group(2), timesince(t))
      bot.reply(msg)
   else: bot.reply("Sorry, I haven't seen %s around." % nick)
f_seen.rule = (['seen'], r'(\S+)')

def f_note(bot, input): 
   def note(bot, input): 
      if not hasattr(bot.bot, 'seen'): 
         bot.bot.seen = {}
      if input.sender.startswith('#'): 
         # if origin.sender == '#inamidst': return
         bot.seen[input.nick.lower()] = (input.sender, time.time())

      # if not hasattr(self, 'chanspeak'): 
      #    self.chanspeak = {}
      # if (len(args) > 2) and args[2].startswith('#'): 
      #    self.chanspeak[args[2]] = args[0]

   try: note(bot, input)
   except Exception, e: print e
f_note.rule = r'(.*)'
f_note.priority = 'low'

if __name__ == '__main__': 
   print __doc__.strip()
