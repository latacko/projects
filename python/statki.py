from random import randrange
import time
import pygame, sys, subprocess
from threading import Thread

withBot = True
size = width, height = 500, 340
if withBot:
    size = width, height = 828, 358

screen = pygame.display.set_mode(size)
pygame.display.set_caption('Statki')

w, h=5, 5

myp = []
for i in range(w*h):
    myp.append(pygame.image.load(f"C:\\Users\\galorf\\Desktop\\L_PROJECTS\\projects\\python\\square.png").convert())


def bganimate():
    bg = []
    if not withBot:
        for i in range(25):
            nr = i
            if i  < 10:
                nr = "0"+str(i)
            bg.append(pygame.image.load(f"C:\\Users\\galorf\\Desktop\\L_PROJECTS\\projects\\python\\bgframes\\without_bot\\frame_{nr}_delay-0.1s.gif"))
    else:
        for i in range(4):
            bg.append(pygame.image.load(f"C:\\Users\\galorf\\Desktop\\L_PROJECTS\\projects\\python\\bgframes\\with_bot\\frame_{i}_delay-0.2s.gif"))
    tlorect = bg[0].get_rect()
    while True:
        for i in range(len(bg)):
            for img2 in bg:
                if bg[i] != img2:
                    screen.blit(img2, [-1000, -1000])
            if not withBot:
                time.sleep(0.1)
            else:
                time.sleep(0.2)
            screen.blit(bg[i], tlorect)
        for i in range(len(bg)-1, 1, -1):
            for img2 in bg:
                if bg[i] != img2:
                    screen.blit(img2, [-1000, -1000])
            if not withBot:
                time.sleep(0.1)
            else:
                time.sleep(0.2)
            screen.blit(bg[i], tlorect)
t2 = Thread(target = bganimate)
t2.start()

def insquare(pos):
    id = -1
    for x in range(w):
        for y in range(h):
            id = id+1
            min_x, min_y =50*x,50*y
            max_x, max_y =50*x+50,50*y+50
            if pos[0] > min_x and pos[0] < max_x and pos[1] > min_y and pos[1] < max_y:
                return i
    return False

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            # Set the x, y postions of the mouse click
            x, y = event.pos
            print(insquare(event.pos))
            # for sq in myp:

            #     print("Sorawdzan img na pozyci " + str(myp.index(sq)) + " collide ?"  + str(sq.get_rect().collidepoint(event.pos)))
            #     if sq.get_rect().collidepoint(event.pos):
            #         print("Clicked " + str(myp.index(sq)))
            #         break


    id = -1
    for x in range(w):
        for y in range(h):
            id = id+1
            screen.blit(myp[i], [50*x,50*y])

    pygame.display.flip()
    pygame.display.update()



