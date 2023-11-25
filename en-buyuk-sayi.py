print("Üç sayı giriniz: ")
s1=int(input("İlk sayı: "))
s2=int(input("İkinci sayı: "))
s3=int(input("Üçüncü sayı: "))
Enb=s1
if s2 > Enb:
    Enb = s2
if s3 > Enb:
    Enb = s3
print("Girilen sayılardan en büyüğü: ",Enb)
