import pygame
import math
import spritesheet
import rect
import random
from pygame import mixer #for sound

def startscreen():
    pygame.init()

    # variables
    clock = pygame.time.Clock()
    FPS = 60  # change how fast background moves
    SCREEN_WIDTH = 1000
    SCREEN_HEIGHT = 600
    BLACK = (0, 0, 0)

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Doodle Zoom")

    # background
    background_img = pygame.image.load(
        "/Users/isahung/Desktop/python/doodlezoom/assets/background.png"
    ).convert_alpha()  # trees, for the start screen
    background_img2 = pygame.image.load(
        "/Users/isahung/Desktop/python/doodlezoom/assets/background2.png"
    ).convert_alpha()  # no trees, for playing the game
    background_img3 = pygame.image.load(
        "/Users/isahung/Desktop/python/doodlezoom/assets/background3.png"
    ).convert_alpha()  # transition from background1 to background2
    bg_width = background_img.get_width()
    background_transition_width = background_img3.get_width()
    scroll = 0
    tiles = math.ceil(SCREEN_WIDTH / bg_width) + 1
    transition_tiles = math.ceil(SCREEN_WIDTH / background_transition_width) + 1

    #sound
    mixer.music.load("/Users/isahung/Desktop/python/doodlezoom/assets/cottagecore.mp3")
    mixer.music.play(-1) #play continuously

    # start button
    startbutton_sprite_img = pygame.image.load(
        "/Users/isahung/Desktop/python/doodlezoom/assets/startbutton_sprite.png"
    ).convert_alpha()
    startbutton_sprite_sheet = spritesheet.SpriteSheet(startbutton_sprite_img)
    startbutton_animation_list = []
    startbutton_animation_steps = 2
    startbutton_frame = 0
    startbutton_x, startbutton_y = 680, 480
    starbutton_width, starbutton_height = 292, 96
    starbutton_rect = rect.Rect(
        startbutton_x, startbutton_y, starbutton_width, starbutton_height
    )
    for c in range(startbutton_animation_steps):
        startbutton_animation_list.append(
            startbutton_sprite_sheet.get_image(
                c, starbutton_width, starbutton_height, BLACK
            )
        )

    # arrows
    arrow_sprite_img = pygame.image.load(
        "/Users/isahung/Desktop/python/doodlezoom/assets/arrow_sprite.png"
    ).convert_alpha()
    arrow_sprite_sheet = spritesheet.SpriteSheet(arrow_sprite_img)
    arrow_animation_list = []
    arrow_animation_steps = 2
    for d in range(arrow_animation_steps):
        arrow_animation_list.append(arrow_sprite_sheet.get_image(d, 56, 56, BLACK))

    # mouse
    mouse_img = pygame.image.load(
        "/Users/isahung/Desktop/python/doodlezoom/assets/mouse.png"
    ).convert_alpha()
    mouse_last_update = pygame.time.get_ticks()
    mouse_animation_cooldown = 250  # change how fast animation is


    # tennis ball
    tb_sprite_img = pygame.image.load(
        "/Users/isahung/Desktop/python/doodlezoom/assets/tennisball_sprite.png"
    ).convert_alpha()
    tb_sprite_sheet = spritesheet.SpriteSheet(tb_sprite_img)
    tb_animation_list = []
    tb_animation_steps = 4
    tb_last_update = pygame.time.get_ticks()
    tb_animation_cool_down = 240
    tb_frame = 0
    for z in range(tb_animation_steps):
        tb_animation_list.append(tb_sprite_sheet.get_image(z, 60, 60, BLACK))


    # cloud 1
    cloud1_img = pygame.image.load(
        "/Users/isahung/Desktop/python/doodlezoom/assets/titlebanner1.png"
    ).convert_alpha()
    # cloud 2
    cloud2_img = pygame.image.load(
        "/Users/isahung/Desktop/python/doodlezoom/assets/titlebanner2.png"
    ).convert_alpha()
    # dog flying rotated
    dogflyingr_sprite_img = pygame.image.load(
        "/Users/isahung/Desktop/python/doodlezoom/assets/dogflying_rotate_sprite_all.png"
    ).convert_alpha()
    corner_points = [ # pygame.draw.rect(screen, BLACK, pygame.Rect (0, 400, 4, 4))
                (0, 400), #sprite 1 start
                (700, 360), #sprite 2 start
                (748, 320),  # first loop
                (800, 240),
                (776, 200),
                (736, 200),
                (700, 240),
                (780, 280), # second loop down
                (1000, 230),#go out of bounds
                (1000, 310),
                (1000, 602),
                (-100, 602),
                (-100, 400),
            ]
    dogflyingr_pos = corner_points[0]
    dogflyingr_sprite_img = pygame.transform.scale(dogflyingr_sprite_img, (1890, 110))
    dogflyingr_sprite_sheet = spritesheet.SpriteSheet(dogflyingr_sprite_img)
    dogflyingr_animation_list = []
    dogflyingr_animation_steps = [2, 2, 2, 2, 2, 2, 2]
    dogflyingr_last_update = pygame.time.get_ticks()
    dogflyingr_animation_cool_down = 100
    dogflyingr_action = 0
    dogflyingr_frame = 0
    dogflyingr_step_counter = 0
    for dogf in dogflyingr_animation_steps:
        dogflyingr_temp_img_list = []
        for q in range(dogf):
            dogflyingr_temp_img_list.append(
                dogflyingr_sprite_sheet.get_image(dogflyingr_step_counter, 135, 110, BLACK)
            )
            dogflyingr_step_counter += 1
        dogflyingr_animation_list.append(dogflyingr_temp_img_list)
    def move(dogflyingr_pos, dogflyingr_speed, dogflyingr_points):
        direction = pygame.math.Vector2(dogflyingr_points[0]) - dogflyingr_pos
        if direction.length() <= dogflyingr_speed:
            dogflyingr_pos = dogflyingr_points[0]
            dogflyingr_points.append(dogflyingr_points[0])
            dogflyingr_points.pop(0)
        else:
            direction.scale_to_length(dogflyingr_speed)
            new_pos = pygame.math.Vector2(dogflyingr_pos) + direction
            dogflyingr_pos = (new_pos.x, new_pos.y)
        return dogflyingr_pos
    dogflyingr_points_clock = pygame.time.Clock()


    #dog flying rotated clouds
    dogflyingcloud_sprite_img = pygame.image.load("/Users/isahung/Desktop/python/doodlezoom/assets/dogflyingcloud_rotate_sprite_all.png"
    ).convert_alpha()
    corner_points2 = [ # pygame.draw.rect(screen, BLACK, pygame.Rect (0, 400, 4, 4))
                (0, 400), #sprite 1 start
                (700, 360), #sprite 2 start
                (748, 320),  # first loop
                (800, 240),
                (776, 200),
                (736, 200),
                (700, 240),
                (780, 280), # second loop down
                (1000, 230),#go out of bounds
                (1000, 310),
                (1000, 602),
                (-100, 602),
                (-100, 400),
            ]
    dogflyingcloud_pos = corner_points2[0]
    dogflyingcloud_sprite_img = pygame.transform.scale(dogflyingcloud_sprite_img, (1890, 110))
    dogflyingcloud_sprite_sheet = spritesheet.SpriteSheet(dogflyingcloud_sprite_img)
    dogflyingcloud_animation_list = []
    dogflyingcloud_animation_steps = [2, 2, 2, 2, 2, 2, 2]
    dogflyingcloud_last_update = pygame.time.get_ticks()
    dogflyingcloud_animation_cool_down = 100
    dogflyingcloud_action = 0
    dogflyingcloud_frame = 0
    dogflyingcloud_step_counter = 0
    for dogc in dogflyingcloud_animation_steps:
        dogflyingcloud_temp_img_list = []
        for q in range(dogc):
            dogflyingcloud_temp_img_list.append(
                dogflyingcloud_sprite_sheet.get_image(dogflyingcloud_step_counter, 135, 110, BLACK)
            )
            dogflyingcloud_step_counter += 1
        dogflyingcloud_animation_list.append(dogflyingcloud_temp_img_list)
    dogflyingcloud_points_clock = pygame.time.Clock()



    # letters
    letters_img = pygame.image.load(
        "/Users/isahung/Desktop/python/doodlezoom/assets/titlebanner4.png"
    ).convert_alpha()
    # cloud 3
    cloud3_img = pygame.image.load(
        "/Users/isahung/Desktop/python/doodlezoom/assets/titlebanner3.png"
    ).convert_alpha()
    # cloud 5
    cloud5_img = pygame.image.load(
        "/Users/isahung/Desktop/python/doodlezoom/assets/titlebanner5.png"
    ).convert_alpha()

    # dogs idle
    dog_sprite_img = pygame.image.load(
        "/Users/isahung/Desktop/python/doodlezoom/assets/dog_sprite.png"
    ).convert_alpha()
    dog_sprite_sheet = spritesheet.SpriteSheet(dog_sprite_img)
    dog_animation_list = []
    dog_animation_steps = [
        3,
        2,
        4,
    ]  # each number correlates to the number of frames in the animation. Type them in the number each animation movement sequence is ordered in the image
    dog_action = 0  # what action is it carrying out
    dog_last_update = pygame.time.get_ticks()
    dog_animation_cooldown = 110  # change how fast animation is
    dog_frame = 0
    dog_step_counter = 0
    for dog_animation in dog_animation_steps:
        dog_temp_img_list = []
        for _ in range(dog_animation):
            dog_temp_img_list.append(
                dog_sprite_sheet.get_image(dog_step_counter, 160, 108, BLACK)
            )
            dog_step_counter += 1
        dog_animation_list.append(dog_temp_img_list)

    run = True
    m = 0
    d = 0
    c = 0

    dogflyingr_x_pos = 0
    dogflyingr_y_pos = 0
    dogflyingr_speed = 3

    dogflyingcloud_x_pos = 0
    dogflyingcloud_y_pos = 0
    dogflyingcloud_speed = 3
    comp_amount_x = 0
    comp_amount_y = 0

    previous_len = 3 #number of repeated clouds
    previous_clouds = []

    status = "PLAYING" #other one is "TRANSITION" which would lead to level 1

    while run:
        # background
        if status == "TRANSITION":
            for i in range(0, transition_tiles):
                screen.blit(background_img3, (i * background_transition_width + scroll, 0))
            scroll -= 1
            if abs(scroll) > background_transition_width / 2:
                status = "PLAYING"

        elif status == "PLAYING":
            for i in range(0, tiles):
                screen.blit(background_img, (i * bg_width + scroll, 0))
            scroll -= 1
            if abs(scroll) > bg_width:
                scroll = 0


            # tennis ball
            screen.blit(tb_animation_list[tb_frame], (212, 508))
            tb_current_time = pygame.time.get_ticks()
            if tb_current_time - tb_last_update >= tb_animation_cool_down:
                tb_frame += 1
                tb_last_update = tb_current_time
                if tb_frame >= len(tb_animation_list):
                    tb_frame = 1


            # cloud 1
            cloud1_current_time = pygame.time.get_ticks()
            screen.blit(cloud1_img, (230, 36))
            # cloud 5
            cloud1_current_time = pygame.time.get_ticks()
            screen.blit(cloud5_img, (186, 60))
            # letters
            letters_current_time = pygame.time.get_ticks()
            screen.blit(letters_img, (200, 60))
            # cloud3
            cloud3_current_time = pygame.time.get_ticks()
            screen.blit(cloud3_img, (704, 210))
            # cloud2
            cloud2_current_time = pygame.time.get_ticks()
            screen.blit(cloud2_img, (46, 216))
        
        
    # dogflying rotated
            dogflyingr_points_clock.tick(100)
            dogflyingr_pos = move(dogflyingr_pos, dogflyingr_speed, corner_points)

            if dogflyingr_pos == (1000, 200) or dogflyingr_pos == (1000, 602) or dogflyingr_pos == (-100, 602) or dogflyingr_pos == (-100, 400):
                dogflyingr_speed = 1000
            else:
                dogflyingr_speed = 3

            dogflyingr_x_pos, dogflyingr_y_pos = dogflyingr_pos

            if dogflyingr_pos == (0, 400):
                dogflyingr_action = 0
                dogflyingcloud_action = 0
                comp_amount_x = -80
                comp_amount_y = 24
            
            elif dogflyingr_pos == (700, 360):
                dogflyingr_action = 1
                dogflyingcloud_action = 1
                comp_amount_x = -44
                comp_amount_y = 74
            
            elif dogflyingr_pos == (748, 320):
                dogflyingr_action = 1
                dogflyingcloud_action = 1
                comp_amount_x = -44
                comp_amount_y = 76
            
            elif dogflyingr_pos == (800, 240):
                dogflyingr_action  = 3
                dogflyingcloud_action  = 3
                comp_amount_x = 80
                comp_amount_y = 0
            
            elif dogflyingr_pos == (776, 200):
                dogflyingr_action = 3
                dogflyingcloud_action = 3
                comp_amount_x = 92
                comp_amount_y = 0

            elif dogflyingr_pos == (736, 200):
                dogflyingr_action = 4
                dogflyingcloud_action = 4
                comp_amount_x = 80
                comp_amount_y = -40
            
            elif dogflyingr_pos == (700, 240):
                dogflyingr_action = 6
                dogflyingcloud_action = 5
                comp_amount_x = -60
                comp_amount_y = -60
            
            elif dogflyingr_pos == (780, 280):
                dogflyingr_action = 0
                dogflyingcloud_action = 0
                comp_amount_x = -84
                comp_amount_y = 20

            elif dogflyingr_pos == (1000, 230):
                dogflyingr_action = 0
                dogflyingcloud_action = 1
                comp_amount_x = 0
                comp_amount_y = 0

            elif dogflyingr_x_pos<=-50:
                comp_amount_x = 0
                comp_amount_y = 0

        
            screen.blit(dogflyingr_animation_list[dogflyingr_action][dogflyingr_frame], (dogflyingr_x_pos, dogflyingr_y_pos))
            dogflyingr_current_time = pygame.time.get_ticks()
            if (
                dogflyingr_current_time - dogflyingr_last_update
                >= dogflyingr_animation_cool_down
            ):
                dogflyingr_frame += 1
                dogflyingr_last_update = dogflyingr_current_time
                if dogflyingr_frame >= len(dogflyingr_animation_list[dogflyingr_action]):
                    dogflyingr_frame = 0

            #doglfying rotated cloud
                    
            dogflyingcloud_points_clock.tick(100)
            dogflyingcloud_pos = move(dogflyingcloud_pos, dogflyingcloud_speed, corner_points2)

            if dogflyingcloud_pos == (1000, 200) or dogflyingcloud_pos == (1000, 602) or dogflyingcloud_pos == (-100, 602) or dogflyingcloud_pos == (-100, 400):
                dogflyingcloud_speed = 1000
            else:
                dogflyingcloud_speed = 3
            
            dogflyingcloud_x_pos, dogflyingcloud_y_pos = dogflyingcloud_pos

            screen.blit(dogflyingcloud_animation_list[dogflyingcloud_action][dogflyingcloud_frame], (dogflyingcloud_x_pos + comp_amount_x, dogflyingcloud_y_pos + comp_amount_y))
            
            dogflyingcloud_current_time = pygame.time.get_ticks()
            if (
                dogflyingcloud_current_time - dogflyingcloud_last_update
                >= dogflyingcloud_animation_cool_down
            ):
                dogflyingcloud_frame += 1
                dogflyingcloud_last_update = dogflyingcloud_current_time
                if dogflyingcloud_frame >= len(dogflyingcloud_animation_list[dogflyingcloud_action]):
                    dogflyingcloud_frame = 0
                
                if len(previous_clouds)>previous_len:
                    previous_clouds.pop(0)
                previous_clouds.append((dogflyingcloud_animation_list[dogflyingcloud_action][dogflyingcloud_frame], (dogflyingcloud_x_pos + comp_amount_x, dogflyingcloud_y_pos + comp_amount_y)))

                
            for previous_cloud in previous_clouds:
                (previous_dogflyingr_frame, (previous_dogflyingr_frame_x_pos, previous_dogflyingr_frame_y_pos)) = previous_cloud
                screen.blit(previous_dogflyingr_frame, (previous_dogflyingr_frame_x_pos, previous_dogflyingr_frame_y_pos))
        
            # dog idle
            screen.blit(dog_animation_list[dog_action][dog_frame], (32, 468))
            dog_current_time = pygame.time.get_ticks()
            if dog_current_time - dog_last_update >= dog_animation_cooldown:
                dog_frame += 1
                dog_last_update = dog_current_time
                if dog_frame >= len(dog_animation_list[dog_action]):
                    dog_frame = 0

            # start button
            screen.blit(
                startbutton_animation_list[startbutton_frame],
                (startbutton_x, startbutton_y),
            )

            # arrows
            screen.blit(arrow_animation_list[0], (936, 8))
            screen.blit(arrow_animation_list[1], (936, 72))

            # mouse
            # for m in range (4):
            mouse_current_time = pygame.time.get_ticks()
            if mouse_current_time - mouse_last_update >= mouse_animation_cooldown:
                mouse_last_update = mouse_current_time
                m += 1
                m %= 4
            screen.blit(mouse_img, (948 - (8 * m), 540 - (8 * m)))

            # press start button / press mouse
            pos_mouse = pygame.mouse.get_pos()
            pos_x, pos_y = pos_mouse
            if pygame.mouse.get_pressed()[0] and starbutton_rect.contains_point(
                pos_x, pos_y
            ):
                startbutton_frame = 1
                status = "TRANSITION"
                run = False
                #change status to level 1
                
            else:
                startbutton_frame = 0

        # user input/quit
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN and dog_action > 0:
                    dog_action -= 1
                    dog_frame = 0
                if event.key == pygame.K_UP and dog_action < len(dog_animation_list) - 1:
                    dog_action += 1
                    dog_frame = 0
                if event.key == pygame.K_SPACE:
                    startbutton_frame = 1
                    status = "TRANSITION"
                    run = False
        clock.tick(FPS)
        pygame.display.update()

    pygame.quit()
