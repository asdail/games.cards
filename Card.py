class Card:
    def __init__(self,value=0,suit="",shape=""):
        self.value=value
        self.suit=suit
        self.shape=shape

    def cardvalue(self,value):
        self.value=value
        self.cards={1:"Ace",2:"Two",3:"Three",4:"Four",5:"Five",6:"Six",7:"Seven",8:"Eight",9:"Nine",10:"Ten",11:"Jack",12:"Queen",13:"King"}
        return self.cards[self.value]