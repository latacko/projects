from random import random, randrange
# import statki
class GameSettings:
    def __init__(self, width, sign_to_win, debug = False, debug_numbers=False):
        self.debug = debug
        self.debug_numbers = debug_numbers
        self.width = width
        self.ile_do_zwy = sign_to_win
        self.public_seq = [
            (1, 0),
            (1, 1),
            (0, 1),
            (-1, 1),
            (-1, 0),
            (-1, -1),
            (0, -1),
            (1, -1),
        ]
        self.plansza = [[ " " for i in range(self.width)] for j in range(self.width)]

        if self.width < 2:
            print("Plansza nie może być mniejsza niż 2 znaki")
            exit()

    def display_board(self, board):
        iloscsrodkowychpol = self.width-1
        print("-----" + "----"*iloscsrodkowychpol)
        id = 0
        for x in board:
            for i in range(len(x)):
                id += 1
                if self.debug_numbers:
                    if x[i] == " ":
                        y = id
                    else:
                        y = x[i]
                else:
                    y = x[i]
                if i == 0:
                    if len(str(y)) == 3:
                        print(f"|{y}|", end="")
                    elif len(str(y)) == 2:
                        print(f"|{y} |", end="")
                    else:
                        print(f"| {y} |", end="")
                else:
                    if len(str(y)) == 3:
                        print(f"{y}|", end="")
                    elif len(str(y)) == 2:
                        print(f"{y} |", end="")
                    else:
                        print(f" {y} |", end="")
            print()
            print("-----" + "----"*iloscsrodkowychpol)
    
    def enter_move(self, board):
        p_pole = input(f"Podaj pole od 1 do {self.width*self.width}: ")
        if (not isinstance(p_pole,int) and not p_pole.isnumeric):
            print("Nie prawidłowe pole")
            self.enter_move(board)
            return
        p_pole = int(p_pole)-1
        if p_pole < 0 or p_pole > self.width*self.width-1:
            print("Nie prawidłowe pole")
            self.enter_move(board)
        else:
            height = p_pole//self.width
            nr = p_pole % self.width
            pole = board[height][nr]
            if pole==" ":
                board[height][nr] = "O"
            else:
                print("Nie prawidłowe pole")
                self.enter_move(board)
    
    def make_list_of_free_fields(self, board):
        lis = []
        for k in range(len(board)):
            for v in range(len(board[k])):
                if board[k][v] == " ":
                    lis.append((k,v))
        return lis
    
    # seq_can_success, ile do wygranej, gfzie postawic znak, wygrana   = test_seq
    def test_seq(self, board, seq_id, znak, pole, last=False, ile_potrzeba = None, debug=False):
        seq = self.public_seq[seq_id]
        pod_x = pole[0]
        pod_y = pole[1]
        if ile_potrzeba == None:
            ile_potrzeba = self.ile_do_zwy
        ile_zostalo = ile_potrzeba
        gdzie_postawic = None
        start_index = 0
        if last:
            start_index = 1
        if debug:
            if last:
                print(f"    ====================== {seq} POLE: {pole} =============================")
            else:
                print(f"====================== {seq} POLE: {pole} =============================")
        for i in range(start_index, ile_potrzeba):
            x = pod_x + seq[0]*i
            y = pod_y + seq[1]*i
            if debug:
                if last:
                    print(f"      > Sprawdzam pole {x, y}")
                else:
                    print(f"  > Sprawdzam pole {x, y}")
            if x < 0  or y < 0 or x >= self.width or y >= self.width:
                if last:
                    if debug:
                        print(f"      > Pole {(x,y)}, jest poza plansz a to ostatnie. Sewkwencja {seq} jest nie możliwa")
                    return False, ile_zostalo, gdzie_postawic, False
                to_seq = (seq[0]*-1, seq[1]*-1)
                new_seq_id = self.public_seq.index(to_seq)
                if debug:
                    print(f"  > Pole {(x,y)} poza planszą, więc szukam w drugą stronę")
                success_2, ile_zostalo_2, gdzie_postawic_2, wyg = self.test_seq(board, new_seq_id, znak, pole, last=True, ile_potrzeba=i-1, debug=debug)
                return success_2, ile_zostalo_2+1, gdzie_postawic, False

            znak_na_polu = board[x][y]

            if znak_na_polu in [" ", znak]:
                if znak_na_polu == znak:
                    ile_zostalo -= 1
                    if ile_zostalo == 0:
                        return True, ile_zostalo, gdzie_postawic, True
                    elif i==ile_potrzeba-1:
                        return True, ile_zostalo, gdzie_postawic, False

                elif znak_na_polu == " " and i==ile_potrzeba-1:
                    if gdzie_postawic == None:
                        gdzie_postawic = (x, y)
                    if debug:
                        if last:
                            print(f"      > Seq {seq} jest możliwa")
                        else:
                            print(f"  > seq {seq} jest możliwa")
                    return True, ile_zostalo, gdzie_postawic, False
                elif gdzie_postawic == None:
                    gdzie_postawic = (x, y)
                    if debug:
                        if last:
                            print(f"      > Ustawiam możliwość postawienia na {gdzie_postawic}")
                        else:
                            print(f"  > Ustawiam możliwość postawienia na {gdzie_postawic}")
            else:
                if last:
                    return False, ile_zostalo, gdzie_postawic, False
                to_seq = (seq[0]*-1, seq[1]*-1)
                if debug:
                    print(f"  > Przeciwnik ma znak na polu {(x,y)}, więc szukam w drugą stronę")
                new_seq_id = self.public_seq.index(to_seq)
                success_2, ile_zostalo_2, gdzie_postawic_2, wyg = self.test_seq(board, new_seq_id, znak, pole, True, ile_potrzeba=i-1, debug=debug)
                return success_2, ile_zostalo_2+1, gdzie_postawic, wyg
        return False, ile_zostalo, gdzie_postawic, False
    
    def victory_for(self, board, sign, debug=False):
        li = self.make_list_of_free_fields(board)
        mozliwosci_wygranej = []
        for k in range(self.width):
            for v in range(self.width):
                if not (k, v) in li and board[k][v] == sign:
                    for seq_id in range(len(self.public_seq)):
                        seq_can_success, to_winj, gdzie_postawic, wygrana = self.test_seq(board, seq_id, sign, (k, v), debug=debug)
                        if wygrana:
                            return wygrana, mozliwosci_wygranej
                        if debug:
                            print(f"Seq {self.public_seq[seq_id]} ma możliwość wygranej {seq_can_success}")
                        if seq_can_success:
                            if debug:
                                print(f"Dodaje możliwość wygranej {gdzie_postawic} piorytet {to_winj}")
                            mozliwosci_wygranej.append({"piority": to_winj, "po": gdzie_postawic})
                    break
        if debug:
            print(f"Możliwości {mozliwosci_wygranej}")
        return False, mozliwosci_wygranej
    
    
    #
    # Funkcja, która dokonuje analizy stanu tablicy w celu sprawdzenia
    # czy użytkownik/gracz stosujący "O" lub "X" wygrał rozgrywkę.
    #
    def takeSecond(self, elem):
        return elem["piority"]
    def draw_move(self, board):
        # pass
        # print("> Komputer: zaczynam sprawdzać pola i pioritety ich")
        print("> Komputer: Sprawdzam piorytet gracza: =============================== GRACZ ==================")
        wygrana2, mozliwosci_gracza = self.victory_for(board, "O", debug=True)
        print("> Komputer: Sprawdzam piorytety moje: =============================== MOJE ==================")
        wygrana, mozliwosci_moje = self.victory_for(board, "X", debug=True)
        print("> Komputer: Zaczynam sortować piorytety: ")
        mozliwosci_gracza.sort(key=self.takeSecond)
        mozliwosci_moje.sort(key=self.takeSecond)
        print(f"Możliwości gracza: {mozliwosci_gracza}")
        print(f"Możliwości moje: {mozliwosci_moje}")
        if len(mozliwosci_moje) == 0 or (len(mozliwosci_gracza) == 0 and len(mozliwosci_moje) == 0):
            if len(mozliwosci_gracza) == 0:
                print("> Komputer: nie ma możliwośc co jest dziwne")
                le = self.make_list_of_free_fields(board)
                if len(le) == 0:
                    po = le[0]
                    board[po[0]][po[1]] = "X"
                else:
                    po = le[randrange(0, len(le)-1)]
                    board[po[0]][po[1]] = "X"
                # wygrana3, mozliwosci_puste = victory_for(board, " ", debug=True)
                # mozliwosci_puste.sort(key=takeSecond)
                # board[mozliwosci_puste[0][0]][mozliwosci_puste[0][1]] = "X"
            else:
                po_enemy = mozliwosci_gracza[0]["po"]
                print(f"> Komputer: stawiam na pole {po_enemy} aby zablokować przeciwnikowi możliwości")
                board[po_enemy[0]][po_enemy[1]] = "X"
        else:
            if (len(mozliwosci_gracza) != 0):
                print(f"> Komputer: Najlepsze logicznie pole gracza to: { mozliwosci_gracza[0] }")
            else:
                print("> Gracz nie ma żadnej igicznie możliwości ruchu")
            print(f"> Komputer: Najlepsze logicznie pole moje to: { mozliwosci_moje[0] }")
    
            po_my = mozliwosci_moje[0]["po"]
            pio_my = mozliwosci_moje[0]["piority"]
            pio_enemy = -1
            if (len(mozliwosci_gracza) != 0):
                po_enemy = mozliwosci_gracza[0]["po"]
                pio_enemy = mozliwosci_gracza[0]["piority"]
            if pio_enemy < pio_my and pio_enemy != -1:
                print(f"> Komputer: stawiam na pole {po_enemy} aby zablokować przeciwnikowi możliwości")
                board[po_enemy[0]][po_enemy[1]] = "X"
            else:
                print(f"> Komputer: stawiam na pole {po_my} aby mieć więcej punktów")
                board[po_my[0]][po_my[1]] = "X"
    
    #
    # Funkcja, która wykonuje ruch za komputer i aktualizuje tablicę.
    
    def Start(self):
        sr = self.width//2
        self.plansza[sr][sr] = "X"
        self.display_board(self.plansza)
        while True:
            self.enter_move(self.plansza)
            self.display_board(self.plansza)
            # print(victory_for(plansza, "O"))
            print("========================================================================================================================"*3)
            if self.victory_for(self.plansza, "O")[0]:
                break
            self.draw_move(self.plansza)
            self.display_board(self.plansza)
            if self.victory_for(self.plansza, "X")[0]:
                break
        if self.victory_for(self.plansza, "O")[0]:
            print("wygrał grasz")
        else:
            print("wygrał bot")

if __name__ == "__main__":
    ttt = GameSettings(width=5, sign_to_win=5, debug=True, debug_numbers=True)
    ttt.Start()