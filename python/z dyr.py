# def validate(text = ""):
#     test = text
#     if test.isalpha():
#         return "Tylko litery"
#     elif test.isdigit():
#         return "Tylko cyfry"
#     elif test.isalnum():
#         return "Tylko litery i cyfry"
#     else:
#         return "Błędne znaki"

# while True:
#     print(validate(input("Podaj ciąg znaków: ")))

# def sex(name):
#     # print("|" + name.replace(" ", "")[-1].lower() + "|")
#     if name.strip()[-1].lower() == "a":
#         return "women"
#     else:
#         return "man"

# while True:
#     print(sex(input("Podaj imie: ")))


# def silnia(ile):
#     i = 0
#     ilo = 1
#     while i<ile:
#         i += 1
#         ilo *= i
#         print(f"Liczba {ilo} mnożnik: {i}")
#     return ilo

# def walidacja(liczba):
#     if liczba.lower() == "koniec":
#         return "koniec"
#     while not isinstance(liczba, int) and not liczba.isdigit():
#         liczba = input("Podaj liczbę: ")
#     return int(liczba)

# while True:
#     liczba = walidacja(input("Podaj liczbę: "))
#     if liczba == "koniec":
#         break
#     print(silnia(liczba))

def podziel(liczba):
    n = 3
    liczba = str(liczba)
    li = [liczba[len(liczba)-i-n:len(liczba)-i] for i in range(0, len(liczba), n)]
    li.reverse()
    tete = join("_")
    return tete

print(podziel(1236542346545645645645))