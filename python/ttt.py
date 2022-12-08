from random import random, randrange


debug = True
tete = 5
ile_do_zwy = 4
if debug:
    plansza = [[ " " for i in range(tete)] for j in range(tete)]
else: 
    plansza = [[ " " for i in range(tete)] for j in range(tete)]

if tete < 2:
    print("Plansza nie może być mniejsza niż 2 znaki")
    exit()

def display_board(board):
    iloscsrodkowychpol = tete-1
    print("-----" + "----"*iloscsrodkowychpol)
    for x in board:
        for i in range(len(x)):
            y = x[i]
            if i == 0:
                print(f"| {y} |", end="")
            else:
                print(f" {y} |", end="")
        print()
        print("-----" + "----"*iloscsrodkowychpol)

def enter_move(board):
    p_pole = input(f"Podaj pole od 1 do {tete*tete}: ")
    if (not isinstance(p_pole,int) and not p_pole.isnumeric):
        print("Nie prawidłowe pole")
        enter_move(board)
        return
    p_pole = int(p_pole)-1
    if p_pole < 0 or p_pole > tete*tete-1:
        print("Nie prawidłowe pole")
        enter_move(board)
    else:
        height = p_pole//tete
        nr = p_pole % tete
        pole = board[height][nr]
        if pole==" ":
            board[height][nr] = "O"
        else:
            print("Nie prawidłowe pole")
            enter_move(board)

def make_list_of_free_fields(board):
    lis = []
    for k in range(len(board)):
        for v in range(len(board[k])):
            if board[k][v] == " ":
                lis.append((k,v))
    return lis

# make_list_of_free_fields(plansza)

# def tet_piority_for_po(board, sign, po, debug = False):
#     seks = [
#         (1, 0),
#         (1, 1),
#         (0, 1),
#         (-1, 1),
#         (-1, 0),
#         (-1, -1),
#         (0, -1),
#         (1, -1),
#     ]
#     mozliwosci_wygranej = []
#     for sek in seks:
#         if debug:
#             print(f"===================SEKWENCJA {sek} =======================")
#         for x in range(0, ile_do_zwy):
#             to_test_k = po[0] + sek[0]*x
#             to_test_v = po[1] + sek[1]*x
#             if to_test_k < 0  or to_test_v < 0 or to_test_k >= tete or to_test_v >= tete:
#                 break
#             # print(f"Sprawdzam {x} pole {to_test_k} {to_test_v} czy ma znak {sign} wynik {board[to_test_k][to_test_v] != sign}")
#             if board[to_test_k][to_test_v] != sign:
#                 if board[to_test_k][to_test_v] == " ":
#                     if debug:
#                         print(f"> Komputer: pole {(to_test_k,to_test_v)} ma znak |{board[to_test_k][to_test_v]}| i piorytet {x}")
#                     ile_zostalo_do_zw = x
#                     for i in range(x, ile_do_zwy):
#                         ile_zostalo_do_zw += 1
#                         to_test_k = po[0] + sek[0]*ile_zostalo_do_zw
#                         to_test_v = po[1] + sek[1]*ile_zostalo_do_zw
#                         if to_test_k < 0  or to_test_v < 0 or to_test_k >= tete or to_test_v >= tete:
#                             if to_test_k < 0:
#                                 to_test_k += 1
#                             if to_test_v < 0:
#                                 to_test_v += 1
#                             if to_test_k < tete:
#                                 to_test_k -= 1
#                             if to_test_v < tete:
#                                 to_test_v -= 1

#                             return tet_piority_for_po(board, sign, (to_test_k,to_test_v))
#                         if board[to_test_k][to_test_v] != " ":
#                             break
#                     if ile_zostalo_do_zw ==ile_do_zwy:
#                         mozliwosci_wygranej.append({"piority":x, "po": (to_test_k,to_test_v)})
#                 break
#         else:
#             return True, None
#     return False, mozliwosci_wygranej

def tet_piority_for_po(board, sign, po, debug = False):
    seks = [
        (1, 0),
        (1, 1),
        (0, 1),
        (-1, 1),
        (-1, 0),
        (-1, -1),
        (0, -1),
        (1, -1),
    ]
    mozliwosci_wygranej = []
    for sek in seks:
        if debug:
            print(f"===================SEKWENCJA {sek} =======================")
        for x in range(0, ile_do_zwy):
            to_test_k = po[0] + sek[0]*x
            to_test_v = po[1] + sek[1]*x
            if to_test_k < 0  or to_test_v < 0 or to_test_k >= tete or to_test_v >= tete:
                if to_test_k < 0:
                    to_test_k += 1
                if to_test_v < 0:
                    to_test_v += 1
                if to_test_k < tete:
                    to_test_k -= 1
                if to_test_v < tete:
                    to_test_v -= 1
                state, mzw = tet_piority_for_po(board, sign, (to_test_k, to_test_v), debug)
                mozliwosci_wygranej += mzw
                break
            # print(f"Sprawdzam {x} pole {to_test_k} {to_test_v} czy ma znak {sign} wynik {board[to_test_k][to_test_v] != sign}")
            if board[to_test_k][to_test_v] != sign:
                if board[to_test_k][to_test_v] == " ":
                    if debug:
                        print(f"> Komputer: pole {(to_test_k,to_test_v)} ma znak |{board[to_test_k][to_test_v]}| i piorytet {x}")
                    ile_zostalo_do_zw = x
                    for i in range(x, ile_do_zwy):
                        ile_zostalo_do_zw += 1
                        to_test_k = po[0] + sek[0]*ile_zostalo_do_zw
                        to_test_v = po[1] + sek[1]*ile_zostalo_do_zw
                        if to_test_k < 0  or to_test_v < 0 or to_test_k >= tete or to_test_v >= tete:
                            if to_test_k < 0:
                                to_test_k += 1
                            if to_test_v < 0:
                                to_test_v += 1
                            if to_test_k < tete:
                                to_test_k -= 1
                            if to_test_v < tete:
                                to_test_v -= 1

                            return tet_piority_for_po(board, sign, (to_test_k,to_test_v))
                        if board[to_test_k][to_test_v] != " ":
                            break
                    if ile_zostalo_do_zw ==ile_do_zwy:
                        mozliwosci_wygranej.append({"piority":x, "po": (to_test_k,to_test_v)})
                break
        else:
            return True, None
    return False, mozliwosci_wygranej

