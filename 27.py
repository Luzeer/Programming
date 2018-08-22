M2 = 0
M13 = 0
M26 = 0
MAX = 0
n = int (input())
for i in range (n):
	a = int (input())
	if ((a % 2) == 0) and ((a % 13) > 0) and (a > M2):
		M2 = a
	if ((a % 13) == 0) and ((a % 2) > 0) and (a > M13):
		M13 = a
	if (a % 26 == 0) and (a > M26):
		if M26 > MAX:
			MAX = M26
			M26 = a
	else:
		if a > MAX:
			MAX = a
	print (M2, M13, M26, MAX)
R = int (input())
if (M2*M13 < M26*MAX):
	result = M26*MAX
else:
	result = M2*M13
print('Вычисленное контрольное значение: ', result)
if R == result:
	print ('Контроль пройден')
else:
	print ('Контроль не пройден')
