#! /usr/bin/python3.5
import pygame, time, glob, sys, os
from random import randint, choice
from PIL import ImageDraw, Image

''' I don't normally go mad on commenting but I thought I would so you can understand whats going on and
you can modify it to make your own.

Please check readMe.txt file on how to use.'''

pygame.init()
pygame.mixer.init()

##### Screen size selection, please check the next 9 lines. #####
# Sets screen window size.
width = 800
height = 600
screen = pygame.display.set_mode((width, height))

# This section will make it fullscreen 
##screenSizes = pygame.display.list_modes() # Gets your display resolution
##width, height = screenSizes[0] # Selects your biggest display but will use it in a window
##screen = pygame.display.set_mode((width, height), pygame.FULLSCREEN) # Makes the pygame run fullscreen no window

pygame.display.set_caption('Fireworks') # Window title
clock = pygame.time.Clock()
fps = 60 # Frames per second

# RGB variables for rocket etc.
white = (255, 255, 255)
yellow = (255, 255, 0)
black = (0, 0, 0)

stopDisplay = 10 # How many fireworks to be used, if missing any check in kaBoom function.
rocketSize = 3 # Pixel size of rocket head
tail = 7 # how many pixels trailing from the rocket head

# Looks in current folder for sound effects for the firework setting off.
woosh = [] # List for found woosh sounds
wooshList = glob.glob('*Woosh.wav') # with filename including "(anything)Woosh.wav"
for sounds in wooshList:
    woosh.append(pygame.mixer.Sound(sounds))

# Looks in current folder for sound effects for the bangs.
bang = [] # List for found Bang sounds
bangList = glob.glob('*Bang.wav') #  with filename including "(anything)Bang.wav"
for bangs in bangList:
    bang.append(pygame.mixer.Sound(bangs))

if len(bang) == 0 and len(woosh) == 0:
    print('SILENT MODE: Open readMe.txt for how to add sound effects.')

# Looks in current folder for pictures.
imagesToLookFor = '*100.png'
images = glob.glob(imagesToLookFor) # with filename including "(anything)100.png"
currPic = 'current.png' # Temp filename for the explosion of the picture currently used

######### If you want to have a set order for pictures to explode add specific filenames in this list. ##########
#EXAMPLE: finale = ['thanks.png', 'thanks1.png', 'happyBirthday.png']
finale = [] # Add your picture filenames in the list of finale like the example of 3 pictures above for a set order.
# If you are using pictures in the finale list go to kaBoom function and setup the order.
if len(finale) != 0:
    isFinale = True
else:
    isFinale = False

def rocket(rocketSize, litRocket):
    i = 0
    for xandy in litRocket:
        if i % 2 == 0:
            pygame.draw.rect(screen, yellow, [xandy[0], xandy[1], rocketSize, rocketSize])
        else:
            pygame.draw.rect(screen, white, [xandy[0], xandy[1], rocketSize, rocketSize])
        i += 1

def pic(file, x, y, newWidth, newHeight, fade, explode):
    if newWidth >= explode: # Starting picture size for picture to explode.
        for i in range(fade): # How many times to explode picture per frame of explosions.
            randX = randint(0, leedsW) # X position to make transparent.
            randY = randint(0, leedsH) # Y position to make transparent.
            leedsData.rectangle((randX, randY, randX, randY), fill=(0, 0, 0, 0)) # Transparent random pixel
        leeds.save(file) # Saves the temporary picture.
    picFile = pygame.image.load(file) # Pygame loads the saved picture
    newMe = pygame.transform.scale(picFile, (newWidth, newHeight)) # Pygame scales the picture
    screen.blit(newMe, ((x - (newMe.get_width() / 2), (y - (newMe.get_height() / 2))))) # Displays image

