
slovnik = {'Jozo': 15, 'Jano': 20}

#print(slovnik['Jozo'])
#print(slovnik['Jano'])
slovnik['Jozo'] += 20

for kluc, hodnota in slovnik.items():
    print(kluc)
    print(hodnota)
