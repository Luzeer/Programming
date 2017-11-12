a=[]
b=input('Введите числа ')
while b!='':
    a.append(b)
    b=input()
a = [int(a[i]) for i in range(len(a))]
print ('Среднее арифметическое введенных чисел: ', sum(a)/len(a), ' Минимальное число ', min(a), ' Максимальное число ', max(a))
