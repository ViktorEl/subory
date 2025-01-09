

zoznam1 = [1, 5, 4, 2]
zoznam2 = [2, 5, 4, 1]

# sposob 1
novy_zoznam = zoznam1 + zoznam2
print(novy_zoznam)

# sposob 2 Vysvetlenie extend
zoznam1.extend(zoznam2)
print(zoznam1)
