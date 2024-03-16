import time
from datetime import datetime
import random
import pyautogui
from pyautogui import hotkey
import pyperclip

userNames = ['amigo1','amigo2']
phrases = [
	'Me gustaria ir al concierto',
	'Yo iria al concierto con',
	'Si gano invitaria a',
	'Vamos',
	'Super jalo si gano te invito',
	'Esta sera nuestra oportunidad?',
]

commentsPerHour = 240
commentsPerTime = round((60/commentsPerHour),2)
countComment = 0

print('------')
print('Actual config...')
print('Post a comments every ', commentsPerTime, 'minute(s)')
print('Comments Per Hour ', round((commentsPerHour),2))
print('Comments Per Day ', round((commentsPerHour*24),2))
print('------')
print('Starting auto comments...')

time.sleep(4)


while True:
	pyautogui.typewrite(random.choice(phrases)+ ' @'+random.choice(userNames))

	time.sleep(1)

	pyautogui.typewrite(["enter"])
	# pyautogui.typewrite(["enter"])
	# pyautogui.typewrite(["enter"])


	now = datetime.now()
	current_time = now.strftime("%H:%M:%S")
	countComment += 1

	print('Comment #', countComment, ' posted at ',current_time)

	# time.sleep(commentsPerTime * 60)
	time.sleep(2)