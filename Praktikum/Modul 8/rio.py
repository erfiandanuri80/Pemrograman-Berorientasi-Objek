import pygame
 
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
PURPLE = (255, 0, 255)
 

class Player(pygame.sprite.Sprite):
    change_x = 0
    change_y = 0
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface([15, 15])
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x
    def changespeed(self, x, y):
        self.change_x += x
        self.change_y += y

def main():
    pygame.init()
    screen=pygame.display.set_mode([800,600])
    pygame.display.set_caption('HMMMMM')
    x=30
    y=30
    player = Player(x, y)
    movingsprites = pygame.sprite.Group()
    movingsprites.add(player) 
    
    clock = pygame.time.Clock()
    done = False

    while not done:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_UP]:
            y -= 3
        if pressed[pygame.K_DOWN]:
            y += 3
        if pressed[pygame.K_LEFT]:
            x -= 3
        if pressed[pygame.K_RIGHT]:
            x += 3
                
 
        screen.fill(BLACK)
        movingsprites.draw(screen)
        pygame.display.flip()
        clock.tick(60)

                        
    pygame.quit()
    quit()
 
if __name__ == "__main__":
    main()
