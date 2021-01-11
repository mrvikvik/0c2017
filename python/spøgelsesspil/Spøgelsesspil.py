# Spøgelselspil
from random import randint
print('Spøgelselspil')
foeler_sig_modig = True
score = 0
while foeler_sig_modig:
    spoegelsesdoer = randint(1, 3)
    print('Tre døre foran dig')
    print('Et spøgelse bag en af dem')
    print('Hvilken dør åbner du?')
    doer = input('1, 2 eller 3?')
    doer_num = int(doer)
    if doer_num == spoegelsesdoer:
        print('SPØGELSE!')
        foeler_sig_modig = False
    else:
        print('Intet spøgelse!')
        print('Du går ind i næste rum')
        score = score + 1
print('Løb væk!')
print('Spillet er slut! Du scorede', score)

    
