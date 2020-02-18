from config import *
import pygame

pygame.init()

run = True

win = pygame.display.set_mode((screenwidth, screenheight))

pygame.display.set_caption("Boom Boom Ciao")

clock = pygame.time.Clock()

# Keeps track of player's direction
walkCount = 0

# Reset flags for keeping score


def reset():
    global strip1, strip2, strip3
    global strip4, strip5
    global strip1_reached, strip2_reached, strip3_reached
    global strip4_reached, strip5_reached
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


def checkGameEnd():
    global player1, player2, player1_score, player2_score, winner

    if player1 == -1 and player2 == -1:

        if player1_score > player2_score:
            winner = 1
        elif player1_score < player2_score:
            winner = 2
        else:
            winner = -1

# Making moving obstacles


def moveships():
    global ship_135x, ship_24x
    global mov_left, mov_right
    global ship_width
    global player1_playing, player2_playing

    if player1_playing:
        if ship_135x < screenwidth and mov_right:
            ship_135x += vel_player1
            ship_24x -= vel_player1
        if ship_135x >= screenwidth-ship_width and mov_right:
            mov_right = False
            mov_left = True
            ship_135x -= vel_player1
            ship_24x += vel_player1
        if ship_135x > 0 and mov_left:
            ship_135x -= vel_player1
            ship_24x += vel_player1
        if ship_135x <= 0 and mov_left:
            mov_left = False
            mov_right = True
            ship_135x += vel_player1
            ship_24x -= vel_player1

    if player2_playing:
        if ship_135x < screenwidth and mov_right:
            ship_135x += vel_player2
            ship_24x -= vel_player2
        if ship_135x >= screenwidth-ship_width and mov_right:
            mov_right = False
            mov_left = True
            ship_135x -= vel_player2
            ship_24x += vel_player2
        if ship_135x > 0 and mov_left:
            ship_135x -= vel_player2
            ship_24x += vel_player2
        if ship_135x <= 0 and mov_left:
            mov_left = False
            mov_right = True
            ship_135x += vel_player2
            ship_24x -= vel_player2

# Reload Window and place sprites


