#Beginning of Chapter 1 Opening
#Each scene is split into a seperate file for ease of navigation
    label Chapter1_Opening: #Script continues here
        $mousex = 0.27
        $mousey = 0.49 #Sets starting player position
        $scenecall = 1 #Sets scene so that scene initiation jump can navigate back here
        $opening = True
        
        scene bar_bg #Sets backdrop
        
        j "Urgh, I need a drink" #This is how RenPy delivers dialogue
        
        while 1>0: #Gameplay loop (not infinite if 0 becomes greater than 1)
            $scene = "bar" #Informs the stagehand of which scene to dress for
            jump stagehand #Stagehand is a section of code that adds all images to the scene
            label setstage1:
    
            #Defines instructions for relevant buttons
            if result == 1:
                $mousex, mousey = 0.9, 0.9 #Sets new location of player character
                show player at Position(xpos = mousex, ypos = mousey) #Places player sprite on canvas
                j "Can I get a non-alcoholic non-pharmaceutical pro-vegan beer?"
                b "Sorry, tap’s dry, mate…"
                j "Hmm… this won’t do..."
                $opening = False
                jump Chapter1_Bar
                
            elif result == 2:
                $mousex, mousey = 0.7, 0.85
                show player at Position(xpos = mousex, ypos = mousey) #Places player sprite on canvas
                j "This glass is empty, I should talk to the bartender."
                
            elif result == 6:
                $mousex, mousey = 0.8, 0.6
                show player at Position(xpos = mousex, ypos = mousey) #Places player sprite on canvas
                j "Looks like smoke coming from the bathroom…"
                j "… I’m more interested in getting a drink right now."
            
            else:
                j "Urgh, I need a drink before I do anything zany and ridiculous again."