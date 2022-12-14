i = 0
while True:
	print(i)

	if i == 5:
		break
	i += 1

print("Program devam ediyor")



"""Örnek1: Break deyiminin kullanımı görmek açısından 1'den 100' e kadar sayıları ekrana yazdırırken, her sayıyı kontrol edelim ve eğer sayı 35 ise döngüden çıkalım."""

 

#while döngüsünden break ile çıkma
i=1
while i<100:
    print(i)
    i=i+1
    if i==35:
        break


"""
Normal şartlarda bu döngü 100'e kadar devam edecekti.
Ancak döngü içinde yer alan if ifadesiyle i 35 olduğunda döngüden çıkıldı.
Break komutu döngüden çıkmak için kullanılır.
"""
"""Burada while ifadesinin yanına True (doğru) yazarsak, sonsuz bir döngüye girmiş olur.
Ve break ifadesiyle yine istediğimiz koşul sağlandığı anda döngüden çıkabiliriz.
"""



# Örnek2: Şimdi kullanıcıya bir sayı girmesini isteyelim ve break komutu kullanarak 1den kullanıcının girdiği sayıya kadar olan sayıları ekrana yazdıralım.

#while döngüsünden break ile çıkma

sayi=int(input("Kaça kadar yazayım sayıları?"))
i=1
while True:
    print(i)
    i=i+1
    if i>sayi:
        break


"""Örnek3:Birlikte sayı bulmaca yapalım.  sayimiz isimli bir değişken tanımlayıp, 1 ile 100 arasında istediğimiz bir sayıyı o değişkene atayalım. Ve kullanıcıya bir sayı girmesini isteyelim. Kullanıcı tuttuğumuz sayıyı yanlış girdiğinde "Yanlış, Bir kez daha dene!" mesajını ekrana yazdıralım. Doğru sayıyı girdiğinde ise ekrana "Tebrikler Kazandınız" şeklinde bir uyarı mesajı yazdıralım.
"""
 

#Sayı bulmaca
print("Hazırsan başlayalım sayı bulmaca oyununa!")
benimsayim=1925
while True:
    sayi=int(input("Sayi Gir"))
    if sayi==benimsayim:
        print("Tebrikler Kazandınız!")
        break
    else:
        print("Yanlış Bir Kez Daha Dene!")







i = 0
while i < 6:
  i += 1
  if i == 3:
    continue
  print(i)




  kullanici_adim="Python"
 
parolam ="1234"
 
giris_hakki=3
 
while giris_hakki>0:
    giris_hakki -=1
 
    kullanici_adi = input("Kullanıcı Adınızı Girin :")
 
    parola = input("Parolayı Giriniz :")
 
    if kullanici_adi==kullanici_adim and parola== parolam:
 
        print("Sisteme başarılı bir şekilde giriş yaptınız.")
 
    else:
 
        print("Kullanıcı bilgileri yanlış tekrar deneyin!")





kullanici_adim="Python"
 
parolam ="1234"
 
giris_hakki=3
 
while giris_hakki>0:
    giris_hakki -=1
    kullanici_adi = input("Kullanıcı Adınızı Girin :")
 
    parola = input("Parolayı Giriniz :")
 
    if kullanici_adi==kullanici_adim and parola== parolam:
 
        print("Sisteme başarılı bir şekilde giriş yaptınız.")
 
        break
 
    else:
 
        print("Kullanıcı bilgileri yanlış tekrar deneyin!")





# 2- Başlangıç ve bitiş değerlerini kullanıcıdan alıp aradaki tüm tek sayıları ekrana yazdırınız.

baslangic = int(input('başlangıç: '))
bitis = int(input('bitiş: '))

i = baslangic

while i < bitis:
    i += 1
    if (i % 2 == 1):
        print(i)

"""3- 1-100 arasındaki sayıları azalan şekilde yazdırınız."""

i = 100
while i > 0:
    print(i)
    i -= 1




# Örnek: Girilen iki sayı arasındaki sayıları toplayan programı while döngüsü ile yazınız.


s1=int(input("Başlangıcı giriniz : "))
s2=int(input("Bitişi giriniz : "))
toplam=0
i = s1
while i <= s2:
  toplam+=i
  i += 1
print(toplam)




a = 4
i = 0
while i<a:
	print(i)
	i+=1
	if i>1:
		break




num = int(input("Enter a number: "))
fac = 1
i = 1
while i <= num:
    fac = fac * i
    i = i + 1
print("Factorial of ", num, " is ", fac)



#Kullanıcıdan 1 ile 5 arasında bir sayı girmesi isteyiniz. Kullanıcı 3 sayısını girdiğinde break komutu ile döngüden çıkılarak “3 sayısı girildi ve döngü sona erdi” çıktısı veren kodu yazınız.
 
while True:
  sayi =input("1-5 arasında bir sayı girin: ")
  if sayi == "3":
    break
 
print("3 sayısı girildi ve döngü sona erdi")
 

"""

 Bu yazıda 60-30 (30 dâhil değil) arasındaki çift sayıları azalan sırada while döngüsü ile ekrana yazdırmayı öğreneceksiniz.
"""

 
i=60 # başlangıç
while i >= 30: #karşılaştırma
    print(i)
    i=i-2  #azaltma