# -*- coding: utf-8 -*-
import pygame
from random import randrange

pygame.init()
FPS = 8 # скорость змейки
H = 800
W = 500

white = (255, 255, 255)


dis = pygame.display.set_mode((H, W))
pygame.display.set_caption("Snake")
pygame.mixer.music.load('bit.mp3')
pygame.mixer.music.play(-1)

clock = pygame.time.Clock()

game_over = False

x1 = H / 2
y1 = W / 2

snake_block = 10

x1_change = 0
y1_change = 0

snake_List = []
Length_of_snake = 1

foodx = round(randrange(0, H - snake_block) / snake_block) * snake_block # для яблока
foody = round(randrange(0, W - snake_block) / snake_block) * snake_block

score_font = pygame.font.SysFont("comicsansms", 25)

fon = pygame.image.load("snake_fon.jpg").convert()
fon = pygame.transform.scale(fon, (800, 500))

def Your_score(score):
    value = score_font.render("Твои очки: " + str(score), True, pygame.Color('yellow'))
    dis.blit(value, [0, 0])

def our_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(dis, pygame.Color('midnightblue'), [x[0], x[1], snake_block, snake_block]) # змейка

while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                x1_change = - snake_block
                y1_change = 0
            elif event.key == pygame.K_d:
                x1_change = snake_block
                y1_change = 0
            elif event.key == pygame.K_w:
                x1_change = 0
                y1_change = - snake_block
            elif event.key == pygame.K_s:
                x1_change = 0
                y1_change = snake_block

    if x1 >= H or x1 < 0 or y1 >= W or y1 < 0:
        game_over = True
    x1 += x1_change
    y1 += y1_change
    dis.blit(fon, (0, 0))
    # dis.fill( )

    pygame.draw.rect(dis, pygame.Color('red'), [foodx, foody, snake_block, snake_block]) # яблоко
    snake_Head = []
    snake_Head.append(x1)
    snake_Head.append(y1)
    snake_List.append(snake_Head)
    if len(snake_List) > Length_of_snake:
        del snake_List[0]

    for x in snake_List[:-1]:
        if x == snake_Head:
            game_over = True

    our_snake(snake_block, snake_List)
    Your_score(Length_of_snake - 1)

    pygame.display.update()

    if x1 == foodx and y1 == foody:
        foodx = round(randrange(0, H - snake_block) / snake_block) * snake_block
        foody = round(randrange(0, W - snake_block) / snake_block) * snake_block
        Length_of_snake += 1

    clock.tick(FPS)

pygame = quit()
quit()
