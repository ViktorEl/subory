
def nacitaj_subor(nazov):
    with open(nazov, 'r', encoding='utf-8') as f:
        nacitany = f.readlines()
        return nacitany

nacitany_subor = nacitaj_subor('odbory.txt')
print(nacitany_subor)