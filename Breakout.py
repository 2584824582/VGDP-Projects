import pygame, sys

#Initialize Pygame
pygame.init()
WIDTH = 800
HEIGHT = 600
playerlives = 3
#Set up the game window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Breakout Pygame")

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
speed = 7
clock = pygame.time.Clock()
paddle = pygame.Rect(350, 500, 100, 20)

#Block dimensions for Colors
BLOCK_WIDTH = 70
BLOCK_HEIGHT = 25
BLOCK_MARGIN = 9
BLOCK_ROWS = 6
BLOCK_COLUMNS = 10

#list of blocks
blocks = []

#Lives Text
def livesText():
  global playerlives
  font1 = pygame.font.Font(None, 48)
  text1 = font1.render("Lives: ", True, BLACK)
  text_rect1 = text1.get_rect(center = (75, 570))
  screen.blit(text1, text_rect1)
  
  font2 = pygame.font.Font(None, 48)
  text2 = font2.render(str(playerlives), True, BLACK)
  text_rect2 = text2.get_rect(center = (135, 570))
  screen.blit(text2, text_rect2)
def endtextLose():
  font3 = pygame.font.Font(None, 48)
  text3 = font3.render("You Lose!", True, BLACK)
  text_rect3 = text3.get_rect(center = (395, 295))
  screen.blit(text3, text_rect3)
def endtextWin():
  font4 = pygame.font.Font(None, 48)
  text4 = font4.render("You Win!!", True, BLACK)
  text_rect4 = text4.get_rect(center = (395, 295))
  screen.blit(text4, text_rect4)
#Create the list
for row in range(BLOCK_ROWS):
  for col in range(BLOCK_COLUMNS):
    x = col * (BLOCK_WIDTH + BLOCK_MARGIN) + BLOCK_MARGIN
    y = row * (BLOCK_HEIGHT + BLOCK_MARGIN) + BLOCK_MARGIN
    block = pygame.Rect(x, y, BLOCK_WIDTH, BLOCK_HEIGHT)
    blocks.append(block)

#Draw Ball
ball_speed = [7, 7]

ball_rect = pygame.Rect(395, 295, 20, 10)

#Ball Movement
def reset_ball():
  global straight
  ball_rect.center = (395, 295)
  straight = True
def ball_movement_straight():
  global ball_speed
  global straight
  global playerlives

  ball_rect.y += ball_speed[1]

  if ball_rect.bottom >= 590:
    ball_speed[1] = -ball_speed[1]
    playerlives -= 1
    reset_ball()
    

  if ball_rect.colliderect(paddle):
    ball_speed[1] = -ball_speed[1]
    straight = False

def ball_movement_sideways():
  global ball_speed
  global playerlives
  ball_rect.x += ball_speed[0]
  ball_rect.y += ball_speed[1]

  if ball_rect.bottom >= 590:
    ball_speed[1] = -ball_speed[1]
    playerlives -= 1
    reset_ball()
  if paddle.x <= 300:
    if ball_rect.top <= 10:
     ball_speed[1] = -ball_speed[1]

  if paddle.x <= 300:
    if ball_rect.left <= 10 or ball_rect.right >= 790:
      ball_speed[0] = -ball_speed[0]

  if paddle.x <= 300:
    if ball_rect.colliderect(paddle):
      ball_speed[1] = -ball_speed[1]
  
  if paddle.x >= 300:
    if ball_rect.top <= 10:
     ball_speed[1] = ball_speed[1]

  if paddle.x >= 300:
    if ball_rect.left <= 10 or ball_rect.right >= 790:
      ball_speed[0] = ball_speed[0]

  if paddle.x >= 300:
    if ball_rect.colliderect(paddle):
      ball_speed[1] = ball_speed[1]
#Border
walls = [
  pygame.Rect(0, 0, 800, 10),  # Top horizontal wall
  pygame.Rect(0, 590, 790, 10), # Bottom horizontal wall
  pygame.Rect(0, 10, 10, 580),  # Left vertical wall
  pygame.Rect(790, 10, 10, 600), # Right vertical wall
]
#Game loop
running = True
straight = True
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
    for block in blocks:
      if ball_rect.colliderect(block):
        blocks.remove(block)
        ball_speed[1] = -ball_speed[1]
            

    screen.fill(WHITE)
    #Draw Shapes
    for block in blocks:
        pygame.draw.rect(screen, RED, block)
    if straight == True:
      ball_movement_straight()
    if straight == False:
      ball_movement_sideways()
    livesText()
    if playerlives == 0:
      endtextLose()
      ball_speed = [0, 0]
    if len(blocks) == 0:
      endtextWin()
    pygame.draw.rect(screen, BLACK, paddle)
    pygame.draw.circle(screen, BLACK, ball_rect.center, 10)
    for wall in walls:
      pygame.draw.rect(screen, BLACK, wall)
    pygame.display.flip()
    clock.tick(30)
pygame.quit()
sys.exit()
