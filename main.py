import time

import pygame
import random
#DEF

def Move_Cloud(move):
    screen.blit(Cloud,(move,y_Cloud))
def Move_Track(x_run):
    screen.blit(Track,(x_run,280))
    screen.blit(Track, (x_run+x_Track-10, 280))
def Dino(index_Dino):
    New_dino=Dino_Run[index_Dino]
    x_Dino=New_dino.get_width()
    y_Dino=New_dino.get_height()
    New_dino = pygame.transform.scale(New_dino, (int(x_Dino * 2 / 3), int(y_Dino * 2 / 3)))
    return New_dino
def Duck(index_Dino):
    New_dino=Dino_Duck[index_Dino]
    x_Dino=New_dino.get_width()
    y_Dino=New_dino.get_height()
    New_dino = pygame.transform.scale(New_dino, (int(x_Dino * 2 / 3), int(y_Dino * 2 / 3)))
    return New_dino

def Create_Tree(index):
    New_Tree = Tree[index]
    New_Tree_Rect = New_Tree.get_rect(midtop=(1700,310-New_Tree.get_height()))
    return New_Tree_Rect
def Move_Tree(list_Tree):
    for tree in list_Tree:
        tree.centerx-=5
    return list_Tree
def ADD(Add,list_Tree):
    for tree in list_Tree:
        tree.centerx-=5
        if tree.centerx<0:
            Add=1
    return Add
def Show_Tree(imgTree,list_Tree):
    for tree in list_Tree:
        screen.blit(imgTree,tree)
def newBird(index):
    New_Bird=bird[index]
    New_Bird=pygame.transform.scale(New_Bird,(int(New_Bird.get_width()*6/7),int(New_Bird.get_height()* 6 / 8)))
    return New_Bird
def Create_Bird(index,Random_HB):
    bird_new=bird[index]
    bird_new_Rect = bird_new.get_rect(midtop=(2500, Random_HB - bird_new.get_height()))
    return bird_new_Rect
def Move_Bird(list_Bird):
    for bird in list_Bird:
        bird.centerx-=10
    return list_Bird
def ADD_BIRD(ADD_Bird,list_Bird):
    for bird in list_Bird:
        bird.centerx-=10
        if bird.centerx<0:
            ADD_Bird=1
    return ADD_Bird
def Show_Bird(bird_spawn,list_Bird):
    for bird in list_Bird:
        screen.blit(bird_spawn,bird)
def check(list_Tree,list_Bird):
    for Tree in list_Tree:
        if What_dino_rect.colliderect(Tree):
            return False
    for BIRD in list_Bird:
        if What_dino_rect.colliderect(BIRD):
            return False
    return True
def GO():
    screen.blit(gameover,(int(Game_W/2-gameover.get_width()/2),int(Game_H/2-gameover.get_height()/2)))
    screen.blit(reset,(int(Game_W/2-reset.get_width()/2),int(-45+Game_H-Game_H/3-reset.get_height()/2+gameover.get_height()/2)))
def Update_HScore(Score,High_Score):
    if(Score > High_Score):
        High_Score=Score
    return High_Score
def display_font():
    score_font = game_font.render(" {}".format(int(Score)), True, (0, 0, 0))
    score_rect = score_font.get_rect(center=(900, 10))
    screen.blit(score_font, score_rect)

    Hscore_font = game_font.render("{}".format(int(High_Score)), True, (0, 0, 0))
    Hscore_rect = score_font.get_rect(center=(800 - Hscore_font.get_width() / 2, 10))
    screen.blit(Hscore_font, Hscore_rect)
def random_TB():
    return random.choice(Tree_Or_Bird)
#value
x_run=0
Game_H=350
Game_W=1000
run=True
Game_Active=True
Score=0
High_Score=0
Bird_list=0
ADD_Bird=1

#pygame
pygame.init()
screen = pygame.display.set_mode((Game_W,Game_H))

#font game
game_font = pygame.font.Font("04B_19.TTF",20)

#img_bg
Track = pygame.image.load("Assets/Other/Track.png")
x_Track =Track.get_width()


