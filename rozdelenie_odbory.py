
def nacitaj_subor(nazov):
    with open(nazov, 'r', encoding='utf-8') as f:
        nacitany = f.readlines()
        return nacitany

def pocet_ziakov_spolu(zoznam):
    return len(zoznam)

def pocet_ziakov_podla_odboru(zoznam, odbor):
    pocet = 0
    for ziak in zoznam:
        rozdeleny = ziak.split(',') # ['Radovan Kliescik', 'IST\n']
        meno = rozdeleny[0]
        odbor_ziaka = rozdeleny[1].strip()
        if odbor_ziaka == odbor:
            pocet += 1
    return pocet




nacitany_subor = nacitaj_subor('odbory.txt')
#print(pocet_ziakov_spolu(nacitany_subor))
print(pocet_ziakov_podla_odboru(nacitany_subor, 'IST'))
