from random import randrange
import time


statki = []
letters = "abcdefghijklmnoprstuwyz"
znaki_na_wysokosc = []
ilosczyc = 5
iloscstatkow = 5
width =15
height = 5
ilosczniszczonychstatkow = 0

with_bot = True

def ciongznakow(ciong, dlugosc):
    list2 = [*ciong]
    wys = len(list2)
    if (dlugosc > len(list2)):
        for zna in list2:
            for leather in ciong:
                wys += 1
                znak = zna +leather
                list2.append(znak)
                if wys >= dlugosc:
                    return list2
    else:
        del list2[dlugosc:]
        return list2

def sprawdzanie_poprawnosci_pola(pole):
    miejscepierwszejliterki = -1
    pole = pole.lower()
    for literka in [*letters]:
        miejsce = pole.find(literka)
        if miejscepierwszejliterki==-1:
            miejscepierwszejliterki = miejsce
        elif miejsce < miejscepierwszejliterki and miejsce != -1:
            miejscepierwszejliterki = miejsce
    if miejscepierwszejliterki == 0:
        print("Brak szerokości")
        return False
    if miejscepierwszejliterki == -1:
        print("Brak wysokości")
        return False
    num = pole[0:miejscepierwszejliterki]
    let = pole[miejscepierwszejliterki:].lower()

    if int(num) <=0 or int(num) > width or not let in znaki_na_wysokosc:
        print("Miejsce poza planszą")
        return False
    return num, let

def create_ship():
    """Tworzy statki"""
    succes = 0
    while succes==0:
        x = randrange(1, width+1)
        y = randrange(0, height-1)
        name = "x" + str(x) + "y"+str(y)
        if not name in statki:
            print("Ship created on " +  str(x) +  znaki_na_wysokosc[y])
            succes = 1
            statki.append(name)
            return x, y

def create_ship_user(table):
    """Tworzy statki"""
    succes = 0
    while succes==0:
        podanepole = input()
        if sprawdzanie_poprawnosci_pola(podanepole) == False:
            continue
        num, let = sprawdzanie_poprawnosci_pola(podanepole)
        # nr = 0
        # e = False
        # if not let in [*letters]:
        #     for x in let:
        #         if x in lethers:
        #             nr += lethers.index(x)
        #         else:
        #             e=True
        # else:
        #     nr = lethers.index(let)
        # if e:
        #     print("Poza planszą")
        #     continue
        po = "x"+num+"y"+str(znaki_na_wysokosc.index(let))
        if not po in table:
            print("Ship created on " +  str(num) + let)
            succes = 1
            table.append(po)
        else:
            print("Masz już tam statek")

def is_there_ship(table, p_pole):
    """Sprawdza czy na danym polu jest statek"""
    for pole in table:
        if pole == p_pole:
            return 1
    return 0
def ishereshoot(pos, table):
    for x in table:
        if x["pos"] == pos:
            return x["hit"]
    return 2

def create_table(bot_table, user_table):
    on_height = -1
    tab = ""
    najdluse = len(znaki_na_wysokosc[len(znaki_na_wysokosc)-1])-1
    while on_height<=height:
        line = ""
        dlugoscspacjiplanszy = len(" "*najdluse+ "    "*width)
        if on_height == -1:
            odlewa = (dlugoscspacjiplanszy-len("Plansza bota"))//2
            line = " "*odlewa + "Plansza bota"+" "*(dlugoscspacjiplanszy-(odlewa+len("Plansza bota"))+4)
        elif on_height == 0:
            line = " "*najdluse+"   |"
            for x in range(width):
                line += " "+str(x+1)+" |"
        else:
            line += znaki_na_wysokosc[on_height-1] + " "*(najdluse-(len(znaki_na_wysokosc[on_height-1])-1)) + "  |"
            for x in range(width):
                isshot = ishereshoot("x" + str(x+1) + "y" + str(on_height-1), bot_table)
                if isshot == 1:
                    line += " * |"
                elif isshot == 0:
                    line += " X |"
                else:
                    line += "   |"

        line += "\t\t\t"

        if with_bot:
            if on_height == -1:
                odlewa = (dlugoscspacjiplanszy-len("Twoja plansza"))//2
                line += " "+" "*odlewa + "Twoja plansza"+" "*(dlugoscspacjiplanszy-(odlewa+len("Twoja plansza")+4))
            elif on_height == 0:
                line += " "*najdluse+"   |"
                for x in range(width):
                    line += " "+str(x+1)+" |"
            else:
                line += znaki_na_wysokosc[on_height-1] + " "*(najdluse-(len(znaki_na_wysokosc[on_height-1])-1)) + "  |"
                for x in range(width):
                    isshot = ishereshoot("x" + str(x+1) + "y" + str(on_height-1), user_table)
                    if isshot == 1:
                        line += " * |"
                    elif isshot == 0:
                        line += " X |"
                    else:
                        line += "   |"

        line += "\n"
        line += "-"*najdluse + "---|"
        for x in range(width):
            line += "---|"
        if with_bot:
            line += "\t\t\t"
            line += "-"*najdluse + "---|"
            for x in range(width):
                line += "---|"
        tab += line+"\n"
        on_height += 1
    print(tab)


