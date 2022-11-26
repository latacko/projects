l = [8,10,6,2,4]
something_change = True
steps = 0
while something_change:
    test = False
    for i in range(len(l)-1):
        steps += 1
        if l[i+1] < l[i]:
            old = l[i+1]
            l[i+1] = l[i]
            l[i] = old
            print("Krok " + str(steps) + " " + str(l))
            test = True
        else:
            print("Krok " + str(steps) + " nic nie robi")
        something_change = test
print("Koniec: " + str(l))