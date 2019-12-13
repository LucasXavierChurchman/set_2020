import random

class Card():
    def __init__(self, count, shape, color, shading):
        self.count = count
        self.shape = shape
        self.color = color
        self.shading = shading

    def show(self):
        print('Count: {} Shape:{} Color:{} Shading{}'.format(self.count, self.shape, self.color, self.shading))

class Deck():
    def __init__(self):
        self.cards = []
        self.build()

    def build(self):
        for count in [1,2,3]:
            for shape in ['Squiggle', 'Diamond', 'Oval']:
                for color in ['Red', 'Green', 'Purple']:
                    for shading in ['Solid', 'Striped', 'Open']:
                        self.cards.append([count, shape, color, shading])
    
    def shuffle(self):
        for i in range(0, len(self.cards)-1, 1):
            r = random.randint(0, i)
            self.cards[i], self.cards[r] = self.cards[r], self.cards[i]        
    
    def show(self):
        for card in self.cards:
            print(card)
        

class Play_Game():
    def __init__(self):
        pass

    def is_set(self, card1, card2, card3):
        '''
        Check whether 3 cards count as a set

        A set is defined as 3 cards where each of the 4 
        features (count, shape, color, shading) must be all the same
        or must be all different
        '''
        cards = [card1, card2, card3]

        counts = [card[0] for card in cards]
        shapes = [card[1] for card in cards]
        colors = [card[2] for card in cards]
        shadings = [card[3] for card in cards]

        features = [counts, shapes, colors, shadings]
        for feature in features:
            if len(set(feature)) == 1 or len(set(feature)) == 3:
                continue
            else:
                return(False)
            return True








    