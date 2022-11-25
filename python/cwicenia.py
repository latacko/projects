def setka():
    num = int(input("Podaj liczbe: "))
    if num < 0:
        print("Ujemna")
    elif num ==0:
        print("Zero")
    elif num > 0 and num <= 100:
        print("Setka")
    else:
        print("większe od setki")

setka()