"""
TEKRAR - 1
Kullanıcıya bir parola belirletirken, belirlenecek parolanın 8 karakterden uzun, 3 karakterden kısa olmamasını sağlayan kod
"""
while True:
    parola = input("Bir parola belirleyin: ")
    if len(parola) > 8 or len(parola) < 3:
        print("parola 8 karakterden uzun 3 karakterden kısa olmamalı")
    else:
        print("Yeni parolanız", parola)
        break


"""
TEKRAR - 2

Klavyeden girilen sayıya kadar olan sayıların toplamını hesaplayan ve sonucu yazdıran python kodunu while döngüsü kullanarak yapan kod
"""
sayac = 0
toplam = 0
bitis=int(input("Bir Sayı Giriniz: "))
while sayac <= bitis:
    sayac = sayac + 1
    toplam = toplam + sayac
print(bitis," saısına kadar olan sayıların toplamı:{0}".format(toplam))



"""
"in" KULLANIMI
"""


print("h" in "abdullah köse") 

print("c" in "abdullah köse")

print("1" in "61539")

print("8" in "61539")

#hata integer değerler arasında 
print(1 in 61539) 



"""
range(başlangıç sayısı,bitiş saysı,artış sayısı) KULLANMI
"""

a=range(0,10)

print (*a)


b=range(0,10,2)

print (*b)

c=range(10,0,-1)

print (*c)

d=range(10,0,-3)

print (*d)






"""
        FOR KOMUTU

for değişken in liste:
    yapılacak_işle


Bu sözdizimini Türkçe olarak şöyle ifade edebiliriz:
liste içindeki her bir öğeyi değişken olarak adlandır:
ve bu öğelerle bir işlem yap.

"""


for k in "nct akademi":
    print(k)



for m in "7632476":
    print(m)

# integer değer liste değildir bunun içinde gezinme yapamaz
for h in 7632476:
    print(h)



"""
FOR RANGE KULLANIMI

Bir sayı listesi içinde gezinme

"""



for i in range(0, 10):
    print(i)


for i in range(3, 20):
    print(i)


for i in range(0, 100,5):
    print(i)

for i in range(10, 0, -1):
    print(i)

for i in range(20, 3, -3):
    print(i)


birinciSayi = int(input("Başlangıç değerini girin:"));
ikinciSayi = int(input("Bitiş Değerini girin :"));
adim = int(input("Artış Miktarını Girin :"));
for i in range(birinciSayi, ikinciSayi, adim):
    print(i)

"""
For-Range Kullanmı
"""


#Ekranda 10 defa isim yazdıran örnek.
for x in range(0,10):
      print("hakan")


#Kullanıcının Girdiği metni ekranda 5 defa yazdıran Python For Döngüsü Örneği

metin=input('Metni Girin : ')
for x in range(10):
      print(metin)


# 100′ e kadar olan çift sayıları listeleyen Python For Döngüsü Örneği


for i in range(1,101):
    if i%2==0:
        print(i)




"""
For İle Kullanıc Girdi Örnekleri
"""

# kullanıcının girdiği 2 sayı arasındaki sayıların toplamını bulan Python For Döngüsü Örneği:

toplam=0;
sayi1=input('1. Sayı: ')
sayi2=input('2. Sayı: ')
for i in range(int(sayi1)+1,int(sayi2)):
    toplam+=i
    print("{0} ile {1} arasındaki sayıların toplamı : {2}".format(sayi1,sayi2,toplam))



#kullanıcının girdiği iki sayı arasındaki sayıları yazdırın

sayi1=input('1. Sayı: ')
sayi2=input('2. Sayı: ')
for i in range(int(sayi1)+1,int(sayi2)):
    print(i)

"""
Karışık Örnekler
"""
#Parola içindeki türkçe karakterleri arama

tr_harfler = "şçöğüİı"

parola = input("Parolanız: ")

for karakter in parola:
    if karakter in tr_harfler:
        print("parolada Türkçe karakter kullanılamaz")



# Bir cümle içerisinde geçen bir harfin kaç defa geçtiğini bulunuz.

yazi="Python üst düzey basit sözdizimine sahip, öğrenmesi oldukça kolay,modülerliği, okunabilirliği desktekeyen, platform bağımsız nesne yönelimliyorumlanabilir bir script dilidir."

harf="a"
sayac=0

for i in yazi:
     if i=="a":
        sayac=sayac+1
print("cümle içerisinde geçen a harfi sayısı: ",sayac)


#Bir cümle içerisinde geçen sesli harfleri bulan kod

yazi="Python üst düzey basit söz dizimine sahip, öğrenmesi oldukça kolay,modülerliği, okunabilirliği destekleyen, platform bağımsız nesne yönelimli yorumlanabilir bir script dilidir."

sesli="aeıioöuü"

for i in yazi:
     if i in sesli:
         print(i,end=",")



#Klavyeden girilen sayıya kadar olan sayılardan tek sayıların toplamını ve çift sayıların toplamını ayrı ayrı bulan python kodunu yazınız.


baslangıc = int(input('Başlangıç Sayı Girin : '))
bitis = int(input('Bitiş  Sayı Girin : '))
tekToplam=0
ciftToplam=0
for i in range(baslangıc,bitis):
      if(i%2==0):
            ciftToplam=ciftToplam+i
      else:
            tekToplam=tekToplam+i
print("Tek Sayıların Toplamı : {0}".format(tekToplam))
print("Çift Sayıların Toplamı : {0}".format(ciftToplam))


# Önceden belirlenen bir liste içerisinde bulunan sayılardan kaç tanesinin 5’in katı olduğunu bulan python kodunu yazınız.



sayilar = [18,15,22,19,85,32,65,30,95,10,12,20,32,55,34,28,101,5,4,32]
sayac=0 
for sayi in sayilar:
   if sayi%5 == 0:
      print (sayi)