def kaBoom(goes, rocketX, rocketY):
    global leedsW; global leedsH; global leedsData; global leeds
    if isFinale == True:
        ############################### START OF FINALE / USER ORDER PICTURE SETUP ######################
        ### YOU CAN SELECT THE PICTURE, TOTAL SIZE, HOW MUCH IT FADES AND START OF PICTURE EXPLOSION ####
        if goes == 1: # Starting set picture of display
            randPicture = finale[0] # Picture index in the finale list
            totalSize = 600 # Total size picture will grow to in exploding.
            fade = 500 # How many times to break up picture per frame of explosion.
            explode = 100 # Starting picture size for picture to explode.
        # REPEAT THE NEXT 3 LINES OF CODE WITH DIFFERENT NUMBER OF GOES TO SETUP AN ORDERED PICTURE 
        elif goes == 8: # Could have specific picture in a set point.
            randPicture = finale[0] # As only 1 picture included as default but you can change
            totalSize = 500; fade = 500; explode = 50 # Settings on one line for how to run.
        ################################# END OF FINALE / USER ORDER PICTURES SETUP #####################
        else: ##### USE THE RANDOM PICTURES IN THE IMAGES LIST THAT HAVE "(anything)100.PNG" IN THIS DIRECTORY
            if len(images) != 0:
                randPicture = choice(images) # Random picture choice found at start of script running.
                totalSize = 300; fade = 700; explode = 10 # Settings on one line for how to run.
            else:
                print('Incorrect stopDisplay number, gap in finale setup numbering or random pictures of *100.png in filename not found.')
                print('Open readMe.txt for how to use.')
                pygame.quit()
                sys.exit()
    else:
        if len(images) != 0: # Settings for the random colour explosions, non specific pictures.
            randPicture = choice(images) # Random picture choice found at start of script running.
            totalSize = 300; fade = 700; explode = 10 # Settings on one line for how to run.
        else:
            print('No images found, or that firework was rubbish!.')
            pygame.quit()
            sys.exit()
        
    leeds = Image.open(randPicture) # PIL Imaging opens up a fresh random picture.
    leeds.convert('RGBA') # If not RGBA already
    leeds.save(currPic) # PIL Imaging saves the picture to be exploded as "current.png",
    leedsW, leedsH = leeds.size # Gets picture size
    leedsData = ImageDraw.Draw(leeds) # PIL ImageDraw used to manipulate the explosion
    newWidth = 1 # Picture starting width
    newHeight = 1 # Picture starting height
    while newWidth <= totalSize: # As image is square only checks width
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:                    
                if event.key == pygame.K_q:
                    pygame.quit()
                    sys.exit()
        screen.fill(black) # Clears background or would leave a trail of picture growing
        if newWidth >= explode:
            rocketY += 1; newWidth += 5; newHeight += 5;
            if len(woosh) != 0:
                ignition = choice(woosh) # Sets up next firework woosh sound
                ignition.play() # Plays woosh sound or comment out for no sound
        pic(currPic, rocketX, rocketY, newWidth, newHeight, fade, explode)
        pygame.display.update()
        newWidth += 1; newHeight += 1 # Increments width and height so increase size.

def gameLoop():
    rocketX = int(width /2) # Starting X point for rocket setting off point.
    rocketY = height - 50 # Starting Y point for rocket setting off point.
    yChange = 3 # Pixels for rocket to climb per frame
    litRocket = [] # List for trailing X and Y positions for rocket tail.
    rocketLength = 1
    if len(woosh) != 0:
        ignition = choice(woosh) # Random choice of first rocket sound.
        ignition.play() # Plays the random woosh sound.
    goes = 1 # Variable to utilize having specific pictures in the firework display.
    while True:
        xChange = choice([-1, 0, 1]) # Makes rocket go left right slightly whilst going up.
        rocketX += xChange
        rocketY -= yChange
        screen.fill(black)
        rocketHead = []
        rocketHead.append(rocketX)
        rocketHead.append(rocketY)
        litRocket.append(rocketHead)
        for event in pygame.event.get(): # Pygame events
            if event.type == pygame.QUIT: # Closing of window
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q: # Waiting for q key to quit
                    pygame.quit()
                    sys.exit()
        if len(litRocket) == tail: # Keeps the tail at a constant length or it would leave a trail.
            del litRocket[0]
        if rocketY <= 180: # 180 being the Y coordinate for when to explode
            if len(bang) != 0:
                boom = choice(bang) # Random choice of explosion sound
                boom.play() # Plays boom
            kaBoom(goes, rocketX, rocketY)
            rocketX = int(width /2) # Resets rocket firing X position
            rocketY = height - 100 # Resets rocket firing Y position
            litRocket.clear() # Clears the rocket tail list so it sets off creating a new tail.
            goes += 1 # Goes + 1 for use of set display patterns
        elif goes == stopDisplay + 1: # + 1 so your last firework in patter set in kaBoom will happen.
            pygame.quit()
            sys.exit()
        else:
            rocket(rocketSize, litRocket)
        pygame.display.update()
        clock.tick(fps)

gameLoop()

    
