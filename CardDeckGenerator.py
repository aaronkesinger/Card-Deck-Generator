# -*- coding: utf-8 -*-
"""
Card Deck Generator

@author: Aaron
"""
def PopulateDeck():
    deck = []
    faces = ["Jack", "Queen", "King"]
    suits = ["Spades", "Diamonds", "Clubs", "Hearts"]
    for i in range(9):
        for j in range(4):
            tempName = i+2,' of ',suits[j] #+2 as indexed at 0 and cards start at 2
            cardName = ''
            for character in tempName:
                cardName = cardName + str(character)
            deck.append(cardName)
    for i in faces:
        for j in suits:
            tempName = i,' of ', j
            cardName = ''
            for character in tempName:
                cardName = cardName + str(character)
            deck.append(cardName)
    for i in suits:
        tempName = "Ace of ", i
        cardName = ''
        for character in tempName:
            cardName = cardName + str(character)
        deck.append(cardName)
    return deck

def GenerateDeck(numberOfDecks):
    deck = []
    tempDeck = PopulateDeck()
    for i in range(numberOfDecks):
        for j in tempDeck:
            deck.append(j)
    return deck