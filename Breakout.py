import pygame, sys

#Initialize Pygame
pygame.init()

#Set up the game window
screen = pygame.display.set_mode((800, 600))

#Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
ORANGE = (255, 165, 0)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
PURPLE = (128, 0, 128)

#Variables
speed = 5
clock = pygame.time.Clock()
paddle = pygame.Rect(350, 500, 100, 20)

#Draw Ball
ball_speed = [5, 5]

ball_rect = pygame.Rect(395, 295, 20, 20)

#Ball Movement
def ball_movement():
  global ball_speed
  ball_rect.x += ball_speed[0]
  ball_rect.y += ball_speed[1]
  if ball_rect.colliderect(paddle):
    ball_speed[1] = -ball_speed[1]
  if ball_rect.top <=0 or ball_rect.bottom >= 600:
    ball_speed[1] = -ball_speed[1]
  if ball_rect.left <=0 or ball_rect.right >= 800:
    ball_speed[0] = -ball_speed[0]
#Border
walls = [
  pygame.Rect(0, 0, 800, 10),  # Top horizontal wall
  pygame.Rect(0, 590, 790, 10), # Bottom horizontal wall
  pygame.Rect(0, 10, 10, 580),  # Left vertical wall
  pygame.Rect(790, 10, 10, 600), # Right vertical wall
]
#Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
          
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        paddle.x -= speed
    if keys[pygame.K_RIGHT]:
        paddle.x += speed

    #Collisions
    for wall in walls:
      if paddle.colliderect(wall):
          if keys[pygame.K_LEFT]:
              paddle.x += speed
          if keys[pygame.K_RIGHT]:
              paddle.x -= speed

    screen.fill(WHITE)
    #Draw Shapes
    ball_movement()
    pygame.draw.rect(screen, BLACK, paddle)
    pygame.draw.circle(screen, BLACK, ball_rect.center, 20)
    for wall in walls:
      pygame.draw.rect(screen, BLACK, wall)
    pygame.display.flip()
    clock.tick(30)
pygame.quit()
sys.exit()
