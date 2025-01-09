

def nacitanie_suboru(nazov):
    with open(nazov, 'r', encoding='utf-8') as f:
        nacitany_subor = f.readlines()
        return nacitany_subor



'''Funkcia podla zadaneho mena a predmetu vrati prislusnu znamku'''
def znamka_podla_mena(meno, predmet, zoznam):
    for prvok in zoznam:
        rozdelenie = prvok.split(',') # ['Alex', 'SIE', '2\n']
        meno_ziaka = rozdelenie[0].strip()
        predmet_ziaka = rozdelenie[1].strip()
        znamka = rozdelenie[2]
        znamka = int(znamka)
        if meno == meno_ziaka and predmet == predmet_ziaka:
            return znamka
    else:
        return 'meno alebo predmet neexistuje'



  
ziaci = nacitanie_suboru('subor.txt')
#print(znamka_podla_mena('Milan', 'SIE', ziaci))