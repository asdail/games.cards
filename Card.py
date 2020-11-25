class Card:
    def __init__(self,value,shape):
        self.value=value
        self.shape=shape
        self.cards={1:"Ace",2:"Two",3:"Three",4:"Four",5:"Five",6:"Six",7:"Seven",8:"Eight",9:"Nine",10:"Ten",11:"Jack",12:"Queen",13:"King"}
        self.suit=self.cards[self.value]
        self.shapes={"Diamond":1,"Spade":2,"Heart":3,"Club":4}
        self.shapevalue=self.shapes[self.shape]

    def __eq__(self,other):
        if self.value==other.value and self.shape==other.shape:
            return True
        else:
            return False

    def __str__(self):
        return f"{self.suit} of {self.shape}s"

    def isBigger(self,other):
        if self.value>other.value:
            return f"{self} is the bigger card."
        elif self.value<other.value:
            return f"{other} is the bigger card."
        elif self.value==other.value:
            if self.shapevalue>other.shapevalue:
                return f"{self} is the bigger card."
            if self.shapevalue<other.shapevalue:
                return f"{other} is the bigger card."



card=Card(13,"Diamond")
card2=Card(13,"Spade")
print(card.__str__())
print(card2.__str__())
print(card.isBigger(card2))