

"""
                MODÜL (KÜTÜPHANE)

Modüller(Kütüphane) 2'ye ayrılır

1-Kendi Yazdığımız Modüller
2-Hazır Modüller
--------------------------------------------------------------------------------------------------------------------------------------
1-KENDİ YAZDIĞIMIZ MODÜLLER

Bu işlemi kullanmak için iki python kodu olması gerekir. 

-Birinci kod modül kodu. Bu kodda kullanılması istenilen işlemler fonksiyon olarak tanımlanır. 

-İkinci kod ise yazdığımız kodların olduğu bir python kodudur. Bu python kodunda ise diğer kodda hazırladığımız modül içe aktarılır(import) ve sonra orda yazmış olduğumuz fonksiyonlardan istediğimizi çağırıp bu kodda kullanabiliriz.

!!! bu işlemde dikkat edilmesi gereken konu ise modül kodu iki yerde bulanabilir.
            !! birinci yer: python kodunu yazdığımız klasörle aynı klasörün içinde
            !! ikinci yer: python kurulumunu yaptığımız yerin altında bulunan Lib klasörü içinde (eğer bu konuma kaydedersek her kodda bu modülü kullanabiliriz)
--------------------------------------------------------------------------------------------------------------------------------------
2- HAZIR MODÜLLER

--- Hazır Modüller python’da iki grupta incelenir

- Birinci Grup:
    Pythonı bilgisayarımıza kurduğumuzda direk olarak kurulan modüller (örn; random , math, os , sys vb.)
    !!! Bu modülleri kullanmak için sadece kodumuza "importh modül_adı" ile dahil etmemiz gerekir

- İkinci Grup:
    İnternetten başka kişlerin yazdığı modülleri indirip kullanabiliriz.
    !!! Bu yöntemi kullanmak için gerekli olan modül belirlendikten sonra terminal ekranına (diğer adı komut satırı veya cmd ekranına) şu komutla direk olarak indirip kullanabiliriz. Komut adı ise şöyledir "pip install modül_adı" olarak indirip kullanabiliriz

--------------------------------------------------------------------------------------------------------------------------------------
!!!! MODÜLLERİ İSİM OLARAK KULLANMA

1- import modül_adı

    modül_adı.foksiyon_adı()


2- import modül_adı as kısa_isim

    kısa_isim.fonksiyon_adı()

3- from modül_adı import kullanılacak_fonksiyon (***burda sadece o fonksiyon kullanılabilir modül adını yazmadan***)

    kullanılacak_fonksiyon()

4- from modül_adı import kullanılacak_fonksiyon1 , kullanılacak_fonksiyon1 (***burda sadece o fonksiyonlar kullanılabilir modül adını yazmadan**)

    kullanılacak_fonksiyon1()
    kullanılacak_fonksiyon2()


5- from modül_adı import * (yıldız  işareti koyarsak tüm fonksiyonları kullanabiliriz modül adını yazmadan)

    kullanılacak_fonksiyon1()
    kullanılacak_fonksiyon2()
    kullanılacak_fonksiyon4()
    kullanılacak_fonksiyon5()


"""








"""
****************************************
        KENDİ YAZDIĞIMIZ MODÜLLER
****************************************
"""



"""
örnek-1
-------modül kodu-------(nct.py)
def ornek():
    print("Merhaba Abdullah")   
    
------python kodu-------

import nct

nct.ornek()

"""


"""
örnek-2
-------modül kodu-------(hesaplama.py)
def toplam():
    print(11+3)

def fark():
    print(11-3)  

------python kodu-------

import hesaplama

hesaplama.toplam()
print("merhaba")
hesaplama.fark()

"""

"""
örnek-3
-------modül kodu-------(param.py)
def toplam(a,b):
    print(a+b)

def fark(a,b):
    print(a-b)  

------python kodu-------

import param

param.toplam(15,5)
param.fark(28,3)

"""



"""
örnek-4

-------modül kodu-------(okul.py)

def kayıt(isim, soyisim, işsis, şehir):
    print("-"*30)   
    print("isim           : ", isim)
    print("soyisim        : ", soyisim)
    print("telefon        : ", işsis)
    print("şehir          : ", şehir)   
    print("-"*30)

------python kodu-------

import okul

okul.kayıt("abdullah","köse","05414428683","denizli")

okul.kayıt("yaman","ebecek","05556667788","denizli")

"""



