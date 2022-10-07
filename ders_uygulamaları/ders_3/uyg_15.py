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