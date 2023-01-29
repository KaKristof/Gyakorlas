# Kísértetház
from random import randint
print('Kísértetház')
bator_vagyok = True
pontszam = 0
while bator_vagyok:
    szellem_ajto = randint(1, 3)
    print('Három ajtó van előtted...')
    print('Az egyik mögött szelem van.')
    print('Melyiket nyitod ki?')
    ajto = input('1, 2 vagy 3?')
    ajto_szam = int(ajto)
    if ajto_szam == szellem_ajto:
        print('SZELLEM!')
        bator_vagyok = False
    else:
        print('Nincs szellem!')
        print('Lépj be a következő szobába!')
        pontszam = pontszam + 1
print('Menekülj!')
print('Vége a játéknak! Az elért pontszám: ', pontszam)