def Start():
    ilosczyc2 = ilosczyc
    heal = ilosczyc
    ilosczniszczonychstatkow = 0
    stopped = 0
    score = 0
    my_hits = []
    bot_hits = []
    mojestatki = []
    global znaki_na_wysokosc
    znaki_na_wysokosc = ciongznakow("abcdefghijklmnoprstuwyz", height)
    while len(znaki_na_wysokosc) == 0:
        for i in range(1, 4):
            print("Loading" + "."*i)
            time.sleep(2)
        for i in range(2, 1, -1):
            print("Loading" + "."*i)
            time.sleep(2)

    print("ustawiono " + str(znaki_na_wysokosc))
    if with_bot:
        for x in range(iloscstatkow):
            print("Podaj miejsce statku np 4D (opcja wyboru od 1 do " + str(width) + " oraz od a do " +znaki_na_wysokosc[height-1]+")")
            create_ship_user(mojestatki)
        print(mojestatki)
    # if height> len(lethers):
    #     print("height is up an max")
    #     return
    for x in range(iloscstatkow):
        create_ship()
    
    while ilosczniszczonychstatkow<iloscstatkow and ilosczyc2>0:
        print("Wpisz pole np 4D (opcja wyboru od 1 do " + str(width) + " oraz od a do " +znaki_na_wysokosc[height-1]+")")
        podanepole = input()
        if podanepole == "stop":
            stopped = 1
            break
        else:
            if sprawdzanie_poprawnosci_pola(podanepole) == False:
                continue
            num, let = sprawdzanie_poprawnosci_pola(podanepole)

            # e=False
            # if not let in lethers:
            #     for x in let:
            #         if x in lethers:
            #             nr += lethers.index(x)
            #         else:
            #             e=True
            # else:
            #     nr = lethers.index(let)
            # if e:
            #     print("Poza planszą")
            #     continue
            po = "x"+num+"y"+str(znaki_na_wysokosc.index(let))
            if ishereshoot(po, my_hits) != 2:
                print("Był już strzał w to pole")
                continue
            if is_there_ship(statki, po) == 1:
                score += 1
                if with_bot:
                    print("Trafiono w statek")
                else:
                    heal += 1
                    print("Trafiono w statek (+1 punkt życia)")
                statki.remove(po)
                customtable = {
                    "pos": po,
                    "hit": 1
                }
                my_hits.append(customtable)
            else:
                if with_bot:
                    print("Nie trafiono w statek")
                else:
                    heal -= 1
                    print("Nie trafiono w statek (-1 punkt życia)")

                customtable = {
                    "pos": po,
                    "hit": 0
                }
                my_hits.append(customtable)
            create_table(my_hits, bot_hits)
        if heal==0:
            break


        if len(statki) == 0:
            create_table(my_hits, bot_hits)
            break

        if with_bot:
            # ustawienia komputera
            print("Tura komputera")
            time.sleep(2)
            bot_shoot_x = 0
            bot_shoot_y = 0
            trafione = None
            while True:
                bot_shoot_x = randrange(1, width+1)
                bot_shoot_y = randrange(0, height)

                bot_shoot = "x" + str(bot_shoot_x) + "y"+str(bot_shoot_y)
                customtable = {}
                if ishereshoot(bot_shoot, bot_hits) != 2:
                    print("Bot strzelić pole " + bot_shoot + " ale już tu strzelał ")
                    print(bot_hits)
                    continue
                if is_there_ship(mojestatki, bot_shoot) == 1:
                    mojestatki.remove(bot_shoot)
                    customtable = {
                        "pos": bot_shoot,
                        "hit": 1
                    }
                    trafione = "trafił"
                    bot_hits.append(customtable)
                    break
                else:
                    customtable = {
                        "pos": bot_shoot,
                        "hit": 0
                    }
                    trafione = "nie trafił"
                    bot_hits.append(customtable)
                    break
            print("Komputer strzelił pole " + str(bot_shoot_x) + znaki_na_wysokosc[bot_shoot_y] + " i " +trafione)
        create_table(my_hits, bot_hits)
        if len(mojestatki) == 0:
            break
    if stopped == 1:
        print("Game stopped")
    elif heal == 0:
        print("Game Over Score: " + str(score))
    else:
        if len(mojestatki) == 0 and with_bot:
            print("Przegrana Score: " + str(score))
        elif len(statki) == 0:
            print("WIN Score: " + str(score))

Start()