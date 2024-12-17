import pygame, sys, time, asyncio

#Initialize pygame
pygame.init()

#set windows size
window_Width = 800
window_Height = 600
speed = 6
scoreLeft = 0
scoreRight = 0
screen = pygame.display.set_mode((window_Width, window_Height))
pygame.display.set_caption("Pygame Pong")

#Set Clock
clock = pygame.time.Clock()

#Define Paddles
paddleLeft = pygame.Rect(75, 200, 10, 150)
paddleRight = pygame.Rect(725, 200, 10, 150)

#Define Colors
WHITE = (255, 255, 255)
PURPLE = (255, 0, 255)
BLACK = (0, 0 ,0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

walls = [
    pygame.Rect(0, 0, 800, 10),  # Top horizontal wall
    pygame.Rect(0, 590, 790, 10), # Bottom horizontal wall
    pygame.Rect(0, 10, 10, 580),  # Left vertical wall
    pygame.Rect(790, 10, 10, 600), # Right vertical wall
]

buttons = [
    pygame.Rect(200, 250, 100, 50),
    pygame.Rect(500, 250, 100, 50),
    pygame.Rect(200, 250, 100, 50),
    pygame.Rect(500, 250, 100, 50)
]

#Draw Center Line
def draw_center_line_Black():
    pos_y = 10
    for i in range(14):
        pygame.draw.rect(screen, BLACK, (390, pos_y, 10, 30))
        pos_y +=50

def draw_center_line_White():
    pos_y = 10
    for i in range(14):
        pygame.draw.rect(screen, WHITE, (390, pos_y, 10, 30))
        pos_y +=50

#Draw ball
ball_speed = [5, 5]

ball_rect = pygame.Rect(395, 295, 40, 40)
#AI Movement
def ai_movement():
    if ball_rect.y < paddleRight.centery:
        paddleRight.top -= 3
    elif ball_rect.y > paddleRight.centery:
        paddleRight.bottom += 3
#2 Player Movement
def handle_ball_move():
    global scoreLeft
    global scoreRight
    global ball_speed
    global timer
    ball_rect.x += ball_speed[0]
    ball_rect.y += ball_speed[1]

    if ball_rect.top <=0 or ball_rect.bottom>= 600:
        ball_speed[1] = -ball_speed[1]

    if ball_rect.colliderect(paddleLeft) or ball_rect.colliderect(paddleRight):
        ball_speed[0] = -ball_speed[0]

    if ball_rect.left <= 0:
        scoreRight += 1
        reset_ball()

    if ball_rect.right >= 800:
        scoreLeft += 1
        reset_ball()
        
def reset_ball():
    global timer
    ball_rect.center = (395, 295)

#Define text
def scoringBlack():
    font1 = pygame.font.Font(None, 96)
    text1 = font1.render(str(scoreLeft), True, BLACK)
    textRect1 = text1.get_rect(center = (200, 50))
    screen.blit(text1, textRect1)
    
    font2 = pygame.font.Font(None, 96)
    text2 = font2.render(str(scoreRight), True, BLACK)
    textRect2 = text2.get_rect(center = (600, 50))
    screen.blit(text2, textRect2)
    
def scoringWhite():
    font6 = pygame.font.Font(None, 96)
    text6 = font6.render(str(scoreLeft), True, WHITE)
    textRect6 = text6.get_rect(center = (200, 50))
    screen.blit(text6, textRect6)
    
    font7 = pygame.font.Font(None, 96)
    text7 = font7.render(str(scoreRight), True, WHITE)
    textRect7 = text7.get_rect(center = (600, 50))
    screen.blit(text7, textRect7)
    
def PlayerText():
    font12 = pygame.font.Font(None, 40)
    text12 = font12.render("One or Two Players?", True, BLACK)
    textRect12 = text12.get_rect(center = (400, 200))
    screen.blit(text12, textRect12),
    
    font13 = pygame.font.Font(None, 40)
    text13 = font13.render("1P", True, BLACK)
    textRect13 = text13.get_rect(center = (250, 275))
    screen.blit(text13, textRect13),

    font14 = pygame.font.Font(None, 40)
    text14 = font14.render("2P", True, BLACK)
    textRect14 = text14.get_rect(center = (550, 275))
    screen.blit(text14, textRect14)

def ThemeText():
    font3 = pygame.font.Font(None, 40)
    text3 = font3.render("Which theme do you want?", True, BLACK)
    textRect3 = text3.get_rect(center = (400, 200))
    screen.blit(text3, textRect3),
    
    font4 = pygame.font.Font(None, 40)
    text4 = font4.render("Black", True, BLACK)
    textRect4 = text4.get_rect(center = (250, 275))
    screen.blit(text4, textRect4),

    font5 = pygame.font.Font(None, 40)
    text5 = font5.render("White", True, WHITE)
    textRect5 = text5.get_rect(center = (550, 275))
    screen.blit(text5, textRect5)

def endText1():
    font8 = pygame.font.Font(None, 40)
    text8 = font8.render("Player 1 Wins", True, WHITE)
    textRect8 = text8.get_rect(center = (200, 150))
    screen.blit(text8, textRect8)

def endText2():
    font9 = pygame.font.Font(None, 40)
    text9 = font9.render("Player 1 Wins", True, BLACK)
    textRect9 = text9.get_rect(center = (200, 150))
    screen.blit(text9, textRect9)

def endText3():
    font10 = pygame.font.Font(None, 40)
    text10 = font10.render("Player 2 Wins", True, WHITE)
    textRect10 = text10.get_rect(center = (600, 150))
    screen.blit(text10, textRect10)

def endText4(): 
    font11 = pygame.font.Font(None, 40)
    text11 = font11.render("Player 2 Wins", True, BLACK)
    textRect11 = text11.get_rect(center = (600, 150))
    screen.blit(text11, textRect11)

#Game Loop Starts
PlayerPick = True
ThemePick = False
BlackTheme = False
WhiteTheme = False

#Game loops
while PlayerPick == True:
    screen.fill(WHITE)
    sprite3 = buttons[2]
    sprite4 = buttons[3]
    pygame.draw.rect(screen, PURPLE, sprite3)
    pygame.draw.rect(screen, PURPLE, sprite4)
    PlayerText()
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            if sprite3.collidepoint(pygame.mouse.get_pos()):
                ThemePick = True
                PlayerPick = False
                playernumber = 1
                break
            elif sprite4.collidepoint(pygame.mouse.get_pos()):
                ThemePick = True
                PlayerPick = False
                playernumber = 2
                break
    pygame.display.flip()
while ThemePick == True:
    screen.fill(WHITE)
    sprite1 = buttons[0]
    sprite2 = buttons[1]
    pygame.draw.rect(screen, PURPLE, sprite1)
    pygame.draw.rect(screen, PURPLE, sprite2)
    ThemeText()
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            if sprite1.collidepoint(pygame.mouse.get_pos()):
                BlackTheme = True
                ThemePick = False
                break
            elif sprite2.collidepoint(pygame.mouse.get_pos()):
                WhiteTheme = True
                ThemePick = False
                break
    pygame.display.flip()

while BlackTheme == True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            BlackTheme = False

    keys = pygame.key.get_pressed()
    if playernumber == 1:
        if keys[pygame.K_w]:
            paddleLeft.y -= speed
        if keys[pygame.K_s]:
            paddleLeft.y += speed
        ai_movement()
    if playernumber == 2:
        if keys[pygame.K_UP]:
            paddleRight.y -= speed
        if keys[pygame.K_DOWN]:
            paddleRight.y += speed
        if keys[pygame.K_w]:
            paddleLeft.y -= speed
        if keys[pygame.K_s]:
            paddleLeft.y += speed
    
    for wall in walls:
        if paddleLeft.colliderect(wall):
            if keys[pygame.K_w]:
                paddleLeft.y += speed
            if keys[pygame.K_s]:
                paddleLeft.y -= speed
        if paddleRight.colliderect(wall):
            if keys[pygame.K_UP]:
                paddleRight.y += speed
            if keys[pygame.K_DOWN]:
                paddleRight.y -= speed
    

    screen.fill(BLACK)
    
    for wall in walls:
        pygame.draw.rect(screen, WHITE, wall)
    draw_center_line_White()
    handle_ball_move()
    scoringWhite()
    if scoreLeft == 3:
        endText1()
        reset_ball()
        ball_speed = [0, 0]
    if scoreRight == 3:
        endText3()
        reset_ball()
        ball_speed = [0, 0]
    pygame.draw.rect(screen, WHITE, paddleRight)
    pygame.draw.rect(screen, WHITE, paddleLeft)
    pygame.draw.circle(screen, WHITE, ball_rect.center, 20)
    pygame.display.flip()
    clock.tick(30)

while WhiteTheme == True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            WhiteTheme = False
            
    pygame.draw.rect(screen, WHITE, sprite1)
    pygame.draw.rect(screen, WHITE, sprite2)
    
    pygame.display.flip()
    keys = pygame.key.get_pressed()
    if playernumber == 1:
        if keys[pygame.K_w]:
            paddleLeft.y -= speed
        if keys[pygame.K_s]:
            paddleLeft.y += speed
        ai_movement()
    if playernumber == 2:
        if keys[pygame.K_UP]:
            paddleRight.y -= speed
        if keys[pygame.K_DOWN]:
            paddleRight.y += speed
        if keys[pygame.K_w]:
            paddleLeft.y -= speed
        if keys[pygame.K_s]:
            paddleLeft.y += speed
    
    for wall in walls:
        if paddleLeft.colliderect(wall):
            if keys[pygame.K_w]:
                paddleLeft.y += speed
            if keys[pygame.K_s]:
                paddleLeft.y -= speed
        if paddleRight.colliderect(wall):
            if keys[pygame.K_UP]:
                paddleRight.y += speed
            if keys[pygame.K_DOWN]:
                paddleRight.y -= speed
    

    screen.fill(WHITE)

    for wall in walls:
        pygame.draw.rect(screen, BLACK, wall)

    draw_center_line_Black()
    handle_ball_move()
    scoringBlack()
    if scoreLeft == 3:
        endText2()
        reset_ball()
        ball_speed = [0, 0]
    if scoreRight == 3:
        endText4()
        reset_ball()
        ball_speed = [0, 0]
    pygame.draw.rect(screen, BLACK, paddleRight)
    pygame.draw.rect(screen, BLACK, paddleLeft)
    pygame.draw.circle(screen, BLACK, ball_rect.center, 20)
    pygame.display.flip()
    clock.tick(30)
pygame.quit()
sys.exit()