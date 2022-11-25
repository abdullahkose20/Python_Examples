i = 0
while i < 6:
    i = i + 1
    
    if i == 3:
        continue

    print(i)






# faktöriyel hesaplama

sayı = int(input("Sayı giriniz:"))
fac = 1
i = 1
while i <= sayı:
    fac = fac * i
    i = i + 1
print("sonuc",fac)





# Örnek: Girilen iki sayı arasındaki sayıları toplayan programı while döngüsü ile yazınız.


s1=int(input("Başlangıcı giriniz : "))
s2=int(input("Bitişi giriniz : "))
toplam=0
i = s1
while i <= s2:
  toplam+=i
  i += 1
print(toplam)



"""
Bilgisayar tarafından 1-100 arası rastgele tutulan sayıyı kullanıcının tahmin etmesini isteyen, kullanıcının girdiği sayı tutulan sayıdan küçük ya da büyük olması durumunda yönlendirme yapan, kullanıcının sayıyı bulması durumunda kaçıncı hakkında bildiğini gösteren Python 3 örneği.

Örnek içerisinde while döngüsü kullanımı,if-elif-else kullanımı ve rand fonksiyonu kullanımını görebilirsiniz.
"""

from random import randint

rand = randint(1, 100)
sayac = 0

while True:
    sayac += 1
    sayi = int(input("1 ile 100 arasında değer girin (0 Çıkış):"))
    if (sayi == 0):
        print("Oyunu İptal Ettiniz")
        break
    elif sayi < rand:
        print("Daha Yüksek Bir Sayı Girin.")
        continue
    elif sayi > rand:
        print("Daha Düşük Bir Sayı Girin.")
        continue
    else:
        print("Rastele seçilen sayı {0}!".format(rand))
        print("Tahmin sayınız {0}".format(sayac))