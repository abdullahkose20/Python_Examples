# parametre almayan değer döndürmeyen

def merhaba():
    print("merhaba")


merhaba()

# parametre alan değer döndürmeyen

def nct(a, b):
    cıkarma = a-b
    print(cıkarma)


nct(8, 5)

# parametre almayan değer döndüren

def toplama():
    a=8
    b=12
    sayı = a+b
    return sayı


print(toplama())


# parametre alan ve değer döndüren


def toplama(a, b):
    sayı = a+b
    return sayı


print(toplama(3, 5))




"""
örnek-1
"""

def kare_bul():
    sayı = 12
    çıktı = "{} sayısının karesi {} sayısıdır"
    print(çıktı.format(sayı, sayı**2))
kare_bul()


"""
örnek-2
"""
def kayıt_oluştur(isim, soyisim, işsis, şehir):
    print("-"*30)
    print("isim : ", isim)
    print("soyisim : ", soyisim)
    print("işletim sistemi: ", işsis)
    print("şehir : ", şehir)
    print("-"*30)


kayıt_oluştur("Ahmet", "Öz", "Debian", "Ankara")
kayıt_oluştur("Debian", "Ankara", "Öz", "Ahmet")



"""
örnek-3
"""

def fonk(n):
    if n < 0:
        return 'eksi değerli sayı olmaz!'
    else:
        return n

f = fonk(-5)

print(f)

"""
örnek-4
"""
def yazdir(metin,kacKere):
       for i in range (1, (kacKere+1)):
            print (metin, end='\n')


yazdir('Merhaba', 5)


"""
örnek-5
"""

def öğrenci (ad,soyad,no,sınıf):
    print ("AD     : ",ad)
    print ("SAYAD  : ",soyad)
    print ("NUMARA : ",no)
    print ("SINIFI : ",sınıf)


ad_bilgi=input ("Adınızı Giriniz:")
soyad_bilgi=input ("Soyadınızı Giriniz:")
no_bilgi=input ("Numaranızı Giriniz:")
sınıf_bilgi=input ("Sınıfınızı Giriniz:")



öğrenci(ad_bilgi,soyad_bilgi,no_bilgi,sınıf_bilgi)


"""
örnek-6
"""

def sayiCiftMi (sayi):
     if sayi%2==0:
         print('Sayı çifttir')
     else: ('Sayı tektir')

sayiCiftMi(10)


"""
örnek-7
"""

def daireAlan(yaricap):
    alan = float(yaricap) * float(yaricap)*3.14
    print ("Alan :",alan)
    return alan


r = input("Yarıçapı Gir :")
 
daireAlan(r)

"""
örnek-8
Kullanıcının girdiği 2 sayı arasındaki çift sayıların ortalamasını bulan Python programı
"""

def ciftMi(x): 
    return x % 2 == 0
 
toplam=0
sayac=0
baslangic = input("Başlangıç Sayısı :")
bitis = input("Bitiş Sayısı :")
for sayi in range (int(baslangic), int(bitis)+1):
    if(ciftMi(int(sayi))):
        toplam=toplam+sayi
        sayac=sayac+1
print('Ortalama',(toplam/sayac))


"""
örnek-9
"""

def toplama(sayi1,sayi2):
    return sayi1+sayi2
 
def cikarma(sayi1,sayi2):
    return sayi1-sayi2
 
def carpma(sayi1,sayi2):
    return sayi1*sayi2
 
def bolme(sayi1,sayi2):
    return sayi1/sayi2
while True:
    secim = input("Bir Seçim Yapın :")
    if secim == "q":
        break
    
    sayi1 = int(input("Birinci sayıyı girin :"))
    sayi2 = int(input("İkinci sayıyı girin :"))

    if secim=="1":
        print("Sonuç :", toplama(sayi1, sayi2))
    elif secim =="2":
        print("Sonuç :", cikarma(sayi1,sayi2))
    elif secim =="3":
        print("Sonuc :",carpma(sayi1,sayi2))
    elif secim=="4":
        print("Sonuç :",bolme(sayi1,sayi2))
    else:
        print("Yanlış seçim lütfen tekrar deneyin")
        break
        
        
"""
örnek-10
"""

def topla(s1, s2):
  if(s1 > s2):
    return s1
  else:
    return s2

sayi1 = int(input('sayı 1:'))
sayi2 = int(input('sayı 2:'))

print(str(topla(sayi1,sayi2)) + " sayısı büyük")