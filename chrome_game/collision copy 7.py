from inspect import isgenerator
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
se_afternoon = None
se_bug = None
se_button = None
se_chill = None
se_clear = None
se_coin = None
se_fire = None
se_loading = None
se_morning = None
se_night = None
se_npc = None
se_opening = None
se_quest = None
se_sleep = None
se_sunny = None
se_woman = None


def play():
    # 소리데이터
    global se_afternoon, se_coin, se_morning, se_, se_night, se_sleep, se_chill, se_npc, se_clear, se_loading, se_fire, se_bug, se_opening, se_quest, se_sunny, se_button, se_woman
    # 초기화

    pygame.init()
    # 화면 타이틀 설정
    pygame.display.set_caption("Juke Dino")  # 게임 이름

    # Font 정의
    game_font = pygame.font.Font(None, 35)
    game_result_1 = "Good Afternoon"
    game_result_2 = "There are swarm of fireflies"
    game_result_3 = "Stay Chill Hear"
    game_result_4 = "Hello, Here is office"
    game_result_5 = "I gathered some wood"
    game_result_6 = "Good Morning"
    game_result_7 = "Good Night"
    game_result_8 = "Hello, I'm Bob"
    game_result_9 = "This is opening song"
    game_result_10 = "This is quest"
    game_result_11 = "Time to Sleep"
    game_result_12 = "Sunny Day"
    sound_off = "Sound OFF"
    want_quit = "Do you Want Quit?"
    song_msg = "None"
    # 날짜 출력
    now = datetime.now()
    game_now = "Today Date : "+str(now.year)+"."+str(now.month)+"."+str(now.day) + \
        "."

    # 화면 크기 설정
    screen_width = 840  # 가로 크기
    screen_height = 600  # 세로 크기
    screen = pygame.display.set_mode((screen_width, screen_height))
    # FPS
    clock = pygame.time.Clock()
    # 소리
    se_afternoon = pygame.mixer.Sound(
        os.path.join(music_path, "afternoon.mp3"))
    se_bug = pygame.mixer.Sound(
        os.path.join(music_path, "bug.mp3"))
    se_button = pygame.mixer.Sound(
        os.path.join(music_path, "button.mp3"))
    se_chill = pygame.mixer.Sound(
        os.path.join(music_path, "chill.mp3"))
    se_clear = pygame.mixer.Sound(
        os.path.join(music_path, "clear.mp3"))
    se_coin = pygame.mixer.Sound(
        os.path.join(music_path, "coin.mp3"))
    se_fire = pygame.mixer.Sound(
        os.path.join(music_path, "fire.mp3"))
    se_loading = pygame.mixer.Sound(
        os.path.join(music_path, "loading.mp3"))
    se_morning = pygame.mixer.Sound(
        os.path.join(music_path, "morning.mp3"))
    se_night = pygame.mixer.Sound(
        os.path.join(music_path, "night.mp3"))
    se_npc = pygame.mixer.Sound(
        os.path.join(music_path, "npc.mp3"))
    se_opening = pygame.mixer.Sound(
        os.path.join(music_path, "opening.mp3"))
    se_quest = pygame.mixer.Sound(
        os.path.join(music_path, "quest.mp3"))
    se_sleep = pygame.mixer.Sound(
        os.path.join(music_path, "sleep.mp3"))
    se_sunny = pygame.mixer.Sound(
        os.path.join(music_path, "sunny.mp3"))
    se_woman = pygame.mixer.Sound(
        os.path.join(music_path, "woman.mp3"))

    se_clear.play()

    character_size = character.get_rect().size  # 이미지의 크기를 구해옴
    character_width = character_size[0]  # 캐릭터의 가로 크기
    character_height = character_size[1]  # 캐릭터의 세로 크기
    character_x_pos = (screen_width / 2) - (character_width /
                                            2)  # 화면 가로의 절반 크기에 해당하는 곳에 위치 (가로)
    # 화면 세로 크기 가장 아래에 해당하는 곳에 위치 (세로)
    character_y_pos = screen_height - character_height

    # 캐릭터가 이동할 좌표
    to_x = 0
    to_y = 0

    # 캐릭터 이동 속도
    character_speed = 0.13

    # afternoon 캐릭터
    afternoon = pygame.image.load(
        os.path.join(image_path, "1.png"))
    afternoon_size = afternoon.get_rect().size  # 이미지의 크기를 구해옴
    afternoon_width = afternoon_size[0]  # 캐릭터의 가로 크기x
    afternoon_height = afternoon_size[1]  # 캐릭터의 세로 크기
    # 왼쪽 상단
    afternoon_x_pos = 300
    afternoon_y_pos = 100

    # bug 캐릭터
    bug = pygame.image.load(
        os.path.join(image_path, "2.png"))
    bug_size = bug.get_rect().size  # 이미지의 크기를 구해옴
    bug_width = bug_size[0]  # 캐릭터의 가로 크기x
    bug_height = bug_size[1]  # 캐릭터의 세로 크기
    # 화면 가로의 절반 크기에 해당하는 곳에 위치 (가로)
    bug_x_pos = 540
    # 화면 세로 크기 가장 아래에 해당하는 곳에 위치 (세로)
    bug_y_pos = 100

    # chill 캐릭터
    chill = pygame.image.load(
        os.path.join(image_path, "3.png"))
    chill_size = chill.get_rect().size  # 이미지의 크기를 구해옴
    chill_width = chill_size[0]  # 캐릭터의 가로 크기x
    chill_height = chill_size[1]  # 캐릭터의 세로 크기
    # 화면 가로의 절반 크기에 해당하는 곳에 위치 (가로)
    chill_x_pos = 420
    chill_y_pos = 200

    # clear 캐릭터
    clear = pygame.image.load(
        os.path.join(image_path, "4.png"))
    clear_size = clear.get_rect().size  # 이미지의 크기를 구해옴
    clear_width = clear_size[0]  # 캐릭터의 가로 크기x
    clear_height = clear_size[1]  # 캐릭터의 세로 크기
    # 화면 가로의 절반 크기에 해당하는 곳에 위치 (가로)
    clear_x_pos = 60
    # 화면 세로 크기 가장 아래에 해당하는 곳에 위치 (세로)
    clear_y_pos = 400

    # fire 캐릭터
    fire = pygame.image.load(
        os.path.join(image_path, "5.png"))
    fire_size = fire.get_rect().size  # 이미지의 크기를 구해옴
    fire_width = fire_size[0]  # 캐릭터의 가로 크기x
    fire_height = fire_size[1]  # 캐릭터의 세로 크기
    # 화면 가로의 절반 크기에 해당하는 곳에 위치 (가로)
    fire_x_pos = 720
    # 화면 세로 크기 가장 아래에 해당하는 곳에 위치 (세로)
    fire_y_pos = 100

    # morning 캐릭터
    morning = pygame.image.load(
        os.path.join(image_path, "6.png"))
    morning_size = morning.get_rect().size  # 이미지의 크기를 구해옴
    morning_width = morning_size[0]  # 캐릭터의 가로 크기x
    morning_height = morning_size[1]  # 캐릭터의 세로 크기
    # 화면 가로의 절반 크기에 해당하는 곳에 위치 (가로)
    morning_x_pos = 180
    # 화면 세로 크기 가장 아래에 해당하는 곳에 위치 (세로)
    morning_y_pos = 200

    # night 캐릭터
    night = pygame.image.load(
        os.path.join(image_path, "7.png"))
    night_size = night.get_rect().size  # 이미지의 크기를 구해옴
    night_width = night_size[0]  # 캐릭터의 가로 크기x
    night_height = night_size[1]  # 캐릭터의 세로 크기
    # 화면 가로의 절반 크기에 해당하는 곳에 위치 (가로)
    night_x_pos = 720
    # 화면 세로 크기 가장 아래에 해당하는 곳에 위치 (세로)
    night_y_pos = 200
    # npc 캐릭터
    npc = pygame.image.load(
        os.path.join(image_path, "8.png"))
    npc_size = npc.get_rect().size  # 이미지의 크기를 구해옴
    npc_width = npc_size[0]  # 캐릭터의 가로 크기x
    npc_height = npc_size[1]  # 캐릭터의 세로 크기
    # 화면 가로의 절반 크기에 해당하는 곳에 위치 (가로)
    npc_x_pos = 420
    # 화면 세로 크기 가장 아래에 해당하는 곳에 위치 (세로)
    npc_y_pos = 400

    # opening 캐릭터
    opening = pygame.image.load(
        os.path.join(image_path, "9.png"))
    opening_size = opening.get_rect().size  # 이미지의 크기를 구해옴
    opening_width = opening_size[0]  # 캐릭터의 가로 크기x
    opening_height = opening_size[1]  # 캐릭터의 세로 크기
    # 화면 가로의 절반 크기에 해당하는 곳에 위치 (가로)
    opening_x_pos = 300
    # 화면 세로 크기 가장 아래에 해당하는 곳에 위치 (세로)
    opening_y_pos = 400

    # quest 캐릭터
    quest = pygame.image.load(
        os.path.join(image_path, "10.png"))
    quest_size = quest.get_rect().size  # 이미지의 크기를 구해옴
    quest_width = quest_size[0]  # 캐릭터의 가로 크기x
    quest_height = quest_size[1]  # 캐릭터의 세로 크기
    # 화면 가로의 절반 크기에 해당하는 곳에 위치 (가로)
    quest_x_pos = 540
    # 화면 세로 크기 가장 아래에 해당하는 곳에 위치 (세로)
    quest_y_pos = 400

    # sleep 캐릭터
    sleep = pygame.image.load(
        os.path.join(image_path, "11.png"))
    sleep_size = sleep.get_rect().size  # 이미지의 크기를 구해옴
    sleep_width = sleep_size[0]  # 캐릭터의 가로 크기x
    sleep_height = sleep_size[1]  # 캐릭터의 세로 크기
    # 화면 가로의 절반 크기에 해당하는 곳에 위치 (가로)
    sleep_x_pos = 720
    # 화면 세로 크기 가장 아래에 해당하는 곳에 위치 (세로)
    sleep_y_pos = 400

    # sunny 캐릭터
    sunny = pygame.image.load(
        os.path.join(image_path, "12.png"))
    sunny_size = sunny.get_rect().size  # 이미지의 크기를 구해옴
    sunny_width = sunny_size[0]  # 캐릭터의 가로 크기x
    sunny_height = sunny_size[1]  # 캐릭터의 세로 크기
    # 화면 가로의 절반 크기에 해당하는 곳에 위치 (가로)
    sunny_x_pos = 60
    # 화면 세로 크기 가장 아래에 해당하는 곳에 위치 (세로)
    sunny_y_pos = 100

    # 이벤트 루프
    # 게임이 진행중인가?
    running = True
    while running:
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
                elif event.key == K_F1:  # F1키 누르면 창확대
                    screen = pygame.display.set_mode(
                        (screen_width, screen_height), FULLSCREEN)
                elif event.key == K_F2:  # F2키 누르면 창 축소
                    screen = pygame.display.set_mode(
                        (screen_width, screen_height))
                elif event.key == pygame.K_SPACE:  # space 누르면 모든 음악 멈춤
                    song_off()
                    msg = game_font.render(
                        sound_off, True, (0, 0, 0))
                    msg_rect = msg.get_rect(
                        center=(int(screen_width / 2), int(screen_height / 2)))
                    screen.blit(msg, msg_rect)
                    pygame.display.update()
                    pygame.time.delay(500)
                    song_msg = "None"

                elif event.key == pygame.K_ESCAPE:  # ESC누르면 아무것도 동작 안함
                    msg = game_font.render(
                        want_quit, True, (0, 0, 0))
                    msg_rect = msg.get_rect(
                        center=(int(screen_width / 2), int(screen_height / 2)))
                    screen.blit(msg, msg_rect)
                    pygame.display.update()
                    pygame.time.delay(1000)
                    # if event.type == pygame.KEYDOWN:  # 방향키를 떼면 주인공 캐릭터 멈춤
                    #     if event.key == pygame.K_a:
                    #         running = False
                    #     elif event.key == pygame.K_n:
                    #         running = True

            if event.type == pygame.KEYUP:  # 방향키를 떼면 주인공 캐릭터 멈춤
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

        afternoon_rect = afternoon.get_rect()
        afternoon_rect.left = afternoon_x_pos
        afternoon_rect.top = afternoon_y_pos

        bug_rect = bug.get_rect()
        bug_rect.left = bug_x_pos
        bug_rect.top = bug_y_pos

        chill_rect = chill.get_rect()
        chill_rect.left = chill_x_pos
        chill_rect.top = chill_y_pos

        clear_rect = clear.get_rect()
        clear_rect.left = clear_x_pos
        clear_rect.top = clear_y_pos

        fire_rect = fire.get_rect()
        fire_rect.left = fire_x_pos
        fire_rect.top = fire_y_pos

        morning_rect = morning.get_rect()
        morning_rect.left = morning_x_pos
        morning_rect.top = morning_y_pos

        night_rect = night.get_rect()
        night_rect.left = night_x_pos
        night_rect.top = night_y_pos

        npc_rect = npc.get_rect()
        npc_rect.left = npc_x_pos
        npc_rect.top = npc_y_pos

        opening_rect = opening.get_rect()
        opening_rect.left = opening_x_pos
        opening_rect.top = opening_y_pos

        quest_rect = quest.get_rect()
        quest_rect.left = quest_x_pos
        quest_rect.top = quest_y_pos

        sleep_rect = sleep.get_rect()
        sleep_rect.left = sleep_x_pos
        sleep_rect.top = sleep_y_pos

        sunny_rect = sunny.get_rect()
        sunny_rect.left = sunny_x_pos
        sunny_rect.top = sunny_y_pos

        # afternoon 충돌 체크
        if character_rect.colliderect(afternoon_rect):
            print("충돌했어요")
            character_y_pos = afternoon_y_pos+afternoon_height
            # 충돌시 사운드
            song_off()
            se_afternoon.play()
            se_coin.play()
            msg = game_font.render(
                game_result_1, True, (0, 0, 0))
            msg_rect = msg.get_rect(
                center=(int(screen_width / 2), int(screen_height / 2)))
            screen.blit(msg, msg_rect)
            pygame.display.update()
            pygame.time.delay(500)
            song_msg = "Afternoon"

        # bug 충돌 체크
        if character_rect.colliderect(bug_rect):
            print("충돌했어요")
            character_y_pos = bug_y_pos+bug_height
            # 충돌시 사운드
            song_off()
            se_bug.play()
            se_coin.play()
            msg = game_font.render(
                game_result_2, True, (0, 0, 0))
            msg_rect = msg.get_rect(
                center=(int(screen_width / 2), int(screen_height / 2)))
            screen.blit(msg, msg_rect)
            pygame.display.update()
            pygame.time.delay(500)
            song_msg = "Bug"

        # chill 충돌 체크
        if character_rect.colliderect(chill_rect):
            print("충돌했어요")
            character_y_pos = chill_y_pos+chill_height
            # 충돌시 사운드
            song_off()
            se_chill.play()
            se_coin.play()
            msg = game_font.render(
                game_result_3, True, (0, 0, 0))
            msg_rect = msg.get_rect(
                center=(int(screen_width / 2), int(screen_height / 2)))
            screen.blit(msg, msg_rect)
            pygame.display.update()
            pygame.time.delay(500)
            song_msg = "Chill"

        # clear 충돌 체크
        if character_rect.colliderect(clear_rect):
            print("충돌했어요")
            character_y_pos = clear_y_pos+clear_height
            # 충돌시 사운드
            song_off()
            se_clear.play()
            se_coin.play()
            msg = game_font.render(
                game_result_4, True, (0, 0, 0))
            msg_rect = msg.get_rect(
                center=(int(screen_width / 2), int(screen_height / 2)))
            screen.blit(msg, msg_rect)
            pygame.display.update()
            pygame.time.delay(500)
            song_msg = "Clear"

        # fire 충돌 체크
        if character_rect.colliderect(fire_rect):
            print("충돌했어요")
            character_y_pos = fire_y_pos+fire_height
            # 충돌시 사운드
            song_off()
            se_fire.play()
            se_coin.play()
            msg = game_font.render(
                game_result_5, True, (0, 0, 0))
            msg_rect = msg.get_rect(
                center=(int(screen_width / 2), int(screen_height / 2)))
            screen.blit(msg, msg_rect)
            pygame.display.update()
            pygame.time.delay(500)
            song_msg = "Fire"

        # morning 충돌 체크
        if character_rect.colliderect(morning_rect):
            print("충돌했어요")
            character_y_pos = morning_y_pos+morning_height
            # 충돌시 사운드
            song_off()
            se_morning.play()
            se_coin.play()
            msg = game_font.render(
                game_result_6, True, (0, 0, 0))
            msg_rect = msg.get_rect(
                center=(int(screen_width / 2), int(screen_height / 2)))
            screen.blit(msg, msg_rect)
            pygame.display.update()
            pygame.time.delay(500)
            song_msg = "Morning"

        # night 충돌 체크
        if character_rect.colliderect(night_rect):
            print("충돌했어요")
            character_y_pos = night_y_pos+night_height
            # 충돌시 사운드
            song_off()
            se_night.play()
            se_coin.play()
            msg = game_font.render(
                game_result_7, True, (0, 0, 0))
            msg_rect = msg.get_rect(
                center=(int(screen_width / 2), int(screen_height / 2)))
            screen.blit(msg, msg_rect)
            pygame.display.update()
            pygame.time.delay(500)
            song_msg = "Night"

        # npc 충돌 체크
        if character_rect.colliderect(npc_rect):
            print("충돌했어요")
            character_y_pos = npc_y_pos+npc_height
            # 충돌시 사운드
            song_off()
            se_npc.play()
            se_coin.play()
            msg = game_font.render(
                game_result_8, True, (0, 0, 0))
            msg_rect = msg.get_rect(
                center=(int(screen_width / 2), int(screen_height / 2)))
            screen.blit(msg, msg_rect)
            pygame.display.update()
            pygame.time.delay(500)
            song_msg = "NPC"

        # opening 충돌 체크
        if character_rect.colliderect(opening_rect):
            print("충돌했어요")
            character_y_pos = opening_y_pos+opening_height
            # 충돌시 사운드
            song_off()
            se_opening.play()
            se_coin.play()
            msg = game_font.render(
                game_result_9, True, (0, 0, 0))
            msg_rect = msg.get_rect(
                center=(int(screen_width / 2), int(screen_height / 2)))
            screen.blit(msg, msg_rect)
            pygame.display.update()
            pygame.time.delay(500)
            song_msg = "Opening"

        # quest 충돌 체크
        if character_rect.colliderect(quest_rect):
            print("충돌했어요")
            character_y_pos = quest_y_pos+quest_height
            # 충돌시 사운드
            song_off()
            se_quest.play()
            se_coin.play()
            msg = game_font.render(
                game_result_10, True, (0, 0, 0))
            msg_rect = msg.get_rect(
                center=(int(screen_width / 2), int(screen_height / 2)))
            screen.blit(msg, msg_rect)
            pygame.display.update()
            pygame.time.delay(500)
            song_msg = "Quest"

        # sleep 충돌 체크
        if character_rect.colliderect(sleep_rect):
            print("충돌했어요")
            character_y_pos = sleep_y_pos+sleep_height
            # 충돌시 사운드
            song_off()
            se_sleep.play()
            se_coin.play()
            msg = game_font.render(
                game_result_11, True, (0, 0, 0))
            msg_rect = msg.get_rect(
                center=(int(screen_width / 2), int(screen_height / 2)))
            screen.blit(msg, msg_rect)
            pygame.display.update()
            pygame.time.delay(500)
            song_msg = "Sleep"

        # sunny 충돌 체크
        if character_rect.colliderect(sunny_rect):
            print("충돌했어요")
            character_y_pos = sunny_y_pos+sunny_height
            # 충돌시 사운드
            song_off()
            se_sunny.play()
            se_coin.play()
            msg = game_font.render(
                game_result_12, True, (0, 0, 0))
            msg_rect = msg.get_rect(
                center=(int(screen_width / 2), int(screen_height / 2)))
            screen.blit(msg, msg_rect)
            pygame.display.update()
            pygame.time.delay(500)
            song_msg = "Sunny"

        screen.blit(background, (0, 0))  # 배경 그리기
        # 주인공캐릭터 그리기
        screen.blit(character, (character_x_pos, character_y_pos))
        # 다른 캐릭터 그리기
        screen.blit(afternoon, (afternoon_x_pos, afternoon_y_pos))
        screen.blit(bug, (bug_x_pos, bug_y_pos))
        screen.blit(chill, (chill_x_pos, chill_y_pos))
        screen.blit(clear, (clear_x_pos, clear_y_pos))
        screen.blit(fire, (fire_x_pos, fire_y_pos))
        screen.blit(morning, (morning_x_pos, morning_y_pos))
        screen.blit(night, (night_x_pos, night_y_pos))
        screen.blit(npc, (npc_x_pos, npc_y_pos))
        screen.blit(opening, (opening_x_pos, opening_y_pos))
        screen.blit(quest, (quest_x_pos, quest_y_pos))
        screen.blit(sleep, (sleep_x_pos, sleep_y_pos))
        screen.blit(sunny, (sunny_x_pos, sunny_y_pos))

        # 타이머:경과시간 계산 (오버시간- 게임시작시간=0=게임종료)
        sec = int(pygame.time.get_ticks()/1000)
        timer = game_font.render("Playtime : " +
                                 str(int(pygame.time.get_ticks()/1000/60))+"m", True, (0, 0, 0))  # 출력할 글자, True, 글자 색상
        screen.blit(timer, (10, 10))
        msg = game_font.render(
            game_now, True, (0, 0, 0))
        screen.blit(msg, (10, 40))

        msg_2 = game_font.render(
            'Play Now : '+song_msg, True, (0, 0, 0))
        screen.blit(msg_2, (540, 40))
        pygame.display.update()  # 게임화면을 다시 그리기!


