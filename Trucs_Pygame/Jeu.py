from pygame import*
from random import*
import pygame

## Initialisation des modules
init()

## Création de la fenêtre
fen=display.set_mode((800,501))

#charger une image
fond=image.load("ciel.jpg")

#coller l'image
fen.blit(fond,(0,0))

#charger une deuxième image
im=image.load("vaisso.jpg")
imRect = im.get_rect()
imRect=imRect.move(450,450)

## Mmissiles
mis=image.load("ball.png")
misRect = mis.get_rect()
misi=image.load("ball.png")
miRect = misi.get_rect()

## Vvaisseaux ennemis
vas=image.load("vaisso1.png")
vasRect = vas.get_rect()

## Quit+tryagain
again=image.load("tryagain.jpg")
againRect = again.get_rect()
quitt=image.load("quit.png")
quitRect = quitt.get_rect()

## Résultat
los=image.load('lost.jpg')
won=image.load('won.png')
won.set_colorkey((255,255,255))
die=image.load('died.jpg')
die.set_colorkey((0,0,0))
lvl=image.load('up.jpg')
lvl.set_colorkey((0,0,0))

#truc
#fonte =font.Font(None,56)
#fonte.set_italic(True)
#fonte.set_underline(True)
#p=-1
#text = fonte.render(str(p),True, (255,255,255),(255,0,0))
#text_position = (150,0)
#fen.blit(text,text_position)

#rafraichir l'affichage
display.flip()

key.set_repeat(2,2)

## Boucle infinie
r,p,boucle,bas,haut,droite,gauche,missile,vaisso,jeu,menu,turbo=0,-1,True,False,False,False,False,False,False,True,False,False
while boucle:
    pygame.time.Clock().tick(60)
    while jeu:
        
    #liste d'evenements
        for evenement in event.get():

            #appui sur la croix
            if evenement.type==QUIT:
                jeu=False
                r=3
                
            #mouvements
                #gauche
            if evenement.type==KEYDOWN:
                if evenement.key==K_LEFT:
                    bas,gauche,haut,droite=False,True,False,False
                #droite
            if evenement.type==KEYDOWN:
                if evenement.key==K_RIGHT:
                    bas,gauche,haut,droite=False,False,False,True

                #missile
            if evenement.type==KEYDOWN:
                if evenement.key==K_SPACE:
                    fen.blit(fond,(0,0))
                    fen.blit(im,imRect)
                    misRect=imRect
                    fen.blit(mis,misRect)
                    missile=True

                #vaisseau ennemi
            if evenement.type==KEYDOWN:
                if evenement.key==K_UP:
                    fen.blit(fond,(0,0))
                    fen.blit(im,imRect)
                    vasRect[0]=randrange(750)
                    vasRect[1]=-10
                    fen.blit(vas,vasRect)
                    vaisso=True

            #turbo
            if evenement.type==KEYDOWN:
                if evenement.key==K_DOWN:
                    turbo=True

            if evenement.type==KEYUP:
                if evenement.key==K_DOWN:
                    turbo=False

        if gauche==True and(haut,droite,bas==False,False,False):
            imRect=imRect.move(-5,0)
            fen.blit(fond,(0,0))
            fen.blit(im,imRect)
#            fen.blit(text,text_position)

        if droite==True and(haut,bas,gauche==False,False,False):
            imRect=imRect.move(5,0)
            fen.blit(fond,(0,0))
            fen.blit(im,imRect)
#            fen.blit(text,text_position)

        if missile==True:
            misRect=misRect.move(0,-50)
            fen.blit(fond,(0,0))
            fen.blit(im,imRect)
            fen.blit(mis,misRect)
#            fen.blit(text,text_position)

        if vaisso==True and(missile==True):
            vasRect=vasRect.move(0,5)
            fen.blit(fond,(0,0))
            fen.blit(im,imRect)
            fen.blit(vas,vasRect)
            fen.blit(mis,misRect)
#            fen.blit(text,text_position)

        if vaisso==True and(missile==False):
            vasRect=vasRect.move(0,5)
            fen.blit(fond,(0,0))
            fen.blit(im,imRect)
            fen.blit(vas,vasRect)
#            fen.blit(text,text_position)

        if imRect[0]>=800:
            droite=False
            gauche=True
        
        if imRect[0]<=0:
            droite=True
            gauche=False

        if misRect.colliderect(vasRect):
            vasRect[0]=randrange(750)
            vasRect[1]=-10
            p=p+1
#            text = fonte.render(str(p),True, (255,255,255),(255,0,0))
#            fen.blit(text,text_position)

        if p==10:
            r=1
            jeu=False

        if vasRect.colliderect(imRect):
            r=3
            jeu=False

        if vasRect[1]>=500:
            r=2
            jeu=False

        if turbo==True and(droite==True):
            imRect=imRect.move(5,0)

        if turbo==True and(gauche==True):
            imRect=imRect.move(-5,0)

        if p==5:
            fen.blit(lvl,(350,200))
