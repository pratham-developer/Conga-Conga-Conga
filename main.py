import sys
import pygame
import time
import random
import os

player_speed = 15
screen_width = 800
screen_height = 500

pygame.init()
player_img = pygame.image.load(os.path.join('assets','player.png'))
player_img=pygame.transform.scale(player_img,(10,10))
friend_img = pygame.image.load(os.path.join('assets','friend.png'))
friend_img=pygame.transform.scale(friend_img,(10,10))

pygame.display.set_caption('Conga, Conga, Conga!')
game_window = pygame.display.set_mode((screen_width, screen_height))

fps = pygame.time.Clock()

player_position = [100, 50]
player_body = [[100, 50],]

friend_position = [random.randrange(1, (screen_width // 10)) * 10,
                  random.randrange(1, (screen_height // 10)) * 10]
friend_spawn = True
direction = 'RIGHT'
change_to = direction
followers = 0

def show_followers(choice, color, font, size):
    followers_font = pygame.font.SysFont(font, size)
    followers_surface = followers_font.render('FOLLOWERS : ' + str(followers), True, color)
    followers_rect = followers_surface.get_rect()
    game_window.blit(followers_surface, followers_rect)

def game_over():
    my_font = pygame.font.SysFont('comic sans', 50)
    game_over_surface = my_font.render('Your score is  ' + str(followers), True, (0,255,0))
    game_over_rect = game_over_surface.get_rect()
    game_over_rect.midtop = (screen_width / 2, screen_height / 4)
    game_window.blit(game_over_surface, game_over_rect)
    pygame.display.flip()
    time.sleep(2)
    pygame.quit()
    sys.exit()

while True:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                change_to = 'UP'
            if event.key == pygame.K_DOWN:
                change_to = 'DOWN'
            if event.key == pygame.K_LEFT:
                change_to = 'LEFT'
            if event.key == pygame.K_RIGHT:
                change_to = 'RIGHT'
        elif event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    if change_to == 'UP' and direction != 'DOWN':
        direction = 'UP'
    if change_to == 'DOWN' and direction != 'UP':
        direction = 'DOWN'
    if change_to == 'LEFT' and direction != 'RIGHT':
        direction = 'LEFT'
    if change_to == 'RIGHT' and direction != 'LEFT':
        direction = 'RIGHT'

    if direction == 'UP':
        player_position[1] -= 10
    if direction == 'DOWN':
        player_position[1] += 10
    if direction == 'LEFT':
        player_position[0] -= 10
    if direction == 'RIGHT':
        player_position[0] += 10

    player_body.insert(0, list(player_position))
    if player_position[0] == friend_position[0] and player_position[1] == friend_position[1]:
        followers += 1
        friend_spawn = False
    else:
        player_body.pop()
    if not friend_spawn:
        friend_position = [random.randrange(1, (screen_width // 10)) * 10,
                          random.randrange(1, (screen_height // 10)) * 10]

    friend_spawn = True
    game_window.fill((50,15,0))

    for x in range(0, screen_width, 10):
        pygame.draw.line(game_window, (0, 0, 0), (x, 0), (x, screen_height))
    for y in range(0, screen_height, 10):
        pygame.draw.line(game_window, (0, 0, 0), (0, y), (screen_width, y))

    for pos in player_body:
        if pos ==player_body[0]:
         game_window.blit(player_img, (pos[0], pos[1]))
        else:
            game_window.blit(friend_img, (pos[0], pos[1]))

    game_window.blit(friend_img, (friend_position[0], friend_position[1]))

    if player_position[0] < 0 or player_position[0] > screen_width - 10:
        game_over()
    if player_position[1] < 0 or player_position[1] > screen_height - 10:
        game_over()

    for block in player_body[1:]:
        if player_position[0] == block[0] and player_position[1] == block[1]:
            game_over()

    show_followers(1, (255,255,255), 'comic sans', 20)
    pygame.display.update()
    fps.tick(player_speed)
