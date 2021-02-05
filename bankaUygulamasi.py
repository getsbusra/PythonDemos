class Account:
    defaultBakiye = 2000
    name = str(input("Adınız? "))
    surname = str (input("Soyadınız?"))
    accountNumber = int(input("4 haneli hesap numaranız?"))
    print("Hosgeldiniz " + name + " " + surname)



def bakiyeSorgula():
    print("Toplam Bakiyeniz = " + str(Account.defaultBakiye))

def paraCek():
    cekilecek = int(input("Cekilecek Miktar?"))
    if cekilecek > Account.defaultBakiye:
        print("Bakiye Yetersiz!")
    else:
        Account.defaultBakiye -= cekilecek
        print("Para Cekme İsleminiz Tamamlandi..\nYeni Bakiye = " + str(Account.defaultBakiye))    

def paraYatir():
    yatirilacak = int(input("Yatırılacak Miktar?"))
    Account.defaultBakiye += yatirilacak
    print("Para Yatırma İsleminiz Tamamlandi..\nYeni Bakiye = " + str(Account.defaultBakiye))

def paraGonder():
    kesimUcreti = 4.7
    str(input("Alıcı Ad Soyad?"))
    int(input("Alıcı Hesap No"))
    gonderilecek = int(input("Gönderilecek Miktar?")) 
      
    if gonderilecek + kesimUcreti > Account.defaultBakiye: 
        print("Bakiye Yetersiz.")

    else:
        print("Bankanız Sizden " + str(kesimUcreti) + " TL tahsil edecektir. ")
        Account.defaultBakiye -= gonderilecek + kesimUcreti
        print("Paraniz basariyla Gonderildi.\nYeni Bakiye = " + str(Account.defaultBakiye))    

while True:
    print("**MENU***\n1- Bakiye Sorgulama\n2- Para Çekme\n3- Para Yatırma\n4- Para Gönderme\n5- Çıkış")
    operation = int(input("Yapmak Istediginiz Islemi Seciniz:"))

    if operation == 1:
        bakiyeSorgula()
    elif operation == 2:
        paraCek()    
    elif operation == 3:
        paraYatir()
    elif operation == 4:
        paraGonder()
    elif operation == 5:
        print("Programdan Cikiliyor..")
        break            
    else:
        print("Lutfen Gecerli Bir Islem Giriniz.")