#            fen.blit(text,text_position)

        if p==8:
            fen.blit(lvl,(350,200))
#            fen.blit(text,text_position)

        if p>=5:
            vasRect=vasRect.move(0,2)

        if p>=8:
            vasRect=vasRect.move(0,2)
        display.flip()

#        fonte =font.Font(None,56)
#        fonte.set_italic(True)
#        fonte.set_underline(True)
#        text = fonte.render("yo",True, (255,255,255),(255,0,0))
#        text_position = (150,0)
#        fen.blit(text,text_position)

## Gagné(1)
    if jeu==False and(r==1):
        fen.blit(fond,(0,0))
        quitRect[0]=340
        quitRect[1]=100
        againRect[0]=300
        againRect[1]=270
        fen.blit(again,againRect)
        fen.blit(quitt,quitRect)
        fen.blit(won,(0,0))
        display.flip()
    
        key.set_repeat(2,2)
        menu=True
        while menu:
    
            for evenement in event.get():
    
                if evenement.type==MOUSEBUTTONDOWN:
                    if evenement.button==1:
                        miRect[0]=evenement.pos[0]
                        miRect[1]=evenement.pos[1]
                        fen.blit(fond,(0,0))
                        fen.blit(again,againRect)
                        fen.blit(quitt,quitRect)
                        fen.blit(misi,miRect)
    
                if miRect.colliderect(againRect):
                    vasRect[0]=randrange(750)
                    vasRect[1]=-10
                    miRect[0]=0
                    miRect[1]=0
                    imRect[0]=450
                    imRect[1]=450
                    p,jeu,menu,gauche,droite,vaisso,missile,turbo=-1,True,False,False,False,False,False,False
                    fen.blit(fond,(0,0))
                    fen.blit(im,imRect)

                if miRect.colliderect(quitRect):
                    boucle,droite,gauche,missile,vaisso,jeu,menu,turbo=False,False,False,False,False,False,False,False
## Perdu(2)
    if jeu==False and(r==2):
        fen.blit(fond,(0,0))
        quitRect[0]=340
        quitRect[1]=100
        againRect[0]=300
        againRect[1]=270
        fen.blit(again,againRect)
        fen.blit(quitt,quitRect)
        fen.blit(los,(0,0))
        display.flip()
    
        key.set_repeat(2,2)
        menu=True
        while menu:
    
            for evenement in event.get():
    
                if evenement.type==MOUSEBUTTONDOWN:
                    if evenement.button==1:
                        miRect[0]=evenement.pos[0]
                        miRect[1]=evenement.pos[1]
                        fen.blit(fond,(0,0))
                        fen.blit(again,againRect)
                        fen.blit(quitt,quitRect)
                        fen.blit(misi,miRect)
    
                if miRect.colliderect(againRect):
                    vasRect[0]=randrange(750)
                    vasRect[1]=-10
                    miRect[0]=0
                    miRect[1]=0
                    imRect[0]=450
                    imRect[1]=450
                    p,jeu,menu,gauche,droite,vaisso,missile,turbo=-1,True,False,False,False,False,False,False
                    fen.blit(fond,(0,0))
                    fen.blit(im,imRect)

                if miRect.colliderect(quitRect):
                    boucle,droite,gauche,missile,vaisso,jeu,menu,turbo=False,False,False,False,False,False,False,False
## Meurt(3)
    if jeu==False and(r==3):
        fen.blit(fond,(0,0))
        quitRect[0]=340
        quitRect[1]=100
        againRect[0]=300
        againRect[1]=270
        fen.blit(again,againRect)
        fen.blit(quitt,quitRect)
        fen.blit(die,(0,0))
        display.flip()
    
        key.set_repeat(2,2)
        menu=True
        while menu:
    
            for evenement in event.get():
    
                if evenement.type==MOUSEBUTTONDOWN:
                    if evenement.button==1:
                        miRect[0]=evenement.pos[0]
                        miRect[1]=evenement.pos[1]
                        fen.blit(fond,(0,0))
                        fen.blit(again,againRect)
                        fen.blit(quitt,quitRect)
                        fen.blit(misi,miRect)
    
                if miRect.colliderect(againRect):
                    vasRect[0]=randrange(750)
                    vasRect[1]=-10
                    miRect[0]=0
                    miRect[1]=0
                    imRect[0]=450
                    imRect[1]=450
                    p,jeu,menu,gauche,droite,vaisso,missile,turbo=-1,True,False,False,False,False,False,False
                    fen.blit(fond,(0,0))
                    fen.blit(im,imRect)

                if miRect.colliderect(quitRect):
                    boucle,droite,gauche,missile,vaisso,jeu,menu,turbo=False,False,False,False,False,False,False,False

            display.flip()
            
    display.flip()
quit()