import pygame, sys, random
from pygame.math import Vector2
from food import Food
from snake import Snake
from colors import Colors

pygame.init()

title_font = pygame.font.Font(None, 50)
score_font = pygame.font.Font(None, 30)

cell_size = 25
number_of_cells = 20

# food is appearing outside boundaries ?
# redo ?
# https://www.youtube.com/watch?v=PHdZdrMCKuY


OFFSET = 70

class Game:
    def __init__(self):
        self.snake = Snake()
        self.food = Food(self.snake.body)
        self.state = "RUNNING"
        self.score = 0
    def draw(self):
        self.food.draw()
        self.snake.draw()
    def update(self):
        if self.state == "RUNNING":
          self.snake.update()
          self.check_collision_with_food()
          self.check_collision_with_edges()
          self.check_collision_with_tail()
    def check_collision_with_food(self):
        if self.snake.body[0] == self.food.position:
            self.food.position = self.food.generate_random_pos(self.snake.body)
            self.snake.add_segment = True
            self.score += 1
    def check_collision_with_edges(self):
        if self.snake.body[0].x == number_of_cells or self.snake.body[0].x == -1:
            self.game_over()
        if self.snake.body[0].y == number_of_cells or self.snake.body[0].y == -1:
            self.game_over()
    def check_collision_with_tail(self):
        headless_body = self.snake.body[1:]
        if self.snake.body[0] in headless_body:
            self.game_over()
    def game_over(self):
        self.snake.reset()
        self.food.position = self.food.generate_random_pos(self.snake.body)
        self.state = "STOPPED"
        self.score = 0

screen = pygame.display.set_mode((2*OFFSET + cell_size*number_of_cells, 2*OFFSET + cell_size*number_of_cells))
pygame.display.set_caption("Retro Snake")

clock = pygame.time.Clock()

game = Game()

SNAKE_UPDATE = pygame.USEREVENT
pygame.time.set_timer(SNAKE_UPDATE, 200)

while True:
    for event in pygame.event.get():
        if event.type == SNAKE_UPDATE:
            game.update()
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if game.state == "STOPPED":
                game.state = "RUNNING"
            if event.key == pygame.K_UP and game.snake.direction != Vector2(0, 1):
                game.snake.direction = Vector2(0, -1)
            if event.key == pygame.K_DOWN and game.snake.direction != Vector2(0, -1):
                game.snake.direction = Vector2(0, 1)
            if event.key == pygame.K_LEFT and game.snake.direction != Vector2(1, 0):
                game.snake.direction = Vector2(-1, 0)
            if event.key == pygame.K_RIGHT and game.snake.direction != Vector2(-1, 0):
                game.snake.direction = Vector2(1, 0)

    screen.fill(Colors.GREEN)
    pygame.draw.rect(screen, Colors.DARK_GREEN, (OFFSET-5, OFFSET-5, cell_size*number_of_cells+10, cell_size*number_of_cells+10), 5)
    game.draw()
    title_surface = title_font.render("Retro Snake", True, Colors.DARK_GREEN)
    score_surface = score_font.render(str(game.score), True, Colors.DARK_GREEN)
    screen.blit(title_surface, (OFFSET-5, 20))
    screen.blit(score_surface, (OFFSET-5, OFFSET + cell_size * number_of_cells + 10))

    pygame.display.update()
    clock.tick(60)