#Dino
Dino_Start =pygame.image.load("Assets/Dino/DinoStart.png")
Dino_Run1=pygame.image.load("Assets/Dino/DinoRun1.png")
Dino_Run2=pygame.image.load("Assets/Dino/DinoRun2.png")
Dino_Duck1=pygame.image.load("Assets/Dino/DinoDuck1.png")
Dino_Duck2=pygame.image.load("Assets/Dino/DinoDuck2.png")
Dino_Jump=pygame.image.load("Assets/Dino/DinoJump.png")
Dino_Die =pygame.image.load("Assets/Dino/DinoDead.png")
x_jump=Dino_Jump.get_width()
y_jump=Dino_Jump.get_height()
Dino_Jump=pygame.transform.scale(Dino_Jump,(int(x_jump*2/3),int(y_jump*2/3)))
Dino_Die=pygame.transform.scale(Dino_Die,(int(Dino_Die.get_width()*2/3),int(Dino_Die.get_height()*2/3)))
Dino_Run=[Dino_Start,Dino_Run1,Dino_Run2]
Dino_Duck=[Dino_Duck1,Dino_Duck2]
index_Dino_Run=0
index_Dino_Duck=0
What_dino=Dino_Run[index_Dino_Run]
Duck_dion=Dino_Duck[index_Dino_Duck]

y_Dino=What_dino.get_height()
x_Dino=What_dino.get_width()
What_dino=pygame.transform.scale(What_dino,(int(x_Dino*2/3),int(y_Dino*2/3)))
y_Dino=What_dino.get_height()
x_Dino=What_dino.get_width()


y_Dino=Duck_dion.get_height()
x_Dino=Duck_dion.get_width()
Duck_dion=pygame.transform.scale(Duck_dion,(int(x_Dino*2/3),int(y_Dino*2/3)))


stop_move = 240
move_dino = 240
X_dino=40
Dino_Array = pygame.USEREVENT
Dino_D=pygame.USEREVENT
Between_RD=1


pygame.time.set_timer(Dino_Array, 130)


#Cloud
Cloud= pygame.image.load("Assets/Other/Cloud.png")
x_Cloud =Cloud.get_width()
y_Cloud = random.randint(20,50)
random.seed(1000)
between_Cloud=random.randint(550,1024)
move=between_Cloud



#Tree
Tree1= pygame.image.load("Assets/Cactus/LargeCactus1.png")
Tree1=pygame.transform.scale(Tree1, (int(Tree1.get_width() * 6 / 7), Tree1.get_height()))
Tree2= pygame.image.load("Assets/Cactus/LargeCactus2.png")
Tree2=pygame.transform.scale(Tree2, (int(Tree2.get_width() * 6 / 7), Tree2.get_height()))
Tree3= pygame.image.load("Assets/Cactus/LargeCactus3.png")
Tree3=pygame.transform.scale(Tree3, (int(Tree3.get_width() * 6 / 7), Tree3.get_height()))
Tree4= pygame.image.load("Assets/Cactus/SmallCactus1.png")
Tree4=pygame.transform.scale(Tree4, (int(Tree4.get_width() * 6 / 7), Tree4.get_height()+10))
Tree5= pygame.image.load("Assets/Cactus/SmallCactus2.png")
Tree5=pygame.transform.scale(Tree5, (int(Tree5.get_width() * 6 / 7), Tree5.get_height()+10))
Tree6= pygame.image.load("Assets/Cactus/SmallCactus3.png")
Tree6=pygame.transform.scale(Tree6, (int(Tree6.get_width() * 6 / 7), Tree6.get_height()+10))

Tree=[Tree1,Tree2,Tree3,Tree4,Tree5,Tree6]
index=random.randint(0,5)
imgTree=Tree[index]
imgTree=pygame.transform.scale(imgTree,(150,150))
list_Tree=[]
Add=1
SPAWNTREE= pygame.USEREVENT

#bird
bird1=pygame.image.load("Assets/Bird/Bird1.png")
bird2=pygame.image.load("Assets/Bird/Bird2.png")
bird=[bird1,bird2]
index_bird=1
bird_spawn=bird1
bird_spawn=pygame.transform.scale(bird_spawn,(int(bird_spawn.get_width()*6/7),int(bird_spawn.get_height()* 6 / 8)))
SPAWNBIRD=pygame.USEREVENT
Array_Bird=pygame.USEREVENT


list_Bird=[]
Tree_Or_Bird=[1,1,1,1,1,1,1,1,1,1,1,1,1,0]
Tree_Bird=1
HB=[235,250,270,280,300,310,315,330]
Random_HB=random.choice(HB)

#tí chỉnh bay cao :< + tỉ lệ spawn chim
#gameover
gameover=pygame.image.load("Assets/Other/GameOver.png")
#gameover=pygame.transform.scale2x(gameover)
reset=pygame.image.load("Assets/Other/Reset.png")
reset=pygame.transform.scale(reset,(int(reset.get_width()/2),int(reset.get_height()/2)))
#ILOVEU
love=pygame.image.load("Assets/Other/Love.png")
love =pygame.transform.scale2x(love)
Dino_love=pygame.image.load("Assets/Dino/D.png")
Dino_love=pygame.transform.scale(Dino_love,(int(Dino_love.get_width()*2/3),int(Dino_love.get_height()*2/3)))


#FPS
clock = pygame.time.Clock()