def victory_for(board, sign, debug=False):
    
    li = make_list_of_free_fields(board)
    mozliwosci_wygranej = []
    for k in range(tete):
        for v in range(tete):
            if not (k, v) in li and board[k][v] == sign:
                stete, mozliwosci_wygranej = tet_piority_for_po(board, sign, (k, v))
                if stete:
                    return stete, mozliwosci_wygranej
                # for sek in seks:
                #     if debug:
                #         print(f"===================SEKWENCJA {sek} =======================")
                #     for x in range(0, ile_do_zwy):
                #         to_test_k = k + sek[0]*x
                #         to_test_v = v + sek[1]*x
                #         if to_test_k < 0  or to_test_v < 0 or to_test_k >= tete or to_test_v >= tete:
                #             break
                #         # print(f"Sprawdzam {x} pole {to_test_k} {to_test_v} czy ma znak {sign} wynik {board[to_test_k][to_test_v] != sign}")
                #         if board[to_test_k][to_test_v] != sign:
                #             if board[to_test_k][to_test_v] == " ":
                #                 if debug:
                #                     print(f"> Komputer: pole {(to_test_k,to_test_v)} ma znak |{board[to_test_k][to_test_v]}| i piorytet {x}")
                #                 ile_zostalo_do_zw = x
                #                 for i in range(x, ile_do_zwy):
                #                     if
                #                     ile_zostalo_do_zw += 1

                #                 mozliwosci_wygranej.append({"piority":x, "po": (to_test_k,to_test_v)})
                #             break
                #     else:
                #         return True, None
                break
    return False, mozliwosci_wygranej


#
# Funkcja, która dokonuje analizy stanu tablicy w celu sprawdzenia
# czy użytkownik/gracz stosujący "O" lub "X" wygrał rozgrywkę.
#
def takeSecond(elem):
    return elem["piority"]
def draw_move(board):
    # print("> Komputer: zaczynam sprawdzać pola i pioritety ich")
    # print("> Komputer: Sprawdzam piorytet gracza: =============================== GRACZ ==================")
    wygrana2, mozliwosci_gracza = victory_for(board, "O", debug=True)
    # print("> Komputer: Sprawdzam piorytety moje: =============================== MOJE ==================")
    wygrana, mozliwosci_moje = victory_for(board, "X", debug=True)
    # print("> Komputer: Zaczynam sortować piorytety: ")
    mozliwosci_gracza.sort(key=takeSecond, reverse=True)
    mozliwosci_moje.sort(key=takeSecond, reverse=True)
    # print(f"Możliwości gracza: {mozliwosci_gracza}")
    # print(f"Możliwości moje: {mozliwosci_moje}")
    if len(mozliwosci_moje) == 0 or (len(mozliwosci_gracza) == 0 and len(mozliwosci_moje) == 0):
        le = make_list_of_free_fields(board)
        po = le[randrange(0, len(le)-1)]
        board[po[0]][po[1]] = "X"
        # print("> Komputer: nie ma możliwośc co jest dziwne")
    else:
        # print(f"> Komputer: Najlepsze logicznie pole gracza to: { mozliwosci_gracza[0] }")
        # print(f"> Komputer: Najlepsze logicznie pole moje to: { mozliwosci_moje[0] }")

        po_my = mozliwosci_moje[0]["po"]
        pio_my = mozliwosci_moje[0]["piority"]
        pio_enemy = -1
        if (len(mozliwosci_gracza) != 0):
            po_enemy = mozliwosci_gracza[0]["po"]
            pio_enemy = mozliwosci_gracza[0]["piority"]
        if pio_enemy > pio_my:
            # print(f"> Komputer: stawiam na pole {po_enemy} aby zablokować przeciwnikowi możliwości")
            board[po_enemy[0]][po_enemy[1]] = "X"
        else:
            # print(f"> Komputer: stawiam na pole {po_my} aby mieć więcej punktów")
            board[po_my[0]][po_my[1]] = "X"

#
# Funkcja, która wykonuje ruch za komputer i aktualizuje tablicę.

def Start():
    sr = tete//2
    plansza[sr][sr] = "X"
    display_board(plansza)
    while True:
        enter_move(plansza)
        display_board(plansza)
        # print(victory_for(plansza, "O"))
        print("=================================================================")
        if victory_for(plansza, "O")[0]:
            break
        draw_move(plansza)
        display_board(plansza)
        if victory_for(plansza, "X")[0]:
            break
    if victory_for(plansza, "O")[0]:
        print("wygrał grasz")
    else:
        print("wygrał bot")

Start()