from random import random, randrange


debug = True
tete = 3
ile_do_zwy = 3
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
        height = p_pole//3
        nr = p_pole % 3
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

def victory_for(board, sign):
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
    li = make_list_of_free_fields(board)
    mozliwosci_wygranej = []
    for k in range(tete):
        for v in range(tete):
            if not (k, v) in li:
                for sek in seks:
                    # print(f"===================SEKWENCJA {sek} =======================")
                    for x in range(0, ile_do_zwy):
                        to_test_k = k + sek[0]*x
                        to_test_v = v + sek[1]*x
                        if to_test_k < 0  or to_test_v < 0 or to_test_k >= tete or to_test_v >= tete:
                            break
                        # print(f"Sprawdzam {x} pole {to_test_k} {to_test_v} czy ma znak {sign} wynik {board[to_test_k][to_test_v] != sign}")
                        if board[to_test_k][to_test_v] != sign:
                            mozliwosci_wygranej.append({"piority":x, "po": {k,v}})
                            break
                    else:
                        return True, None
                break
    return False, mozliwosci_wygranej
#
# Funkcja, która dokonuje analizy stanu tablicy w celu sprawdzenia
# czy użytkownik/gracz stosujący "O" lub "X" wygrał rozgrywkę.
#
def takeSecond(elem):
    return elem["piority"]
def draw_move(board):
    wygrana, mozliwosci = victory_for(board, "X")
    mozliwosci.sort(key=takeSecond, reverse=True)
    if len(mozliwosci) == 0:
        le = make_list_of_free_fields(board)
        po = le[randrange(0, len(le)-1)]
        board[po[0]][po[1]] = "X"
    else:
        print(mozliwosci)
        po = mozliwosci[0][1]
        board[po[0]][po[1]] = "X"

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