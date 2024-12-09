
def nacitaj_subor(nazov):
    with open(nazov, 'r', encoding='utf-8') as f:
        nacitany = f.readlines()
        return nacitany

def pocet_ziakov_spolu(zoznam):
    return len(zoznam)

nacitany_subor = nacitaj_subor('odbory.txt')
#print(pocet_ziakov_spolu(nacitany_subor))
