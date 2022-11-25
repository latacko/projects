def random_string(ciag, znakow=9999999999999999):
    wsp_x=list(ciag)
    wsp_y_count=len(wsp_x)
    for znak in wsp_x:
        for litera in ciag:
            # if len(znak) == znakow or wsp_y_count >= wsp_y:
            if len(znak) == znakow:
                return wsp_x
            print("dodaje " + znak+litera, end=" | ")
            wsp_x.append(znak+litera)
            wsp_y_count+=1
    
adresy=random_string("abcdefghijklmnoprstuwyz2016!@#$%^&*()", 16)[:]
print(adresy)