yas = int(input("yasınızı giriniz: "))
okul = input("Okuyor musunuz? (evet: e, hayır: h): ")

if yas >= 20 and okul == 'h':
    print("askere gitmeniz gerekiyor")

elif yas >= 20 and okul == 'e':
    print("okulunuz bitince askere gitmeniz gerekiyor")

else:
    print("askerlik yasınız gelmedi")
