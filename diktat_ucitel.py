

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


nacitany_text = nacitaj_subor('ucitel.txt')
