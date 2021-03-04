import datetime

now = datetime.datetime.now()

if now.minute <= 9:
	print (str(now.hour) + ':0' + str(now.minute) + ' do dia ' + str(now.day) + '/' + str(now.month) + '/' + str(now.year))
else:
	print (str(now.hour) + ':' + str(now.minute) + ' do dia ' + str(now.day) + '/' + str(now.month) + '/' + str(now.year))

if now.hour == 21 and now.minute == 48:
	print('FOI PORRA')