import pygame
import random


class body: 
    def __init__(self, window):
        self.x = 0
        self.y = 0
        self.window = window
        self.dir = 0  

    def draw(self):
        pygame.draw.rect(self.window, (40, 114, 51), (self.x, self.y, 10, 10))

    def movement(self):
        if self.dir == 0:
            self.x += 10
        elif self.dir == 1:
            self.x -= 10
        elif self.dir == 2:
            self.y += 10
        elif self.dir == 3:
            self.y -= 10


class food:
    def __init__(self, window):
        self.x = random.randrange(60) * 10
        self.y = random.randrange(60) * 10
        self.window = window
    

    def draw(self):
        pygame.draw.rect(self.window, (255, 0, 0), (self.x, self.y, 10, 10))

    def relocate(self):
        self.x = random.randrange(40) * 10
        self.y = random.randrange(40) * 10


def redraw(window):
    window.fill((0, 0, 0))
    food.draw()
    for i in range(len(snake)):
        snake[i].draw()


def snake_ubication():
    if(len(snake)) > 1:
        for i in range(len(snake)-1):
            snake[len(snake)-i-1].x = snake[len(snake)-i-2].x
            snake[len(snake) - i - 1].y = snake[len(snake) - i - 2].y


def Colision():
    hit = False
    if (len(snake)) > 1:
        for i in range(len(snake) - 1):
            if snake[0].x == snake[i + 1].x and snake[0].y == snake[i + 1].y:
                hit = True
    return hit


def main():
    global food, snake
    window = pygame.display.set_mode((500, 500))
    window.fill((0, 0, 0))
    pygame.display.set_caption("Snake")
    snake = [body(window)]
    snake[0].draw()
    food = food(window)
    redraw(window)
    run = True
    speed = 100
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    snake[0].dir = 2
                if event.key == pygame.K_LEFT:
                    snake[0].dir = 1
                if event.key == pygame.K_RIGHT:
                    snake[0].dir = 0
                if event.key == pygame.K_UP:
                    snake[0].dir = 3
        snake_ubication()
        snake[0].movement()
        redraw(window)
        pygame.display.update()
        pygame.time.delay(speed)

        if snake[0].x >= 500:
            snake[0].x = 0
        elif snake[0].x < 0:
            snake[0].x = 490

        if snake[0].y >= 500:
            snake[0].y = 0
        elif snake[0].y < 0:
            snake[0].y = 490

        if Colision():
            snake = [body(window)]
            food.relocate()
            speed = 100

        if snake[0].x == food.x and snake[0].y == food.y:
            if speed > 35:
                speed -= 5
            food.relocate()
            snake.append(body(window))
            snake_ubication()


main()
pygame.quit()