moja_lista = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]

del_c = 0
for i in range(len(moja_lista)):
    exi = True
    copy = moja_lista[:]
    del copy[i-del_c]
    if moja_lista[i-del_c] in copy:
        dfsd = moja_lista[i-del_c]
        del moja_lista[i-del_c]
        del_c +=1


print("Lista tylko z unikalnymi elementami:")
print(moja_lista)