"""
örnek-5

-------modül kodu-------(hesap.py)

def toplam(sayı_1,sayı_2):
    print("toplam:", sayı_1+sayı_2)

def fark(sayı_1,sayı_2):
    print("fark:", sayı_1-sayı_2)

def çarpım(sayı_1,sayı_2):
    print("çarpım:", sayı_1*sayı_2)

def bölüm(sayı_1,sayı_2):
    print("bölüm:", sayı_1/sayı_2)



------python kodu-------

import hesap

sayı_1=int(input("birinci Sayı giriniz"))
sayı_2=int(input("ikinci Sayı giriniz"))
islem=input("işlem seçiniz")

if islem=="+":
    hesap.toplam(sayı_1,sayıı_2)
if islem=="-":
    hesap.fark(sayı_1,sayıı_2)
if islem=="*":
    hesap.çarpım(sayı_1,sayıı_2)
if islem=="/":
    hesap.bölüm(sayı_1,sayıı_2)
else:
    print("yanlış işlem girdiniz")

"""






"""
****************************************
            HAZIR MODÜLLER
****************************************

import time
import random
import math 
import os
import webbrowser
import sys
import turtle

"""
# -----------------TİME--------------------------------------------

"""
# örnek 1 //zamanı gösterme

import time

print(time.localtime()) 
"""

"""
# örnek 2 //zamanı düzenli gösterme

import time

print(time.asctime())
"""

"""
# örnek 3 // bekleme

import time

print("abdullah")

time.sleep(3)

print("köse")

"""
# -----------------RANDOM--------------------------------------------
"""
# örnek 1 //rasgele sayı seçme

import random

print(random.randint(0,50))

"""

"""
# örnek 2 //listeden rastgele seçme

import random

nct=["ayşe","ali","veli","45","12"]

print(random.choice(nct))

"""

"""
# örnek 3 //listeyi karışık sıralama

import random

sayılar = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9,10]

random.shuffle(sayılar)

print(sayılar)

"""


# -----------------MATH--------------------------------------------
"""
# örnek 1 //sayıyı tam sayıya tamamlama 

 **math.ceil()  üst sayıya tamamlar
 **math.floor() alt sayıya tamamlar 

import math

k=35.2

y=74.8

print(math.ceil(k))

print(math.floor(y))
"""

"""
# örnek 2 //faktoriyel hesabı

import math

f = 4

print(math.factorial(f))

"""

"""
# örnek 3 //üst hesaplama , karekök bulma ,

import math

print(math.pow(5,2))

print(math.sqrt(81))

"""


# -----------------OS--------------------------------------------
"""
# örnek 1 // işletim sistemini öğrenme

import os

print(os.name)

** Windows için nt yazar
** Linux-Ubuntu için posix yazar
"""

"""
# örnek 2 //bulunduğumuz dizini gösterme

import os

print(os.getcwd())

"""

"""
# örnek 3 //başka bir dizine geçmek için

import os

os.chdir('C:/Users/Abdullah Köse/Desktop')

print(os.getcwd())

"""

# -----------------WEBBROWSER--------------------------------------------
"""
# örnek 1 // web sayfası açma

import webbrowser 

webbrowser.open("https://tr-tr.facebook.com/")

"""

"""
# örnek 2 // sırayla farklı web sitelerini açma

import webbrowser
import time


webbrowser.open("https://twitter.com/?lang=tr")
time.sleep(4)
webbrowser.open("https://elearning.wsldp.com/python3/python-open-web-browser/")
time.sleep(4)
"""

"""
# örnek 3 // kullanıcıdan alınan ismin sitesini açma (harflari küçük harf yapma)

import webbrowser

url = input("Adres giriniz:")

yeni_url = url.lower()

print(yeni_url)
if yeni_url == "facebook":
    webbrowser.open("https://tr-tr.facebook.com/")

if yeni_url == "google":
    webbrowser.open("https://www.google.com/")

if yeni_url == "youtube":
    webbrowser.open("https://www.youtube.com/")

if yeni_url == "instagram":
    webbrowser.open("https://www.instagram.com/?hl=tr")

"""



# -----------------SYS--------------------------------------------
"""
# örnek 1 // Kurulmuş olan python versiyon öğrenme

import sys

print(sys.version)

"""
"""
# örnek 2 // Kurulmuş olan python hangi işletim sistemine kurulduğunu öğrenme

import sys 

print(sys.platform)

"""
"""
# örnek 3 // Yazmış olduğumuz kodu bitirme(sonlandırma) işlemi

import sys

sayı = input('Bir sayı girin: ')

if int(sayı) < 0:
    print('çıkılıyor...')
    sys.exit()
    print('abdullah')

else:
    print(sayı)

"""