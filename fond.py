
def uloz_do_suboru(nazov_suboru, hodnoty):
    try:
        with open(nazov_suboru, 'w', encoding='utf-8') as f:
            #f.write()
            f.writelines(hodnoty)
    except PermissionError:
        raise PermissionError('chyba do suboru sa neda zapisovat')


def nacitaj_subor(nazov_suboru):
    try:
        with open(nazov_suboru, 'r', encoding='utf-8') as f:
            nacitany_subor = f.readlines()
            #nacitany_riadok = f.readline()
            #nacitany_subor = f.read()
            return nacitany_subor
    except FileNotFoundError:
        uloz_do_suboru(nazov_suboru, [])
        
    
def registruj_vklad(meno, vklad, zoznam):
    zoznam.append(f'{meno}, {vklad}\n')

def registruj_vyber(meno, vyber, zoznam):
    zoznam.append(f'{meno}, -{vyber}\n')

def zisti_zostatok(zoznam):
    zostatok = 0
    for prvok in zoznam:                    # prvok je zatial string 'Karol, 5'
        oddeleny_retazec = prvok.split(',') # ['Karol', '5\n']
        suma = float(oddeleny_retazec[1])  # vybrali sme prvok sumu a pretypovali na float
        zostatok = zostatok + suma
    return zostatok

def zisti_zostatok_podla_mena(zoznam, meno):
    zostatok = 0
    for prvok in zoznam:
        oddelene = prvok.split()
        meno_v_stringu = oddelene[0]
        meno_v_stringu = meno_v_stringu.replace(',', '')
        suma = float(oddelene[1])
        if meno_v_stringu == meno:
            zostatok = zostatok + suma
    return zostatok

def zisti_zostatok_podla_mien(zoznam):
    slovnik = {}
    for prvok in zoznam:
        oddeleny_prvok = prvok.split(',')
        meno = oddeleny_prvok[0]
        suma = float(oddeleny_prvok[1])
        if meno in slovnik:
            slovnik[meno] += suma
        else:
            slovnik[meno] = suma
    return slovnik







nacitany_subor = nacitaj_subor('triedny_fond.txt')
registruj_vklad('Jano', 50, nacitany_subor)
registruj_vyber('Jozo', 5, nacitany_subor)
registruj_vklad('Viktor', 50, nacitany_subor)
print(zisti_zostatok(nacitany_subor))
print(zisti_zostatok_podla_mena(nacitany_subor, 'Jozo'))
print(zisti_zostatok_podla_mien(nacitany_subor))
#uloz_do_suboru('triedny_fond.txt', nacitany_subor)
print(nacitany_subor)