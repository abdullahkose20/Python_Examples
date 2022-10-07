
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



