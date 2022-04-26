# 블럭에 닿으면 소리남
import os
import pygame
import sys
from pygame import *
from datetime import datetime


current_path = os.path.dirname(__file__)  # 현재 파일의 위치 반환
image_path = os.path.join(current_path, "images")  # images 폴더 위치 반환
music_path = os.path.join(current_path, "music")  # music 폴더 위치 반환

# 배경 이미지 불러오기
background = pygame.image.load(
    os.path.join(image_path, "white.png"))

# 캐릭터(스프라이트) 불러오기
character = pygame.image.load(
    os.path.join(image_path, "dino1.png"))

# 소리초기화
se_crash = None
se_ding = None


def main():
    # 소리데이터
    global se_crash
    # 초기화
    pygame.init()
    # 화면 타이틀 설정
    pygame.display.set_caption("code dino world")  # 게임 이름
    # Font 정의
    game_font = pygame.font.Font(None, 35)
    game_result = "play song"
    # 날짜 출력
    now = datetime.now()
    game_now = "today date : "+str(now.year)+"."+str(now.month)+"."+str(now.day) + \
        "."

    # 화면 크기 설정
    screen_width = 800  # 가로 크기
    screen_height = 600  # 세로 크기
    screen = pygame.display.set_mode((screen_width, screen_height))
    # FPS
    clock = pygame.time.Clock()
    # 소리
    se_crash = pygame.mixer.Sound(
        os.path.join(music_path, "afternoon.mp3"))
    se_ding = pygame.mixer.Sound(
        os.path.join(music_path, "coin.mp3"))

    character_size = character.get_rect().size  # 이미지의 크기를 구해옴
    character_width = character_size[0]  # 캐릭터의 가로 크기
    character_height = character_size[1]  # 캐릭터의 세로 크기
    character_x_pos = (screen_width / 2) - (character_width /
                                            2)  # 화면 가로의 절반 크기에 해당하는 곳에 위치 (가로)
    # 화면 세로 크기 가장 아래에 해당하는 곳에 위치 (세로)
    character_y_pos = screen_height - character_height

    # 이동할 좌표
    to_x = 0
    to_y = 0

    # 이동 속도
    character_speed = 0.3

    # radio 캐릭터
    radio = pygame.image.load(
        os.path.join(image_path, "10.png"))
    radio_size = radio.get_rect().size  # 이미지의 크기를 구해옴
    radio_width = radio_size[0]  # 캐릭터의 가로 크기x
    radio_height = radio_size[1]  # 캐릭터의 세로 크기
    # 화면 가로의 절반 크기에 해당하는 곳에 위치 (가로)
    radio_x_pos = 100
    # 화면 세로 크기 가장 아래에 해당하는 곳에 위치 (세로)
    radio_y_pos = 500

    # 이벤트 루프
    # 게임이 진행중인가?
    while True:
        dt = clock.tick(60)  # 게임화면의 초당 프레임 수를 설정

        for event in pygame.event.get():  # 어떤 이벤트가 발생하였는가?
            if event.type == pygame.QUIT:  # 창이 닫히는 이벤트가 발생하였는가?
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:  # 키가 눌러졌는지 확인
                if event.key == pygame.K_LEFT:  # 캐릭터를 왼쪽으로
                    to_x -= character_speed  # to_x = to_x - 5
                elif event.key == pygame.K_RIGHT:  # 캐릭터를 오른쪽으로
                    to_x += character_speed
                elif event.key == pygame.K_UP:  # 캐릭터를 위로
                    to_y -= character_speed
                elif event.key == pygame.K_DOWN:  # 캐릭터를 아래로
                    to_y += character_speed
                elif event.key == K_F1:
                    screen = pygame.display.set_mode(
                        (screen_width, screen_height), FULLSCREEN)
                elif event.key == K_F2:
                    screen = pygame.display.set_mode(
                        (screen_width, screen_height))
                elif event.key == pygame.K_SPACE:
                    se_crash.stop()

                elif event.key == pygame.K_ESCAPE:
                    pass
            if event.type == pygame.KEYUP:  # 방향키를 떼면 멈춤
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    to_x = 0
                elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    to_y = 0

        character_x_pos += to_x * dt
        character_y_pos += to_y * dt

        # 가로 경계값 처리
        if character_x_pos < 0:
            character_x_pos = 0
        elif character_x_pos > screen_width - character_width:
            character_x_pos = screen_width - character_width

        # 세로 경계값 처리
        if character_y_pos < 0:
            character_y_pos = 0
        elif character_y_pos > screen_height - character_height:
            character_y_pos = screen_height - character_height

        # 충돌 처리를 위한 rect 정보 업데이트
        character_rect = character.get_rect()
        character_rect.left = character_x_pos
        character_rect.top = character_y_pos

        radio_rect = radio.get_rect()
        radio_rect.left = radio_x_pos
        radio_rect.top = radio_y_pos

        # 충돌 체크
        if character_rect.colliderect(radio_rect):
            print("충돌했어요")
            character_x_pos = radio_x_pos-radio_width-character_width
            # 충돌시 사운드
            se_ding.play()
            se_crash.play()
            msg = game_font.render(
                game_result, True, (0, 0, 0))
            msg_rect = msg.get_rect(
                center=(int(screen_width / 2), int(screen_height / 2)))
            screen.blit(msg, msg_rect)
            pygame.display.update()
            pygame.time.delay(500)

            # running = False
        screen.blit(background, (0, 0))  # 배경 그리기
        screen.blit(character, (character_x_pos, character_y_pos))  # 캐릭터 그리기
        screen.blit(radio, (radio_x_pos, radio_y_pos))  # 적 그리기

        # 타이머:경과시간 계산 (오버시간- 게임시작시간=0=게임종료)
        sec = int(pygame.time.get_ticks()/1000)
        timer = game_font.render("time laps : " +
                                 str(int(pygame.time.get_ticks()/1000/60))+"m"+str(sec)+"s", True, (0, 0, 0))  # 출력할 글자, True, 글자 색상
        screen.blit(timer, (10, 10))
        msg = game_font.render(
            game_now, True, (0, 0, 0))
        screen.blit(msg, (10, 40))
        pygame.display.update()  # 게임화면을 다시 그리기!


if __name__ == '__main__':
    main()
