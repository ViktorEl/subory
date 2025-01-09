
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


'''Funkcia vráti zoznam neprospievajucich ziakov z daného predmetu'''
def neprospievajuci(predmet, zoznam):
    novy_zoznam = []
    for prvok in zoznam:
        rozdelenie = prvok.split(',') 
        meno_ziaka = rozdelenie[0].strip()
        predmet_ziaka = rozdelenie[1].strip()
        znamka = rozdelenie[2]
        znamka = int(znamka)
        if znamka == 5 and predmet == predmet_ziaka:
            novy_zoznam.append(f'{meno_ziaka}, {predmet_ziaka}\n')

    return novy_zoznam

def vsetci_neprospievajuci(zoznam):
    n_siete = neprospievajuci('SIE', zoznam)
    n_sjl = neprospievajuci('SJL', zoznam)
    spolu_predmety = n_siete + n_sjl
    return spolu_predmety

def uloz_do_suboru(nazov, udaje):
    with open(nazov, 'w', encoding='utf-8') as f:
        f.writelines(udaje)


  
ziaci = nacitanie_suboru('subor.txt')
# print(znamka_podla_mena('Milan', 'SIE', ziaci))
#print(neprospievajuci('SJL', ziaci))
neprospievajuci_vsetci_ziaci = vsetci_neprospievajuci(ziaci)
uloz_do_suboru('subor2.txt', neprospievajuci_vsetci_ziaci)