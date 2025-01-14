import pygame, sys, pickle

#Initialize Pygame
pygame.init()
WIDTH = 800
HEIGHT = 600
playerlives = 3
#Set up the game window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Breakout Pygame")

#High Scores
try:
    with open('score.txt', 'rb') as file:
        score = pickle.load(file)
except:
    score = 0
#Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
ORANGE = (255, 165, 0)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
PURPLE = (128, 0, 128)
#images
Galaxy_image = pygame.image.load('Galaxy.jpg')
blockimage = pygame.image.load('BlockImage.jpg')
MrHaye = pygame.image.load('MRHAYE.jpg')

#Variables
speed = 9
clock = pygame.time.Clock()
paddle = pygame.Rect(350, 500, 100, 20)
#highscoretxt = open('score.txt')
#Block dimensions for Colors
BLOCK_WIDTH = 80
BLOCK_HEIGHT = 45
BLOCK_MARGIN = 9
BLOCK_ROWS = 6
BLOCK_COLUMNS = 10

#list of blocks
blocks = []

#list of buttons
buttons = [
    pygame.Rect(200, 250, 100, 50),
    pygame.Rect(500, 250, 100, 50)
]

#Lives Text
def livesText():
  global playerlives
  font1 = pygame.font.Font(None, 48)
  text1 = font1.render("Lives: ", True, WHITE)
  text_rect1 = text1.get_rect(center = (75, 570))
  screen.blit(text1, text_rect1)
  
  font2 = pygame.font.Font(None, 48)
  text2 = font2.render(str(playerlives), True, WHITE)
  text_rect2 = text2.get_rect(center = (135, 570))
  screen.blit(text2, text_rect2)

def endtextLose():
  font3 = pygame.font.Font(None, 48)
  text3 = font3.render("You Lose!", True, WHITE)
  text_rect3 = text3.get_rect(center = (395, 270))
  screen.blit(text3, text_rect3)

def endtextWin():
  font4 = pygame.font.Font(None, 48)
  text4 = font4.render("You Win!!", True, WHITE)
  text_rect4 = text4.get_rect(center = (395, 270))
  screen.blit(text4, text_rect4)

def Theme():
  font5 = pygame.font.Font(None, 48)
  text5 = font5.render("Which theme do you want?", True, BLACK)
  text_rect5 = text5.get_rect(center = (400, 200))
  screen.blit(text5, text_rect5)

  font6 = pygame.font.Font(None, 48)
  text6 = font6.render("Haye", True, BLACK)
  text_rect6 = text6.get_rect(center = (250, 275))
  screen.blit(text6, text_rect6)

  font7 = pygame.font.Font(None, 48)
  text7 = font7.render("Space", True, BLACK)
  text_rect7 = text7.get_rect(center = (550, 275))
  screen.blit(text7, text_rect7)

def scoring():
  font8 = pygame.font.Font(None, 48)
  text8 = font8.render("Score:", True, WHITE)
  text_rect8 = text8.get_rect(center = (700, 570))
  screen.blit(text8, text_rect8)

  font9 = pygame.font.Font(None, 48)
  text9 = font9.render(str(score), True, WHITE)
  text_rect9 = text9.get_rect(center = (775, 570))
  screen.blit(text9, text_rect9)
def highscore():
  font10 = pygame.font.Font(None, 48)
  text10 = font10.render("High Score: ", True, WHITE)
  text_rect10 = text10.get_rect(center = (400, 400))
  screen.blit(text10, text_rect10)

  #font11 = pygame.font.Font(None, 48)
  #text11 = font11.render(str(highscoretxt), True, WHITE)
  #text_rect11 = text11.get_rect(center = (775, 570))
  #screen.blit(text11, text_rect11)
#Create the list
for row in range(BLOCK_ROWS):
  for col in range(BLOCK_COLUMNS):
    x = col * (BLOCK_WIDTH + BLOCK_MARGIN) + BLOCK_MARGIN
    y = row * (BLOCK_HEIGHT + BLOCK_MARGIN) + BLOCK_MARGIN
    block = pygame.Rect(x, y, BLOCK_WIDTH, BLOCK_HEIGHT)
    blocks.append(block)

#Draw Ball
ball_speed = [7, 7]

ball_rect = pygame.Rect(395, 350, 20, 10)

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
    
  if ball_rect.top <= 10:
     ball_speed[1] = -ball_speed[1]

  
  if ball_rect.left <= 10 or ball_rect.right >= 790:
      ball_speed[0] = -ball_speed[0]

  if ball_rect.colliderect(paddle):
      ball_speed[1] = -ball_speed[1]
      
#Border
walls = [
  pygame.Rect(0, 0, 800, 10),  # Top horizontal wall
  pygame.Rect(0, 590, 790, 10), # Bottom horizontal wall
  pygame.Rect(0, 10, 10, 580),  # Left vertical wall
  pygame.Rect(790, 10, 10, 600), # Right vertical wall
]
#Game loops
ThemePick = True
game_script_space = False
game_script_haye = False
straight = True

while ThemePick:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            ThemePick = False
    score = 0
    button1 = buttons[0]
    button2 = buttons[1]
    screen.fill(WHITE)
    pygame.draw.rect(screen, PURPLE, button1)
    pygame.draw.rect(screen, PURPLE, button2)
    Theme()
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            if button1.collidepoint(pygame.mouse.get_pos()):
                game_script_haye = True
                ThemePick = False
                break
            elif button2.collidepoint(pygame.mouse.get_pos()):
                game_script_space = True
                ThemePick = False
                break
    pygame.display.flip()

while game_script_space:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_script_space = False
          
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
        score += 1
            

    screen.blit(Galaxy_image, (0, 0))
    #Draw Shapes
    scoring()
    for block in blocks:
      pygame.draw.rect(screen, RED, block)
      screen.blit(blockimage, block)
    if straight == True:
      ball_movement_straight()
    if straight == False:
      ball_movement_sideways()
    livesText()
    if playerlives == 0:
      endtextLose()
      highscore()
      ball_speed = [0, 0]
    if len(blocks) == 0:
      endtextWin()
      reset_ball()
      ball_speed [0, 0]
    pygame.draw.rect(screen, WHITE, paddle)
    pygame.draw.circle(screen, WHITE, ball_rect.center, 10)
    for wall in walls:
      pygame.draw.rect(screen, WHITE, wall)
    pygame.display.flip()
    clock.tick(30)

while game_script_haye:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_script_haye = False
          
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
        score += 1
            

    screen.blit(Galaxy_image, (0, 0))
    #Draw Shapes
    scoring()
    for block in blocks:
      pygame.draw.rect(screen, RED, block) 
      screen.blit(MrHaye, block)
    if straight == True:
      ball_movement_straight()
    if straight == False:
      ball_movement_sideways()
    livesText()
    if playerlives == 0:
      endtextLose()
      highscore()
      ball_speed = [0, 0]
    if len(blocks) == 0:
      endtextWin()
      reset_ball()
      ball_speed [0, 0]
    pygame.draw.rect(screen, WHITE, paddle)
    pygame.draw.circle(screen, WHITE, ball_rect.center, 10)
    for wall in walls:
      pygame.draw.rect(screen, WHITE, wall)
    pygame.display.flip()
    clock.tick(30)
with open('score.txt', 'wb') as file:
    pickle.dump(score, file)
pygame.quit()
sys.exit()
