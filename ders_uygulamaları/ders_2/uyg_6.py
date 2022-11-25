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




sayac = 0
toplam = 0
while sayac <= 100:
    sayac = sayac + 2
    toplam = toplam+sayac

print(toplam)


"""
Klavyeden girilen sayıya kadar olan sayıların toplamını hesaplayan ve sonucu yazdıran python kodunu while döngüsü kullanarak yapan kodunu yazınız.

"""
sayac = 0
toplam = 0
bitis=int(input("Bir Sayı Giriniz: "))
while sayac <= bitis:
    sayac = sayac + 1
    toplam = toplam + sayac
print(bitis," saısına kadar olan sayıların toplamı:{0}".format(toplam))











sayac = 0

while sayac < 100:
    if sayac % 2 == 0:
        print(sayac)

    sayac = sayac+1



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