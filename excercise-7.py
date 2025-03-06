# Aufgabe 1
def index_min(L):
    min = 0
    for x in range(1,len(L)):
        if L[x]<= L[min]:
            min = x
    return min

# Aufgabe 2 a)
def temp_abnahme(L):
    abnahme = 0
    for i in range(len(L)-1):
        for j in range(i+1,len(L)):
            if abnahme < L[i]-L[j]:
                abnahme = L[i]-L[j]
    return abnahme

# Aufgabe 2 b)
def temp_abnahme_schnell(L):
    abnahme = 0
    max = 0
    for i in range(1,len(L)):
        if L[i]>L[max]:
            max = i
        elif abnahme < L[max]-L[i]:
            abnahme = L[max]-L[i]
    return abnahme