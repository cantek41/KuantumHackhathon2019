import pygame
from pygame.locals import *

import Game
 
class App:
    def __init__(self):
        self._running = True
        self._display_surf = None
        self.size = self.weight, self.height = 640, 400        
        self._image_surf=None
        self._image_Cards=[]
        self._image_B_Card=None
        self._InitalStatus=None
        self._selectCardX=180
        self._selectCardIndex=0
        self._GAME=None
        self._GAME_loop=True
        self.BGCOLOR=(40,150,40)
        self.img_SCORE=None
        
        
    def on_init(self):
        pygame.init()
        self._display_surf = pygame.display.set_mode(self.size, pygame.HWSURFACE | pygame.DOUBLEBUF)
        self._display_surf.fill(self.BGCOLOR)
        self._running = True
        self.createGame()
            
    def createGame(self):            
        cards=Game.getCards() 
        self._InitalStatus=Game.getInitalStatus()
        self._GAME=Game.Game()
        self._GAME.new(self._InitalStatus)        
        a=180
        bGates=[]
        for c in cards:            
            if c.whose=="A":
                c.setRect((a,290))
                c.draw = pygame.image.load(c.picture).convert_alpha()
                c.draw = pygame.transform.scale(c.draw, (70, 100))
                self._image_Cards.append(c)
                a=a+80
            else:
               bGates.append(c.name)
        
        self._GAME.setBot(bGates)
        
        self._image_B_Card = pygame.image.load("images/cardBack.png").convert_alpha()
        self._image_B_Card = pygame.transform.scale(self._image_B_Card, (70, 100))


    def on_event(self, event):
        if event.type == pygame.QUIT:
            self._running = False
        if self._GAME_loop:
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                for card in self._image_Cards:
                    r=pygame.Rect(card.getRect(),(70,100))
                    if r.collidepoint(x, y):
                        card.setRect((self._selectCardX,150))
                        self._selectCardX +=80
                        self._GAME.playerA.addGate(card.name,self._selectCardIndex)
                        self._selectCardIndex +=1                        
                        if self._selectCardIndex ==4:
                            self._GAME_loop=False
                            self.score()
#                            print("hesapla")
#                    self._display_surf.blit(card.draw,(200,50))
    
    def tabela(self):
        font=pygame.font.SysFont("Helvetica",16)
        text=font.render("Hedefiniz Inital",1,(255,255,255),self.BGCOLOR)
        self._display_surf.blit(text,(10,10))
        
        text=font.render("Status Değerini",1,(255,255,255),self.BGCOLOR)
        self._display_surf.blit(text,(10,30))
        
        text=font.render("0 a yakınlaştıracak",1,(255,255,255),self.BGCOLOR)
        self._display_surf.blit(text,(10,50))
        
        text=font.render("devreyi kurmak",1,(255,255,255),self.BGCOLOR)
        self._display_surf.blit(text,(10,70))
        
        font=pygame.font.SysFont("Helvetica",36)
        text=font.render("Bilgisayar",1,(255,156,57),self.BGCOLOR)
        self._display_surf.blit(text,(500,10))
        
        font=pygame.font.SysFont("Helvetica",25)
        text=font.render("Score",1,(60,60,60),self.BGCOLOR)
        self._display_surf.blit(text,(500,50))
        
        if self._selectCardIndex<=3:
            text=font.render("Hesaplıyor",1,(60,60,60),self.BGCOLOR)
        else:
            text=font.render(str(self._GAME.playerB.score),1,(60,60,60),self.BGCOLOR)
        self._display_surf.blit(text,(500,80))
        
        
        font=pygame.font.SysFont("Helvetica",36)
        text=font.render("Oyuncu",1,(255,156,57),self.BGCOLOR)
        self._display_surf.blit(text,(500,290))
        
        
        font=pygame.font.SysFont("Helvetica",25)
        text=font.render("Score",1,(60,60,60),self.BGCOLOR)
        self._display_surf.blit(text,(500,330))
        
        text=font.render(str(self._GAME.playerA.score),1,(60,60,60),self.BGCOLOR)
        self._display_surf.blit(text,(500,360))
        
        
    def score(self):
        self._GAME.calcScoreA()
        if(self._GAME.playerA.score>self._GAME.playerB.score):
            print("Kazandınız")
            self.img_SCORE = pygame.image.load("images/win.png").convert_alpha()
            self.img_SCORE=pygame.transform.scale(self.img_SCORE, (300, 240))
        else:
            print("Yapay Zeka Kazandı")
            self.img_SCORE = pygame.image.load("images/l.png").convert_alpha()
            self.img_SCORE=pygame.transform.scale(self.img_SCORE, (200, 200))
#        print(score[0],score[1])
        
    def on_loop(self):
        pass
    def on_render(self):  
        self._display_surf.fill(self.BGCOLOR)
        a=180;
        for i in range(4):  
            self._display_surf.blit(self._image_B_Card,(a,10))
            a=a+80
        
        for c in self._image_Cards:   
                self._display_surf.blit(c.draw,c.getRect())  
                #print(c.getRect())
        if self._InitalStatus == 0:
            st = pygame.image.load("images/0.png").convert_alpha()
        else:
            st = pygame.image.load("images/1.png").convert_alpha()
        st=pygame.transform.scale(st, (70, 100))
        self._display_surf.blit(st,(50,160))  
        
        self.tabela()
        if self.img_SCORE:
            self._display_surf.blit(self.img_SCORE,(200,100))  
            
        pygame.display.flip()
    def on_cleanup(self):
        pygame.quit()
 
    def show_start_screen(self):
        pygame.mixer.music.load("music/m.mp3") 
        pygame.mixer.music.play(-1,0.0)
        self._display_surf.fill(self.BGCOLOR)
        splash = pygame.image.load("images/zemin.png").convert_alpha()
        self._display_surf.blit(splash,(160,50))
        pygame.display.flip()
        self.wait_for_key()
    
    def wait_for_key(self):
        waiting=True
        while waiting:
            for event in pygame.event.get():
                if event.type==pygame.KEYUP:
                    waiting=False
        
    def on_execute(self):
        
        if self.on_init() == False:
            self._running = False
        
        self.show_start_screen()
        while( self._running ):
            for event in pygame.event.get():
                self.on_event(event)
            self.on_loop()
            self.on_render()
        self.on_cleanup()
 
if __name__ == "__main__" :
    theApp = App()
    theApp.on_execute()