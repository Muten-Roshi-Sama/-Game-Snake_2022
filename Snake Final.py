"""
Author : Flioris Vassily
Date : 03.12.2022

Goal :
This is a simple code that creates an interactive snake game.
You, the player, moves with the arrow keys, try to eat a maximum of food to grow without touching your body !
Good luck !
Input : The four arrows to move around or the W, A, S, D or Z, Q, S, D
Output : The Interactive Snake game itself.


INFO :

The game space is (x, y) ;


"""



# IMPORTS
import pygame
from pygame import mixer
import pygame_gui
import sys
import os
import time
import random
import json
#import freetype

#initialization
pygame.mixer.pre_init(44100, 16, 2, 4096) #frequency, size, channels, buffersize
pygame.init()
pygame.font.init()
pygame.mixer.init()
pygame.freetype.init()


#colors
black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)
red = pygame.Color(255, 0, 0)
green = pygame.Color(0, 255, 0)
blue = pygame.Color(0, 0, 255)
yellow = pygame.Color(255,239,0)
bg_color = black

#variables
pygame.display.set_caption('Snake, by VF')
snake_speed = 25
food_color = yellow
snake_size = 10 #do not touch
millis = lambda: int(round(time.time() * 1000))
last_millis_sound = 0
last_millis_food = 0

class ValueTooLowError(Exception):
    pass

class ValueTooHighError(Exception):
    pass

#QUESTIONS FOR USERS
pseudo = str(input('Input name :'))
valid = False
while not valid:
    try:
        Screen_Width = round((int(input("Width of window ?")))/10)*10 #gets rounded to a multiple of 10 or 5
        Screen_Height = round((int(input("Height of window ?")))/10)*10 
        if Screen_Height < 100 or Screen_Width < 100:
            raise ValueTooLowError()
        elif Screen_Height > 800 or Screen_Width > 1280:
            raise ValueTooHighError()
        else:
            valid = True
    except ValueError:
        print('Error. Width and Height must be integers.')
    except (ValueTooLowError, ValueTooHighError) :
        print('Error. Width must be between 100 and 1280. Height must between 100 and 800.')
        
        

#Screen setup
size = (Screen_Width, Screen_Height)
screen = pygame.display.set_mode(size)
background = pygame.Surface(size)
background.fill(black)
manager = pygame_gui.UIManager(size)

#manager = pygame_gui.UIManager(size)
clock = pygame.time.Clock()

#sound effects
FLAG_play_sound = True # change to False to stop sound effects
sound_list = ['meow.wav','eeeyye.wav', 'male-voice.wav', 'mario-grabish.wav', 'me-saying.wav']
sound_1 = pygame.mixer.Sound(random.choice(sound_list))
sound_endgame = pygame.mixer.Sound('game_over_sound.wav')
sound_endgame_you_win = pygame.mixer.Sound('AND HIS NAME IS JOHN CENA.wav')


