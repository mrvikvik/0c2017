navn = ['Jonas', 'Clara', 'Niels', 'Karla', 'Jens', 'Viktor']
verbum = ['køber', 'spiser', 'slår', 'leger med', 'laver', 'bliver spist af']
sub = ['en løve', 'en cykel', 'et fly', 'en firkant', 'et hus', 'en bøvs']
from random import randint
def vaelg(ord):
    antal_ord = len(ord)
    antal_valgt = randint(0, antal_ord - 1)
    ord_valgt = ord[antal_valgt]
    return ord_valgt
while True:
    print(vaelg(navn), vaelg(verbum), vaelg(sub), end='.')
    input()
