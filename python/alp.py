znaki = ["a","b","c","d","e","f","g","h","i", "j", "k", "l", "m", "n", "o", "p", "r", "s", "t", "u", "w", "y", "z"]
        # 0   1   2   3   4   5   6   7   8   9   10  1   2   3   4   5   6   7   8   9   20  1   2
        # 3   4   5   6   7   8   9   30  1   2   3   4   5   6   7   8   9   40  1   2   3   4   5
        # 6   7   8   9   50  1   2   3   4   5   6   7   8   9   60  1   2   3   4   5   6   7   8
pop = []

def same(stre):
    for i in range(len(stre)-1):
        if stre[i] != stre[i+1]:
            return False, stre[0]
    return True, stre[0]


def up(stre, index):
    char = stre[index:index+1]
    podmiana = False
    new_charindex = znaki.index(char)+1
    if (new_charindex >= len(znaki)):
        podmiana = True
    if podmiana:
        samee, character = same(stre)
        stre = stre[:index] + znaki[0] + stre[index+1:]
        if samee and character==znaki[len(znaki)-1]:
            dlugos = len(stre)+1
            stre = ""
            for k in range(dlugos):
                stre += znaki[0]
        else:
            stre = up(stre, index-1)
    else:
        new_char = znaki[new_charindex]
        stre = stre[:index] + new_char + stre[index+1:]
    return stre



dlugosc = 25
for i in range(dlugosc):
    lastchars = None
    if (len(pop) == 0):
        lastchars = znaki[i]
        pop.append(lastchars)
        print("Daje nowy element " + lastchars)
        continue
    else:
        lastchars = pop[len(pop)-1]
        print("Last char: " + lastchars + " dlugosc listy " + str(len(pop)))
    
    char = lastchars[len(lastchars)-1:]
    new_charindex = znaki.index(char)+1
    lastchars = up(lastchars, len(lastchars)-1)
    pop.append(lastchars)
    print(str(i) + " ==> " + lastchars)
    print("==================================================================")