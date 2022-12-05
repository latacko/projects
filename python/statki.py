import pygame
from random import randrange
from time import sleep as t_sleep
from sys import exit as sys_exit
from os import path as os_path
from threading import Thread

# =========== POBIERANIE PYGAME ================
# python -m pip install -U pygame --user

class ShipsGame:
    def __init__(self, width=5, height=5, ship_cout=5, health=5, with_bot=False, graphic = True, letters="abcdefghijklmnoprstuwyz", debug=False):
        # game settings
        self.gameStarted = False
        self.letters = letters
        self.ilosczyc = health
        self.iloscstatkow = ship_cout
        self.width =width
        self.height = height
        self.with_bot = with_bot
        self.debug = debug
        self.show_expolsion = False
        self.score = 0
        self.graphic = graphic
        self.setingship = False
        # values
        self.statki = []
        self.znaki_na_wysokosc = []
        self.ilosczniszczonychstatkow = 0
        self.my_hits = []
        self.bot_hits = []
        self.createshipuser = False
        self.mojestatki = []



        self.__path__ = os_path.dirname(__file__)
        print(self.__path__)

        if self.graphic:
            self.size = [500, 340]
            if self.with_bot:
                self.size = [828, 358]
            self.screen = pygame.display.set_mode(self.size)
            pygame.display.set_caption('Statki')
        
            self.myp = []
            for i in range(self.width*self.height+1):
                self.myp.append(pygame.image.load(f"{self.__path__}\\square.png"))
            self.byp = []
            if self.with_bot:
                for i in range(self.width*self.height+1):
                    self.byp.append(pygame.image.load(f"{self.__path__}\\square.png"))
            self.explosion = pygame.image.load(f"{self.__path__}\\explosion.png")
            self.water_splash = pygame.image.load(f"{self.__path__}\\water_splash.png")

            self.missed = []
            for i in range(((self.width*self.height)*2)-(self.iloscstatkow*2)):
                self.missed.append(pygame.image.load(f"{self.__path__}\\x.png"))
            self.hitted = []
            for i in range(self.iloscstatkow*2):
                self.hitted.append(pygame.image.load(f"{self.__path__}\\hit_ship.png"))

            self.mojestatki_spray = []
            for i in range(self.iloscstatkow):
                self.mojestatki_spray.append(pygame.image.load(f"{self.__path__}\\moj_statek.png"))

            self.loose_text = pygame.image.load(f"{self.__path__}\\lose.png")
            self.win_text = pygame.image.load(f"{self.__path__}\\win.jpg")

        # Thread(target = self.ShowGameWindows).start()
        Thread(target = self.bganimate).start()
        Thread(target = self.Start).start()
        if self.graphic:
            self.ShowGameWindows()
        # self.ShowGameWindows()
    
    def ShowGameWindows(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT: 
                    sys_exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    x, y = event.pos
                    if self.insquare(event.pos) != False and not self.createshipuser and self.setingship:
                        i, x2, y2 = self.insquare(event.pos)
                        print(f"Lewa x{x2}y{y2}")
                        is_hi = self.ishereshoot(f"x{x2+1}y{y2}", self.my_hits)
                        if self.debug:
                            print(f"Sprawdzam czy na polu x{x2}y{y2+1} jest trafienie {is_hi}")
                        if is_hi == 2:
                            self.show_expolsion = [x2*50+20, y2*50+20, 0]
                            Thread(target = self.expolsioneddect).start()
                            print(f"Strzelam na pole x{x2+1}y{y2} statki bota: {self.statki}")
                            trafione = self.Shoot(f"x{x2+1}y{y2}", self.statki, True)
                        self.setingship = False
                    elif self.createshipuser and self.insquare(event.pos, "right") != False and len(self.mojestatki)<self.iloscstatkow:
                        i, x2, y2 = self.insquare(event.pos, "right")
                        if not f"x{x2+1}y{y2}" in self.mojestatki:
                            self.mojestatki.append(f"x{x2+1}y{y2}")
                            # if self.debug:
                            print(self.mojestatki)
                    # else:
                        # print("nigdzie nie klikam")
            if self.show_expolsion != False:
                if self.show_expolsion[2]:
                    self.screen.blit(self.explosion, [self.show_expolsion[0],self.show_expolsion[1]])
                else:
                    self.screen.blit(self.water_splash, [self.show_expolsion[0],self.show_expolsion[1]])

            id_obrazka = -1
            show_missed = -1
            show_hitteded = -1
            moje_statki_sprte = -1

            for x in range(self.width):
                for y in range(self.height):
                    id_obrazka = id_obrazka+1
                    self.screen.blit(self.myp[id_obrazka], [50*y+20,50*x+20])
                    is_here = self.ishereshoot(f"x{y+1}y{x}", self.my_hits)
                    if is_here != 2:
                        if is_here == 1:
                            show_hitteded += 1
                            self.screen.blit(self.hitted[show_hitteded], [50*y+20,50*x+20])
                        else:
                            show_missed += 1
                            self.screen.blit(self.missed[show_missed], [50*y+20,50*x+20])
            if self.with_bot:
                id_obrazka = 0
                for x in range(self.width):
                    for y in range(self.height):
                        id_obrazka = id_obrazka+1
                        sze = 50*self.width
                        odlewa = self.size[0] - sze - 20
                        self.screen.blit(self.byp[id_obrazka], [50*y+odlewa,50*x+20])
                        is_here2 = self.ishereshoot(f"x{y+1}y{x}", self.bot_hits)

                        if is_here2 != 2:
                            if is_here2 == 1:
                                show_hitteded += 1
                                self.screen.blit(self.hitted[show_hitteded], [50*y+odlewa,50*x+20])
                            else:
                                show_missed += 1
                                self.screen.blit(self.missed[show_missed], [50*y+odlewa,50*x+20])
                        elif f"x{y+1}y{x}" in self.mojestatki:
                            moje_statki_sprte += 1
                            self.screen.blit(self.mojestatki_spray[moje_statki_sprte], [50*y+odlewa,50*x+20])

            if self.gameStarted :
                if self.ilosczyc == 0:
                    self.screen.blit(self.loose_text, [0,0])
                else:
                    if len(self.mojestatki) == 0 and self.with_bot:
                        self.screen.blit(self.loose_text, [0,0])
                    elif len(self.statki) == 0:
                        self.screen.blit(self.win_text, [0,0])
            # pygame.display.flip()
            pygame.display.update()

    def bganimate(self):
        bg = []
        if not self.with_bot:
            for i in range(25):
                nr = i
                if i  < 10:
                    nr = "0"+str(i)
                bg.append(pygame.image.load(f"{self.__path__}\\bgframes\\without_bot\\frame_{nr}_delay-0.1s.gif"))
        else:
            for i in range(4):
                bg.append(pygame.image.load(f"{self.__path__}\\bgframes\\with_bot\\frame_{i}_delay-0.2s.gif"))
        tlorect = bg[0].get_rect()
        while True:
            for i in range(len(bg)):
                for img2 in bg:
                    if bg[i] != img2:
                        self.screen.blit(img2, [-1000, -1000])
                if not self.with_bot:
                    t_sleep(0.1)
                else:
                    t_sleep(0.2)
                self.screen.blit(bg[i], tlorect)
            for i in range(len(bg)-1, 1, -1):
                for img2 in bg:
                    if bg[i] != img2:
                        self.screen.blit(img2, [-1000, -1000])
                if not self.with_bot:
                    t_sleep(0.1)
                else:
                    t_sleep(0.2)
                self.screen.blit(bg[i], tlorect)

    def insquare(self, pos, side="left"):
        id = -1
        for x in range(self.width):
            for y in range(self.height):
                id = id+1
                min_x, min_y =50*x+20,50*y+20
                max_x, max_y =50*x+70,50*y+70
                # print("=================================")
                if side != "left":
                    # print("sprawdzam prawą stronę")
                    sze = 50*self.width
                    odlewa = self.size[0] - sze - 20
                    min_x, min_y =50*x+20,50*y+odlewa
                    max_x, max_y =50*x+70,50*y+50+odlewa
                # print(f"min x: {min_x} max x: {max_x}")
                # print(f"min y: {min_y} max y: {max_y}")
                if max_x > pos[1] and pos[1] > min_x and max_y > pos[0] and pos[0] > min_y:
                    return id, y, x
        return False

    def expolsioneddect(self):
        t_sleep(1)
        self.show_expolsion = False

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
        ilosczniszczonychstatkow = 0
        stopped = 0
        self.score = 0
        self.mojestatki = []
        global znaki_na_wysokosc
        znaki_na_wysokosc = self.ciongznakow(self.letters, self.height)
        while len(znaki_na_wysokosc) == 0:
            for i in range(1, 4):
                print("Loading" + "."*i)
                t_sleep(2)
            for i in range(2, 1, -1):
                print("Loading" + "."*i)
                t_sleep(2)

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
            if self.graphic:
                self.createshipuser = True
                while len(self.mojestatki) < self.iloscstatkow:
                    t_sleep(0.1)
                self.createshipuser = False
            else:
                for x in range(self.iloscstatkow):
                    print("Podaj miejsce statku np 4D (opcja wyboru od 1 do " + str(self.width) + " oraz od a do " +znaki_na_wysokosc[self.height-1]+")")
                    self.create_ship_user(self.mojestatki)
                if self.debug:
                    print(self.mojestatki)
        for x in range(self.iloscstatkow):
            self.create_ship()
        self.gameStarted = True
        while ilosczniszczonychstatkow<self.iloscstatkow and ilosczyc2>0:
            if not self.graphic:
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

                    if self.ishereshoot(po, self.my_hits) != 2:
                        print("Był już strzał w to pole")
                        continue
                    trafione = self.Shoot(po, self.statki, True)
                    # if trafione == "trafione" and self.with_bot:
                        # print("Trafiono w statek")
                    # if self.is_there_ship(self.statki, po) == 1:
                    #     self.score += 1
                    #     if self.with_bot:
                    #         print("Trafiono w statek")
                    #     else:
                    #         self.ilosczyc += 1
                    #         print("Trafiono w statek (+1 punkt życia)")
                    #     self.statki.remove(po)
                    #     customtable = {
                    #         "pos": po,
                    #         "hit": 1
                    #     }
                    #     self.my_hits.append(customtable)
                    # else:
                    #     if self.with_bot:
                    #         print("Nie trafiono w statek")
                    #     else:
                    #         self.ilosczyc -= 1
                    #         print("Nie trafiono w statek (-1 punkt życia)")

                    #     customtable = {
                    #         "pos": po,
                    #         "hit": 0
                    #     }
                    #     self.my_hits.append(customtable)
                    self.create_table(self.my_hits, self.bot_hits)
            else:
                self.setingship = True
                while self.setingship:
                    t_sleep(0.5)
                self.create_table(self.my_hits, self.bot_hits)
            if self.ilosczyc==0:
                # print("koniec życia")
                break
            if len(self.statki) == 0:
                # print("koniec statkow bota")
                self.create_table(self.my_hits, self.bot_hits)
                break

            if self.with_bot:
                # ustawienia komputera
                print("Tura komputera")
                t_sleep(2)
                bot_shoot_x = 0
                bot_shoot_y = 0
                trafione = None
                while True:
                    bot_shoot_x = randrange(1, self.width+1)
                    bot_shoot_y = randrange(0, self.height)

                    bot_shoot = "x" + str(bot_shoot_x) + "y"+str(bot_shoot_y)
                    if self.ishereshoot(bot_shoot, self.bot_hits) != 2:
                        if self.debug:
                            print("Bot strzelić pole " + bot_shoot + " ale już tu strzelał ")
                            print(self.bot_hits)
                        continue
                    trafione = self.Shoot(bot_shoot, self.mojestatki, False)
                    break
                    # if self.is_there_ship(self.mojestatki, bot_shoot) == 1:
                    #     self.mojestatki.remove(bot_shoot)
                    #     customtable = {
                    #         "pos": bot_shoot,
                    #         "hit": 1
                    #     }
                    #     trafione = "trafił"
                    #     self.bot_hits.append(customtable)
                    #     break
                    # else:
                    #     customtable = {
                    #         "pos": bot_shoot,
                    #         "hit": 0
                    #     }
                    #     trafione = "nie trafił"
                    #     self.bot_hits.append(customtable)
                        # break
                print("Komputer strzelił pole " + str(bot_shoot_x) + znaki_na_wysokosc[bot_shoot_y] + " i " +trafione)
                self.create_table(self.my_hits, self.bot_hits)
            
            if len(self.mojestatki) == 0 and self.with_bot:
                # print("nie mam statkow")
                break
        if stopped == 1:
            print("Game stopped")
        elif self.ilosczyc == 0:
            print("Game Over Score: " + str(self.score))
        else:
            if len(self.mojestatki) == 0 and self.with_bot:
                print("Przegrana Score: " + str(self.score))
            elif len(self.statki) == 0:
                print("WIN Score: " + str(self.score))

    def Shoot(self, pole, table, Player):
        trafione = ""
        if self.is_there_ship(table, pole) == 1:
            table.remove(pole)
            customtable = {
                "pos": pole,
                "hit": 1
            }
            trafione = "trafił"
            if Player:
                self.score += 1
                if self.with_bot:
                    print("Trafiono w statek")
                else:
                    self.ilosczyc += 1
                    print("Trafiono w statek (+1 punkt życia)")
                self.my_hits.append(customtable)
            else:
                self.bot_hits.append(customtable)
        else:
            customtable = {
                "pos": pole,
                "hit": 0
            }
            trafione = "nie trafił"
            if Player:
                if self.with_bot:
                    print("Nie trafiono w statek")
                else:
                    self.ilosczyc -= 1
                    print("Nie trafiono w statek (-1 punkt życia)")
                self.my_hits.append(customtable)
            else:
                self.bot_hits.append(customtable)
        return trafione

ShipsGame(with_bot=True, ship_cout=20, width=5, height=5)