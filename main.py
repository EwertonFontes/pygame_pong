import pygame

pygame.init()

#set the dimensions of window
window = pygame.display.set_mode([1280, 720])

#set the title of the window
title = pygame.display.set_caption("Pong")

win_img = pygame.image.load("assets/win.png")

score_player_one = 0
score_player_one_img = pygame.image.load(f"assets/score/{score_player_one}.png")
score_player_two = 0
score_player_two_img = pygame.image.load(f"assets/score/{score_player_two}.png")

#INIT LOAD OBJECTS IN SCREEN
background_image = pygame.image.load("assets/field.png")

player_one = pygame.image.load("assets/player1.png")
player_one_y = 310
player_one_moveup = False
player_one_movedown = False

player_two = pygame.image.load("assets/player2.png")
player_two_y = 310
player_two_moveup = False
player_two_movedown = False

#BALL CENTER POSITION
ball = pygame.image.load("assets/ball.png")
ball_x = 617
ball_y = 337
ball_dir = -3
ball_dir_y = 1
#END LOAD OBJECTS IN SCREN


def center_ball():
    global ball_x
    global ball_y
    global ball_dir
    global ball_dir_y 

    ball_x = 617
    ball_y = 337
    ball_dir_y *= -1
    ball_dir *= -1
    if ball_dir > 0:
        ball_dir +=1
    elif ball_dir < 0:
        ball_dir -=1


#MOVING BALL
def move_ball():
    global ball_x
    global ball_y
    global ball_dir
    global ball_dir_y 
    global score_player_two
    global score_player_one
    global score_player_one_img
    global score_player_two_img

    ball_x += ball_dir
    ball_y += ball_dir_y
    if ball_x < 120:
        if player_one_y < ball_y + 23:
            if player_one_y + 146 > ball_y:
                ball_dir *= -1
    
    if ball_x > 1100:
        if player_two_y < ball_y + 23:
            if player_two_y + 146 > ball_y:
                ball_dir *= -1

    if ball_y > 670:
        ball_dir_y *= -1
    if ball_y <= 0:
        ball_dir_y *= -1

    if ball_x < -50:
        center_ball()
        score_player_two += 1
        score_player_two_img = pygame.image.load(f"assets/score/{str(score_player_two)}.png")
    elif ball_x > 1320:
        center_ball()
        score_player_one += 1
        score_player_one_img = pygame.image.load(f"assets/score/{str(score_player_one)}.png")


def move_player_one():
    global player_one_y
    
    if player_one_moveup:
        player_one_y -= 5
    else: 
        player_one_y += 0

    if player_one_movedown:
        player_one_y += 5
    else:
        player_one_y += 0
    
    if player_one_y <= 0:
        player_one_y = 0
    elif player_one_y >= 575:
        player_one_y = 575

def move_player_two():
    global player_two_y
    
    if player_two_moveup:
        player_two_y -= 5
    else: 
        player_two_y += 0

    if player_two_movedown:
        player_two_y += 5
    else:
        player_two_y += 0

    if player_two_y <= 0:
        player_two_y = 0
    elif player_two_y >= 575:
        player_two_y = 575


def draw(over: bool):
    #draw image on window in axis (x 0-1280,y 0-720)
    if over:
        window.blit(win_img, (300,330))
    else:
        window.blit(background_image, (0, 0))
        window.blit(player_one, (50, player_one_y))
        window.blit(player_two, (1150, player_two_y))
        window.blit(ball, (ball_x, ball_y))
        window.blit(score_player_one_img, (500, 50))
        window.blit(score_player_two_img, (710, 50))
        move_ball()
        move_player_one()
        move_player_two()       

loop = True
while loop:
    #This enables de window running in infinity loop
    for events in pygame.event.get():
        #foreach event got in screen
        if events.type == pygame.QUIT:
            loop = False
        if events.type == pygame.KEYDOWN:
            if events.key == pygame.K_w:
                #UP
                player_one_moveup = True
            if events.key == pygame.K_s:
                #DOWN
                player_one_movedown = True
            if events.key == pygame.K_UP:
                player_two_moveup = True
            if events.key == pygame.K_DOWN:
                player_two_movedown = True
        
        if events.type == pygame.KEYUP:
            if events.key == pygame.K_w:
                player_one_moveup = False
            if events.key == pygame.K_s:
                player_one_movedown = False
            if events.key == pygame.K_UP:
                player_two_moveup = False
            if events.key == pygame.K_DOWN:
                player_two_movedown = False
    
    over = False
    if score_player_one > 9:
        over = True
    if score_player_two > 9:
        over = True
        
    draw(over=over)
    
    pygame.display.update() 

