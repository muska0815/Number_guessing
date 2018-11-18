import random
a = input('請輸入下限: ')
a = int(a)
b = input('請輸入上限: ')
b = int(b)
r = random.randint(a, b)
n = 0
while True:
	n += 1 # n= n + 1
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
		print('你猜了第', n, '次')
