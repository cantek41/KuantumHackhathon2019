# -*- coding: utf-8 -*-
import pickle
from sklearn.ensemble import RandomForestRegressor
from random import shuffle

filename = 'model/finalized_model.sav'
loaded_model = pickle.load(open(filename, 'rb'))


class BotGame:
    gates=[]
    state=0
    maxScore=0
    lastGates=[]
    gateArray=[]
    def setGates(self,gate):
        self.gateArray=gate
        self.gates=[]
        for g in gate:
            if g=="h":
                self.gates.append(0)
            elif g=="x":
                self.gates.append(1)
            elif g=="z":
                self.gates.append(2)
            elif g=="y":
                self.gates.append(3)

    def getPredict(self):
        result=loaded_model.predict([[self.state,
                                      self.gates[0],
                                      self.gates[1],
                                      self.gates[2],
                                      self.gates[3]]])
        print(self.gateArray,result[0])
        if result[0]>self.maxScore:
            self.maxScore=result
            self.lastGates=self.gateArray
            
    def getArray(self):
        print(self.maxScore,self.lastGates)
        return self.lastGates
    
    def mixStart(self):
        for i in range(100):            
            shuffle(self.gateArray)
            self.setGates(self.gateArray)
            self.getPredict()
            
                

#b=BotGame() 
#b.setGates(["y","h","z","x"])
#b.mixStart()
#k=b.getArray()  
#k 
#d=[state,gates[0],gates[1],gates[2],gates[3]]

#setGates(["y","h","z","x"])
#getPredict()

#h=0 x=1 z=2 y=3
#loaded_model.predict([[state,3,0,2,1]])


