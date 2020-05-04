import pygame
import random
import math
from pygame import mixer
#initialize the pygame
pygame.init()
#screen display
screen=pygame.display.set_mode((900,600))
#change the title&logo
pygame.display.set_caption("space game created by ramya lavanya")
icon=pygame.image.load('space ship logo.png')
pygame.display.set_icon((icon))
spaceImg=pygame.image.load('space_craft.png')
enemyImg=pygame.image.load('enemy.png')
bbackground=pygame.image.load('bbackground.jpg')
mixer.music.load('background.wav')
mixer.music.play(-2)
bullet=pygame.image.load('bullet.png')
spaceX=380
spaceY=510
#enemy
enemyX=[]
enemyY=[]
enemyX_change=[]
enemyY_change=[]
enemyImg=[]
num_of_enemies=6
for i in range(num_of_enemies):
       enemyImg.append(pygame.image.load('enemy.png'))
       enemyX.append(random.randint(0,800))
       enemyY.append(random.randint(50,150))
       enemyX_change.append(10)
       enemyY_change.append(40)

spaceX_change=0

#bullet
bulletX=0
bulletY=random.randint(50,150)
bulletX_change=0
bulletY_change=10
bullet_state="ready"
score_value=0
font=pygame.font.Font('freesansbold.ttf',38)
textX=10
testY=10
over_font=pygame.font.Font('freesansbold.ttf',64)
def show_score(X,Y):
    score=font.render("score :"+str(score_value),True,(255,255,255))
    screen.blit(score,(X,Y))
def game_over_text():
    over_text = font.render("GAME OVER" , True, (255, 255, 255))
    screen.blit(over_text, (300, 250))
def player(X,Y):
    screen.blit(spaceImg,(X,Y))
def enemy(X,Y,i):
    screen.blit(enemyImg[i],(X,Y))
def fire_bullet(X,Y):
     global bullet_state
     bullet_state="fire"
     screen.blit(bullet,(X+16,Y+10))
def collision(enemyX,enemyY,bulletX,bulletY):
    distance=math.sqrt((math.pow(enemyX-bulletX,2))+(math.pow(enemyY-bulletY,2)))
    if distance<27:
        return True
    else:
        return False




#game loop
running=True
while running:
    screen.fill((0, 255, 0))
    screen.blit(bbackground,(0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running=False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                spaceX_change = -5

            if event.key == pygame.K_RIGHT:
                spaceX_change = 5
            if event.key == pygame.K_SPACE:
                if bullet_state is "ready":
                    bullet_Sound=mixer.Sound('laser.wav')
                    bullet_Sound.play()
                    bulletX=spaceX
                    fire_bullet(bulletX,bulletY)



        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                spaceX_change=0

#checking boundary
    spaceX += spaceX_change
    if spaceX <= 0:
        spaceX =0
    elif spaceX >=836:
        spaceX = 836
    for i in range(num_of_enemies):
        if enemyY[i] > 440:
            for j in range(num_of_enemies):
                enemyY[j] = 2000
            game_over_text()
            break

        enemyX[i] += enemyX_change[i]
        if enemyX[i] <= 0:
          enemyX_change[i] = 2
          enemyY[i] += enemyY_change[i]
        elif enemyX[i] >= 836:
          enemyX_change[i] = -2
          enemyY[i] += enemyY_change[i]
        iscollision = collision(enemyX[i], enemyY[i], bulletX, bulletY)
        if iscollision:
            explosion_Sound=mixer.Sound('explosion.wav')
            explosion_Sound.play()
            bulletY = 480
            bullet_state = "ready"
            score_value += 1
            print(score_value)
            enemyX[i] = random.randint(0, 800)
            enemyY[i] = random.randint(50, 150)
        enemy(enemyX[i],enemyY[i],i)
    if bulletY<=0:
        bulletY=480
        bullet_state="ready"
    if bullet_state is "fire":
        fire_bullet(bulletX,bulletY)
        bulletY-=bulletY_change



    player(spaceX,spaceY)
    show_score(textX,testY)

    pygame.display.update()



