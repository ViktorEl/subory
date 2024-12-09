

def nacitaj_subor(nazov_suboru):
    with open(nazov_suboru, 'r', encoding='utf-8') as f:
        nacitany = f.read()
        return nacitany

def vytvor_diktat_ziak(text, nahradit):
    novy_text = ''
    for pismeno in text:
        if pismeno in nahradit:
            novy_text = novy_text + '_'
        else:
            novy_text = novy_text + pismeno
    return novy_text


def uloz_do_suboru(nazov_suboru, text):
    with open(nazov_suboru, 'w', encoding='utf-8') as f:
        f.write(text)



nacitany_text = nacitaj_subor('ucitel.txt')
diktat_ziak = vytvor_diktat_ziak(nacitany_text, ['y', 'Ý', 'i', 'Í'])
uloz_do_suboru('ziak_diktat.txt', diktat_ziak)
