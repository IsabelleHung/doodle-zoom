import pygame
import math
import spritesheet
import rect
from pygame import mixer #for sound
import random

#how to put on a live link on my website?

def level1():
    pygame.init()

    #variables
    clock = pygame.time.Clock()
    FPS = 60 #change how fast background moves
    SCREEN_WIDTH = 1000
    SCREEN_HEIGHT = 600
    BLACK = (0, 0, 0)
    # startscreen = True  #False means it is the game screen
    status = "PLAYING" #other status is "NEW PERSONAL BEST" and "DIED/OUT OF BOUNDS"
    play_again = False #turned on if they choose to play the game again. then a personal best will show
    instruction_screen = True
    end_of_game_screen = False
    level = 1

    #screen
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Doodle Zoom")

    #background
    background_img = pygame.image.load("assets/background2.png").convert_alpha()
    bg_width = background_img.get_width()
    scroll = 0
    tiles = math.ceil(SCREEN_WIDTH/bg_width) + 1

    #hearts
    heart_sprite_img = pygame.image.load("assets/heart_sprite.png").convert_alpha()
    heart_sprite_sheet = spritesheet.SpriteSheet(heart_sprite_img)
    heart_animation_list = []
    heart_animation_steps = 2
    heart_last_update = pygame.time.get_ticks()
    heart_animation_cooldown = 800 #change how fast hearts pump
    heart_frame = 0
    for x in range(heart_animation_steps):
        heart_animation_list.append(heart_sprite_sheet.get_image(x, 60, 53, BLACK))
    heart_counter = 3
    another_life_lost = False


    #dog flying propeller animation
    dogflying_sprite_img = pygame.image.load("assets/dogflying_sprite.png").convert_alpha()
    dogflying_sprite_sheet = spritesheet.SpriteSheet(dogflying_sprite_img)
    dogflying_animation_list = []
    dogflying_animation_steps = 2
    dogflying_last_update = pygame.time.get_ticks()
    dogflying_animation_cool_down = 100
    dogflying_frame = 0
    for b in range(dogflying_animation_steps):
        dogflying_animation_list.append(dogflying_sprite_sheet.get_image(b, 200, 140, BLACK))
    #dog flying moving down
    dogflying_play_animation_cool_down = 150
    dogflying_play_last_update = pygame.time.get_ticks()
    move = False
    idle = True
    change_increment = 88
    key_down = False

    #tennis ball
    tb_sprite_img = pygame.image.load("assets/tennisball_sprite.png").convert_alpha()
    tb_sprite_img = pygame.transform.scale(tb_sprite_img, (160, 40))
    tb_sprite_sheet = spritesheet.SpriteSheet(tb_sprite_img)
    tb_animation_list = []
    tb_animation_steps = 4
    tb_last_update = pygame.time.get_ticks()
    tb_animation_cool_down = 400
    tb_frame = 0
    tb_width = 40
    for z in range(tb_animation_steps):
        tb_animation_list.append(tb_sprite_sheet.get_image(z, tb_width, 60, BLACK))
    tb_scroll = 0
    tb_tiles = math.ceil(SCREEN_WIDTH/tb_width) + 1

    tb_num_balls = 10
    tb_balls = []

    add_ball_last_update = pygame.time.get_ticks()
    add_ball_animation_cooldown = 2000 #change how fast ball moves between frames in sprite

    #tennis ball counter top right
    tb_sprite_img_2 = pygame.image.load("assets/tennisball_sprite.png").convert_alpha()
    tb_sprite_sheet_2 = spritesheet.SpriteSheet(tb_sprite_img_2)
    tb_animation_list_2 = []
    for z in range(tb_animation_steps):
        tb_animation_list_2.append(tb_sprite_sheet_2.get_image(z, 60, 60, BLACK))
    tb_counter_x_pos = 872
    tb_counter = 0
    tb_counter_last_score = 0

    # tennis ball counter text top tight
    tb_font = pygame.font.Font("assets/PressStart2P-Regular.ttf",50)
    # pygame.draw.rect(screen, BLACK, pygame.Rect (872, 0, 4, 4))
    counter_text_x_pos = 944


    #fire hydrant/obstacles
    fh_sprite_img = pygame.image.load("assets/firehydrant_sprite.png").convert_alpha()
    fh_width = 66 #each image from sprite width
    fh_height = 171 #each image from sprite height
    tb_sprite_img = pygame.transform.scale(tb_sprite_img, (fh_width, fh_height))
    fh_sprite_sheet = spritesheet.SpriteSheet(fh_sprite_img)
    fh_animation_list = []
    fh_animation_steps = 3 #number of images in each sprite
    fh_last_update = pygame.time.get_ticks()
    fh_animation_cool_down = 3000 #cahnge how fast new hydrant added
    fh_frame = 0
    for g in range(fh_animation_steps):
        fh_animation_list.append(fh_sprite_sheet.get_image(g, fh_width, fh_height, BLACK))
    fh_scroll = 0
    fh_tiles = math.ceil(SCREEN_WIDTH/fh_width) + 1
    if level == 2:
        fh_num = 3
    if level == 3:
        fh_num = 5
    else:
        fh_num = 1
    fh_balls = []
    add_fh_last_update = pygame.time.get_ticks()
    add_fh_animation_cooldown = 2000 # change how fast frame moves in sprite


    #personal best trophy and numbers
    pb_trophy = pygame.image.load("assets/trophy.png")
    pb_trophy = pygame.transform.scale(pb_trophy, (60, 62))
    pb_trophy_x_position = 872
    pb_font = pygame.font.Font("assets/PressStart2P-Regular.ttf",50)
    pb_text_x_pos = 944
    pb_score = 0


    # instructions banner
    instructions_banner_img = pygame.image.load("assets/instructionsbanner.png")
    # instructions banner spacebar button
    bannerbackgrounddarkener_img = pygame.image.load("assets/bannerbackgrounddarkener.png")
    spacebutton_sprite_img = pygame.image.load("assets/spacebutton_sprite.png")
    spacebutton_sheet = spritesheet.SpriteSheet(spacebutton_sprite_img)
    spacebutton_animation_list = []
    spacebutton_animation_steps = 2
    spacebutton_action = 0
    spacebutton_last_update = pygame.time.get_ticks()
    spacebutton_animation_cooldown = 800 #change how fast hearts pump
    spacebutton_frame = 0
    for m in range(spacebutton_animation_steps):
        spacebutton_animation_list.append(spacebutton_sheet.get_image(m, 460, 60, BLACK))

    #try again banner
    tryagain_banner_img = pygame.image.load("assets/tryagainbanner.png")
    #new personal best banner
    personalbest_banner_img = pygame.image.load("assets/personalbestbanner.png")

    #try again and new personal bestbuttons
    transitionbuttons_sprite_img = pygame.image.load("assets/transitionbuttons_sprite.png")
    transitionbuttons_sprite_sheet = spritesheet.SpriteSheet(transitionbuttons_sprite_img)
    transtionbuttons_animation_list = []
    transitionbuttons_animation_steps = 6
    transitionbuttons_last_update = pygame.time.get_ticks()
    transtionbuttons_animation_cooldown = 800
    transitionbuttons_frame1 = 0 #left
    transitionbuttons_frame2 = 0
    if level == 1 or level == 2:
        transitionbuttons_frame2 = 2 #right
    if level == 3:
        transitionbuttons_frame2 = 4
    replaybutton_x, replaybutton_y = 120, 408 #cahnge
    nextlevelhomerect_x, nextlevelhomerect_y = 520, 408 #change 
    transitionbutton_width, transitionbutton_height = 360, 80
    replaybutton_rect = rect.Rect(replaybutton_x, replaybutton_y , transitionbutton_width, transitionbutton_height)
    nextlevelhomebutton_rect = rect.Rect(nextlevelhomerect_x, nextlevelhomerect_y, transitionbutton_width, transitionbutton_height)
    for a in range(transitionbuttons_animation_steps):
        transtionbuttons_animation_list.append(transitionbuttons_sprite_sheet.get_image(a, transitionbutton_width, transitionbutton_height, BLACK))

    #sound
    mixer.music.load("assets/cottagecore.mp3")
    mixer.music.play(-1) #play continuously

    run = True


    while run:
        #background
        for i in range(0, tiles):
            screen.blit(background_img, (i * bg_width + scroll, 0)) 
        scroll -= 1
        if abs(scroll) > bg_width:
            scroll = 0


        #dogflying
        if idle == True:
            dogflying_x_pos = 300
            dogflying_y_pos = 200

        dogflying = screen.blit(dogflying_animation_list[dogflying_frame], (dogflying_x_pos, dogflying_y_pos))

        dogflying_play_current_time = pygame.time.get_ticks()
        if dogflying_play_current_time - dogflying_play_last_update >= dogflying_play_animation_cool_down:
            dogflying_play_last_update = dogflying_play_current_time  
            if idle == False:
                if key_down == False:
                    dogflying_y_pos += change_increment/2
                if key_down == True:
                    dogflying_y_pos -= change_increment/2
        if dogflying_y_pos < -141 or dogflying_y_pos > 601:
            dogflying_y_pos = 300
            heart_counter -= 1
            #loose a life, start over by pressing space bar

        dogflying_current_time = pygame.time.get_ticks()
        if dogflying_current_time - dogflying_last_update >= dogflying_animation_cool_down:
            dogflying_frame += 1
            dogflying_last_update = dogflying_current_time
            if dogflying_frame >= len(dogflying_animation_list):
                dogflying_frame = 0
        

        #stationery tennis ball and number counter
        if tb_counter < 10: #1 digit
            tb_counter_x_pos = 872
            counter_text_x_pos = 944

        elif tb_counter < 100: #2 digits
            tb_counter_x_pos = 816
            counter_text_x_pos = 892

        elif tb_counter < 1000: # 3 digits
            tb_counter_x_pos = 764
            counter_text_x_pos = 840

        elif tb_counter < 10000: #4 digits
            tb_counter_x_pos = 716
            counter_text_x_pos = 792

        screen.blit(tb_animation_list_2[3], (tb_counter_x_pos, 12))
        
        tb_current_time = pygame.time.get_ticks()
        if tb_current_time - tb_last_update >= tb_animation_cool_down:
            tb_frame += 1
            tb_last_update = tb_current_time
            if tb_frame >= len(tb_animation_list):
                tb_frame = 1

        text = tb_font.render(str(tb_counter), True, BLACK)
        text_rect = text.get_rect()
        text_rect = (counter_text_x_pos, 20 )
        screen.blit(text, text_rect)

    #personal best trophy and counter
        if play_again:
            if tb_counter_last_score < tb_counter:
                tb_counter_last_score = tb_counter
            pb_score = tb_counter_last_score
            tb_counter = 0
            heart_counter = 3
            play_again = False
            
        if pb_score>0:
            if pb_score < 10: #1 digit
                pb_trophy_x_position = 872
                pb_text_x_pos = 944

            elif pb_score < 100: #2 digits
                pb_trophy_x_position = 816
                pb_text_x_pos = 892

            elif pb_score < 1000: # 3 digits
                pb_trophy_x_position = 764
                pb_text_x_pos = 840

            elif pb_score < 10000: #4 digits
                pb_trophy_x_position = 716
                pb_text_x_pos = 792

            screen.blit(pb_trophy, (pb_trophy_x_position, 84))
            pb_text = pb_font.render(str(pb_score), True, BLACK)
            pb_text_rect = pb_text.get_rect()
            pb_text_rect = (pb_text_x_pos, 92)
            screen.blit(pb_text, pb_text_rect)

        #instructions banner
        if idle and instruction_screen:
            screen.blit(bannerbackgrounddarkener_img, (0, 0))
            screen.blit(instructions_banner_img, (SCREEN_WIDTH/2 - 450, SCREEN_HEIGHT/2 - 250))
            screen.blit(spacebutton_animation_list[spacebutton_frame], (260, 440))



        #heart
        if heart_counter == 3:
            screen.blit(heart_animation_list[heart_frame], (12, 12))
            screen.blit(heart_animation_list[heart_frame], (88, 12))
            screen.blit(heart_animation_list[heart_frame], (164, 12))
        elif heart_counter == 2:
            screen.blit(heart_animation_list[heart_frame], (12, 12))
            screen.blit(heart_animation_list[heart_frame], (88, 12))
        elif heart_counter == 1:
            screen.blit(heart_animation_list[heart_frame], (12, 12))
        else:
            #show the screen options to replay or next level

            end_of_game_screen = True
            if end_of_game_screen:
                idle = True
                if pb_score >= tb_counter:
                    screen.blit(bannerbackgrounddarkener_img, (0, 0))
                    screen.blit(tryagain_banner_img, (SCREEN_WIDTH/2 - 450, SCREEN_HEIGHT/2 - 250))
                if pb_score < tb_counter:
                    screen.blit(bannerbackgrounddarkener_img, (0, 0))
                    screen.blit(personalbest_banner_img, (SCREEN_WIDTH/2 - 450, SCREEN_HEIGHT/2 - 250))
                screen.blit(transtionbuttons_animation_list[transitionbuttons_frame1], (replaybutton_x, replaybutton_y))
                screen.blit(transtionbuttons_animation_list[transitionbuttons_frame2], (nextlevelhomerect_x, nextlevelhomerect_y))
                    

        heart_current_time = pygame.time.get_ticks()
        if heart_current_time - heart_last_update >= heart_animation_cooldown:
            heart_frame += 1
            heart_last_update = heart_current_time
            if heart_frame >= len(heart_animation_list):
                heart_frame = 0

        
        #tennis ball while playing
        if idle == False:
            add_ball_current_time = pygame.time.get_ticks()
            if add_ball_current_time - add_ball_last_update >= add_ball_animation_cooldown:
                add_ball_last_update = add_ball_current_time
                tb_x_pos = random.randint(1000, 1210)
                tb_y_pos = random.randint(60, 380)
                # Adding new balls
                if len(tb_balls) < tb_num_balls:
                    tb_balls.append((tb_x_pos, tb_y_pos))

            # Adjust the x value of balls that are outside of the screen
            for i in range(len(tb_balls)):
                # Get the current position of the ball
                curr_tb_x_pos, curr_tb_y_pos = tb_balls[i]
                curr_tb_x_pos -= 1
                tb_rect = rect.Rect(curr_tb_x_pos, curr_tb_y_pos, 45, 45)
                if tb_rect.contains_point(dogflying_x_pos, dogflying_y_pos) or tb_rect.contains_point(dogflying_x_pos + 200, dogflying_y_pos + 140) or tb_rect.contains_point(dogflying_x_pos + 100, dogflying_y_pos + 70) or tb_rect.contains_point(dogflying_x_pos + 50, dogflying_y_pos + 35) or tb_rect.contains_point(dogflying_x_pos + 150, dogflying_y_pos + 105 ):
                    curr_tb_x_pos = random.randint(1000, 1210)
                    tb_counter += 1
                    ding_sound = mixer.Sound("assets/ding.mp3")
                    
                    ding_sound.play()
                # If it is outside, make it change position
                if curr_tb_x_pos < -100:
                    curr_tb_x_pos = random.randint(1000, 1210)

                tb_balls[i] = (curr_tb_x_pos, curr_tb_y_pos)
                screen.blit(tb_animation_list[tb_frame], (curr_tb_x_pos, curr_tb_y_pos))
            tb_scroll -= 1
            if abs(tb_scroll) > tb_width:
                tb_scroll = 0

        #fire hydrant
        if idle == False:
            if idle == False:
                # if level == 2 or level == 3:
                add_fh_current_time = pygame.time.get_ticks()
                if add_fh_current_time - add_fh_last_update >= add_fh_animation_cooldown:
                    add_fh_last_update = add_fh_current_time
                    fh_x_pos = random.randint(1000, 1308) #when range of where it can spawn x-wise
                    fh_y_pos = random.randint(400, 440) #when range of where it can spawn y-wise
                    #add new hydrants
                    if len(fh_balls) < fh_num:
                        fh_balls.append((fh_x_pos, fh_y_pos))

                fh_current_time = pygame.time.get_ticks()
                if fh_current_time - fh_last_update >= fh_animation_cool_down:
                    fh_frame += 1
                    fh_last_update = fh_current_time
                    if fh_frame >= len(fh_animation_list):
                        fh_frame = 0
                

                #adjust the x value of balls that are outside the screen
                for i in range(len(fh_balls)):
                    #get current position of the ball
                    curr_fh_x_pos, curr_fh_y_pos = fh_balls[i]
                    curr_fh_x_pos -= 1
                    fh_rect = rect.Rect(curr_fh_x_pos, curr_fh_y_pos, fh_width, fh_height)
                    if fh_rect.contains_point(dogflying_x_pos, dogflying_y_pos) or fh_rect.contains_point(dogflying_x_pos + 200, dogflying_y_pos + 140) or fh_rect.contains_point(dogflying_x_pos + 100, dogflying_y_pos + 70) or fh_rect.contains_point(dogflying_x_pos + 50, dogflying_y_pos + 35) or fh_rect.contains_point(dogflying_x_pos + 150, dogflying_y_pos + 105 ):
                        curr_fh_x_pos = random.randint(1000, 1308) #repeat the range where it can spawn x-wise
                        heart_counter -= 1
                    if curr_fh_x_pos < -fh_width:
                        curr_fh_x_pos = random.randint(1000, 1308)#repeat the range where it can spawn x-wise
                    
                    fh_balls[i] = (curr_fh_x_pos, curr_fh_y_pos)
                    screen.blit(fh_animation_list[fh_frame], (curr_fh_x_pos, curr_fh_y_pos))
                fh_scroll -= 1
                if abs(fh_scroll) > fh_width:
                    fh_scroll = 0 


        #pressing play again
        pos_mouse = pygame.mouse.get_pos()
        pos_x, pos_y = pos_mouse
        
        if pygame.mouse.get_pressed()[0]:
            if nextlevelhomebutton_rect.contains_point(
                    pos_x, pos_y
                ):
                    if idle and end_of_game_screen:
                        pygame.time.wait(200)
                        if level == 1:
                            transitionbuttons_frame2 = 3
                            screen.blit(transtionbuttons_animation_list[transitionbuttons_frame2], (nextlevelhomerect_x, nextlevelhomerect_y))
                            pygame.display.update()
                            pygame.time.wait(200)
                            transitionbuttons_frame2 = 2
                            level = 2
                            play_again = True
                        elif level == 2:
                            transitionbuttons_frame2 = 3
                            screen.blit(transtionbuttons_animation_list[transitionbuttons_frame2], (nextlevelhomerect_x, nextlevelhomerect_y))
                            pygame.display.update()
                            pygame.time.wait(200)
                            transitionbuttons_frame2 = 4
                            level = 3
                            play_again = True
                        elif level == 3:
                            transitionbuttons_frame2 = 5
                            screen.blit(transtionbuttons_animation_list[transitionbuttons_frame2], (nextlevelhomerect_x, nextlevelhomerect_y))
                            pygame.display.update()
                            pygame.time.wait(200)
                            play_again = False
                            level = 1
                            run = False
                        end_of_game_screen = False
                        idle = False
                        tb_counter = 0
                        tb_counter_last_score = 0
                        pb_score = 0
            else:
                    if idle and end_of_game_screen:
                        if level == 1 or level == 2:
                            transitionbuttons_frame2 = 2
                        elif level == 3:
                                transitionbuttons_frame2 = 4

            if replaybutton_rect.contains_point(
                pos_x, pos_y
            ):
                if idle and end_of_game_screen:
                    transitionbuttons_frame1 = 1
                    screen.blit(transtionbuttons_animation_list[transitionbuttons_frame1], (replaybutton_x, replaybutton_y))
                    pygame.display.update()
                    pygame.time.wait(200)
                    end_of_game_screen = False
                    play_again = True
                    idle = False
                    transitionbuttons_frame1 = 0
                    

        clock.tick(FPS)

        #user input and quit
        pos = pygame.mouse.get_pos()
        pos_x, pos_y = pos
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if idle and instruction_screen:
                    spacebutton_frame = 1
                    screen.blit(spacebutton_animation_list[1], (260, 440))
                    pygame.display.update()
                    pygame.time.wait(300)
                    instruction_screen = False
                    idle = False
                if event.key == pygame.K_SPACE:
                    key_down = True 
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_SPACE:
                    key_down = False

        pygame.display.update()

    pygame.quit()

