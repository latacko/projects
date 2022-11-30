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

def sex(name):
    if name[-1].lower() == "a":
        return "women"
    else:
        return "man"

while True:
    print(sex(input("Podaj imie: ")))