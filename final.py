'''ROCK PAPER SISSOR
GUESS THE NUMBER'''
import random as rr

def RPSGAME():
    flag=0
    com=0
    user=0

    while flag==0:
        print('==ROCK PAPER SISSOR==')
        print('chose 1=rock\n2=paper\n3=sissor')
        ch=int(input('Enter choice...'))
        comchoice= rr.randrange(1,4)
        if ch in range(1,4):
            if comchoice==1:
                print('COMPUTER CHOICE=ROCK')
                if ch==1:
                    print('draw')
                elif ch==2:
                    print('you win')
                    user+=1
                else:
                    print('you lose')
                    com+=1
            if comchoice==2:
                print('COMPUTER CHOICE=PAPER')
                if ch==2:
                    print('draw')
                elif ch==3:
                    print('you win')
                    user+=1
                else:
                    print('you lose')
                    com+=1
            if comchoice==3:
                print('COMPUTER CHOICE=SISSOR')
                if ch==3:
                    print('draw')
                elif ch==1:
                    print('you win')
                    user+=1
                else:
                    print('you lose')
                    com+=1
        else:
            print('invalid choice')
        print('*******SCORE*******\nYOU=',user,'\nCOMPUTER=',com)
        con=int(input('do you want to continue(1=yes,2=no)'))
        if con==2:
            flag+=1
        else:
            flag+=0


 
''' tic tak toe game
function to be made
play game
display board
change turn
turn
check win
check game over\tie
'''
cturn='x'
board=["-","-","-","-","-","-","-","-","-"]
game_on=True
fill=''
def display_board():
    print('positions are as follows\n1-2-3\n4-5-6\n7-8-9 ')
    print(board[0]+'|'+board[1]+'|'+board[2])
    print(board[3]+'|'+board[4]+'|'+board[5])
    print(board[6]+'|'+board[7]+'|'+board[8])

    return

def turn():
    global cturn,board
    print(cturn,"'s turn")
    position=int(input('enter the position'))
    position= position-1
    board[position]=cturn            

def check_win():
    global board,cturn,game_on
    if board[0]==board[1]==board[2]!='-'or board[3]==board[4]==board[5]!='-'or board[6]==board[7]==board[8]!='-':
        print('GAME OVER')
        game_on=False
    elif  board[0]==board[3]==board[6]!='-'or board[1]==board[4]==board[7]!='-'or board[2]==board[5]==board[8]!='-':
        print('GAME OVER')
        game_on=False
    elif board[0]==board[4]==board[8]!='-'or board[2]==board[4]==board[6]!='-':
        print('GAME OVER')
        game_on=False
    else:
        game_on=True

def change_turn():
    global cturn
    if game_on==True:
        if cturn=='x':
            cturn='o'
        elif cturn=='o':
            cturn='x'
    return

def display_winner():
    global cturn,fill
    if fill==False:
        print('====TIE====')
    elif game_on==False:
        print('WINNER IS ',cturn)

def board_fill():
    global board,fill
    if '-' not in board:
        print('GAME OVER')
        game_on=False
        fill=False
    else:
        game_on=True

def play_game():
    global game_on
    print('======TIC TAK TOE======')
    while game_on:
        display_board()
        turn()
        check_win()
        board_fill()
        change_turn()
        display_winner()


'''input range
select number
check num in range
display result'''
import random as rr
num=1
lrange=1
urange=20
def input_range():
    global lrange,urange
    while True:
        lrange=int(input('enter the lower limit '))
        urange=int(input('enter the upper limit '))
        if lrange-urange<30:
            print('ENTER RANGE AGAIN')
            break
            
    

def select_number():
    global num
    num=rr.randrange(1,101)

def check_num_range():
    global num,lrange,urange
    if num in range(lrange,urange+1):
        print("YOU WIN NUM SI IN THE RANGE")
    else:
        print('YOU LOSE NUM IS NOT IN RANGE')

