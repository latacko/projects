import time
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

# ======================================== 28.11.2022 =====================================================

# def czy_przestepny(rok):
#     if (rok%4 == 0) & (rok%100!=0) | (rok%400==0):
#         return True
#     return False

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


# def dni_w_miesiacu(rok, miesiac):
#     dni = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
#     if miesiac ==2 and czy_przestepny(rok):
#         return 29
#     return dni[miesiac-1]


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


# def dzien_w_roku(rok, miesiac, dzien):
#     iloscdni = 0
#     for mie in range(miesiac):
#         dni = dni_w_miesiacu(rok, mie)
#         if dni > dzien:
#             return iloscdni+dzien
#         iloscdni += dni
#     return iloscdni


# print(dzien_w_roku(2000, 12, 31))
# ========================================03.12.2022 =====================================================
# def l100kmtompg(litry):
#     galony = litry/3.785411784
#     stokmNaMile = 100*1000/1609.344
#     return stokmNaMile/galony

# def mpgtol100km(mile):
#     km = mile*1.609344
#     l =3.785411784
#     return 100*l/km

# print(l100kmtompg(3.9))
# print(l100kmtompg(7.5))
# print(l100kmtompg(10.))
# print(mpgtol100km(60.3))
# print(mpgtol100km(31.4))
# print(mpgtol100km(23.5))

# def czy_trojkot(bok_1, bok_2, bok_3):
#     for ar in [bok_1, bok_2, bok_3]:
#         if not isinstance(ar,int) and not isinstance(ar,int) and not ar.isnumeric():
#             return
#     boks = [int(bok_1), int(bok_2), int(bok_3)]
#     boks.sort()
#     return boks[2] < boks[1]+ boks[0]

# def czy_prostokonty(bok_1, bok_2, bok_3):
#     if czy_trojkot(bok_1, bok_2, bok_3) != True:
#         return czy_trojkot(bok_1, bok_2, bok_3)

#     boks = [int(bok_1), int(bok_2), int(bok_3)]
#     boks.sort()
#     return boks[0]**2+boks[1]**2==boks[2]**2

# def pole(a,b,c):
#     if czy_trojkot(a,b,c) != True:
#         return czy_trojkot(a,b,c)
#     a,b,c = int(a), int(b), int(c)
#     s = (a+b+c)/2
#     return (s*(s- a)*(s-b)*(s-c))**.5

# while True:
#     bo = []
#     for i in range(3):
#         bo.append(input(f"Podaj bok {i+1}: "))
#     print(czy_prostokonty(bo[0], bo[1], bo[2]))
#     print(f"Pole {pole(bo[0], bo[1], bo[2])}")


# def silnia(ile):
#     licz= 1
#     for i in range(1,ile+1):
#         licz *=i
#     return licz

# print(silnia(0))

# def fib(ile):
#     lis = [1, 1]

#     if ile <= 0:
#         ile = 1

#     if ile <= len(lis):
#         return lis[ile]

#     for i in range(ile-2):
#         dlul = len(lis)
#         lis.append(lis[dlul-2]+lis[dlul-1])
#     # print(lis)
#     return lis[ile-1]

# def fib(ile):
#     if ile <= 0:
#         return 1

#     if ile < 3:
#         return 1

#     return fib(ile-2)+fib(ile-1)
# lis = [0.0009999275207519531,
# 0.0019998550415039062,
# 0.0009856224060058594,
# 0.0]

# def sil(ile, last=1, i=1):
#     if ile <= 0:
#         return last

#     ile -=1
#     last*=i
#     i+=1
#     return sil(ile, last, i)

# def sil(ile, last=1, i=1):
#     if ile <= 0:
#         return last

#     ile -=1
#     last*=i
#     i+=1
#     return sil(ile, last, i)
# start_time = time.time()
# print(sil(100))
# print("--- %s seconds ---" % (time.time() - start_time))

# def spt(str):
#     li = []
#     last = 0
#     sep = " "
#     if str[0].lower() == sep:
#         last = 1
#     for i in range(last, len(str)):
#         cha = str[i]
#         if cha.lower() == sep:
#             li.append(str[last:i])
#             last = i+1
#         elif i == len(str)-1:
#             li.append(str[last:i+1])
#     return li
# print(spt("Ania ma kota"))

# def wyswietlac_seg(num):
#     if (isinstance(num,str) and not num.isdigit()) or not isinstance(num,str):
#         print("musi być liczbą")
#         return
#     segments = [
#         """
#  ------- 
# |       |
# |       |
# |       |
         
# |       |
# |       |
# |       |
#  ------- 
#         """,
#         """
         
#         |
#         |
#         |
         
#         |
#         |
#         |
         
#         """,
#         """
#  ------- 
#         |
#         |
#         |
#  ------- 
# |        
# |        
# |        
#  ------- 
#         """,
#         """
#  ------- 
#         |
#         |
#         |
#  ------- 
#         |
#         |
#         |
#  ------- 
#         """,
#         """
         
# |       |
# |       |
# |       |
#  ------- 
#         |
#         |
#         |
         
#         """,
#         """
#  ------- 
# |        
# |        
# |        
#  ------- 
#         |
#         |
#         |
#  ------- 
#         """,
#         """
#  ------- 
# |        
# |        
# |        
#  ------- 
# |       |
# |       |
# |       |
#  ------- 
#         """,
#         """
#  ------- 
#         |
#         |
#         |
         
#         |
#         |
#         |
         
#         """,
#         """
#  ------- 
# |       |
# |       |
# |       |
#  ------- 
# |       |
# |       |
# |       |
#  ------- 
#         """,
#         """
#  ------- 
# |       |
# |       |
# |       |
#  ------- 
#         |
#         |
#         |
#  ------- 
#         """,
#     ]

#     numbers = list(num)

#     linijki = []
#     for i in range(9):
#         for number in numbers:
#             number = int(number)
#             if i<len(linijki):
#                 linijki[i]+="    "+segments[number][i*10:i*10+10].replace("\n", "")
#             else:
#                 linijki.append(segments[number][i*10:i*10+10].replace("\n", ""))
#     for linij in linijki:
#         print(linij)

# while True:
#     liczba = input("Podaj liczbę (wpisz stop aby zatrzymać program): ")
#     if liczba.strip().lower() == "stop":
#         break
#     wyswietlac_seg(liczba)

def cezar(text):
       texta = ""
       ile_prz = int(input("O ile chcesz przesunąć: "))
       if ile_prz < 1 or ile_prz > 26:
              print("zły przedział")
              return text;
       for let in text:
              asc = ord(let)
              duza = asc>= 65 and asc <= 90
              mala = asc>= 97 and asc <= 122
              asc +=ile_prz
              if duza:
                     if asc > 90:
                            asc = 65+(asc-90)
              if mala:
                     if asc > 122:
                            asc = 97+(asc-122)
              texta += chr(asc) 
       return texta
while True:
       print(cezar("abcABCZ"))