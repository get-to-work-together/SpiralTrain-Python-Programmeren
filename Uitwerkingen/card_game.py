#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb  3 10:19:00 2023

@author: peter
"""

import random

class Speelkaart:
    
    KLEUREN = list('♣♦♥♠')
    RANGEN = list('23456789BVHA')
    
    def __init__(self, kleur, rang):
        self.kleur = kleur
        self.rang = rang
        
    @property
    def waarde(self):
        if self.rang in 'JQKABVH':
            return 10
        else:
            return int(self.rang)
        
    def __str__(self):
        return f'{self.kleur}{self.rang}'
    
    def __repr__(self):
        return f'{self.kleur}{self.rang}'

class Cards:

    def __init__(self):
        self.cards = None

    def __str__(self):
        return '\n'.join(map(str, self.cards))

    def __repr__(self):
        return repr(self.cards)
    
    @property
    def score(self):
        return sum(card.waarde for card in self.cards)
    
    
class Deck(Cards):
    
    def __init__(self):
        super().__init__()
        self.cards = [Speelkaart(kleur, rang) 
                     for kleur in Speelkaart.KLEUREN
                     for rang in Speelkaart.RANGEN]

    def deel(self, aantal = 1):
        return [self.cards.pop() for _ in range(aantal)]
    
    def shuffle(self):
        random.shuffle(self.cards)
        
        
class Speler:
    
    def __init__(self, naam, cards = None):
        self.naam = naam
        self.hand = []
        
    def krijg_kaarten(self, cards):
        self.hand.extend(cards)
        
    @property
    def score(self):
        return sum(card.waarde for card in self.hand)


class Game:
    
    def __init__(self):
        self.deck = Deck()
        self.deck.shuffle()
        self.players = []
        
    def add_speler(self, naam):
        self.players.append(Speler(naam))
        
    def start(self):
        while True:
            naam = input('Naam speler: ')
            if naam:
                game.add_speler(naam)
            else:
                break
            
        for player in self.players:
            player.krijg_kaarten(self.deck.deel(5))

        for player in self.players:
            print(f'{player.naam} heeft de kaarten: {player.hand}')

        for nr, player in enumerate(sorted(self.players, key = lambda item: item.score, reverse = True), start = 1):
            print(f'{nr} - {player.naam} met {player.score} punten')

    
# ----------------------------------------------------------

if __name__ == '__main__':
    
    game = Game()
    game.start()    
    