class ShipsGame:
    def __init__(self, width=5, height=5, ship_cout=5, health=5, with_bot=False, letters="abcdefghijklmnoprstuwyz", debug=False):
        # game settings
        self.letters = letters
        self.ilosczyc = health
        self.iloscstatkow = ship_cout
        self.width =width
        self.height = height
        self.with_bot = with_bot
        self.debug = debug
        # values
        self.statki = []
        self.znaki_na_wysokosc = []
        self.ilosczniszczonychstatkow = 0
        self.Start()

    def ciongznakow(self, ciong, dlugosc):
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

    def sprawdzanie_poprawnosci_pola(self, pole):
        miejscepierwszejliterki = -1
        pole = pole.lower()
        for literka in [*self.letters]:
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

        if int(num) <=0 or int(num) > self.width or not let in znaki_na_wysokosc:
            print("Miejsce poza planszą")
            return False
        return num, let

    def create_ship(self):
        """Tworzy statki"""
        succes = 0
        while succes==0:
            x = randrange(1, self.width+1)
            y = randrange(0, self.height)
            name = "x" + str(x) + "y"+str(y)
            if not name in self.statki:
                if self.debug:
                    print("Ship created on " +  str(x) +  znaki_na_wysokosc[y])
                succes = 1
                self.statki.append(name)
                return x, y

    def create_ship_user(self, table):
        """Tworzy statki"""
        succes = 0
        while succes==0:
            podanepole = input()
            if self.sprawdzanie_poprawnosci_pola(podanepole) == False:
                continue
            num, let = self.sprawdzanie_poprawnosci_pola(podanepole)
            po = "x"+num+"y"+str(znaki_na_wysokosc.index(let))
            if not po in table:
                print("Ship created on " +  str(num) + let)
                succes = 1
                table.append(po)
            else:
                print("Masz już tam statek")

    def is_there_ship(self, table, p_pole):
        """Sprawdza czy na danym polu jest statek"""
        for pole in table:
            if pole == p_pole:
                return 1
        return 0
    def ishereshoot(self, pos, table):
        for x in table:
            if x["pos"] == pos:
                return x["hit"]
        return 2

    def create_table(self, bot_table, user_table):
        on_height = -1
        tab = ""
        najdluse = len(znaki_na_wysokosc[len(znaki_na_wysokosc)-1])-1
        while on_height<=self.height:
            line = ""
            dlugoscspacjiplanszy = len(" "*najdluse+ "    "*self.width)
            if on_height == -1:
                odlewa = (dlugoscspacjiplanszy-len("Plansza bota"))//2
                line = " "*odlewa + "Plansza bota"+" "*(dlugoscspacjiplanszy-(odlewa+len("Plansza bota"))+4)
            elif on_height == 0:
                line = " "*najdluse+"   |"
                for x in range(self.width):
                    line += " "+str(x+1)+" |"
            else:
                line += znaki_na_wysokosc[on_height-1] + " "*(najdluse-(len(znaki_na_wysokosc[on_height-1])-1)) + "  |"
                for x in range(self.width):
                    isshot = self.ishereshoot("x" + str(x+1) + "y" + str(on_height-1), bot_table)
                    if isshot == 1:
                        line += " * |"
                    elif isshot == 0:
                        line += " X |"
                    else:
                        line += "   |"

            line += "\t\t\t"

            if self.with_bot:
                if on_height == -1:
                    odlewa = (dlugoscspacjiplanszy-len("Twoja plansza"))//2
                    line += " "+" "*odlewa + "Twoja plansza"+" "*(dlugoscspacjiplanszy-(odlewa+len("Twoja plansza")+4))
                elif on_height == 0:
                    line += " "*najdluse+"   |"
                    for x in range(self.width):
                        line += " "+str(x+1)+" |"
                else:
                    line += znaki_na_wysokosc[on_height-1] + " "*(najdluse-(len(znaki_na_wysokosc[on_height-1])-1)) + "  |"
                    for x in range(self.width):
                        isshot = self.ishereshoot("x" + str(x+1) + "y" + str(on_height-1), user_table)
                        if isshot == 1:
                            line += " * |"
                        elif isshot == 0:
                            line += " X |"
                        else:
                            line += "   |"

            line += "\n"
            line += "-"*najdluse + "---|"
            for x in range(self.width):
                line += "---|"
            if self.with_bot:
                line += "\t\t\t"
                line += "-"*najdluse + "---|"
                for x in range(self.width):
                    line += "---|"
            tab += line+"\n"
            on_height += 1
        print(tab)


    def Start(self):
        ilosczyc2 = self.ilosczyc
        heal = self.ilosczyc
        ilosczniszczonychstatkow = 0
        stopped = 0
        score = 0
        my_hits = []
        bot_hits = []
        mojestatki = []
        global znaki_na_wysokosc
        znaki_na_wysokosc = self.ciongznakow(self.letters, self.height)
        while len(znaki_na_wysokosc) == 0:
            for i in range(1, 4):
                print("Loading" + "."*i)
                time.sleep(2)
            for i in range(2, 1, -1):
                print("Loading" + "."*i)
                time.sleep(2)

        if self.debug:
            print("ustawiono " + str(znaki_na_wysokosc))
        if not self.with_bot:
            odmiana = ""
            if self.ilosczyc ==1:
                odmiana = "punkt życia"
            elif self.ilosczyc >1 & self.ilosczyc <5 |self.ilosczyc > 1 & self.ilosczyc < 5 & self.ilosczyc > 20:
                odmiana = "punkty życia"
            else:
                odmiana = "punktów życia"
            odmiana2 = ""
            if self.iloscstatkow ==1:
                odmiana2 = "statek"
            elif self.iloscstatkow >1 & self.iloscstatkow <5 |self.iloscstatkow > 1 & self.iloscstatkow < 5 & self.iloscstatkow > 20:
                odmiana2 = "statki"
            else:
                odmiana2 = "statków"
            print("Masz " + str(self.ilosczyc) + " " + odmiana + ", bot ma " + str(self.iloscstatkow) + " " + odmiana2)
        else:
            odmiana2 = ""
            if self.iloscstatkow ==1:
                odmiana2 = "statek"
            elif self.iloscstatkow >1 & self.iloscstatkow <5 |self.iloscstatkow > 1 & self.iloscstatkow < 5 & self.iloscstatkow > 20:
                odmiana2 = "statki"
            else:
                odmiana2 = "statków"
            print("Masz do postawienia " + str(self.iloscstatkow) + " " + odmiana2)
        if self.with_bot:
            for x in range(self.iloscstatkow):
                print("Podaj miejsce statku np 4D (opcja wyboru od 1 do " + str(self.width) + " oraz od a do " +znaki_na_wysokosc[self.height-1]+")")
                self.create_ship_user(mojestatki)
            if self.debug:
                print(mojestatki)
        for x in range(self.iloscstatkow):
            self.create_ship()

        while ilosczniszczonychstatkow<self.iloscstatkow and ilosczyc2>0:
            print("Wpisz pole np. 4D (opcja wyboru od 1 do " + str(self.width) + " oraz od a do " +znaki_na_wysokosc[self.height-1]+")")
            podanepole = input()
            if podanepole == "stop":
                stopped = 1
                break
            else:
                if self.sprawdzanie_poprawnosci_pola(podanepole) == False:
                    continue
                num, let = self.sprawdzanie_poprawnosci_pola(podanepole)
                po = "x"+num+"y"+str(znaki_na_wysokosc.index(let))

                if self.ishereshoot(po, my_hits) != 2:
                    print("Był już strzał w to pole")
                    continue
                if self.is_there_ship(self.statki, po) == 1:
                    score += 1
                    if self.with_bot:
                        print("Trafiono w statek")
                    else:
                        heal += 1
                        print("Trafiono w statek (+1 punkt życia)")
                    self.statki.remove(po)
                    customtable = {
                        "pos": po,
                        "hit": 1
                    }
                    my_hits.append(customtable)
                else:
                    if self.with_bot:
                        print("Nie trafiono w statek")
                    else:
                        heal -= 1
                        print("Nie trafiono w statek (-1 punkt życia)")

                    customtable = {
                        "pos": po,
                        "hit": 0
                    }
                    my_hits.append(customtable)
                self.create_table(my_hits, bot_hits)

            if heal==0:
                # print("koniec życia")
                break
            if len(self.statki) == 0:
                # print("koniec statkow bota")
                self.create_table(my_hits, bot_hits)
                break

            if self.with_bot:
                # ustawienia komputera
                print("Tura komputera")
                time.sleep(2)
                bot_shoot_x = 0
                bot_shoot_y = 0
                trafione = None
                while True:
                    bot_shoot_x = randrange(1, self.width+1)
                    bot_shoot_y = randrange(0, self.height)

                    bot_shoot = "x" + str(bot_shoot_x) + "y"+str(bot_shoot_y)
                    customtable = {}
                    if self.ishereshoot(bot_shoot, bot_hits) != 2:
                        if self.debug:
                            print("Bot strzelić pole " + bot_shoot + " ale już tu strzelał ")
                            print(bot_hits)
                        continue
                    if self.is_there_ship(mojestatki, bot_shoot) == 1:
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
                self.create_table(my_hits, bot_hits)
            
            if len(mojestatki) == 0 and self.with_bot:
                # print("nie mam statkow")
                break
        if stopped == 1:
            print("Game stopped")
        elif heal == 0:
            print("Game Over Score: " + str(score))
        else:
            if len(mojestatki) == 0 and self.with_bot:
                print("Przegrana Score: " + str(score))
            elif len(self.statki) == 0:
                print("WIN Score: " + str(score))

# ShipsGame(with_bot=True, ship_cout=10, width=10, height=10)
# f = ["dwa", "trzy"]
# f.insert(0, "jeden")
# f.insert(-0, "cztery")
# print(f)