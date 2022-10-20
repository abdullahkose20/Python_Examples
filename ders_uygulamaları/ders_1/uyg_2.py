"""
Bir otoparkın ücret tarifesi aşağıdaki gibidir:

1 saate kadar: 5 TL
1-5 saat arası: Saat başı 4 TL
5 saatten fazla: Saat başı 3 TL
Bakınız: Python if else Kullanımı

Buna göre kullanıcının girdiği otoparkta kalınan saat süresine göre ödenecek miktarı bularak ekrana yazdırınız.

"""

saat=int(input(" Kaldığınız Süreyi Girin:"))
 
ucret=0
 
if saat <=1 :
  ucret = 5
elif saat <= 5:
  ucret = 4 * saat
else:
  ucret = 3*saat
 
print("Ödemeniz Gereken Ücret :{}".format(ucret))






"""
Kullanıcın girdiği iki sayıyı karşılaştırarak sayı sayıdan büyüktür, küçüktür veya sayılar eşittir mesajı veren kodları sadece “if” koşul yapısını kullanarak yazınız.

"""

sayi1= int(input('1. sayıyı giriniz: '))
sayi2= int(input('2. sayıyı giriniz: '))
 
if sayi1>sayi2:
    print('1. sayı 2. sayıdan büyüktür.')
elif sayi1<sayi2:
    print ('1.sayi 2. sayıdan küçüktür.')
else: 
    print ('Sayılar eşittir.')







"""
Beden kitle endeksini kilo/(boy**2) formülü ile hesaplanarak bireyin kilo durumunu kontrol eden programın kodlarını aşağıdaki aralık durumlarına göre yazınız.

Kitle Endeksi (KE) < 18.5 ise Zayıf,
18.5 < (KE) <=25 ise Normal,
25 < (KE) <= 30 ise Kilolu, (KE) > 25 ise birey obez sınıfına girmektedir.

"""


boy = float(input("Boyunuzu Giriniz '(m)': Örnek 1.73----:"))
kilo = float(input("Kilonuzu Giriniz '(kg)': Örnek: 78----:"))
 
endeks = kilo/(boy**2)
 
if endeks<18.5:
    print("Zayıfsınız")
elif endeks > 18.5 and endeks <=25 :
    print("Normalsiniz")
elif endeks > 25 and endeks <=30:
    print("Kilolusunuz")
elif endeks > 30:
    print("Dikkat! obezsiniz")




"""
Problem 1
Kullanıcıdan alınan boy ve kilo değerlerine göre beden kitle indeksini hesaplayın ve şu kurallara göre ekrana şu yazıları yazdırın.

 Beden Kitle İndeksi: Kilo / Boy(m) *  Boy(m)

 BKİ 18.5'un altındaysa -------> Zayıf

 BKİ 18.5 ile 25 arasındaysa ------> Normal

 BKİ 25 ile 30 arasındaysa --------> Fazla Kilolu

 BKİ 30'un üstündeyse -------------> Obez

"""
boy = float(input("Boyunuzu Giriniz:"))
kilo = int(input("Kilonuzu Giriniz:"))

bki =  kilo / (boy ** 2)

if (bki < 18.5):
    print("Zayıf")
elif (bki >= 18.5 and bki < 25):
    print("Normal")
elif (bki >= 25 and bki < 30):
    print("Fazla Kilolu")
else:
    print("Obez")




"""

Problem 2
Kullanıcıdan 3 tane sayı alın ve en büyük sayıyı ekrana yazdırın.


"""
a =  int(input("a:"))

b = int(input("b:"))

c = int(input("c:"))

if (a > b and a > c):
    print("En büyük sayı:",a)
elif (b > a and b > c):
    print("En büyük sayı:",b)
elif (c > a and c > b):
    print("En büyük sayı:",c)
    



"""
Problem 3
Kullanıcının girdiği vize1,vize2,final notlarına notlarına göre harf notunu hesaplayın.

    Vize1 toplam notun %30'una etki edecek.

    Vize2 toplam notun %30'una etki edecek.

    Final toplam notun %40'ına etki edecek.


    Toplam Not >=  90 -----> AA

    Toplam Not >=  85 -----> BA

    Toplam Not >=  80 -----> BB

    Toplam Not >=  75 -----> CB

    Toplam Not >=  70 -----> CC

    Toplam Not >=  65 -----> DC

    Toplam Not >=  60 -----> DD

    Toplam Not >=  55 -----> FD

    Toplam Not <  55 -----> FF


"""

vize1 = int(input("Vize1:"))
vize2 = int(input("Vize2:"))
final = int(input("Final:"))


genel_not =  vize1 * 3/10 + vize2 * 3/10 + final * 4/10

if (genel_not >= 90):
    print("AA")
elif (genel_not >= 85):
    print("BA")
elif (genel_not >= 80):
    print("BB")
elif (genel_not >= 75):
    print("CB")
elif (genel_not >= 70):
    print("CC")
elif (genel_not >= 65):
    print("DC")
elif (genel_not >= 60):
    print("DD")
elif (genel_not >= 55):
    print("FD")
else:
    print("FF")
    

"""
Problem 4
Şimdi de geometrik şekil hesaplama işlemi yapalım. İlk olarak kullanıcıdan üçgenin mi dörtgenin mi tipini bulmak istediğini sorun.

Eğer kullanıcı "Dörtgen" cevabını verirse , 4 tane kenar isteyip bu dörtgenin kare mi , dikdörtgen mi yoksa sıradan bir dörtgen mi olduğunu bulmaya çalışın.

Eğer kullanıcı "Üçgen" cevabını verirse , 3 tane kenar isteyip bu üçgenin ikizkenar mı , eşkenar mı yoksa sıradan bir üçgen mi olduğunu bulmaya çalışın. Eğer verilen kenarlar bir üçgen belirtmiyorsa, ekrana "Üçgen belirtmiyor" şeklinde bir yazı yazın.o


"""

şekil =  input("Hangi şeklin tipini öğrenmek istiyorsunuz?")

if (şekil == "Dörtgen"):
    print("Lütfen kenarları sırayla giriniz.")
    a = int(input("Kenar-1:"))
    b = int(input("Kenar-2:"))
    c = int(input("Kenar-3:"))
    d = int(input("Kenar-4:"))
    
    if (a == b and a == c and a == d):
        print("Kare")
    elif (a == c and b == d):
        print("Dikdörtgen")
    else:
        print("Dörtgen")
        
    
    
elif (şekil == "Üçgen"):
    a = int(input("Kenar-1:"))
    b = int(input("Kenar-2:"))
    c = int(input("Kenar-3:"))
    if ( abs(a+b) > c and abs(a+c) > b and abs(b+c) > a):
        if (a == b and a == c ):
            print("Eşkenar Üçgen...")
        elif ((a == b and a != c) or (a == c and a != b) or (b == c and b != a)):
            print("İkizkenar Üçgen....")
        else:
            print("Çeşitkenar Üçgen...")
    else:
        print("Üçgen belirtmiyor...")
        
else:
    print("Geçersiz Şekil...")

