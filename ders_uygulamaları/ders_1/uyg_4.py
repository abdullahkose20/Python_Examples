"""
WHİLE ÖRNEKLERİ

"""
a = 1
while a == 1:
    print("bilgisayar çıldırdı!")


a = 1
while a < 10:
    print("bilgisayar yine çıldırdı!")


a = 1
while a < 10:
    a = a+1
    print("bilgisayar yine çıldırdı!")


a = 1
while a < 10:
    a = a+1
    print(a)


"""
Python ile while döngüsü kullanarak 0-100 arası çift sayıların toplamını hesaplayan ve ekranda gösteren örneğe ait kodlar:
"""

sayac = 0
toplam = 0
while sayac <= 100:
    sayac = sayac + 2
    toplam = toplam+sayac

print(toplam)


"""
Python ile While Döngüsü kullanılarak 0 ile 100 arasındaki çift sayıları yazdıran örneğe ait kodlar.

"""

sayac = 0

while sayac < 100:
    if sayac % 2 == 0:
        print(sayac)

    sayac = sayac+1

"""
while hesap makinesi

"""

anahtar = 1

while anahtar == 1:
    soru = input(
        "Yapmak istediğiniz işlemin numarasını girin (Çıkmak için q): ")

    if soru == "q":
        print("çıkılıyor...")
        anahtar = 0

    elif soru == "1":
        sayı1 = int(input("Toplama işlemi için ilk sayıyı girin: "))
        sayı2 = int(input("Toplama işlemi için ikinci sayıyı girin: "))
        print(sayı1, "+", sayı2, "=", sayı1 + sayı2)

    elif soru == "2":
        sayı3 = int(input("Çıkarma işlemi için ilk sayıyı girin: "))
        sayı4 = int(input("Çıkarma işlemi için ikinci sayıyı girin: "))
        print(sayı3, "-", sayı4, "=", sayı3 - sayı4)

    elif soru == "3":
        sayı5 = int(input("Çarpma işlemi için ilk sayıyı girin: "))
        sayı6 = int(input("Çarpma işlemi için ikinci sayıyı girin: "))
        print(sayı5, "x", sayı6, "=", sayı5 * sayı6)

    elif soru == "4":
        sayı7 = int(input("Bölme işlemi için ilk sayıyı girin: "))
        sayı8 = int(input("Bölme işlemi için ikinci sayıyı girin: "))
        print(sayı7, "/", sayı8, "=", sayı7 / sayı8)

    elif soru == "5":
        sayı9 = int(input("Karesini hesaplamak istediğiniz sayıyı girin: "))
        print(sayı9, "sayısının karesi =", sayı9 ** 2)

    elif soru == "6":
        sayı10 = int(input("Karekökünü hesaplamak istediğiniz sayıyı girin: "))
        print(sayı10, "sayısının karekökü = ", sayı10 ** 0.5)

    else:
        print("Yanlış giriş.")
        print("Aşağıdaki seçeneklerden birini giriniz:")


"""
while true 
break ile hesap makinası
"""

while True:
    soru = input("Yapmak istediğiniz işlemin numarasını girin (Çıkmak için q): ")

    if soru == "q":
        print("çıkılıyor...")
        break

    elif soru == "1":
        sayı1 = int(input("Toplama işlemi için ilk sayıyı girin: "))
        sayı2 = int(input("Toplama işlemi için ikinci sayıyı girin: "))
        print(sayı1, "+", sayı2, "=", sayı1 + sayı2)

    elif soru == "2":
        sayı3 = int(input("Çıkarma işlemi için ilk sayıyı girin: "))
        sayı4 = int(input("Çıkarma işlemi için ikinci sayıyı girin: "))
        print(sayı3, "-", sayı4, "=", sayı3 - sayı4)

    elif soru == "3":
        sayı5 = int(input("Çarpma işlemi için ilk sayıyı girin: "))
        sayı6 = int(input("Çarpma işlemi için ikinci sayıyı girin: "))
        print(sayı5, "x", sayı6, "=", sayı5 * sayı6)

    elif soru == "4":
        sayı7 = int(input("Bölme işlemi için ilk sayıyı girin: "))
        sayı8 = int(input("Bölme işlemi için ikinci sayıyı girin: "))
        print(sayı7, "/", sayı8, "=", sayı7 / sayı8)

    elif soru == "5":
        sayı9 = int(input("Karesini hesaplamak istediğiniz sayıyı girin: "))
        print(sayı9, "sayısının karesi =", sayı9 ** 2)

    elif soru == "6":
        sayı10 = int(input("Karekökünü hesaplamak istediğiniz sayıyı girin: "))
        print(sayı10, "sayısının karekökü = ", sayı10 ** 0.5)

    else:
        print("Yanlış giriş.")
        print("Aşağıdaki seçeneklerden birini giriniz:")



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





        