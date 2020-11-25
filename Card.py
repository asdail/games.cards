class Card:
    def __init__(self,value=0,suit="",shape=""):
        self.value=value
        self.suit=suit
        self.shape=shape
        self.cards={1:"Ace",2:"Two",3:"Three",4:"Four",5:"Five",6:"Six",7:"Seven",8:"Eight",9:"Nine",10:"Ten",11:"Jack",12:"Queen",13:"King"}
        self.shapes={"Diamond":1,"Spade":2,"Heart":3,"Club":4}

    def cardvalue(self,value):
        self.value=value
        self.suit=self.cards[self.value]
        return self.cards[self.value]

    def shapevalue(self,shape):
        self.shape=shape
        return self.shapes[self.shape]

    def __eq__(self,other):
        if self.value==other.value:
            return True
        else:
            return False






card=Card()
print(card.cardvalue(13))
print(card.value)
print(card.suit)
print(card.shapevalue("Diamond"))
print(card.shape)