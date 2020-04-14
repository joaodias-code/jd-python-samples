# Códigos para testes e aprendizado.
# Leitura do livro: Ramalho, Luciano. Fluent Python (p. 5). O'Reilly Media. Edição do Kindle. 
# Treinando "Data Model" do Python
import collections
from random import choice

Card = collections.namedtuple('Card', ['rank', 'suit'])
print(Card)

class frenchdeck:
    ranks = [str(n) for n in range(2,11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits
                                       for rank in self.ranks]

    def __len__(self): 
        return len(self._cards)
    
    def __getitem__(self, position): 
        return self._cards[position]

       
# -----------------------------
# Testes:
# -----------------------------
beer_card = Card('7', 'diamonds') 
print(beer_card )

deck = frenchdeck() 
#len(deck)
print(deck[0])
print(deck[-1])

#pegar carta aleatória (função choice do python para interator)
print("Carta aleatória: " + str(choice(deck)))
print("Carta aleatória: " + str(choice(deck)))

#ordernar o baralho
suit_values = dict(spades=3, hearts=2, diamonds=1, clubs=0)

def spades_high(card): 
    rank_value = frenchdeck.ranks.index(card.rank) 
    return rank_value * len(suit_values) + suit_values[card.suit]

for card in sorted(deck, key=spades_high):
    print(card)




