import pygame,sys,random,time
from pygame.locals import *

#initializing 
pygame.init()

FPS = 60
frame_per_sec = pygame.time.Clock()

#setting colours 
BLACk = (0,0,0)
RED = (255,0,0)
BLUE = (0,0,255)
GREEN = (0,255,0)
WHITE = (255,255,255)

DISPLAY_SURF = pygame.display.set_mode((500,600))
DISPLAY_SURF.fill(WHITE)
pygame.display.set_caption('LIZA AND ZOMBIES')
ICON = pygame.image.load('my_projects/liza.png')
pygame.display.set_icon(ICON)
SPEED = 4
SCORE = 0
font = pygame.font.SysFont("verdana",60)
font_small = pygame.font.SysFont('verdana',20)
GAME_OVER = font.render("GAME OVER",True,BLUE)


BACKGROUND = pygame.image.load("my_projects/zombie_back.png")

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('my_projects/zombie.png')
        self.surf = pygame.Surface((45,45))
        self.rect = self.surf.get_rect(center = (random.randint(40,450),0))
    
    def move(self):
        self.rect.move_ip(0,10)
        if self.rect.bottom > 700:
            self.rect.top = 0
            self.rect.center =(random.randint(40,450),0)
    def pos_enemy(self,surface):
        surface.blit(self.image,self.rect)  

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('my_projects/liza.png')
        self.surf = pygame.Surface((50,50))
        self.rect = self.surf.get_rect(center = (150,500))
    
    def move(self):
        press_key = pygame.key.get_pressed()
        # if self.rect.up >0:
        #     if press_key[K_UP]:
        #         self.rect.move_ip(0,-5)
        # if self.rect.down < 0: 
        #     if press_key[K_DOWN]:
        #         self.rect.move_ip(0,5)
        if self.rect.left >0:
            if press_key[K_LEFT]:
                self.rect.move_ip(-5,0)
        if self.rect.right < 500:
            if press_key[K_RIGHT]:
                self.rect.move_ip(5,0)

    def pos_player(self,surface):
        surface.blit(self.image,self.rect)






P1 = Player()
E1 = Enemy()
E2 = Enemy()

# craeting sprites group()
enemy_group = pygame.sprite.Group()
enemy_group.add(E1)
# enemy_group.add(E2)
all_sprites = pygame.sprite.Group()
all_sprites.add(P1)
all_sprites.add(E1)
# all_sprites.add(E2)

# adding a custom event

EN_SPEED = pygame.USEREVENT + 1
pygame.time.set_timer(EN_SPEED, 1000)



pygame.mixer.music.load("my_projects/2019-04-18_-_The_Epic_Boss_Fight_-_David_Fesliyan.mp3")

pygame.mixer.music.play()

while True:

    s =  E1.rect.center[0] - E2.rect.center[0]
    

    if  -80 < s > 80:
        try:
            enemy_group.add(E2)
            all_sprites.add(E2)
        except:
            pass
    else:
        try:
            enemy_group.remove(E2)
            all_sprites.remove(E2)
        except:
            pass
    
    for event in pygame.event.get():
        if event.type == EN_SPEED:
             SPEED += 1
             SCORE += 1
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    DISPLAY_SURF.blit(BACKGROUND,(0,0))
    scores = font_small.render(str(SCORE),True,RED)
    DISPLAY_SURF.blit(scores,(10,10))
    for entity in all_sprites:
        DISPLAY_SURF.blit(entity.image,entity.rect)
        entity.move()
    if pygame.sprite.spritecollideany(P1, enemy_group):
        pygame.mixer.music.stop()
        pygame.mixer.music.load("my_projects/zombie_sound.mp3")
        pygame.mixer.music.play()
        time.sleep(2)
        pygame.mixer.music.stop()
        DISPLAY_SURF.fill(RED)
        DISPLAY_SURF.blit(GAME_OVER,(40,350))
        total_score = font.render("SCORE :{}".format(SCORE),True,BLUE)
        DISPLAY_SURF.blit(total_score,(50,100))
        pygame.display.update()
        time.sleep(1.5)
        for entity in all_sprites:
            entity.kill()
        
        pygame.quit()
        sys.exit()
    
    # E2.pos_enemy(DISPLAY_SURF)
    
    pygame.display.update()
    frame_per_sec.tick(FPS)
