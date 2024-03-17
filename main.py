import time
from datetime import datetime
import random
import pyautogui
from pyautogui import hotkey
import pyperclip

usernames = ['gabolopezs', 'jairacevedo4', 'erickaracely']
phrases = [
	'El mas escuchado es Imagine Dragons y me gustaria ir al concierto con',
	'Es Imagine Dragons!!! espero que ganemos',
	'Obviamente el artista mas escuchado es Imagine Dragons, espero que ganemos',
	'Es Imagine Dragons, vamos o que',
	'El top es imagine dragons, te invito',
	'El mas escuchado es Imagine Dragons y Esta sera nuestra oportunidad?',
]

commentsPerHour = 5
commentsPerTime = round((60/commentsPerHour),2)
countComment = 0

print('------')
print('Actual config...')
print('Post a comments every ', commentsPerTime, 'minute(s)')
print('Comments Per Hour ', round(commentsPerHour, 2))
print('Comments Per Day ', round((commentsPerHour*24),2))
print('------')
print('Starting auto comments...')

time.sleep(4)


while True:
	pyautogui.typewrite(random.choice(phrases)+ ' @'+random.choice(usernames))

	time.sleep(2)
	pyautogui.press("down")
	time.sleep(2)
	pyautogui.typewrite(["enter"])
	time.sleep(2)
	pyautogui.typewrite(["enter"])
	# pyautogui.typewrite(["enter"])


	now = datetime.now()
	current_time = now.strftime("%H:%M:%S")
	countComment += 1

	print('Comment #', countComment, ' posted at ',current_time)

	time.sleep(commentsPerTime * 60)