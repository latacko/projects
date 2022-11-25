def ciongznakow(ciong, dlugosc):
    list2 = [*ciong]
    wys = len(list2)
    for zna in list2:
        for leather in ciong:
            wys += 1
            znak = zna +leather
            list2.append(znak)
            if wys >= dlugosc:
                return list2


test = ciongznakow("abcdefghijklmnoprstuwyz", 25)
print(test)