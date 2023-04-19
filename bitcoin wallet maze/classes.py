from pygame import *
WIDTH = 700
HEIGHT = 500
screen = display.set_mode((WIDTH,HEIGHT))

class Main(sprite.Sprite):
    def __init__(self, img,player_x,player_y,speed):
        super().__init__()
        self.image = transform.scale(image.load(img),(50,50))
        self.speed = speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
        
    def game_end(self):
        screen.blit(self.image,(self.rect.x,self.rect.y))
        
        
class Player(Main):
    def controls(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < HEIGHT - 50:
            self.rect.y += self.speed
        if keys[K_LEFT] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys[K_RIGHT] and self.rect.x < WIDTH - 50:
            self.rect.x += self.speed   
            
class Ghost(Main):
    direction = 'left'
    def update(self):
        if self.rect.x <= 250:
            self.direction = 'right'
        elif self.rect.x > WIDTH -50:
            self.direction = 'left'
        
        if self.direction == 'left':
            self.rect.x -= self.speed
        else:
            self.rect.x += self.speed



class Coins(sprite.Sprite):
    def __init__(self,coin_x,coin_y):
        super().__init__()
        self.rect = Rect(coin_x,coin_y,25,25)
        self.image = transform.scale(image.load("dollar.png"),(25,25))
        
    def mint_coin(self):
        screen.blit(self.image,(self.rect.x,self.rect.y))
        
        
class Border(sprite.Sprite):
    def __init__(self, color,x,y,width,height):
        super().__init__()
        self.width = width
        self.height = height
        self.image = Surface((self.width,self.height))
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        
    def build_wall(self):
        screen.blit(self.image,(self.rect.x,self.rect.y))