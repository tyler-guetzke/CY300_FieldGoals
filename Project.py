import pygame, math, os.path, sys
from pygame import mixer

pygame.init()
mixer.init()

#Functions to load necessary images and sounds
def load_image(file):
    image = pygame.image.load(file)
    image = image.convert()
    return image

def load_sound(soundfile):
    sound = pygame.mixer.Sound(soundfile)
    return sound

#Defining the classes
class Maketest(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.images = []
        img = load_image('yellowline.png')
        self.images.append(img)
        self.image = self.images[0]
        self.rect = self.image.get_rect()       
        self.rect.x = 615
        self.rect.y = 92

    def maketest(self,start,end,player,make_list):
        clipped_line = self.rect.clipline(start,end)
        if clipped_line:
            make = True
            score(player,make,make_list)
        else:
            make = False
            score(player,make,make_list)
    
class Distancemeter(pygame.sprite.Sprite):
    """moves a bar across the screen along the distance meter and when the space bar is clicked,
    the bar will stop and the distance will get saved for the football."""
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.images = []
        img = load_image('bar_horizontal.png')
        self.images.append(img)
        self.image = self.images[0]
        self.rect = self.image.get_rect()
        self.counter = 0
        self.isclicked = False
        self.ready = True
        self.distance = 0
    
    def update(self,lvl,reset,round_num):
        """moves or stops, depending on if space bar is pushed"""
        if self.isclicked == True and reset == None:
            self.clicked(round_num)
        else:
            self.unclicked(lvl)

    def move(self,lvl):
        """
        automate stick movement
        """
        if lvl == 1:
            distance = 43
            y = level_select(lvl)
        elif lvl == 2:
            distance = 30
            y = level_select(lvl)
        elif lvl == 3:
            distance = 20
            y = level_select(lvl)
        
        speed = y

        if self.counter >= 0 and self.counter <= distance:
                self.rect.y += speed
        elif self.counter >= distance and self.counter <= distance*2:
                self.rect.y -= speed
        else:
            self.counter = 0
        
        self.counter += 1

    def clicked(self,round_num):
        """saves the image and sends the distance to the Football"""
        if self.rect.y < 222 and self.rect.y >= 200:
            if round_num == 1 or round_num == 2:    
                self.distance = (85)
            if round_num == 3 or round_num == 4:
                self.distance = (110)
            if round_num == 5 or round_num == 6:
                self.distance = (135)
            if round_num == 7 or round_num == 8:
                self.distance = (160)
            if round_num == 9 or round_num == 10:
                self.distance = (185)
            if round_num == 11 or round_num == 12:
                self.distance = (210)
        elif self.rect.y < 242 and self.rect.y >= 222:
            if round_num == 1 or round_num == 2:    
                self.distance = (105)
            if round_num == 3 or round_num == 4:
                self.distance = (130)
            if round_num == 5 or round_num == 6:
                self.distance = (155)
            if round_num == 7 or round_num == 8:
                self.distance = (180)
            if round_num == 9 or round_num == 10:
                self.distance = (205)
            if round_num == 11 or round_num == 12:
                self.distance = (230)
        elif self.rect.y < 263 and self.rect.y >= 242:
            if round_num == 1 or round_num == 2:    
                self.distance = (125)
            if round_num == 3 or round_num == 4:
                self.distance = (150)
            if round_num == 5 or round_num == 6:
                self.distance = (175)
            if round_num == 7 or round_num == 8:
                self.distance = (200)
            if round_num == 9 or round_num == 10:
                self.distance = (225)
            if round_num == 11 or round_num == 12:
                self.distance = (250)
        elif self.rect.y < 281 and self.rect.y >= 263:
            if round_num == 1 or round_num == 2:    
                self.distance = (145)
            if round_num == 3 or round_num == 4:
                self.distance = (170)
            if round_num == 5 or round_num == 6:
                self.distance = (195)
            if round_num == 7 or round_num == 8:
                self.distance = (220)
            if round_num == 9 or round_num == 10:
                self.distance = (245)
            if round_num == 11 or round_num == 12:
                self.distance = (270)
        elif self.rect.y < 302 and self.rect.y >= 281:
            if round_num == 1 or round_num == 2:    
                self.distance = (165)
            if round_num == 3 or round_num == 4:
                self.distance = (190)
            if round_num == 5 or round_num == 6:
                self.distance = (215)
            if round_num == 7 or round_num == 8:
                self.distance = (240)
            if round_num == 9 or round_num == 10:
                self.distance = (265)
            if round_num == 11 or round_num == 12:
                self.distance = (290)
        elif self.rect.y < 322 and self.rect.y >= 302:
            if round_num == 1 or round_num == 2:    
                self.distance = (185)
            if round_num == 3 or round_num == 4:
                self.distance = (210)
            if round_num == 5 or round_num == 6:
                self.distance = (235)
            if round_num == 7 or round_num == 8:
                self.distance = (260)
            if round_num == 9 or round_num == 10:
                self.distance = (285)
            if round_num == 11 or round_num == 12:
                self.distance = (310)
        elif self.rect.y < 342 and self.rect.y >= 322:
            if round_num == 1 or round_num == 2:    
                self.distance = (165)
            if round_num == 3 or round_num == 4:
                self.distance = (190)
            if round_num == 5 or round_num == 6:
                self.distance = (215)
            if round_num == 7 or round_num == 8:
                self.distance = (240)
            if round_num == 9 or round_num == 10:
                self.distance = (265)
            if round_num == 11 or round_num == 12:
                self.distance = (290)
        elif self.rect.y < 362 and self.rect.y >= 342:
            if round_num == 1 or round_num == 2:    
                self.distance = (145)
            if round_num == 3 or round_num == 4:
                self.distance = (170)
            if round_num == 5 or round_num == 6:
                self.distance = (195)
            if round_num == 7 or round_num == 8:
                self.distance = (220)
            if round_num == 9 or round_num == 10:
                self.distance = (245)
            if round_num == 11 or round_num == 12:
                self.distance = (270)
        elif self.rect.y < 382 and self.rect.y >= 362:
            if round_num == 1 or round_num == 2:    
                self.distance = (125)
            if round_num == 3 or round_num == 4:
                self.distance = (150)
            if round_num == 5 or round_num == 6:
                self.distance = (175)
            if round_num == 7 or round_num == 8:
                self.distance = (200)
            if round_num == 9 or round_num == 10:
                self.distance = (225)
            if round_num == 11 or round_num == 12:
                self.distance = (250)
        elif self.rect.y < 405 and self.rect.y >= 382:
            if round_num == 1 or round_num == 2:    
                self.distance = (105)
            if round_num == 3 or round_num == 4:
                self.distance = (130)
            if round_num == 5 or round_num == 6:
                self.distance = (155)
            if round_num == 7 or round_num == 8:
                self.distance = (180)
            if round_num == 9 or round_num == 10:
                self.distance = (205)
            if round_num == 11 or round_num == 12:
                self.distance = (230)
        elif self.rect.y < 427 and self.rect.y >= 405:
            if round_num == 1 or round_num == 2:    
                self.distance = (85)
            if round_num == 3 or round_num == 4:
                self.distance = (110)
            if round_num == 5 or round_num == 6:
                self.distance = (135)
            if round_num == 7 or round_num == 8:
                self.distance = (160)
            if round_num == 9 or round_num == 10:
                self.distance = (185)
            if round_num == 11 or round_num == 12:
                self.distance = (210)
        return self.distance
    
    def unclicked(self,lvl):
        """moves the bar on the meter until the space bar is hit"""
        self.move(lvl)        
        
class Directionmeter(pygame.sprite.Sprite):
    """moves a bar across the screen along the direction meter and when the space bar is clicked,
    the bar will stop and the direction will get saved for the football."""
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.images = []
        img = load_image('bar_vertical.png')
        self.images.append(img)
        self.image = self.images[0]
        self.rect = self.image.get_rect()
        self.counter = 0 
        self.isclicked = False
        self.ready = False
    
    def update(self,lvl,reset):
        """moves or stops, depending on if space bar is pushed"""   
        if self.isclicked == True and reset == None:
            self.clicked(self)
        else:
            self.unclicked(lvl)

    def move(self,lvl):
        """automate stick movement"""
        if lvl == 1:
            distance = 43
            x = level_select(lvl)
        elif lvl == 2:
            distance = 30
            x = level_select(lvl)
        elif lvl == 3:
            distance = 20
            x = level_select(lvl)
       
        speed = x

        if self.counter >= 0 and self.counter <= distance:
                self.rect.x += speed
        elif self.counter >= distance and self.counter <= distance*2:
                self.rect.x -= speed
        else:
            self.counter = 0
        
        self.counter += 1

    def clicked(self):
        """saves the image and sends the direction to the Football"""
        if self.rect.x < 545 and self.rect.x >= 525:
            self.angle = (120) 
        elif self.rect.x < 568 and self.rect.x >= 545:
            self.angle = (110)
        elif self.rect.x < 588 and self.rect.x >= 568:
            self.angle = (100)
        elif self.rect.x < 608 and self.rect.x >= 588:
            self.angle = (95)
        elif self.rect.x < 628 and self.rect.x >= 608:
            self.angle = (92.5)
        elif self.rect.x < 648 and self.rect.x >= 628:
            self.angle = (90)
        elif self.rect.x < 668 and self.rect.x >= 648:
            self.angle = (87.5)
        elif self.rect.x < 687 and self.rect.x >= 668:
            self.angle = (85)
        elif self.rect.x < 708 and self.rect.x >= 687:
            self.angle = (75)
        elif self.rect.x < 728 and self.rect.x >= 708:
            self.angle = (65)
        elif self.rect.x < 750 and self.rect.x >= 728:
            self.angle = (55)       
        return self.angle

    def unclicked(self,lvl):
        """moves the bar on the meter until the space bar is hit"""
        self.move(lvl) 

class Kick(pygame.sprite.Sprite):
    """Creates the football that will be kicked across the screen"""
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        
    def update(self,x,angle,round_num):
        """move the football based on the inputs from the kick meter"""
        if round_num <= 13: 
            pygame.draw.line(screen, (0,0,0), self.calcstartpos(round_num), self.calcnewpos(x,angle,round_num), 3) 
        return self.calcnewpos(x,angle,round_num)
    
    def calcnewpos(self,x,angle,round_num):
        if round_num == 1 or round_num == 2:    
            if angle < 90:
                (dx,dy) = (635+(x*math.cos(math.pi/180*angle))),(192-(x*math.sin(math.pi/180*angle)))
                vector = (dx,dy)
            else:
                (dx,dy) = (635-(x*math.cos(math.pi/180*(180-angle)))),(192-(x*math.sin(math.pi/180*(180-angle))))
                vector = (dx,dy)
            return vector
        elif round_num == 3 or round_num == 4:    
            if angle < 90:
                (dx,dy) = (635+(x*math.cos(math.pi/180*angle))),(216-(x*math.sin(math.pi/180*angle)))
                vector = (dx,dy)
            else:
                (dx,dy) = (635-(x*math.cos(math.pi/180*(180-angle)))),(216-(x*math.sin(math.pi/180*(180-angle))))
                vector = (dx,dy)
            return vector
        elif round_num == 5 or round_num == 6:    
            if angle < 90:
                (dx,dy) = (635+(x*math.cos(math.pi/180*angle))),(244-(x*math.sin(math.pi/180*angle)))
                vector = (dx,dy)
            else:
                (dx,dy) = (635-(x*math.cos(math.pi/180*(180-angle)))),(244-(x*math.sin(math.pi/180*(180-angle))))
                vector = (dx,dy)
            return vector
        elif round_num == 7 or round_num == 8:    
            if angle < 90:
                (dx,dy) = (635+(x*math.cos(math.pi/180*angle))),(298-(x*math.sin(math.pi/180*angle)))
                vector = (dx,dy)
            else:
                (dx,dy) = (635-(x*math.cos(math.pi/180*(180-angle)))),(298-(x*math.sin(math.pi/180*(180-angle))))
                vector = (dx,dy)
            return vector
        elif round_num == 9 or round_num == 10:    
            if angle < 90:
                (dx,dy) = (635+(x*math.cos(math.pi/180*angle))),(350-(x*math.sin(math.pi/180*angle)))
                vector = (dx,dy)
            else:
                (dx,dy) = (635-(x*math.cos(math.pi/180*(180-angle)))),(350-(x*math.sin(math.pi/180*(180-angle))))
                vector = (dx,dy)
            return vector
        if round_num == 11 or round_num == 12:    
            if angle < 90:
                (dx,dy) = (635+(x*math.cos(math.pi/180*angle))),(398-(x*math.sin(math.pi/180*angle)))
                vector = (dx,dy)
            else:
                (dx,dy) = (635-(x*math.cos(math.pi/180*(180-angle)))),(398-(x*math.sin(math.pi/180*(180-angle))))
                vector = (dx,dy)
            return vector
    
    def calcstartpos(self,round_num):
        if round_num == 1 or round_num == 2:
            startpos = ((635,192))
            return startpos
        elif round_num == 3 or round_num == 4:
            startpos = ((635,216))
            return startpos
        elif round_num == 5 or round_num == 6:
            startpos = ((635,244))
            return startpos
        elif round_num == 7 or round_num == 8:
            startpos = ((635,298))
            return startpos
        elif round_num == 9 or round_num == 10:
            startpos = ((635,350))
            return startpos
        elif round_num == 11 or round_num == 12:
            startpos = ((635,398))
            return startpos
        else:
            startpos = ((635,200))
            return startpos

'''SET UP SECTION'''
size = width, height = 1275, 650
fps = 100 # frame rate

screen = pygame.display.set_mode(size)
pygame.display.set_caption('Field Goals')
clock = pygame.time.Clock()

horizontal_meter = load_image('meter_horizontal.png')
horizontal_meter_rect = ((525,550))
vertical_meter = load_image('meter_vertical.png')
vertical_meter_rect = ((900,200))

distance_meter = Distancemeter()
distance_meter.rect.x = 900 
distance_meter.rect.y = 200 
distance_meter_list = pygame.sprite.Group()
distance_meter_list.add(distance_meter)
distance_reset = False

direction_meter = Directionmeter()   
direction_meter.rect.x = 525
direction_meter.rect.y = 549
direction_meter_list = pygame.sprite.Group()
direction_meter_list.add(direction_meter)
direction_reset = False

maketester = Maketest()
maketester_list = pygame.sprite.Group()
maketester_list.add(maketester)

fieldgoal = Kick()

sound1 = load_sound("game_intro.mp3")
sound2 = load_sound("game_playing.mp3")
sound_cheer = load_sound("applause.mp3")
sound_boo = load_sound("crowdaw.mp3")

'''OTHER FUNCTIONS'''

#WINNING AND LOSING
def score(player,make,make_list):
    if player == 1 and make == True:
        make_list.append(1)
    elif player == 1 and make == False:
        make_list.append(0)
    if player == 2 and make == True:
        make_list.append(1)
    elif player == 2 and make == False:
        make_list.append(0)
    return make_list

def score_total(make_list):
    player1_score = 0
    player2_score = 0
    for i in range(0,len(make_list),2):
        if make_list[i] == 1:
            player1_score += 1
    for i in range(1,len(make_list),2):
        if make_list[i] == 1:
            player2_score += 1
    return player1_score, player2_score

#Reseting the meters
def reset(lvl,round_num):
    distance_meter = Distancemeter()  # spawn player
    distance_meter.rect.x = 900   # go to x
    distance_meter.rect.y = 200   # go to y
    distance_meter_list = pygame.sprite.Group()
    distance_meter_list.add(distance_meter)
    direction_meter = Directionmeter()  # spawn player
    direction_meter.rect.x = 525   # go to x
    direction_meter.rect.y = 549   # go to y
    direction_meter_list = pygame.sprite.Group()
    direction_meter_list.add(direction_meter)
    reset = True
    distance_meter.update(lvl,reset,round_num)
    direction_meter.update(lvl,reset)

def level_select(lvl):
    if lvl == 1:
        barspeed = 5
    if lvl == 2:
        barspeed = 7
    if lvl == 3:
        barspeed = 10
    return barspeed

#Probability of making the kick based on previous attempts
def probability(file,makelist,round_num,players):
    file_exists = os.path.exists('probability.txt')   
    if file_exists == True:
        with open(file,"r") as totalscore:
            probability_list = totalscore.read().split('/')
            if players == 2:
                total_makes = int(probability_list[0]) + makelist[round_num-2]
                total_kicks = int(probability_list[1]) + 1
                with open(file,"w") as totalscore:
                    totalscore.write(str(total_makes) + "/" + str(total_kicks))
                    totalscore.close()
                return total_makes, total_kicks
            elif players == 1 and makelist[len(makelist)-1] != 2:
                total_makes = int(probability_list[0]) + makelist[len(makelist)-1]
                total_kicks = int(probability_list[1]) + 1
                with open(file,"w") as totalscore:
                    totalscore.write(str(total_makes) + "/" + str(total_kicks))
                    totalscore.close()
                return total_makes, total_kicks
            else:
                total_makes = 0
                total_kicks = 0
                return total_kicks, total_kicks
    if file_exists == False: 
        with open(file,"w") as totalscore:
                totalscore.write(str(0) + "/" + str(0))
        total_makes = 0
        total_kicks = 0
        return total_makes, total_kicks 

#Button and title
def text_objects(text, font,darkmode):
    if darkmode == False:    
        textSurface = font.render(text, True, (0,0,0))
    else:
        textSurface = font.render(text, True, (255,255,255))
    return textSurface, textSurface.get_rect()

def button(msg,x,y,w,h,ic,ac,darkmode=False,action=None,sound=False,players=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(screen, ac,(x,y,w,h))
        if click[0] == 1 and action != None:
            if action == 'player_select':
                game_player_select(darkmode,sound)
            elif action == 'settings':
                game_settingmenu(darkmode)
            elif action == 'darkmodeon':
                darkmode = True
                game_sound_settingmenu(darkmode)
            elif action == 'darkmodeoff':
                darkmode = False
                game_sound_settingmenu(darkmode)
            elif action == 'soundon':
                sound = True
                if sound == True:
                    sound1.stop()
                    sound2.stop()
                game_intro(darkmode,sound)
            elif action == 'soundoff':
                sound = False
                if sound == False:
                    sound1.stop()
                    sound2.stop()
                game_intro(darkmode,sound)
            elif action == '1player_game':
                players = 1
                game_level_select(players,darkmode,sound)
            elif action == '2player_game':
                players = 2
                game_level_select(players,darkmode,sound)
            elif action == 'easy':
                if sound == True:
                    sound1.stop()
                    sound2.play()
                if sound == False:
                    sound1.stop()
                    sound2.stop()
                lvl = 1
                player = 1
                round_num = 0
                if players == 2:    
                    make_list = []
                if players == 1:
                    make_list = [2]
                reset(lvl,round_num)
                main_game(player,lvl,round_num,make_list,players,darkmode,sound)
                return lvl, player, round_num
            elif action == 'medium':
                if sound == True:
                    sound1.stop()
                    sound2.play()
                if sound == False:
                    sound1.stop()
                    sound2.stop()
                lvl = 2
                player = 1
                round_num = 0
                if players == 2:    
                    make_list = []
                if players == 1:
                    make_list = [2]
                reset(lvl,round_num)
                main_game(player,lvl,round_num,make_list,players,darkmode,sound)
                return lvl, player, round_num
            elif action == 'hard':
                if sound == True:
                    sound1.stop()
                    sound2.play()
                if sound == False:
                    sound1.stop()
                    sound2.stop()
                lvl = 3
                player = 1
                round_num = 0
                if players == 2:    
                    make_list = []
                if players == 1:
                    make_list = [2]
                reset(lvl,round_num)
                main_game(player,lvl,round_num,make_list,players,darkmode,sound)
                return lvl, player, round_num
            elif action == 'back_to_start':
                if sound == True:
                    sound2.stop()
                if sound == False:
                    sound1.stop()
                    sound2.stop()
                game_intro(darkmode,sound)
            elif action == 'quit':
                pygame.quit
                quit()
    else:
        pygame.draw.rect(screen,ic,(x,y,w,h))

    smallText = pygame.font.Font("freesansbold.ttf",20)
    textSurf, textRect = text_objects(msg, smallText,darkmode)
    textRect.center = ((x+(w/2)),(y+(h/2)))
    screen.blit(textSurf, textRect)

#GAME CODE

#Creates the intro screen
def game_intro(darkmode=False,sound=False):

    intro = True
    if sound == True:
        sound1.play() 
    if sound == False:
        sound1.stop()
        sound2.stop()

    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        if darkmode == False:
            screen.fill((255,255,255))
        else:
            screen.fill((0,0,0))
        largeText = pygame.font.Font('freesansbold.ttf',60)
        TextSurf, TextRect = text_objects("Welcome to Field Goals!", largeText,darkmode)
        TextRect.center = ((width/2),(height/4))
        screen.blit(TextSurf, TextRect)

        button('Start',(width/2)-50,450,100,50,(0,250,0),(0,230,0),darkmode,'player_select',sound)
       
        button('Settings',(width-190),50,150,50,(250,0,0),(230,0,0),darkmode,'settings',sound)

        pygame.display.update()
        clock.tick(15)

#Creates the help menu
def game_settingmenu(darkmode):

    settings_menu = True

    while settings_menu:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        
        if darkmode == False:
            screen.fill((255,255,255))
        else:
            screen.fill((0,0,0))
        largeText = pygame.font.Font('freesansbold.ttf',60)
        TextSurf, TextRect = text_objects("Darkmode:", largeText,darkmode)
        TextRect.center = ((width/2),(height/4))
        screen.blit(TextSurf, TextRect)
        
        button('On',(width/4)+110,(height/2)+50,150,50,(250,0,0),(230,0,0),darkmode,'darkmodeon')

        button('Off',(width-width/4)-260,(height/2)+50,150,50,(250,0,0),(230,0,0),darkmode,'darkmodeoff')

        pygame.display.update()
        clock.tick(15)

def game_sound_settingmenu(darkmode):

    sound_settings_menu = True

    while sound_settings_menu:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        
        if darkmode == False:
            screen.fill((255,255,255))
        else:
            screen.fill((0,0,0))
        largeText = pygame.font.Font('freesansbold.ttf',60)
        TextSurf, TextRect = text_objects("Sound:", largeText,darkmode)
        TextRect.center = ((width/2),(height/4))
        screen.blit(TextSurf, TextRect)
        
        button('On',(width/4)+110,(height/2),150,50,(250,0,0),(230,0,0),darkmode,'soundon')

        button('Off',(width-width/4)-260,(height/2),150,50,(250,0,0),(230,0,0),darkmode,'soundoff')

        pygame.display.update()
        clock.tick(15)

def game_player_select(darkmode,sound):

    players_select_menu = True

    while players_select_menu:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        if darkmode == False:
            screen.fill((255,255,255))
        else:
            screen.fill((0,0,0))
        largeText = pygame.font.Font('freesansbold.ttf',60)
        TextSurf, TextRect = text_objects("Choose how many players:", largeText,darkmode)
        TextRect.center = ((width/2),(height/4))
        screen.blit(TextSurf, TextRect)

        button('One Player',(width/4)+110,(height/2)-50,150,50,(250,0,0),(230,0,0),darkmode,'1player_game',sound)

        button('Two Players',(width-width/4)-260,(height/2)-50,150,50,(250,0,0),(230,0,0),darkmode,'2player_game',sound)
        
        pygame.display.update()
        clock.tick(15)

#Creates the level select menu
def game_level_select(players,darkmode,sound):

    level_select = True

    while level_select:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
    
        if darkmode == False:
            screen.fill((255,255,255))
        else:
            screen.fill((0,0,0))
        largeText = pygame.font.Font('freesansbold.ttf',60)
        TextSurf, TextRect = text_objects("Choose a difficulty:", largeText,darkmode)
        TextRect.center = ((width/2),(height/4))
        screen.blit(TextSurf, TextRect)
        
        button('Easy',((width/4)-50)+75,400,100,50,(0,250,0),(0,230,0),darkmode,'easy',sound,players)
        
        button('Medium',(width/2)-50,400,100,50,(250,0,0),(230,0,0),darkmode,'medium',sound,players)

        button('Hard',((width-(width/4))-50)-75,400,100,50,(0,0,250),(0,0,230),darkmode,'hard',sound,players)
        
        pygame.display.update()
        clock.tick(15)

#Creates the main game
def main_game(player,lvl,round_num,make_list,players,darkmode,sound):

    reset(lvl,round_num)
    
    sound_cheer.stop()
    sound_boo.stop()
    
    if players == 2:    
        round_num += 1
    
    if players == 1:    
        total_makes, total_kicks = probability('probability.txt',make_list,round_num,players)
        if total_kicks != 0:    
            probability1 = float(total_makes)/float(total_kicks)
            probability1 = round(probability1,2)
        else:
            probability1 = 0
        
    if players == 2:    
        if round_num >= 2:    
            total_makes, total_kicks = probability('probability.txt',make_list,round_num,players)
            if total_kicks != 0:    
                probability1 = float(total_makes)/float(total_kicks)
                probability1 = round(probability1,2)
        elif round_num == 1:
            probability1 = 0
    
    makestring = ''
    for i in make_list:
        makestring += str(i)

    if player == 1 and round_num <= 12 and players == 2:
        game_player1(player,lvl,round_num,make_list,probability1,players,darkmode,sound)
    elif player == 2 and round_num <= 12 and players == 2:
        game_player2(player,lvl,round_num,make_list,probability1,players,darkmode,sound)
    elif players == 1 and makestring.find('0') == -1:
        round_num = 8
        game_single_player(player,lvl,round_num,make_list,probability1,players,darkmode,sound)
    elif players == 1 and makestring.find('0') != -1: 
        game_over(make_list,players,darkmode,sound)

#Creates the player1 instance of the main game
def game_player1(player,lvl,round_num,make_list,probability1,players,darkmode,sound):
    ready = True
    game_distance(player,lvl,ready,round_num,make_list,probability1,players,darkmode,sound)

#Creates the player2 instance of the main game
def game_player2(player,lvl,round_num,make_list,probability1,players,darkmode,sound):
    ready = True
    game_distance(player,lvl,ready,round_num,make_list,probability1,players,darkmode,sound)

#Creates single player instance
def game_single_player(player,lvl,round_num,make_list,probability1,players,darkmode,sound):
    ready = True
    game_distance(player,lvl,ready,round_num,make_list,probability1,players,darkmode,sound)

#Creates the movement of the distance meter
def game_distance(player,lvl,ready,round_num,make_list,probability1,players,darkmode,sound):

    distance =True
    distance_meter.rect.x = 900
    distance_meter.rect.y = 200
    distance_meter.counter = 0
    distance_meter.ready = ready
    
    while distance:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                try:
                    sys.exit()
                finally:
                    distance = False

            if event.type == pygame.KEYDOWN and distance_meter.ready == True:
                if event.key == pygame.K_SPACE:
                    distance_meter.move(lvl)
                    distance_meter.isclicked = True
                    direction_meter.ready = True
                    distance = False
                    game_direction(player,lvl,direction_meter.ready,round_num,make_list,probability1,players,darkmode,sound)
                    
                if event.key == ord('q'):
                    pygame.quit()
                    sys.exit()   
        
        if darkmode == False:
            screen.fill((255,255,255))
        else:
            screen.fill((0,0,0))
        screen.blit(horizontal_meter,horizontal_meter_rect)
        screen.blit(vertical_meter,vertical_meter_rect)
        screen.blit(load_image('field.png'), (415,65))
        distance_meter_list.draw(screen) # draw distance player
        maketester_list.draw(screen)
        reset = False

        player1_score, player2_score = score_total(make_list)
        total_score = player1_score + player2_score

        if players == 1:    
            screen.blit(load_image('scoreboard_singleplayer.png'), (100,65))

            largeText = pygame.font.Font('freesansbold.ttf',20)
            TextSurf, TextRect = text_objects(str(total_score), largeText,False)
            TextRect.center = ((169),(120))
            screen.blit(TextSurf, TextRect)

            if probability1 != 0:
                largeText = pygame.font.Font('freesansbold.ttf',15)
                TextSurf, TextRect = text_objects('You have a '+ str(probability1) +' chance of making the kick', largeText,darkmode)
                TextRect.center = ((200),(320))
                screen.blit(TextSurf, TextRect)
            
            distance_meter.update(lvl,reset,6)

        if players == 2:
            screen.blit(load_image('scoreboard_main.png'), (100,65))

            largeText = pygame.font.Font('freesansbold.ttf',20)
            TextSurf, TextRect = text_objects('Player ' + str(player) +'\'s turn', largeText,darkmode)
            TextRect.center = ((1100),(300))
            screen.blit(TextSurf, TextRect)
            
            if round_num %2 != 0:
                round = (round_num/2)+.5
            else:
                round = round_num/2

            largeText = pygame.font.Font('freesansbold.ttf',20)
            TextSurf, TextRect = text_objects('Round: ' + str(int(round)), largeText,darkmode)
            TextRect.center = ((1100),(325))
            screen.blit(TextSurf, TextRect)

            largeText = pygame.font.Font('freesansbold.ttf',20)
            TextSurf, TextRect = text_objects(str(player1_score), largeText,False)
            TextRect.center = ((157),(120))
            screen.blit(TextSurf, TextRect)

            largeText = pygame.font.Font('freesansbold.ttf',20)
            TextSurf, TextRect = text_objects(str(player2_score), largeText,False)
            TextRect.center = ((270),(120))
            screen.blit(TextSurf, TextRect)

            if probability1 != 0:
                largeText = pygame.font.Font('freesansbold.ttf',15)
                TextSurf, TextRect = text_objects('You have a '+ str(probability1) +' chance of making the kick', largeText,darkmode)
                TextRect.center = ((200),(320))
                screen.blit(TextSurf, TextRect)
            
            distance_meter.update(lvl,reset,round_num)

        button('Quit',(width-190),50,150,50,(250,0,0),(230,0,0),darkmode,'quit',sound)

        pygame.display.flip()
        clock.tick(fps)

#Creates the movement of the direction meter
def game_direction(player,lvl,ready,round_num,make_list,probability1,players,darkmode,sound):

    direction = True
    direction_meter.rect.x = 525
    direction_meter.rect.y = 549
    direction_meter.counter = 0
    direction_meter.ready = ready
    
    while direction: 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                try:
                    sys.exit()
                finally:
                    direction = False
            
            if event.type == pygame.KEYDOWN and direction_meter.ready == True:
                if event.key == pygame.K_SPACE:
                    direction_meter.move(lvl)
                    direction_meter.isclicked = True
                    direction = False
                    if players == 1:    
                        maketester.maketest(fieldgoal.calcstartpos(7),fieldgoal.calcnewpos(distance_meter.clicked(7),direction_meter.clicked(),round_num),player,make_list)
                    if players == 2:
                        maketester.maketest(fieldgoal.calcstartpos(round_num),fieldgoal.calcnewpos(distance_meter.clicked(round_num),direction_meter.clicked(),round_num),player,make_list)
                    game_kick(player,lvl,round_num,make_list,players,darkmode,sound)
                if event.key == ord('q'):
                    pygame.quit()
                    sys.exit()  

        if darkmode == False:
            screen.fill((255,255,255))
        else:
            screen.fill((0,0,0))
        screen.blit(horizontal_meter,horizontal_meter_rect)
        screen.blit(vertical_meter,vertical_meter_rect)
        screen.blit(load_image('field.png'), (415,65))
        distance_meter_list.draw(screen) # draw distance player
        direction_meter_list.draw(screen) # draw direction player
        maketester_list.draw(screen)
        reset = False
        direction_meter.update(lvl,reset)

        player1_score, player2_score = score_total(make_list)
        total_score = player1_score + player2_score

        if players == 1:
            screen.blit(load_image('scoreboard_singleplayer.png'), (100,65))

            largeText = pygame.font.Font('freesansbold.ttf',20)
            TextSurf, TextRect = text_objects(str(total_score), largeText,False)
            TextRect.center = ((169),(120))
            screen.blit(TextSurf, TextRect)
            
            if probability1 != 0:
                largeText = pygame.font.Font('freesansbold.ttf',15)
                TextSurf, TextRect = text_objects('You have a '+ str(probability1) +' chance of making the kick', largeText,darkmode)
                TextRect.center = ((200),(320))
                screen.blit(TextSurf, TextRect)

        if players == 2:
            screen.blit(load_image('scoreboard_main.png'), (100,65))
            
            largeText = pygame.font.Font('freesansbold.ttf',20)
            TextSurf, TextRect = text_objects('Player ' + str(player) +'\'s turn', largeText,darkmode)
            TextRect.center = ((1100),(300))
            screen.blit(TextSurf, TextRect)
            
            if round_num %2 != 0:
                round = (round_num/2)+.5
            else:
                round = round_num/2

            largeText = pygame.font.Font('freesansbold.ttf',20)
            TextSurf, TextRect = text_objects('Round: ' + str(int(round)), largeText,darkmode)
            TextRect.center = ((1100),(325))
            screen.blit(TextSurf, TextRect)

            largeText = pygame.font.Font('freesansbold.ttf',20)
            TextSurf, TextRect = text_objects(str(player1_score), largeText,False)
            TextRect.center = ((157),(120))
            screen.blit(TextSurf, TextRect)

            largeText = pygame.font.Font('freesansbold.ttf',20)
            TextSurf, TextRect = text_objects(str(player2_score), largeText,False)
            TextRect.center = ((270),(120))
            screen.blit(TextSurf, TextRect)

            if probability1 != 0:
                largeText = pygame.font.Font('freesansbold.ttf',15)
                TextSurf, TextRect = text_objects('You have a '+ str(probability1) +' chance of making the kick', largeText,darkmode)
                TextRect.center = ((200),(320))
                screen.blit(TextSurf, TextRect)

        button('Quit',(width-190),50,150,50,(250,0,0),(230,0,0),darkmode,'quit',sound)

        pygame.display.flip()
        clock.tick(fps)

#Creates the kicked screen
def game_kick(player,lvl,round_num,make_list,players,darkmode,sound):
    
    kick = True

    if sound == True:
        if players == 2:
            if make_list[round_num-1] == 1:
                sound_cheer.play()
            else:
                sound_boo.play()
        else:
            if make_list[len(make_list)-1] == 1:
                sound_cheer.play()
            else:
                sound_boo.play()

    while kick: 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                try:
                    sys.exit()
                finally:
                    kick = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    kick = False
                    if players == 2:
                        player1_score, player2_score = score_total(make_list)
                        if round_num < 10:
                            if player == 1:
                                player = 2
                                sound_cheer.stop()
                                sound_boo.stop()
                                kick = False
                                main_game(player,lvl,round_num,make_list,players,darkmode,sound)
                            elif player == 2:
                                player = 1
                                sound_cheer.stop()
                                sound_boo.stop()
                                kick = False
                                main_game(player,lvl,round_num,make_list,players,darkmode,sound)
                        elif round_num == 10 and player1_score == player2_score:
                            if player == 1:
                                player = 2
                                sound_cheer.stop()
                                sound_boo.stop()
                                kick = False
                                main_game(player,lvl,round_num,make_list,players,darkmode,sound)
                            elif player == 2:
                                player = 1
                                sound_cheer.stop()
                                sound_boo.stop()
                                kick = False
                                main_game(player,lvl,round_num,make_list,players,darkmode,sound)
                        elif round_num == 11:
                            if player == 1:
                                player = 2
                                sound_cheer.stop()
                                sound_boo.stop()
                                kick = False
                                main_game(player,lvl,round_num,make_list,players,darkmode,sound)
                            elif player == 2:
                                player = 1
                                sound_cheer.stop()
                                sound_boo.stop()
                                kick = False
                                main_game(player,lvl,round_num,make_list,players,darkmode,sound)
                        else:
                            sound_cheer.stop()
                            sound_boo.stop()    
                            kick = False
                            game_over(make_list,players,darkmode,sound)
                    if players == 1:
                        main_game(player,lvl,round_num,make_list,players,darkmode,sound)
                if event.key == ord('q'):
                    pygame.quit()
                    sys.exit() 

        if darkmode == False:
            screen.fill((255,255,255))
        else:
            screen.fill((0,0,0))
        screen.blit(horizontal_meter,horizontal_meter_rect)
        screen.blit(vertical_meter,vertical_meter_rect)
        screen.blit(load_image('field.png'), (415,65))
        distance_meter_list.draw(screen) # draw distance player
        direction_meter_list.draw(screen) # draw direction player
        maketester_list.draw(screen) # draws the hitbox
        fieldgoal.update(distance_meter.clicked(round_num),direction_meter.clicked(),round_num)

        player1_score, player2_score = score_total(make_list)
        total_score = player1_score + player2_score

        if players == 1:
            screen.blit(load_image('scoreboard_singleplayer.png'), (100,65))

            largeText = pygame.font.Font('freesansbold.ttf',20)
            TextSurf, TextRect = text_objects(str(total_score), largeText, False)
            TextRect.center = ((169),(120))
            screen.blit(TextSurf, TextRect)

        if players == 2:
            screen.blit(load_image('scoreboard_main.png'), (100,65))

            largeText = pygame.font.Font('freesansbold.ttf',20)
            TextSurf, TextRect = text_objects(str(player1_score), largeText,False)
            TextRect.center = ((157),(120))
            screen.blit(TextSurf, TextRect)

            largeText = pygame.font.Font('freesansbold.ttf',20)
            TextSurf, TextRect = text_objects(str(player2_score), largeText,False)
            TextRect.center = ((270),(120))
            screen.blit(TextSurf, TextRect)

        button('Quit',(width-190),50,150,50,(250,0,0),(230,0,0),darkmode,'quit',sound)

        button('Back to Start',(width-390),50,150,50,(0,250,0),(0,230,0),darkmode,'back_to_start',sound)

        pygame.display.flip()
        clock.tick(fps)

#Creates the end screen
def game_over(make_list,players,darkmode,sound):
    
    game_over = True
    
    while game_over == True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                try:
                    sys.exit()
                finally:
                    game_over = False
        
        if darkmode == False:
            screen.fill((255,255,255))
        else:
            screen.fill((0,0,0))         

        player1_score, player2_score = score_total(make_list)
        total_score = player1_score + player2_score 

        if players == 1:
            screen.blit(load_image('scoreboard_singleplayer.png'), ((width/2)-68,65))

            largeText = pygame.font.Font('freesansbold.ttf',20)
            TextSurf, TextRect = text_objects(str(total_score), largeText,False)
            TextRect.center = ((width/2),(120))
            screen.blit(TextSurf, TextRect)

        if players == 2:
            screen.blit(load_image('scoreboard_main.png'), ((width/2)-111,65))

            largeText = pygame.font.Font('freesansbold.ttf',20)
            TextSurf, TextRect = text_objects(str(player1_score), largeText,False)
            TextRect.center = ((582),(120))
            screen.blit(TextSurf, TextRect)

            largeText = pygame.font.Font('freesansbold.ttf',20)
            TextSurf, TextRect = text_objects(str(player2_score), largeText,False)
            TextRect.center = ((697),(120))
            screen.blit(TextSurf, TextRect)

            if player1_score > player2_score:
                largeText = pygame.font.Font('freesansbold.ttf',20)
                TextSurf, TextRect = text_objects('The winner is player 1!', largeText,darkmode)
                TextRect.center = ((width/2),(height/2))
                screen.blit(TextSurf, TextRect)            
            elif player1_score < player2_score:
                largeText = pygame.font.Font('freesansbold.ttf',20)
                TextSurf, TextRect = text_objects('The winner is player 2!', largeText,darkmode)
                TextRect.center = ((width/2),(height/2))
                screen.blit(TextSurf, TextRect)
            else:
                largeText = pygame.font.Font('freesansbold.ttf',20)
                TextSurf, TextRect = text_objects('The game is a tie!', largeText,darkmode)
                TextRect.center = ((width/2),(height/2))
                screen.blit(TextSurf, TextRect)

        button('Quit',(width-190),50,150,50,(250,0,0),(230,0,0),darkmode,'quit',sound)

        button('Back to Start',(width-390),50,150,50,(0,250,0),(0,230,0),darkmode,'back_to_start',sound)

        pygame.display.flip()
        clock.tick(fps)

'''RUNNING THE GAME AND EVENTS'''
game_intro()

pgzrun.go()
