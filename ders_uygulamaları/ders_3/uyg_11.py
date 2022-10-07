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
 