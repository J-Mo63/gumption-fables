#Welcome to THE SCRIPT, where Ren'Py does things highly inefficiently

#This is where characters are declared to RenPy
define s = Character('Sash', color="#ff4d4d", image = "sashside", window_left_padding = 200)
define n = Character('Nathan', color="#00abff", image = "nathside", window_left_padding = 200)
define m = Character('Matt', color="#4c946e", image = "mattside", window_left_padding = 200)
define b = Character('Bartender', color="#f0ff00", image = "bartenderside", window_left_padding = 170)
define j = Character('J-Mo', color="#6f6bf4", image = "j-moside", window_left_padding = 200)
define a = Character('Alia', color="#FFCC66", window_left_padding = 200)

#This is where images are declared to RenPy
image bar_bg = "images/backgrounds/bar.png"
image bath_bg = im.Scale("images/backgrounds/bathroom.png", 1694, 940)
image black_bg = im.Scale("images/backgrounds/black.png", 1694, 940)
image player = im.Scale("images/items/jmomemes.png", 83, 325.25) 
image side j-moside = im.Scale("images/items/jmoside.png", 200, 290) 
image side mattside = im.Scale("images/items/mattside.png", 200, 290) 
image side nathside = im.Scale("images/items/nathside.png", 200, 290) 
image side sashside = im.Scale("images/items/sashside.png", 200, 290) 
image side bartenderside = im.Scale("images/items/bartendside.png", 160, 290) 
image blackbar = im.Scale("images/UI/black.png", 1400, 120) 
image smoke = im.Scale("images/items/smoke.png", 700, 300) 
image dead_spider = im.Scale("images/items/spider.png", 20, 20) 
image playerbig = im.Flip(im.Scale("images/items/jmomemes.png", 150, 500), horizontal=True)
image playerbigrev = im.Scale("images/items/jmomemes.png", 150, 500)

init python: #Setting variables for the game
    
    DLC = False #Tells the game to look for DLC
    dlcfile = open(renpy.loader.transfn("dlc.txt"),"r") #Opens file
    for line in dlcfile:
        if line == "1":
            DLC = True
    dlcfile.close() #Closes file

    config.layers.insert(2, 'sudo')
    deadspider = False
    bartending = True
    toiletlocked = True
    peeps = False
    contractbool = False
    choice = False
    seen = False
    dead = False
    loopcount = 0

#My mainline
label start:      
    jump Chapter1_Opening #Continues in chapter 1 opening
    
label end:
    return
