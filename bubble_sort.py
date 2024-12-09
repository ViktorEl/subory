
zoznam = [2, 1, 8, 7, 5, 4, 9]

def bublinkove_usporiadanie(zoznam):
    for i in range(1, len(zoznam)):
        if zoznam[i] < zoznam[i-1]:
            zoznam[i], zoznam[i-1] = zoznam[i-1], zoznam[i]

bublinkove_usporiadanie(zoznam)
print(zoznam)
