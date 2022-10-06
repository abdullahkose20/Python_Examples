sayı1 = int(input("birinci sayı giriniz:"))
islem = input("İşlem seçiniz:")
sayı2 = int(input("ikinci sayı giriniz:"))


if islem == '+':
    sonuc = sayı1+sayı2
if islem == '-':
    sonuc = sayı1-sayı2
if islem == '*':
    sonuc = sayı1*sayı2
if islem == '/':
    sonuc = sayı1/sayı2

print("işlemin sonucu:{}". format(int(sonuc)))