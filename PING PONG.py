'''
create player
blit background
move obsticles
detect collitions
random size '''

import pygame
import self as self

pygame.init()
pygame.display.set_caption('FIRST GAME')
win = pygame.display.set_mode((800, 600))

# left paddle
score_p1=0
y1 = 250
def player1():
    global y1
    pygame.draw.rect(win, (255, 255, 255), (50, y1, 20, 100), 0)

# right paddle
score_p2=0
y2 = 250
def player2():
    global y2
    pygame.draw.rect(win, (255, 255, 255), (750, y2, 20, 100), 0)
# ball
x=400
y=300
vely=3
velx=3
def ball(x,y):
    pygame.draw.rect(win,(255,255,255),(x,y,20,20),0)


clock = pygame.time.Clock()
run = True
# MAIN LOOP
while run:
    clock.tick(50)
    win.fill((0, 0, 0))


    player1()
    player2()
    ball(x,y)

    #ball movement
    y+=vely
    x+=velx
    if y<=0:
        vely*=-1
    elif y>=580:
        vely*=-1


    #ball collition
    if x<=70 and y>=y1 and y<=y1+100 and x>=50:
        velx*=-1
    elif x+20>=750 and y>=y2 and y<=y2+100 and x<=770:
        velx*=-1

    # score point
    if x<=0:
        x=300

        velx*=-1
        score_p2+=1

    elif x>=780:
        x=300

        velx*=-1
        score_p1+=1

    # print score
    font = pygame.font.SysFont('comicsans', 40, True)
    text = font.render('SCORE: ' + str(score_p1), 1, (255, 255, 255))
    win.blit(text, (200, 50))
    text = font.render('SCORE: ' + str(score_p2), 1, (255, 255, 255))
    win.blit(text, (400, 50))

    # game over
    font = pygame.font.SysFont('comicsans', 40, True)
    final_text=font.render('GAME OVER',1,(255,255,255))
    if score_p2==7 or score_p1==7:
        win.blit(final_text,(300,300))
        i = 0
        while i < 100:
            pygame.time.delay(10)
            i += 1
        run=False


    keys = pygame.key.get_pressed()

    if keys[pygame.K_w] and y1 >= 0:
        y1 -= 5
    if keys[pygame.K_s] and y1 <=500:
        y1 += 5
    if keys[pygame.K_UP] and y2 >= 0:
        y2 -= 5
    if keys[pygame.K_DOWN] and y2 <=500:
        y2 += 5

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()

pygame.quit()
