#List of names [yes]
#Pick one randomly [no]
#Delete each one as they're picked [no]
#Reset the list [no]
#"Trigger" button [in progress]
#Words on screen [almost done]

import random

#initiating pygame and font
import pygame
WHITE = (255, 255, 255)
SCREEN_WIDTH = 300
SCREEN_HEIGHT = 200
pygame.init()
screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])


#other stuff
hungrykids = ["Sophie", "Colton", "Julia", "Isaac", "Owen", "Rose",
         "Jillian", "Paisley", "Lily", "Samson", "Lucas", "Sophia",
              "Sven", "Grace", "JM", "Violet", "Carson", "Stephen",
              "Caden", "Abby", "Ella", "Wade", "Reed"]
random.shuffle(hungrykids)
print hungrykids

def reset 
def nextkid

while True: 
    for event in pygame.event.get():
        keys = pygame.key.get_pressed()
        if keys[K_ESCAPE]: 
            pygame.quit()
        elif keys[K_r]:
            reset()
        elif keys[K_SPACE]:
            nextkid()
    screen.fill(WHITE)
    myfont = pygame.font.SysFont("georgia", 18)
    intro = myfont.render("Snackerator 9000 TM", 1, (255, 0, 0))
    yourname = myfont.render("Name", 1, (255, 0, 0))
    screen.blit(intro, (50, 10))
    screen.blit(yourname, (100, 40))
    
    pygame.display.flip()
#K_r K_SPACE
