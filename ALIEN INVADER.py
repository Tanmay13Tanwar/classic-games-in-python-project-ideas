import pygame
import self as self

pygame.init()

win = pygame.display.set_mode((800, 600))

pygame.display.set_caption('ALIEN INVADER')

walkright = [pygame.image.load('R1.png'), pygame.image.load('R2.png'), pygame.image.load('R3.png'),
             pygame.image.load('R4.png'), pygame.image.load('R5.png'), pygame.image.load('R6.png'),
             pygame.image.load('R7.png'), pygame.image.load('R8.png'), pygame.image.load('R9.png')]
walkleft = [pygame.image.load('L1.png'), pygame.image.load('L2.png'), pygame.image.load('L3.png'),
            pygame.image.load('L4.png'), pygame.image.load('L5.png'), pygame.image.load('L6.png'),
            pygame.image.load('L7.png'), pygame.image.load('L8.png'), pygame.image.load('L9.png')]
bg = pygame.transform.scale(pygame.image.load('bg.png'), (800, 600))
char = pygame.image.load('standing.png')

score = 0


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
        print('hit')

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
