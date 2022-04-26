# 움직이는 공룡
import pygame
import os
current_path = os.path.dirname(__file__)  # 현재 파일의 위치 반환
image_path = os.path.join(current_path, "images")  # images 폴더 위치 반환

pygame.init()
screen_width = 600
screen_height = 300
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('chrome game')

background = pygame.image.load(
    os.path.join(image_path, "white.png"))
character = pygame.image.load(
    os.path.join(image_path, "dino1.png"))
character_size = character.get_rect().size
character_width = character_size[0]
character_height = character_size[1]
character_x_pos = (screen_width/2-character_width/2)
character_y_pos = (screen_height/2)

to_x = 0
to_y = 0

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                to_x -= 2

            elif event.key == pygame.K_RIGHT:
                to_x += 2
            elif event.key == pygame.K_UP:
                to_y -= 2
            elif event.key == pygame.K_DOWN:
                to_y += 2

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                to_y = 0

    character_x_pos += to_x
    character_y_pos += to_y

    if character_x_pos < 0:
        character_x_pos = 0
    elif character_x_pos > screen_width-character_width:
        character_x_pos = screen_width-character_width

    if character_y_pos < 0:
        character_y_pos = 0
    elif character_y_pos > screen_height-character_height:
        character_y_pos = screen_height-character_height

    screen.blit(background, (0, 0))
    screen.blit(character, (character_x_pos, character_y_pos))
    pygame.display.update()

pygame.quit()