def intro():
    global sec, se_opening

    pygame.init()
    screen_width = 840
    screen_height = 600
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption('Juke Dino')
    game_font = pygame.font.Font(None, 35)
    background = pygame.image.load(
        os.path.join(image_path, "white.png"))
    character = pygame.image.load(
        os.path.join(image_path, "dino1.png"))
    character_size = character.get_rect().size
    character_width = character_size[0]
    character_height = character_size[1]
    character_x_pos = (screen_width/2-character_width/2)
    character_y_pos = (screen_height/2)

    se_opening = pygame.mixer.Sound(
        os.path.join(music_path, "opening.mp3"))
    se_opening.play()

    to_x = 0
    to_y = 0
    loading = "Pleas Wait ..."

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
                elif event.key == pygame.K_SPACE:
                    sec = 0
                    msg = game_font.render(
                        loading, True, (0, 0, 0))
                    msg_rect = msg.get_rect(
                        center=(int(screen_width / 2), 400))
                    screen.blit(msg, msg_rect)
                    pygame.display.update()
                    pygame.time.delay(500)
                    se_opening.stop()
                    play()

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
        msg = game_font.render(
            'Juke Dino', True, (0, 0, 0))
        msg_rect = msg.get_rect(
            center=(int(screen_width / 2), 200))
        screen.blit(msg,  msg_rect)
        msg = game_font.render(
            'Press [SPACE] to Start', True, (0, 0, 0))
        msg_rect = msg.get_rect(
            center=(int(screen_width / 2), 500))
        screen.blit(msg,  msg_rect)
        pygame.display.update()  # 게임화면을 다시 그리기!


def main():
    intro()


def song_off():
    global se_afternoon, se_coin, se_morning, se_, se_night, se_sleep, se_chill, se_npc, se_clear, se_loading, se_fire, se_bug, se_opening, se_quest, se_sunny, se_button, se_woman
    se_afternoon.stop()
    se_bug.stop()
    se_button.stop()
    se_chill.stop()
    se_clear.stop()
    se_coin.stop()
    se_fire.stop()
    se_loading.stop()
    se_morning.stop()
    se_night.stop()
    se_npc.stop()
    se_opening.stop()
    se_quest.stop()
    se_sleep.stop()
    se_sunny.stop()
    se_woman.stop()
    se_coin.play()


if __name__ == '__main__':
    main()
