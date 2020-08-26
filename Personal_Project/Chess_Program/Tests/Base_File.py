#=================================Chess=Program================================#

#==============Game=Setup===============#
import pygame
import random
import os
import Seek_codes

#====Set=Some=Variables====#

#Game
WIDTH = 600
HIEGHT = 600
FPS = 11

#Colors
WHITE = (215, 215, 215)
BLACK = (30, 30, 30)
RED = (200, 20, 20)
GREEN = (20, 200, 20)
BLUE = (100, 210, 255)
YELLOW = (255, 255, 0)
BROWN = (100,50,0)

#Sprites
TILESIZE = 75


#===========Set=Up=Pygame==========#


pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH,HIEGHT))
pygame.display.set_caption("Chess")
clock = pygame.time.Clock()
all_sprites = pygame.sprite.Group()
tiles = pygame.sprite.Group()
peices = pygame.sprite.Group()
white = pygame.sprite.Group()
game_folder = os.path.dirname(__file__)
peice_folder = os.path.join(os.path.join(game_folder,'Pictures'),'Chess')
wkimage = pygame.transform.scale(pygame.image.load(os.path.join(peice_folder,'knightB.png')).convert(),(50,50))


font_name = pygame.font.match_font('comic sans ms')


#==============================Start=Creating=The=Game=============================#

#============Create=The=Sprites=============#

#Create a basic tile sprite
class Tile(pygame.sprite.Sprite):
    def __init__(self,tilex,tiley,name,colour):
        pygame.sprite.Sprite.__init__(self)
        self.name = name
        self.tilex = tilex
        self.tiley = tiley
        self.colour = colour
        self.incol = colour
        self.image = pygame.Surface((TILESIZE,TILESIZE))
        self.image.fill(self.colour)
        self.rect = self.image.get_rect()
        self.rect.right = self.tilex * TILESIZE
        self.rect.bottom = self.tiley * TILESIZE
    def update(self):
        self.image.fill(self.colour)
        self.colour = self.incol
    def check_for_mouse(self):
        self.mpos = pygame.mouse.get_pos()
        if self.mpos[0] in range(self.rect.left,self.rect.right) and self.mpos[1] in range(self.rect.top,self.rect.bottom):
            return True
        else:
            return False


#Create a simple knight
class WKnight(pygame.sprite.Sprite):
    def __init__(self,tilex,tiley,name,image,team):
        pygame.sprite.Sprite.__init__(self)
        self.image = image
        self.tilex = tilex
        self.tiley = tiley
        self.name = name
        self.tile = 'x' + str(self.tilex)+ 'y'+str(self.tiley)
        self.colorkey = BLACK
        self.rect = self.image.get_rect()
        self.team = team
        self.rect.center = (self.tilex * (TILESIZE / 2),self.tiley *(TILESIZE / 2))
    def update(self):
        self.teleport(self.tile)
    def teleport(self,tilename):
        for tile in tiles:
            if tile.name == tilename:
                self.rect.center = tile.rect.center
                self.tilex = tile.tilex
                self.tiley = tile.tiley
    def seek(self):
        return Seek_codes.wknightseek(self,tiles)




#===================Create=Some=Functions=For=Ease-of-use=================#

#Create a text draw function
def draw_text(surf=screen,text='TEXT',x=0,y=0,size=20,color=(0,0,0)):
#===================Create=Some=Functions=Fourf=screen,text='Text',size=20,x=0,y=0,color=BLACK):
    font = pygame.font.Font(font_name,size)
    text_surf = font.render(text, True , color)
    text_rect = text_surf.get_rect()
    text_rect.y = y
    text_rect.x = x
    surf.blit(text_surf, text_rect)

#Create a board creating function
def create_board():
    starcol = WHITE
    tx = 1
    ty = 1
    for i in range(8):
        for i in range(8):
            tile = Tile(tx,ty,"x"+str(tx)+"y"+str(ty),starcol)
            all_sprites.add(tile)
            tiles.add(tile)
            tx += 1
            if starcol == WHITE:
                starcol = BLACK
            else:
                starcol = WHITE
        ty += 1
        if starcol == WHITE:
            starcol = BLACK
        else:
            starcol = WHITE
        tx = 1



#========Game=Start=======#
#Spawn Sprites

#Create the game board
create_board()

#Create a knight
wknight = WKnight(2,7,'wknight1',wkimage,white)
all_sprites.add(wknight)
peices.add(wknight)
white.add(wknight)

#==define some variables====#
mousetile = "x0y0"

#========================================Game=Loop=======================#
running = True
while running:
    all_sprites.update()
    screen.fill(BLUE)
    all_sprites.draw(screen)
    peices.draw(screen)
    # draw_text(surf=screen,text='Knight Info:',y = 3,color=GREEN)
    # draw_text(surf=screen,text='Available Squares: '+str(wknight.seek())+',',size=13,color=GREEN,y = 30)
    # draw_text(surf=screen,text='Knight Position: '+ str(wknight.tile)+',',size=15,color=GREEN,y=45)
    # draw_text(surf=screen,text='Mouse Position: '+str(mousetile),size=15,color=GREEN,y=60)
    # draw_text(surf=screen,text='Number of Available Squares: '+str(len(wknight.seek())),size=15,color=GREEN,y=75)
    clock.tick(FPS)
    for tile in tiles:
        if tile.check_for_mouse():
            mousetile = tile.name
    for tile in tiles:
       if tile.name in wknight.seek():
           tile.colour = RED

    for tile in tiles:
        if tile.name == mousetile:
            if tile.colour == BLACK:
                tile.colour = (30,100,30)
            elif tile.colour == WHITE:
                tile.colour = (150,255,150)
            elif tile.colour == RED:
                tile.colour = BROWN
    pygame.display.flip()
    for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                wknight.tile = mousetile
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