#position
x = round(((round(round(((round(Screen_Width/10)*10))//2)/10)*10))//2)*2 #start at the middle of the map
y = round(((round(round(((round(Screen_Height/10)*10))//2)/10)*10))//2)*2 # make sure to be at a multiple of 10 to be aligned with the food
delta_x = 0
delta_y = 0
event_count = 0

#score
points = 0


#food
food_list = [random.randrange(20, Screen_Width-20, 10), random.randrange(20, Screen_Height-20, 10) ] #quadrille le screen, ne PAS toucher sinon le mécanisme de manger ne fonctionnera plus
rotten_food = False
#print(food_list)

#position log
pos_log = [[x,y], [x-snake_size, y], [x-2*snake_size, y], [x-3*snake_size, y], [x-4*snake_size, y], [x-5*snake_size, y], [x-6*snake_size, y]]






#---------Functions-----------------

def high_score():
    """Save all scores to a JSON file."""
    try:
        with open('high_score.json', 'r') as file:
            data = json.load(file)
    except FileNotFoundError:
        data = {}

    data[pseudo] = points

    with open('high_score.json', 'w') as file:
        file.write(json.dumps(data, indent = 4))



def game_over():
    """Stops the game, display a message and close the game."""

        # 2nd parameter is size of the font
    font = pygame.font.Font('freesansbold.ttf', 32)


    #create a text surface object on which text is drawn on it.
    text = font.render('You lose', True, red, black)

    # create a rectangular object for the text surface object
    textRect = text.get_rect()

    # set the center of the rectangular object.
    textRect.center = (Screen_Width//2, Screen_Height//2)

    screen.blit(text, textRect)

    pygame.display.flip() #Update the full display Surface to the screen

    if FLAG_play_sound:
        if points > 500:
            sound_endgame_you_win.play()
        else:
            sound_endgame.play()
        pygame.time.wait(5000)
        sys.exit()
        
    else:
        pygame.time.wait(5000)
        sys.exit()
    
    
    



def score():
    """Display the score at all time on the screen."""

    # 2nd parameter is size of the font
    font = pygame.font.Font('freesansbold.ttf', 20)
    
    # create a text surface object on which text is drawn on it.
    text = font.render(str(points), True, white, black)


    # create a rectangular object for the text surface object
    textRect = text.get_rect()
    
    # set the center of the rectangular object.
    textRect.center = (Screen_Width//2, Screen_Height//20)
    screen.blit(text, textRect)




#---------Main_Loop-------------------




while True :
    time_delta = clock.tick(snake_speed)
    #print(food_list)
    # print(rotten_food)


    for event in pygame.event.get():  # event gestion
        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == pygame.KEYDOWN:
            event_count += 1
            if delta_y ==0 and (event.key == pygame.K_w or event.key == pygame.K_z or event.key == pygame.K_UP): #use the arrow keys or W, A, S, D to move
                delta_x = 0
                delta_y = -snake_size

            elif delta_y ==0 and (event.key == pygame.K_s or event.key == pygame.K_DOWN):
                delta_x = 0
                delta_y = snake_size
            
            elif delta_x == 0 and (event.key == pygame.K_a  or event.key == pygame.K_q or event.key == pygame.K_LEFT):
                delta_x = -snake_size
                delta_y = 0

            elif delta_x == 0 and (event.key == pygame.K_d or event.key == pygame.K_RIGHT):
                delta_x = snake_size
                delta_y = 0

    #if snake goes beyond its boundaries
            #indentation OUT of the FOR loop !!!
    if (delta_x + x) >= Screen_Width : # Right
        x = 0
    if (delta_x + x) <= 0 : # Left
        x = Screen_Width
    
    if (delta_y + y) >= Screen_Height:  # Down
        y = 0
    if (delta_y + y) <= 0 : # Up
        y = Screen_Height

    #movement
    x += delta_x
    y += delta_y


    #save position in list
    pos_log.insert(0, [x, y])

    if millis() - last_millis_food > 8000 and event_count > 3:
        rotten_food = True
        pygame.draw.rect(screen, red, [food_list[0], food_list[1], snake_size, snake_size])
        


    #if snake eats food
    if x == food_list[0] and y == food_list[1] :
        if not rotten_food:
            points += 100
            if FLAG_play_sound:
                if millis() - last_millis_sound > 5000:
                    sound_1.play()
                    sound_1 = pygame.mixer.Sound(random.choice(sound_list))
                    last_millis_sound = millis()

        #food_list.clear()
        food_list = [random.randrange(20, Screen_Width-20, 10), random.randrange(20, Screen_Height-20, 10)]
        rotten_food = False
        last_millis_food = millis()
    else :
        pos_log.pop() #if snake doesn't eat, pop last position to maintain correct snake length


    screen.fill(bg_color)

    for i in pos_log:
        pygame.draw.rect(screen, white, [i[0], i[1], snake_size, snake_size]) #draw the body of the snake

    if rotten_food:
        pygame.draw.rect(screen, red, [food_list[0], food_list[1], snake_size, snake_size]) #draw the food
    else:
        pygame.draw.rect(screen, food_color, [food_list[0], food_list[1], snake_size, snake_size]) #draw the food

    

    score()


    for i in pos_log[1:]:   #if snakes touches its body ===> game_over !
        if event_count > 3:
            if x == i[0] and y == i[1]: 
                high_score()
                game_over()

    

    # print('food: ', food_list)
    # print(x,':', y)
    # print(event_count)

    pygame.display.update()

    clock.tick(snake_speed)
    
    manager.process_events(event)   #permet à pygame_gui de recevoir les events
    manager.update(time_delta)

# pygame.quit()







#---------Documentation------------

# Pygame : https://www.geeksforgeeks.org/pygame-event-handling/
#          https://www.geeksforgeeks.org/pygame-time/
#          https://www.pygame.org/docs/ref/display.html
#          https://www.techwithtim.net/tutorials/game-development-with-python/pygame-tutorial/sound-effects-music/
#          https://opensource.com/article/20/9/add-sound-python-game

# Pygame_GUI : https://pygame-gui.readthedocs.io/en/latest/events.html#event-list

# Random : https://docs.python.org/3/library/random.html
#          https://datagy.io/python-random-element-from-list/

# Display text pygame : https://www.geeksforgeeks.org/python-display-text-to-pygame-window/

#JSON : https://www.programiz.com/python-programming/json