#begin_game
key=1
k=0
while run:
    screen.fill((255,255,255))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and key==1 and Game_Active:
                move_dino-=240
                key+=1
                What_dino = Dino_Jump
                k=1

            if event.key == pygame.K_RIGHT and Game_Active:
                X_dino+=20
            if event.key == pygame.K_LEFT and Game_Active:
                if X_dino>=40:
                    X_dino-=20
            if event.key == pygame.K_DOWN and Game_Active:
                k=2
                move_dino=stop_move
                Between_RD=2
            if event.key == pygame.K_UP and Game_Active== False:
                Add=1
                Score=0

                list_Tree.clear()
                list_Bird.clear()
                ADD_Bird=1
                Tree_Bird = 1
                X_dino=40
                time.sleep(0.2)
                Game_Active = True

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_DOWN or event.key == pygame.K_UP:
                Between_RD=1
                k=0
        if Between_RD==1 and Game_Active and key==1:
            if event.type == Dino_Array and k==0:
                    if index_Dino_Run < 2:
                        index_Dino_Run += 1
                    else:
                        index_Dino_Run = 1
                    What_dino = Dino(index_Dino_Run)
        if Between_RD==2 and Game_Active and key==1:
            if event.type == Dino_D and k==2:
                    if index_Dino_Duck < 1:
                        index_Dino_Duck += 1
                    else:
                        index_Dino_Duck = 0
                    Duck_dion=Duck(index_Dino_Duck)
                    What_dino = Duck_dion
        if event.type==SPAWNTREE and Game_Active and Tree_Bird==1:
            if Add==1 and ADD_Bird==1:
                index = random.randint(0, 5)
                list_Tree.append(Create_Tree(index))
                X_list = len(list_Tree)
                imgTree = Tree[index]

                del list_Tree[0:X_list - 1]
                Add+=1


        if event.type==SPAWNBIRD and Game_Active and Tree_Bird==0:
            if event.type==Array_Bird:
                if index_bird<1:
                    index_bird+=1
                else:
                    index_bird=0
                bird_spawn=newBird(index_bird)
            if Score>=200 and ADD_Bird==1 :
                Random_HB = random.choice(HB)
                list_Bird.append(Create_Bird(index_bird,Random_HB))
                Bird_list = len(list_Bird)
                del list_Bird[0:Bird_list-1]
                ADD_Bird+=1
                Add += 1



    if Game_Active:
        # Track
        x_run -= 4
        Move_Track(x_run)
        if x_run <= -x_Track:
            x_run = 0

        # Cloud
        move -= 4
        Move_Cloud(move)
        if move <= -100:
            move = between_Cloud
        # Dino

        move_dino += 5
        if move_dino - 5 == stop_move:
            key = 1
            move_dino = stop_move

        What_dino_rect = What_dino.get_rect(midleft=(X_dino, 30 + move_dino))

        if Between_RD == 1:
            screen.blit(What_dino, What_dino_rect)
        if Between_RD == 2:
            screen.blit(What_dino, (X_dino, 20 + move_dino))
        # Tree
        list_Tree=Move_Tree(list_Tree)
        Add=ADD(Add,list_Tree)
        Show_Tree(imgTree,list_Tree)

        #BIRD
        list_Bird = Move_Bird(list_Bird)
        Show_Bird(bird_spawn,list_Bird)
        ADD_Bird = ADD_BIRD(ADD_Bird, list_Bird)
        Game_Active = check(list_Tree,list_Bird)
        if ADD_Bird==1:
            Tree_Bird=random_TB()
        Score+=0.5
        display_font()
        if Score>1000:
            Game_Active=False
    elif Score<1000:
        Move_Track(x_run)
        Move_Cloud(move)
        screen.blit(Dino_Die, What_dino_rect)
        Show_Tree(imgTree, list_Tree)
        Show_Bird(bird_spawn, list_Bird)
        High_Score=Update_HScore(Score, High_Score)
        display_font()
        GO()
    else:
        move_dino = stop_move
        screen.blit(love, (int(Game_W / 2 - love.get_width() / 2), int(Game_H / 2 - love.get_height() / 2)))
        Move_Track(x_run)
        Move_Cloud(move)
        What_dino = pygame.transform.scale(Dino_Start,(int(Dino_Start.get_width() * 2 / 3), int(Dino_Start.get_height() * 2 / 3)))
        screen.blit(What_dino, What_dino_rect)
        What_Love_rect = What_dino.get_rect(midright=(1000-X_dino, 30 + move_dino))
        screen.blit(Dino_love, What_Love_rect)
        High_Score = Update_HScore(Score, High_Score)
        display_font()
    clock.tick(120)
    pygame.display.update()



#end_game