def redrawGameWindow():
    global walkCount, bulletx, bullety, winner
    global scorefont, popfont
    global player1_success, player2_success, drawgame
    global player1_hit, player2_hit, end

    win.blit(bg, (0, 0))
    pygame.draw.rect(win, yellow, (0, 920, 1720, 70))
    pygame.draw.rect(win, yellow, (0, 739, 1720, 60))
    pygame.draw.rect(win, yellow, (0, 543, 1720, 60))
    pygame.draw.rect(win, yellow, (0, 347, 1720, 60))
    pygame.draw.rect(win, yellow, (0, 151, 1720, 60))
    pygame.draw.rect(win, yellow, (0, 0, 1720, 70))

    if walkCount + 1 >= 27:
        walkCount = 0

    if left:
        win.blit(walkLeft[walkCount//3], (x, y))
        walkCount += 1
    elif right:
        win.blit(walkRight[walkCount//3], (x, y))
        walkCount += 1
    else:
        win.blit(char, (x, y))

    if walkCount + 1 >= 27:
        walkCount = 0

    if left_2:
        win.blit(walkLeft_2[walkCount//3], (x_2, y_2))
        walkCount += 1
    elif right_2:
        win.blit(walkRight_2[walkCount//3], (x_2, y_2))
        walkCount += 1
    else:
        win.blit(char_2, (x_2, y_2))

    scoretext1 = scorefont.render(
        "Player 1 Score = "+str(player1_score), 1, white)
    win.blit(scoretext1, (5, 920))

    scoretext2 = scorefont.render(
        "Player 2 Score = "+str(player2_score), 1, white)
    win.blit(scoretext2, (5, 10))

    time = scorefont.render("Time Elapsed: "+str(end//1000), 1, white)
    win.blit(time, (1500, 10))

    win.blit(ship_1, (ship_135x, ship_1y))
    win.blit(ship_2, (ship_24x, ship_2y))
    win.blit(ship_3, (ship_135x, ship_3y))
    win.blit(ship_4, (ship_24x, ship_4y))
    win.blit(ship_5, (ship_135x, ship_5y))
    moveships()

    win.blit(spike, (150, 150))
    win.blit(spike, (450, 150))
    win.blit(spike, (750, 150))
    win.blit(spike, (1050, 150))
    win.blit(spike, (1350, 150))

    win.blit(spike, (300, 345))
    win.blit(spike, (600, 345))
    win.blit(spike, (900, 345))
    win.blit(spike, (1200, 345))
    win.blit(spike, (1500, 345))

    win.blit(spike, (150, 540))
    win.blit(spike, (450, 540))
    win.blit(spike, (750, 540))
    win.blit(spike, (1050, 540))
    win.blit(spike, (1350, 540))

    win.blit(spike, (300, 740))
    win.blit(spike, (600, 740))
    win.blit(spike, (900, 740))
    win.blit(spike, (1200, 740))
    win.blit(spike, (1500, 740))

    # Message for HIT WITH OBSTACLE
    if player1 == -1:
        win.blit(player1_hit, (1400, 920))

    if player2 == -1:
        win.blit(player2_hit, (1400, 940))

    # Message for winner
    if winner == 1:
        pygame.draw.rect(win, black, (0, 420, 1720, 80))
        win.blit(player1_success, (500, 420))
        run = False
    elif winner == 2:
        pygame.draw.rect(win, black, (0, 420, 1720, 80))
        win.blit(player2_success, (500, 420))
        run = False
    elif winner == -1:
        pygame.draw.rect(win, black, (0, 420, 1720, 80))
        win.blit(drawgame, (800, 420))
        run = False

    pygame.display.update()

# Check collision of players and update timer


def checkCollision():
    global player1, player2, x, y, x_2, y_2
    global ship_135x, ship_24x
    global vel_player1, vel_player2, start, end
    global ship_1y, ship_2y, ship_3y, ship_4y, ship_5y
    global player1_playing, player2_playing
    global start, end, player1_score, player2_score

    if x > ship_135x-vel_player1 and x < ship_135x+ship_width+vel_player1:
        if y > ship_1y and y < ship_1y+ship_height:
            reset()
            player1_score -= end//1000
            start = pygame.time.get_ticks()
            end = pygame.time.get_ticks()
            player1 = -1

    if x > ship_24x-vel_player1 and x < ship_24x+ship_width+vel_player1:
        if y > ship_2y and y < ship_2y+ship_height:
            reset()
            player1_score -= end//1000
            start = pygame.time.get_ticks()
            end = pygame.time.get_ticks()
            player1 = -1

    if x > ship_135x-vel_player1 and x < ship_135x+ship_width+vel_player1:
        if y > ship_3y and y < ship_3y+ship_height:
            reset()
            player1_score -= end//1000
            start = pygame.time.get_ticks()
            end = pygame.time.get_ticks()
            player1 = -1

    if x > ship_24x-vel_player1 and x < ship_24x+ship_width+vel_player1:
        if y > ship_4y and y < ship_4y+ship_height:
            reset()
            player1_score -= end//1000
            start = pygame.time.get_ticks()
            end = pygame.time.get_ticks()
            player1 = -1

    if x > ship_135x-vel_player1 and x < ship_135x+ship_width+vel_player1:
        if y > ship_5y and y < ship_5y+ship_height:
            reset()
            player1_score -= end//1000
            start = pygame.time.get_ticks()
            end = pygame.time.get_ticks()
            player1 = -1

    if x_2 > ship_135x-vel_player2 and x_2 < ship_135x+ship_width+vel_player2:
        if y_2 > ship_1y and y_2 < ship_1y+ship_height:
            reset()
            player2_score -= end//1000
            start = pygame.time.get_ticks()
            end = pygame.time.get_ticks()
            player2 = -1

    if x_2 > ship_24x-vel_player2 and x_2 < ship_24x+ship_width+vel_player2:
        if y_2 > ship_2y and y_2 < ship_2y+ship_height:
            reset()
            player2_score -= end//1000
            start = pygame.time.get_ticks()
            end = pygame.time.get_ticks()
            player2 = -1

    if x_2 > ship_135x-vel_player2 and x_2 < ship_135x+ship_width+vel_player2:
        if y_2 > ship_3y and y_2 < ship_3y+ship_height:
            reset()
            player2_score -= end//1000
            start = pygame.time.get_ticks()
            end = pygame.time.get_ticks()
            player2 = -1

    if x_2 > ship_24x-vel_player2 and x_2 < ship_24x+ship_width+vel_player2:
        if y_2 > ship_4y and y_2 < ship_4y+ship_height:
            reset()
            player2_score -= end//1000
            start = pygame.time.get_ticks()
            end = pygame.time.get_ticks()
            player2 = -1

    if x_2 > ship_135x-vel_player2 and x_2 < ship_135x+ship_width+vel_player2:
        if y_2 > ship_5y and y_2 < ship_5y+ship_height:
            reset()
            player2_score -= end//1000
            start = pygame.time.get_ticks()
            end = pygame.time.get_ticks()
            player2 = -1

    if y >= 140 and y <= 195:
        if x >= 110 and x <= 195:
            reset()
            player1_score -= end//1000
            start = pygame.time.get_ticks()
            end = pygame.time.get_ticks()
            player1 = -1
        if x >= 410 and x <= 495:
            reset()
            player1_score -= end//1000
            start = pygame.time.get_ticks()
            end = pygame.time.get_ticks()
            player1 = -1
        if x >= 710 and x <= 795:
            reset()
            player1_score -= end//1000
            start = pygame.time.get_ticks()
            end = pygame.time.get_ticks()
            player1 = -1
        if x >= 1010 and x <= 1095:
            reset()
            player1_score -= end//1000
            start = pygame.time.get_ticks()
            end = pygame.time.get_ticks()
            player1 = -1
        if x >= 1310 and x <= 1395:
            reset()
            player1_score -= end//1000
            start = pygame.time.get_ticks()
            end = pygame.time.get_ticks()
            player1 = -1

    if y >= 480 and y <= 585:
        if x >= 110 and x <= 195:
            reset()
            player1_score -= end//1000
            start = pygame.time.get_ticks()
            end = pygame.time.get_ticks()
            player1 = -1
        if x >= 410 and x <= 495:
            reset()
            player1_score -= end//1000
            start = pygame.time.get_ticks()
            end = pygame.time.get_ticks()
            player1 = -1
        if x >= 710 and x <= 795:
            reset()
            player1_score -= end//1000
            start = pygame.time.get_ticks()
            end = pygame.time.get_ticks()
            player1 = -1
        if x >= 1010 and x <= 1095:
            reset()
            player1_score -= end//1000
            start = pygame.time.get_ticks()
            end = pygame.time.get_ticks()
            player1 = -1
        if x >= 1310 and x <= 1395:
            reset()
            player1_score -= end//1000
            start = pygame.time.get_ticks()
            end = pygame.time.get_ticks()
            player1 = -1

    if y >= 295 and y <= 385:
        if x >= 26 and x <= 340:
            reset()
            player1_score -= end//1000
            start = pygame.time.get_ticks()
            end = pygame.time.get_ticks()
            player1 = -1
        if x >= 560 and x <= 640:
            reset()
            player1_score -= end//1000
            start = pygame.time.get_ticks()
            end = pygame.time.get_ticks()
            player1 = -1
        if x >= 860 and x <= 940:
            reset()
            player1_score -= end//1000
            start = pygame.time.get_ticks()
            end = pygame.time.get_ticks()
            player1 = -1
        if x >= 1160 and x <= 1240:
            reset()
            player1_score -= end//1000
            start = pygame.time.get_ticks()
            end = pygame.time.get_ticks()
            player1 = -1
        if x >= 1460 and x <= 1540:
            reset()
            player1_score -= end//1000
            start = pygame.time.get_ticks()
            end = pygame.time.get_ticks()
            player1 = -1

    if y >= 685 and y <= 780:
        if x >= 26 and x <= 340:
            reset()
            player1_score -= end//1000
            start = pygame.time.get_ticks()
            end = pygame.time.get_ticks()
            player1 = -1
        if x >= 560 and x <= 640:
            reset()
            player1_score -= end//1000
            start = pygame.time.get_ticks()
            end = pygame.time.get_ticks()
            player1 = -1
        if x >= 860 and x <= 940:
            reset()
            player1_score -= end//1000
            start = pygame.time.get_ticks()
            end = pygame.time.get_ticks()
            player1 = -1
        if x >= 1160 and x <= 1240:
            reset()
            player1_score -= end//1000
            start = pygame.time.get_ticks()
            end = pygame.time.get_ticks()
            player1 = -1
        if x >= 1460 and x <= 1540:
            reset()
            player1_score -= end//1000
            start = pygame.time.get_ticks()
            end = pygame.time.get_ticks()
            player1 = -1

    if y_2 >= 140 and y_2 <= 195:
        if x_2 >= 110 and x_2 <= 195:
            reset()
            player2_score -= end//1000
            start = pygame.time.get_ticks()
            end = pygame.time.get_ticks()
            player2 = -1
        if x_2 >= 410 and x_2 <= 495:
            reset()
            player2_score -= end//1000
            start = pygame.time.get_ticks()
            end = pygame.time.get_ticks()
            player2 = -1
        if x_2 >= 710 and x_2 <= 795:
            reset()
            player2_score -= end//1000
            start = pygame.time.get_ticks()
            end = pygame.time.get_ticks()
            player2 = -1
        if x_2 >= 1010 and x_2 <= 1095:
            reset()
            player2_score -= end//1000
            start = pygame.time.get_ticks()
            end = pygame.time.get_ticks()
            player2 = -1
        if x_2 >= 1310 and x_2 <= 1395:
            reset()
            player2_score -= end//1000
            start = pygame.time.get_ticks()
            end = pygame.time.get_ticks()
            player2 = -1

    if y_2 >= 480 and y_2 <= 585:
        if x_2 >= 110 and x_2 <= 195:
            reset()
            player2_score -= end//1000
            start = pygame.time.get_ticks()
            end = pygame.time.get_ticks()
            player2 = -1
        if x_2 >= 410 and x_2 <= 495:
            reset()
            player2_score -= end//1000
            start = pygame.time.get_ticks()
            end = pygame.time.get_ticks()
            player2 = -1
        if x_2 >= 710 and x_2 <= 795:
            reset()
            player2_score -= end//1000
            start = pygame.time.get_ticks()
            end = pygame.time.get_ticks()
            player2 = -1
        if x_2 >= 1010 and x_2 <= 1095:
            reset()
            player2_score -= end//1000
            start = pygame.time.get_ticks()
            end = pygame.time.get_ticks()
            player2 = -1
        if x_2 >= 1310 and x_2 <= 1395:
            reset()
            player2_score -= end//1000
            start = pygame.time.get_ticks()
            end = pygame.time.get_ticks()
            player2 = -1

    if y_2 >= 295 and y_2 <= 385:
        if x_2 >= 26 and x_2 <= 340:
            reset()
            player2_score -= end//1000
            start = pygame.time.get_ticks()
            end = pygame.time.get_ticks()
            player2 = -1
        if x_2 >= 560 and x_2 <= 640:
            reset()
            player2_score -= end//1000
            start = pygame.time.get_ticks()
            end = pygame.time.get_ticks()
            player2 = -1
        if x_2 >= 860 and x_2 <= 940:
            reset()
            player2_score -= end//1000
            start = pygame.time.get_ticks()
            end = pygame.time.get_ticks()
            player2 = -1
        if x_2 >= 1160 and x_2 <= 1240:
            reset()
            player2_score -= end//1000
            start = pygame.time.get_ticks()
            end = pygame.time.get_ticks()
            player2 = -1
        if x_2 >= 1460 and x_2 <= 1540:
            reset()
            player2_score -= end//1000
            start = pygame.time.get_ticks()
            end = pygame.time.get_ticks()
            player2 = -1

    if y_2 >= 685 and y_2 <= 780:
        if x_2 >= 26 and x_2 <= 340:
            reset()
            player2_score -= end//1000
            start = pygame.time.get_ticks()
            end = pygame.time.get_ticks()
            player2 = -1
        if x_2 >= 560 and x_2 <= 640:
            reset()
            player2_score -= end//1000
            start = pygame.time.get_ticks()
            end = pygame.time.get_ticks()
            player2 = -1
        if x_2 >= 860 and x_2 <= 940:
            reset()
            player2_score -= end//1000
            start = pygame.time.get_ticks()
            end = pygame.time.get_ticks()
            player2 = -1
        if x_2 >= 1160 and x_2 <= 1240:
            reset()
            player2_score -= end//1000
            start = pygame.time.get_ticks()
            end = pygame.time.get_ticks()
            player2 = -1
        if x_2 >= 1460 and x_2 <= 1540:
            reset()
            player2_score -= end//1000
            start = pygame.time.get_ticks()
            end = pygame.time.get_ticks()
            player2 = -1

    if player1 == -1:
        left = False
        right = False
        x = 860
        y = 920

        if player2 != -1:
            player1_playing = False
            player2_playing = True

        else:
            player1_playing = False
            player2_playing = False

    if player2 == -1:
        left_2 = False
        right_2 = False
        x_2 = 860
        y_2 = 10

        if player1 != -1:
            player1_playing = True
            player2_playing = False

        else:
            player1_playing = False
            player2_playing = False

# Check Score of player and update timer


def checkScore():
    global x, y, strip1, strip2, strip3, strip4, strip5, x_2, y_2
    global player1_score, player2_score
    global strip1_reached, strip2_reached, strip3_reached
    global strip4_reached, strip5_reached
    global player1_playing, player2_playing
    global vel_player1, vel_player2, start, end, winner

    if player1_playing:

        if y >= 739 and y <= 809:
            strip1 = 1

        if y >= 543 and y <= 613:
            strip2 = 1

        if y >= 347 and y <= 417:
            strip3 = 1

        if y >= 151 and y <= 221:
            strip4 = 1

        if y >= 0 and y <= 70:
            strip5 = 1

        if strip1 and not(strip1_reached):
            player1_score += 15
            strip1_reached = 1

        if strip2 and not(strip2_reached):
            player1_score += 15
            strip2_reached = 1

        if strip3 and not(strip3_reached):
            player1_score += 15
            strip3_reached = 1

        if strip4 and not(strip4_reached):
            player1_score += 15
            strip4_reached = 1

        if strip5 and not(strip5_reached):
            player1_score += 15
            strip5_reached = 1

        if strip5_reached == 1:
            reset()
            vel_player1 += 5
            player1_playing = False
            player2_playing = True
            y = 920
            start = pygame.time.get_ticks()
            end = pygame.time.get_ticks()
            player1_score -= end//1000

    if player2_playing:

        if y_2 >= 739 and y_2 <= 809:
            strip1 = 1

        if y_2 >= 543 and y_2 <= 613:
            strip2 = 1

        if y_2 >= 347 and y_2 <= 417:
            strip3 = 1

        if y_2 >= 151 and y_2 <= 221:
            strip4 = 1

        if y_2 >= 920 and y_2 <= 980:
            strip5 = 1

        if strip1 and not(strip1_reached):
            player2_score += 15
            strip1_reached = 1

        if strip2 and not(strip2_reached):
            player2_score += 15
            strip2_reached = 1

        if strip3 and not(strip3_reached):
            player2_score += 15
            strip3_reached = 1

        if strip4 and not(strip4_reached):
            player2_score += 15
            strip4_reached = 1

        if strip5 and not(strip5_reached):
            player2_score += 15
            strip5_reached = 1

        if strip5_reached == 1:
            reset()
            vel_player2 += 5
            player1_playing = True
            player2_playing = False
            y_2 = 10
            start = pygame.time.get_ticks()
            end = pygame.time.get_ticks()
            player2_score -= end//1000


while run:

    clock.tick(fps)

    end = pygame.time.get_ticks()-start
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()

    # Player Movements
    if keys[pygame.K_LEFT] and x > vel and player1_playing:
        x -= vel
        left = True
        right = False
    if keys[pygame.K_RIGHT] and x < screenwidth-width and player1_playing:
        x += vel
        right = True
        left = False
    if keys[pygame.K_UP] and y > vel and player1_playing:
        y -= vel
        left = False
        right = False
    if keys[pygame.K_DOWN] and y < screenheight-height and player1_playing:
        y += vel
        right = False
        left = False

    if keys[pygame.K_a] and x_2 > vel and player2_playing:
        x_2 -= vel
        left_2 = True
        right_2 = False
    if keys[pygame.K_d] and x_2 < screenwidth-width and player2_playing:
        x_2 += vel
        right_2 = True
        left_2 = False
    if keys[pygame.K_w] and y_2 > vel and player2_playing:
        y_2 -= vel
        left_2 = False
        right_2 = False
    if keys[pygame.K_s] and y_2 < screenheight-height and player2_playing:
        y_2 += vel
        right_2 = False
        left_2 = False

    checkScore()
    checkCollision()
    checkGameEnd()
    redrawGameWindow()


pygame.quit()
