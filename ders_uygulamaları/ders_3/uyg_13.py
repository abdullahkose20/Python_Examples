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