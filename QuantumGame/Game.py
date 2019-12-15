import IBMSim as ibm
import Gamer
import random as rd
import BotGame

whose=["A","B"]
gates=["h","x","z","y"]
pictures=["images/cardH.png","images/cardX.png","images/cardZ.png","images/cardY.png"]
cards=[]

def getInitalStatus():
    return rd.randint(0,2)


def getCards():
    cards=[]
    for w in whose:
        for i in range(4):
            a=rd.randint(0,3)
            card=Gamer.Card()            
            card.name=gates[a]
            if w=="A":
                card.picture=pictures[a]
            else:
                card.picture="cardBack.png"
            card.whose=w
            cards.append(card)
    return cards


class Game:
    playerA=Gamer.Gamer()
    playerB=Gamer.Gamer()
    status=None
    
    def new(self,status):
        self.playerA=Gamer.Gamer()
        self.playerA.gola="0"
        playerB=Gamer.Gamer()
        playerB.gola="1"
        self.status=status
    
    def setBot(self,gates):
        
        b=BotGame.BotGame() 
        b.setGates(gates)
        b.mixStart()
        k=b.getArray()  
        self.playerB.addGate(k[0],0)
        self.playerB.addGate(k[1],1)
        self.playerB.addGate(k[2],2)
        self.playerB.addGate(k[3],3)
        
#        self.playerB.addGate("h",0)
#        self.playerB.addGate("z",1)
#        self.playerB.addGate("z",2)
#        self.playerB.addGate("x",3)
        self.playerB.setScore(ibm.send(self.status,self.playerB.getGate()))
        print("B",self.playerB.score)
    
    def calcScoreA(self):
        self.playerA.setScore(ibm.send(self.status,self.playerA.getGate()))
    
    def score(self):
        print(self.playerA.score,self.playerB.score)
        return [self.playerA.score,self.playerB.score]
        
#playerA.addGate("h",0)
#playerA.addGate("x",1)
#playerA.addGate("z",2)
#playerA.addGate("x",3)



#playerB=Gamer.Gamer()
#playerB.gola="1"
#playerB.addGate("h",0)
#playerB.addGate("z",1)
#playerB.addGate("z",2)
#playerB.addGate("x",3)

#playerB.setScore(ibm.send(0,playerB.getGate()))
#print(playerB.score)
#
#if playerB.score > playerA.score:
#    print("B kazandı")
#else:
#    print("A kazandı")
