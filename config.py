import pygame
pygame.init()

# Window Size
screenwidth = 1720
screenheight = 980

# FPS
fps = 27

# Sprites

walkRight = [
    pygame.image.load('images/sprite1/R1.png'),
    pygame.image.load('images/sprite1/R2.png'),
    pygame.image.load('images/sprite1/R3.png'),
    pygame.image.load('images/sprite1/R4.png'),
    pygame.image.load('images/sprite1/R5.png'),
    pygame.image.load('images/sprite1/R6.png'),
    pygame.image.load('images/sprite1/R7.png'),
    pygame.image.load('images/sprite1/R8.png'),
    pygame.image.load('images/sprite1/R9.png')]

walkLeft = [
    pygame.image.load('images/sprite1/L1.png'),
    pygame.image.load('images/sprite1/L2.png'),
    pygame.image.load('images/sprite1/L3.png'),
    pygame.image.load('images/sprite1/L4.png'),
    pygame.image.load('images/sprite1/L5.png'),
    pygame.image.load('images/sprite1/L6.png'),
    pygame.image.load('images/sprite1/L7.png'),
    pygame.image.load('images/sprite1/L8.png'),
    pygame.image.load('images/sprite1/L9.png')]

bg = pygame.image.load('images/bg.jpg')

walkRight_2 = [
    pygame.image.load('images/sprite2/R1E.png'),
    pygame.image.load('images/sprite2/R2E.png'),
    pygame.image.load('images/sprite2/R3E.png'),
    pygame.image.load('images/sprite2/R4E.png'),
    pygame.image.load('images/sprite2/R5E.png'),
    pygame.image.load('images/sprite2/R6E.png'),
    pygame.image.load('images/sprite2/R7E.png'),
    pygame.image.load('images/sprite2/R8E.png'),
    pygame.image.load('images/sprite2/R9E.png')]

walkLeft_2 = [
    pygame.image.load('images/sprite2/L1E.png'),
    pygame.image.load('images/sprite2/L2E.png'),
    pygame.image.load('images/sprite2/L3E.png'),
    pygame.image.load('images/sprite2/L4E.png'),
    pygame.image.load('images/sprite2/L5E.png'),
    pygame.image.load('images/sprite2/L6E.png'),
    pygame.image.load('images/sprite2/L7E.png'),
    pygame.image.load('images/sprite2/L8E.png'),
    pygame.image.load('images/sprite2/L9E.png')]

char = pygame.image.load('images/sprite1/standing.png')
char_2 = pygame.image.load('images/sprite2/R5E.png')

ship_1 = pygame.image.load('images/ship/ship.png')
ship_2 = pygame.image.load('images/ship/ship.png')
ship_3 = pygame.image.load('images/ship/ship.png')
ship_4 = pygame.image.load('images/ship/ship.png')
ship_5 = pygame.image.load('images/ship/ship.png')

spike = pygame.image.load('images/spike/spike.png')

# Flags to check which player is dead
player1 = 0
player2 = 0

# Winner
winner = 0

# Flags to check which player is playing
player1_playing = True
player2_playing = False

# Scores of each player
player1_score = 0
player2_score = 0

# Flags to check score based on player position
strip1 = 0
strip2 = 0
strip3 = 0
strip4 = 0
strip5 = 0
strip1_reached = 0
strip2_reached = 0
strip3_reached = 0
strip4_reached = 0
strip5_reached = 0

# Initial coordinates of both players
x = 860
y = 920
x_2 = 860
y_2 = 10

# Player Width and Height
width = 64
height = 64

# Ship Width and Height
ship_width = 80
ship_height = 73

# Player Velocity
vel = 5

# Ships Inital Coordinates
ship_135x = 0
ship_24x = screenwidth-ship_width
ship_1y = 820
ship_2y = 634
ship_3y = 438
ship_4y = 242
ship_5y = 76

# Ships Initial Velocities for each player
vel_player1 = 5
vel_player2 = 5

# Flags for player movements
left = False
right = False
left_2 = False
right_2 = False

# Flags for Ship movements
mov_right = True
mov_left = False

# Timer Variables
start = 0
end = 0

# Colors
black = (0, 0, 0)
red = (255, 0, 0)
yellow = (155, 135, 12)
white = (255, 255, 255)
blue = (0, 255, 255)

# Fonts
scorefont = pygame.font.SysFont("monospace", 16)
popfont = pygame.font.SysFont("monospace", 76)
player1_success = popfont.render("Player 1 WINS", 1, red)
player2_success = popfont.render("Player 2 WINS", 1, red)
player1_hit = scorefont.render("Player 1 HIT WITH OBSTACLE", 1, white)
player2_hit = scorefont.render("Player 2 HIT WITH OBSTACLE", 1, white)
drawgame = popfont.render("DRAW", 1, red)