def GAMEPLAY():
    while True:
        print('****GUESS THE NUMBER****')
        print('RULES:set a range of length 30\nif the lucky number in range\nyou win else lose')
        input_range()
        select_number()
        check_num_range()
        chose=input('do you want to continue(yes,no)..')
        if chose=='no'or chose=='NO':
            break


#**********ALIEN INVADER*********

import pygame
import self as self

def ALIENINVADE():

    pygame.init()

    win = pygame.display.set_mode((800, 600))

    pygame.display.set_caption('first game')

    walkright = [pygame.image.load('R1.png'), pygame.image.load('R2.png'), pygame.image.load('R3.png'),
                 pygame.image.load('R4.png'), pygame.image.load('R5.png'), pygame.image.load('R6.png'),
                 pygame.image.load('R7.png'), pygame.image.load('R8.png'), pygame.image.load('R9.png')]
    walkleft = [pygame.image.load('L1.png'), pygame.image.load('L2.png'), pygame.image.load('L3.png'),
                pygame.image.load('L4.png'), pygame.image.load('L5.png'), pygame.image.load('L6.png'),
                pygame.image.load('L7.png'), pygame.image.load('L8.png'), pygame.image.load('L9.png')]
    bg = pygame.transform.scale(pygame.image.load('bg.png'), (800, 600))
    char = pygame.image.load('standing.png')

    score = 0

    music=pygame.mixer.music.load('music.mp3')
    pygame.mixer.music.play(-1)




    class player(object):
        def __init__(self, x, y, width, height):
            self.x = x
            self.y = y
            self.width = width
            self.height = height
            self.vel = 8
            self.isjump = False
            self.jumpcount = 10
            self.left = False
            self.right = False
            self.walkcount = 0
            self.standing = True
            self.hitbox = (int(self.x) + 15, int(self.y) + 10, 30, 50)

        def draw(self, win):
            if self.walkcount + 1 >= 27:
                self.walkcount = 0
            if not (self.standing):
                if self.left:
                    win.blit(walkleft[self.walkcount // 3], (int(self.x), int(self.y)))
                    self.walkcount += 1
                elif self.right:
                    win.blit(walkright[self.walkcount // 3], (int(self.x), int(self.y)))
                    self.walkcount += 1
            else:
                if self.right:
                    win.blit(walkright[0], (int(self.x), int(self.y)))
                else:
                    win.blit(walkleft[0], (int(self.x), int(self.y)))
            self.hitbox = (self.x + 15, self.y + 10, 30, 50)
            #pygame.draw.rect(win, (0, 0, 0), self.hitbox, 2)

        def hit(self):
            self.x=100
            self.walkcount=0
            font1=pygame.font.SysFont('comicsans',200)
            text=font1.render('-5',1,(255,0,0))
            win.blit(text,(300,300))
            pygame.display.update()

            i=0
            while i <100:
                pygame.time.delay(10)
                i+=1







    class bullet(object):
        def __init__(self, x, y, radius, color, facing):
            self.x = x
            self.y = y
            self.radius = radius
            self.color = color
            self.facing = facing
            self.vel = 15 * facing

        def draw(self, win):
            pygame.draw.circle(win, self.color, (self.x, self.y), self.radius)


    class enemy(object):

        def __init__(self, x, y, width, height, end):
            self.walkright = [pygame.image.load('R1E.png'), pygame.image.load('R2E.png'), pygame.image.load('R3E.png'),
                              pygame.image.load('R4E.png'), pygame.image.load('R5E.png'), pygame.image.load('R6E.png'),
                              pygame.image.load('R7E.png'), pygame.image.load('R8E.png'), pygame.image.load('R9E.png'),
                              pygame.image.load('R10E.png'), pygame.image.load('R11E.png')]
            self.walkleft = [pygame.image.load('L1E.png'), pygame.image.load('L2E.png'), pygame.image.load('L3E.png'),
                             pygame.image.load('L4E.png'), pygame.image.load('L5E.png'), pygame.image.load('L6E.png'),
                             pygame.image.load('L7E.png'), pygame.image.load('L8E.png'), pygame.image.load('L9E.png'),
                             pygame.image.load('L10E.png'), pygame.image.load('L11E.png')]

            self.x = x
            self.y = y
            self.width = width
            self.height = height
            self.end = end
            self.walkcount = 0
            self.vel = 4
            self.path = [self.x, self.end]
            self.hitbox = (int(self.x) + 20, int(self.y), 30, 60)
            self.health=20
            self.visible=True

        def draw(self, win):
            self.move()
            if self.visible:
                if self.walkcount + 1 >= 33:
                    self.walkcount = 0

                if self.vel > 0:
                    win.blit(self.walkright[self.walkcount // 3], (self.x, self.y))
                    self.walkcount += 1
                else:
                    win.blit(self.walkleft[self.walkcount // 3], (self.x, self.y))
                    self.walkcount += 1

                pygame.draw.rect(win, (255, 0, 0), (300, 50, 200, 40))
                pygame.draw.rect(win, (0, 255, 0), (300, 50, 200-((200//20)*(20-int(self.health))), 40))

                self.hitbox = (self.x + 20, self.y, 30, 60)
                #pygame.draw.rect(win, (0, 0, 0), self.hitbox, 2)

        def move(self):
            if self.vel > 0:
                if self.x < self.path[1] + self.vel:
                    self.x += self.vel
                else:
                    self.vel = self.vel * -1
                    self.walkcount = 0
            else:
                if self.x > self.path[0] - self.vel:
                    self.x += self.vel
                else:
                    self.vel = self.vel * -1
                    self.walkcount = 0

        def hit(self):
            if self.health>0:
                self.health-=1
            else:
                self.visible=False
                run=False



            pass


    def redrawgamewindow():
        win.blit(bg, (0, 0))
        text = font.render('SCORE: ' + str(score), 1, (255, 0, 0))
        win.blit(text, (600, 50))
        man.draw(win)
        alien.draw(win)
        for bull in bullets:
            bull.draw(win)

        pygame.display.update()


    clock = pygame.time.Clock()

    # main loop
    facing=-1
    font = pygame.font.SysFont('comicsans', 40, True)
    bullets = []
    shoottime = 0
    man = player(300, 500, 64, 64)
    alien = enemy(100, 500, 64, 64, 700)
    run = True
    while run:
        clock.tick(27)
        if alien.visible == True:
            if man.hitbox[1] < alien.hitbox[1] + alien.hitbox[3] and man.hitbox[1] + man.hitbox[3] > alien.hitbox[1]:
                if man.hitbox[0] + man.hitbox[2] > alien.hitbox[0] and man.hitbox[0] < alien.hitbox[0] + alien.hitbox[2]:
                    man.hit()
                    score -= 5



        if shoottime > 0:
            shoottime += 1
        if shoottime > 3:
            shoottime = 0

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        for bull in bullets:
            if bull.y - bull.radius < alien.hitbox[1] + alien.hitbox[3] and bull.y + bull.radius > alien.hitbox[1]:
                if bull.x + bull.radius > alien.hitbox[0] and bull.x - bull.radius < alien.hitbox[0] + alien.hitbox[2]:
                    alien.hit()
                    score += 1
                    bullets.pop(bullets.index(bull))
                if bull.x < 800 and bull.x > 0:
                    bull.x += bull.vel
                else:
                    bullets.pop(bullets.index(bull))

        keys = pygame.key.get_pressed()

        if keys[pygame.K_ESCAPE]:
            run=False

        if keys[pygame.K_SPACE] and shoottime == 0 and alien.visible:
            if man.left:
                facing = -1
            elif man.right:
                facing = 1
            if len(bullets) < 6:
                bullets.append(bullet(round(man.x + man.width // 2), round(man.y + man.height // 2), 5, (0, 0, 0), facing))

            shoottime = 1

        if keys[pygame.K_LEFT] and man.x > man.vel:
            man.x -= man.vel
            man.left = True
            man.right = False
            man.standing = False
        elif keys[pygame.K_RIGHT] and man.x < 800 - man.width - man.vel:
            man.x += man.vel
            man.right = True
            man.left = False
            man.standing = False
        else:
            man.standing = True
            man.walkcount = 0

        if not (man.isjump):

            if keys[pygame.K_UP]:
                man.isjump = True

                man.walkcount = 0
        else:
            if man.jumpcount >= -10:
                neg = 1
                if man.jumpcount < 0:
                    neg = -1
                man.y -= (man.jumpcount ** 2) * 0.5 * neg
                man.jumpcount -= 1
            else:
                man.isjump = False
                man.jumpcount = 10
        redrawgamewindow()
    pygame.quit()


def pp():
    pygame.init()
    pygame.display.set_caption('PING PONG')
    win = pygame.display.set_mode((800, 600))

    # left paddle
    score_p1 = 0
    y1 = 250

    def player1(y1):
        pygame.draw.rect(win, (255, 255, 255), (50, y1, 20, 100), 0)

    # right paddle
    score_p2 = 0
    y2 = 250

    def player2(y2):
        pygame.draw.rect(win, (255, 255, 255), (750, y2, 20, 100), 0)

    # ball
    x = 400
    y = 300
    vely = 3
    velx = 3

    def ball(x, y):
        pygame.draw.rect(win, (255, 255, 255), (x, y, 20, 20), 0)

    clock = pygame.time.Clock()
    run = True
    # MAIN LOOP
    while run:
        clock.tick(50)
        win.fill((0, 0, 0))

        player1(y1)
        player2(y2)
        ball(x, y)


        # ball movement
        y += vely
        x += velx
        if y <= 0:
            vely *= -1
        elif y >= 580:
            vely *= -1

        # ball collition
        if x <= 70 and y >= y1 and y <= y1 + 100 and x >= 50:
            velx *= -1
        elif x + 20 >= 750 and y >= y2 and y <= y2 + 100 and x <= 770:
            velx *= -1

        # score point
        if x <= 0:
            x = 300

            velx *= -1
            score_p2 += 1

        elif x >= 780:
            x = 300

            velx *= -1
            score_p1 += 1

        # print score
        font = pygame.font.SysFont('comicsans', 40, True)
        text = font.render('SCORE: ' + str(score_p1), 1, (255, 255, 255))
        win.blit(text, (200, 50))
        text = font.render('SCORE: ' + str(score_p2), 1, (255, 255, 255))
        win.blit(text, (400, 50))

        # game over
        font = pygame.font.SysFont('comicsans', 40, True)
        final_text = font.render('GAME OVER', 1, (255, 255, 255))
        if score_p2 == 7 or score_p1 == 7:
            win.blit(final_text, (300, 300))
            i = 0
            while i < 100:
                pygame.time.delay(10)
                i += 1
            run = False

        keys = pygame.key.get_pressed()

        if keys[pygame.K_w] and y1 >= 0:
            y1 -= 5
        if keys[pygame.K_s] and y1 <= 500:
            y1 += 5
        if keys[pygame.K_UP] and y2 >= 0:
            y2 -= 5
        if keys[pygame.K_DOWN] and y2 <= 500:
            y2 += 5

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        pygame.display.update()

    pygame.quit()


def MENU():
    while True:
        print('*****WELCOME*****')
        print('1 FOR GUESS THE NUMBER')
        print('2 FOR ROCK PAPER SISSOR')
        print('3 FOR TIC TAK TOE (two player)')
        print('4 FOR PING PONG (two player)')
        print('5 FOR ALIEN INVADER')
        print('6 FOR EXIT')
        choice=int(input('enter your choice....'))
        if choice==1:GAMEPLAY()
        elif choice==2:RPSGAME()
        elif choice==3:play_game()
        elif choice==4:pp()
        elif choice==5:ALIENINVADE()
        elif choice==6:
            print('EXITING..........')
            break
        else:
            print('wrong input')

MENU()
    
    




        
    
        


    
    
    
    
    
    

