import pygame
import random
pygame.init()
width,height=500,500
screen=pygame.display.set_mode((width,height))
pygame.display.set_caption("Color Changing Ball!")
WHITE=(225,225,225)
BLACK=(0,0,0)
circle_radius=50
circle_pos=(width //2,height //2)
running=True
def random_color():
     return (
          random.randint(0,255),
          random.randint(0,255),
          random.randint(0,255)
     )
clock=pygame.time.Clock()
while running:
     for event in pygame.event.get():
          if event.type==pygame.QUIT:
               running=False
     screen.fill(BLACK)
     pygame.draw.circle(
          screen,random_color(),
          circle_pos,
          circle_radius
     )
     pygame.display.flip()
     clock.tick(2)
pygame.quit()     

