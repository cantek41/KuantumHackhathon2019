# -*- coding: utf-8 -*-
import pygame

class Card:
    name=None
    picture=None
    whose=None
    rect=None
    draw=None
       
    def setRect(self,r):
        self.rect=r
        
    def getRect(self):
        return self.rect
        
    
    

class Gamer:
    endStatus={}
    score=0
    goal="0"

    def addGate(self,gate,order):
        self.endStatus[order]=gate;
    
    def getGate(self):
        result=[]
        result.append(self.endStatus[0])
        result.append(self.endStatus[1])
        result.append(self.endStatus[2])
        result.append(self.endStatus[3])
        print(self.endStatus)
        return result
    
    def setScore(self,val):
        try:
            self.score=val["0"]
        except:
            self.score=0





#A=Gamer()
#
#A.addGate("h",0)
#
#print(A.endStatus)