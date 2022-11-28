# def setka():
#     num = int(input("Podaj liczbe: "))
#     if num < 0:
#         print("Ujemna")
#     elif num ==0:
#         print("Zero")
#     elif num > 0 and num <= 100:
#         print("Setka")
#     else:
#         print("większe od setki")

# setka()



def czy_przestepny(rok):
    if (rok%4 == 0) & (rok%100!=0) | (rok%400==0):
        return True
    return False

# dane_testowe = [1900, 2000, 2016, 1987]
# wyniki_testow = [False, True, True, False]
# for i in range(len(dane_testowe)):
# 	r = dane_testowe[i]
# 	print(r,"->",end="")
# 	wynik = czy_przestepny(r)
# 	if wynik == wyniki_testow[i]:
# 		print("OK")
# 	else:
# 		print("Nie powiodło się")


def dni_w_miesiacu(rok, miesiac):
    dni = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if miesiac ==2 and czy_przestepny(rok):
        return 29
    return dni[miesiac-1]


# testuj_lata = [1900, 2000, 2016, 1987]
# testuj_miesiace = [2, 2, 1, 11]
# testuj_wynik = [28, 29, 31, 30]
# for i in range(len(testuj_lata)):
# 	r = testuj_lata[i]
# 	m = testuj_miesiace[i]
# 	print(r, m, "-> ", end="")
# 	wynik = dni_w_miesiacu(r, m)
# 	if wynik == testuj_wynik[i]:
# 		print("OK")
# 	else:
# 		print("Nie powiodło się")


def dzien_w_roku(rok, miesiac, dzien):
    iloscdni = 0
    for mie in range(miesiac):
        dni = dni_w_miesiacu(rok, mie)
        if dni > dzien:
            return iloscdni+dzien
        iloscdni += dni
    return iloscdni


print(dzien_w_roku(2000, 12, 31))
