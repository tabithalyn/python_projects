import pygame
import time
import random

pygame.init()

white = (255, 255, 255)
black = (0, 0, 0)
green = (173, 204, 96)
dark_green = (43, 51, 24)

width, height = 600, 600

game_display = pygame.display.set_mode((width, height))
pygame.display.set_caption("Retro Snake")

clock = pygame.time.Clock()

snake_size = 10
snake_speed = 15

message_font = pygame.font.SysFont("ubuntu", 20)
score_font = pygame.font.SysFont("ubuntu", 15)

def print_score(score):
    text = score_font.render("Score: " + str(score), True, dark_green)
    game_display.blit(text, [0,0])

def draw_snake(snake_size, snake_px):
    for pixel in snake_px:
        pygame.draw.rect(game_display, white, [pixel[0], pixel[1], snake_size, snake_size])

def run_game():
    game_over = False
    game_close = False

    x = width / 2
    y = height / 2
    x_speed = 0
    y_speed = 0

    snake_px = []
    snake_length = 1

    food_x = round(random.randrange(0, width - snake_size) / 10.0) * 10
    food_y = round(random.randrange(0, height - snake_size) / 10.0) * 10

    while not game_over:
        while game_close:
            game_display.fill(dark_green)
            game_over_message = message_font.render("Game Over!", True, white)
            play_again_message = message_font.render("Press ENTER to play again or ESC to quit", True, white)
            game_display.blit(game_over_message, [width / 2, height / 2])
            game_display.blit(play_again_message, [width / 3, height / 3])
            print_score(snake_length - 1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_RETURN:
                        run_game()
                if event.type == pygame.QUIT:
                    game_over: True
                    game_close: False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_speed = -snake_size
                    y_speed = 0
                if event.key == pygame.K_RIGHT:
                    x_speed = snake_size
                    y_speed = 0
                if event.key == pygame.K_DOWN:
                    x_speed = 0
                    y_speed = snake_size
                if event.key == pygame.K_UP:
                    x_speed = 0
                    y_speed = -snake_size
        if x >= width or x < 0 or y >= height or y < 0:
            game_close = True
        
        x += x_speed
        y += y_speed

        game_display.fill(green)
        pygame.draw.rect(game_display, dark_green, [food_x, food_y, snake_size, snake_size])

        snake_px.append([x,y])
        if len(snake_px) > snake_length:
            del snake_px[0]
        for px in snake_px[:-1]:
            if px == [x,y]:
                game_close = True

        draw_snake(snake_size, snake_px)
        print_score(snake_length - 1)

        pygame.display.update()

        if x == food_x and y == food_y:
            food_x = round(random.randrange(0, width - snake_size) / 10.0) * 10
            food_y = round(random.randrange(0, height - snake_size) / 10.0) * 10
            snake_length += 1
        
        clock.tick(snake_speed)

    pygame.quit()
    quit()

run_game()