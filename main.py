import time
from datetime import datetime
import random
import pyautogui
from pyautogui import hotkey
import pyperclip

userNames = ['elisaalopezs','nikolasagrio', 'gregm.v', 'chemagtzr']
commentsPerHour = 15
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
	pyautogui.typewrite('@'+random.choice(userNames))	

	time.sleep(2)

	pyautogui.typewrite(["enter"])
	pyautogui.typewrite(["enter"])
	pyautogui.typewrite(["enter"])


	now = datetime.now()
	current_time = now.strftime("%H:%M:%S")
	countComment += 1

	print('Comment #', countComment, ' posted at ',current_time)

	time.sleep(commentsPerTime * 60)