"""
Klavyeden girilen bir sayının 2 ve 3 e veya sadece 2 ye veya sadece 3 e tam bölünüp bölünmediğini yada hiç birine bölünmediğini kontrol eden python kodunu yazınız.
"""



print("-----Girilen Sayının 2 ve 3'e Bölünme Durumu----")
sayi=int(input("Sayı Giriniz: "))
if sayi%2==0 and sayi%3==0:
 print("Girdiğiniz sayı 2 ve 3'e tam bölünüyor.")
if sayi%2==0 and sayi%3!=0:
 print("Girdiğiniz sayı sadece 2'ye tam bölünür.")
if sayi%3==0 and sayi%2!=0:
 print("Girdiğiniz sayı sadece 3'e tam bölünür.")
if sayi%2!=0 and sayi%3!=0:
 print("Girdiğiniz sayı 2 ve 3'e tam bölünmez.")




 """
 0 dan 30’a kadar olan sayılardan 2 ve 3 bölünenleri ekranda sıralayan programın python kodlarını yazınız.
 """

 a=0
while(a<30):
    a=a+1
    if (a%2==0):
        print(a, "2'ye bölünür")
    if (a%3==0):
        print(a, "3'e bölünür")



"""
 0 ile 50 sayısı arasında 4 e bölünen sayıları listeleyen programın python kodlarını yazınız.
"""

a=0
while(a<50):
    a=a+1
    if (a%4==0):
        print(a)




"""
 Klavyeden kullanıcının girdiği ismin kaç harfli olduğunu bulan programın python kodlarını yazınız.
"""

metin=input("Bir ifade giriniz:")
print("----------------------------------")
sayi=len(metin)
print("Girilen ifadenin uzunluğu:",sayi)
