
"""

 Bir üçgenin iç açıları toplamı 180 derecedir. Kullanıcının girdiği üç açı değerine göre “Bu bir üçgendir.” ya da
 “Bu bir üçgen değildir.” çıktıları veren kodu yazınız.

"""
aci1= int(input('1. AÇI : '))
aci2=int(input('2. AÇI : '))
aci3=int(input('3. AÇI : '))
toplam = aci1 + aci2 + aci3
 
if toplam ==180 :
  print("Bu bir üçgendir")
else:
  print("Bu bir üçgen değildir")




"""
Kullanıcıdan kullanıcı adı ve şifre girilmesi istensin. Kullanıcı adı “Türkiye”; şifre 1923 ise “Giriş başarılı”;
değilse “Kullanıcı adı ya da şifre yanlış” çıktıları veren kodu yazınız.


"""

kadi = input("Kullanıcı adını girin:")
ksifre = input("Kullanıcı şifresi girin:")
 
if kadi == 'Türkiye' and ksifre == '1923' :
  print("Giriş başarılı")
else:
  print("Kullanıcı adı ya da şifre yanlış")



"""
Kullanıcı tarafından girilen hava sıcaklığı 5 °C ve altındaysa “Soğuk”; 6-14 °C arasındaysa “Ilık”;
15 °C ve daha fazlaysa “Sıcak” çıktılarını veren kodu yazınız.

"""
sicaklik=int(input("Sıcaklık Girin(℃):"))
if sicaklik <=5 :
  print("Soğuk")
elif sicaklik <= 14:
  print("Ilık")
else:
  print("Sıcak")



"""
Sayının NEGATIF, POZİTİF yada SIFIR olduğunu yazdıran python programını yazınız.

"""

sayi = input('Sayı : ')
if(int(sayi)<0):
      print("Sayı Negatif")
elif(int(sayi)>0):
      print("Sayı Pozitif")
else:
      print("Sayı Sıfır")
 


"""

Kullanıcının girdiği iki ürünün toplam fiyatı 200 TL ve altıysa “Ödenecek miktar=…. TL”;
200 TL’yi geçerse %25 indirim yaparak “Ödenecek miktar, indirimden sonra ….. TL’dir.” çıktılarını veren kodu yazınız.

"""

urun1=int(input("Birinci ürün fiyatını Giriniz:"))
urun2=int(input("İkinci ürün fiyatını Giriniz:"))
 
toplam=urun1+urun2
 
if(toplam<200):
    print("Ödenecek miktar:",toplam)
else:
    indirim=toplam-(toplam*0.25)
    toplam=toplam-indirim
    print("İndirim miktarı:",indirim)
    print("Ödenecek miktar:",toplam)


"""
Kullanıcıdan iki sınav ve bir performans notu girmesini isteyiniz. Girilen 3 notun ortalaması 50 ve daha büyükse “Başarılı”;
değilse “Başarısız” çıktıları veren kodu yazınız.

"""

not1= int(input('Birin Sınav Notu : '))
not2=int(input('İkinci Sınav Notu : '))
not3=int(input('Performans Notu : '))
ortalama = (not1+not2+not3) / 3
 
if ortalama >=50 :
  print("Başarılı {}".format(ortalama))
else:
  print("Başarısız {}".format(ortalama))
 




"""
Bir hava yolu firması en fazla 20 kilogram bagaj hakkı vermektedir. 20 kilogramdan sonraki her kilogram için 10 TL ek ücret almaktadır.
Buna göre bagajı 20 kg ya da daha az olan yolculara “Herhangi bir ücret ödemeniz gerekmiyor.”;
20 kg’den fazla olanlar için de ne kadar ek ücret ödeneceğini hesaplayarak “Fazla bagaj için ….. TL ödemelisiniz.” çıktılarını veren kodu yazınız.


"""

kilo = int(input("Bagajınızı girin (kg):"))
 
if kilo <=20:
  print("Herhangi bir ücret ödemeniz gerekmiyor")
else:
  ek_kilo  = kilo - 20
  ek_ucret = ek_kilo * 10
  print("Fazla bagaj için {} TL ödemelisiniz.".format(ek_ucret))