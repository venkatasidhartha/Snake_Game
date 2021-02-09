import pygame as game
import random

"""Display"""
game.init()
display_width = 800
display_height = 600
display = game.display.set_mode((display_width,display_height))
game.display.set_caption("Snake Game")


"""Colors"""
blue = (0,0,255)
red = (255,0,0)
yellow = (255,255,0)
black = (0,0,0)
green = (0, 255, 0)


"""Snake properties"""
snake_size = 10
snake_speed = 10
snake_list = []
clock = game.time.Clock()
score_font = game.font.SysFont("comicsansms", 35)

"""Score"""
def message(text,score,x,y):
    value = score_font.render(str(text) + str(score), True, blue)
    display.blit(value, [x, y])



"""snake Array"""
def snake(snake_list,snake_size,Length_of_snake):
    for x in snake_list:
        game.draw.rect(display, red, [x[0], x[1], snake_size, snake_size])
    if len(snake_list) > Length_of_snake:
        del snake_list[0]


def Gameloop():
    """Game"""
    game_over = True
    game_close = False
    snake_x1 = display_width // 2
    snake_y1 = display_height // 2

    snake_x2_change = 0
    snake_y2_change = 0
    """Food"""
    food_x = round(random.randrange(0, display_width - 50) / 10.0) * 10.0
    food_y = round(random.randrange(0, display_height - 100) / 10.0) * 10.0
    Length_of_snake = 1
    while game_over:

        while game_close == True:
            message("You Lost! Press C-Play Again or Q-Quit : ",Length_of_snake-1,display_width//5,display_height//2)
            game.display.update()

            for event in game.event.get():
                if event.type == game.KEYDOWN:
                    if event.key == game.K_q:
                        game_over = False
                        game_close = False
                    if event.key == game.K_c:
                        Gameloop()


        for event in game.event.get():
            if event.type == game.QUIT:
                game_over = False
                """Keys"""
            if event.type == game.KEYDOWN:
                if event.key == game.K_LEFT:
                    snake_x2_change = -10
                    snake_y2_change = 0
                if event.key == game.K_RIGHT:
                    snake_x2_change = 10
                    snake_y2_change = 0
                if event.key == game.K_UP:
                    snake_x2_change = 0
                    snake_y2_change = -10
                if event.key == game.K_DOWN:
                    snake_x2_change = 0
                    snake_y2_change = +10
        if snake_x1 < 0 or snake_x1 >= display_width or snake_y1 < 0 or snake_y1 >= display_height:
            game_close = True

        snake_x1 += snake_x2_change
        snake_y1 += snake_y2_change
        display.fill(black)

        snake_Head = []
        snake_Head.append(snake_x1)
        snake_Head.append(snake_y1)
        snake_list.append(snake_Head)
        """snake function"""
        snake(snake_list,snake_size,Length_of_snake)
        message("Your Score : ",Length_of_snake-1,0,0)
        game.draw.rect(display,yellow,[food_x,food_y,snake_size,snake_size])
        game.display.update()
        if snake_x1 == food_x and snake_y1 == food_y:
            food_x = round(random.randrange(0, display_width - 50) / 10.0) * 10.0
            food_y = round(random.randrange(0, display_height - 100) / 10.0) * 10.0
            Length_of_snake += 1

        clock.tick(snake_speed)
    game.quit()
    quit()
Gameloop()



