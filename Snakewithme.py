import pygame
import random
import os

pygame.init()


# Colors
White = (255, 255, 255)
Black = (0, 0, 0)
Red = (255, 0, 0)
Green = (0, 128, 0)

# Coordinates & Size
screen_width = 900
screen_height = 600

# Display
Surface = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Hungry Snake")
image = pygame.image.load("Snake.jpg")
image = pygame.transform.scale(image, (screen_width, screen_height))
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 55)


def surface_text(text, color, x, y):
    makeing_text = font.render(text, True, color)
    new_text = Surface.blit(makeing_text, [x, y])


def plot_snake(Surface, color, snake_list, snake_size):
    for snake_x, snake_y in snake_list:
        pygame.draw.rect(Surface, Green, [snake_x, snake_y, snake_size, snake_size])

def Welcome():
   exit_game = False
   while not exit_game:
       Surface.fill(White)
       surface_text("Welcome To Hungry Snakes", Black, 200, 200)
       surface_text("Press Space Bar To Play!", Black, 232, 270)
       for event in pygame.event.get():
           if event.type == pygame.QUIT:
               exit_game = True
           if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    game_loop()                 
       pygame.display.update()
       clock.tick(60)



# Loop
def game_loop():
    # Specific Variables
    snake_x = 54
    snake_y = 30
    snake_size = 30
    exit_game = False
    game_over = False
    FPS = 60
    velocity_x = 0
    velocity_y = 0
    score = 0
    snake_list = []
    snake_length = 0
    food_x = random.randint(20, screen_width) / 2
    food_y = random.randint(20, screen_height) / 2
    main_velocity = 5
    if(not os.path.exists("hiscore.txt")):
        with open("hiscore.txt", "w") as f:
            f.write("0")
    with open('hiscore.txt', "r") as f:
        highscore = f.read()
        

    while not exit_game:
        if game_over:
            with open("hiscore.txt", "w") as f:
                 f.write(str(highscore))
            Surface.fill(White)
            surface_text("Game Over!", Red, 350, 245)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        Welcome()
        else:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        velocity_x = main_velocity
                        velocity_y = 0
                    if event.key == pygame.K_LEFT:
                        velocity_x = -(main_velocity)
                        velocity_y = 0
                    if event.key == pygame.K_UP:
                        velocity_x = 0
                        velocity_y = -(main_velocity)
                    if event.key == pygame.K_DOWN:
                        velocity_x = 0
                        velocity_y = main_velocity
                    if event.key == pygame.K_q:
                        main_velocity += 0.65
                    if event.key == pygame.K_p:
                        score += 10

            snake_x += velocity_x
            snake_y += velocity_y  
            if abs(snake_x - food_x) <= 10 and abs(snake_y - food_y) <= 10:
                score += 10
                if score > int(highscore):
                    highscore = score
                food_x = random.randint(20, screen_width)/2
                food_y = random.randint(20, screen_height)/2
                snake_length += 4

            Surface.fill(White)  # Fill the surface with white
            Surface.blit(image, (0, 0))
            surface_text("Score " + str(score) + "   Highscore " + str(highscore), Red, 10, 10)

            pygame.draw.rect(Surface, Green, [snake_x, snake_y, snake_size, snake_size])
            pygame.draw.rect(Surface, Red, [food_x, food_y, snake_size, snake_size])

            head = []
            head.append(snake_x)
            head.append(snake_y)
            snake_list.append(head)
            if head in snake_list[:-1]:
                game_over=True
            if snake_x>screen_width or snake_y>screen_height or snake_x<0 or snake_y<0:
                game_over = True

            plot_snake(Surface, Black, snake_list, snake_size)
            if len(snake_list) > snake_length:
                del snake_list[0]

        pygame.display.update()
        clock.tick(FPS)

    pygame.quit()
    quit()


Welcome()
