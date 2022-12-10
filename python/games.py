import statki as Statki
import ttt as TTT

game = input("W jaką gre chcesz zagrać? (ttt, statki)\n")
game.lower().replace(" ", "")
if game == "ttt":
    ttt = TTT.GameSettings(width=5, sign_to_win=5, debug=False)
    ttt.Start()
elif game == "statki":
    statki = Statki.GameSettings(with_bot=True, ship_cout=2, width=5, height=5)
    statki.Run()
