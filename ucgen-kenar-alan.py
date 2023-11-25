a=int(input('a kenarının uzunluğunu giriniz: '))
b=int(input('b kenarının uzunluğunu giriniz: '))
c=int(input('c kenarının uzunluğunu giriniz: '))

u=(a+b+c)/2
alan=(u*(u-a)*(u-b)*(u-c))**0.5
print('Alan= ',alan)
