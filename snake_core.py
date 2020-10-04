# -*- coding: utf-8 -*-
"""
Created on Sun Oct  4 11:07:42 2020

@author: Nellman

Snake with Pygame
Inspired by: https://www.edureka.co/blog/snake-game-with-pygame/

Your task, should you choose to accept it, is to write an Algorithm/AI
to play Snake. Your solution will be evaluated by your score divided by
the number of steps. The score calulated every time you pick up food using
the following formula: score += 10 + score//100.
The final points are the sum from 10 runs rounded to 4 decimals.

To slow down the Simulation, see near the bottom.
Only code inside your function.
Please don't search online for a perfect solutions, this spoils the fun for you
and others!.
"""

__author__ = " Nellman"

import pygame as pg
import random
from time import sleep
from lib.nellmans_solution import ki


# Colours
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
black = (0, 0, 0)
white = (255, 255, 255)


# size and position initialisation
game_size_x = 1080 // 10 * 10  # in pixels, ony divisible by 10 (see snake size), ONLY CHANGE FIRST VALUE!
game_size_y = 720 // 10 * 10
x_snake = game_size_x // 2 // 10 * 10
y_snake = game_size_y // 2 // 10 * 10
x_food = random.randint(10, ((game_size_x-10)//10*10))//10*10
y_food = random.randint(10, ((game_size_y-10)//10*10))//10*10
score = 0
steps = 0
snake_len = 1
snake_body_x = [x_snake]
snake_body_y = [y_snake]


# initialising pygame
pg.init()
dis = pg.display.set_mode((game_size_x, game_size_y))  # set display for snake (Tuple)
pg.display.update()
pg.display.set_caption("Snake")
dead = False
clock = pg.time.Clock()
font_style = pg.font.SysFont(None, 50)


# displays a text
def show_text(text, colour):
    """Show text on screen."""
    message = font_style.render(text, True, colour)
    dis.blit(message, [game_size_x/2, game_size_y/2])


# gameloop
while (dead == False):
    change = False

    for event in pg.event.get():
        # print(event)
        if event.type == pg.QUIT:
            dead = True

        # button presses
        if event.type == pg.KEYDOWN:  # key identifier https://www.pygame.org/docs/ref/key.html
            change = True
            if event.key == pg.K_a:
                x_snake -= 10
            elif event.key == pg.K_d:
                x_snake += 10
            elif event.key == pg.K_w:
                y_snake -= 10
            elif event.key == pg.K_s:
                y_snake += 10
            else:
                pass

########################## deactivate this following section, if you want to play around manually
    snakebody_x = []
    snakebody_y = []
    for i in range(0, len(snake_body_x)):
        snakebody_x.append(snake_body_x[i]//10)
        snakebody_y.append(snake_body_y[i]//10)

    x_change, y_change = 0, 0
    x_change, y_change = ki(game_size_x//10, game_size_y//10, snakebody_x, snakebody_y, x_snake//10, y_snake//10, x_food//10, y_food//10)
    if ((int(x_change) + int(y_change)) == 1 or (int(x_change) + int(y_change)) == -1):
        change = True
        x_snake += x_change * 10
        y_snake += y_change * 10
    elif (int(x_change) + int(y_change)) != 1 or (int(x_change) + int(y_change)) != -1:
        print("Wrong return from the AI")
    else:
        print("häh?")
##########################

    if change:
        snake_body_x.append(x_snake)
        snake_body_y.append(y_snake)
        steps += 1
        if x_snake == x_food and y_snake == y_food:
            snake_len += 1
            score += 10 + score//100
            while(True):
                x_food = random.randint(10, ((game_size_x-10)//10*10))//10*10
                y_food = random.randint(10, ((game_size_y-10)//10*10))//10*10
                if x_food != x_snake and y_food != y_snake:
                    break

    if len(snake_body_x) > snake_len:
        del snake_body_x[0]
        del snake_body_y[0]

    # die when touching walls or self
    if (x_snake >= game_size_x or x_snake < 0
        or y_snake >= game_size_y or y_snake < 0):
        dead = True
    if len(snake_body_x) > 1:
        for i in range(0, (len(snake_body_x)-1)):
            if x_snake == snake_body_x[i] and y_snake == snake_body_y[i]:
                dead = True

# print all objects on screen
    dis.fill(green)
    if snake_len > 1:
        for i in range(0, len(snake_body_x)):
            pg.draw.rect(dis, black, [snake_body_x[i], snake_body_y[i], 10, 10])
    pg.draw.rect(dis, red, [x_snake, y_snake, 10, 10])
    pg.draw.rect(dis, blue, [x_food, y_food, 10, 10])

    pg.display.update()
    # sleep(0.5)  # disable to speed up AI
    clock.tick(30)

final_score = score/steps  # this is the final metric for evaluation
print("You lost")
print("Your Score is: " + str(score))
print("It took you ", steps, " steps to achieve this score!")
print("Your overall score is: ", final_score)
input("Press Enter to continue")

pg.quit()
