import random
r = random.randint(0, 100)
while True:
	num = input('請猜數字: ')
	num = int(num)
	if num == r:
		print('恭喜你猜對了')
		break
	else:
		if num > r:
			print('比你小')
		else:
			print('比你大')
