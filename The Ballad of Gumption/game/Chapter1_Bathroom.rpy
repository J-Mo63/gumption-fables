#Run when entering the bathroom (with the stall closed)
label Chapter1_Bathroom:
    $mousex = 0.9
    $mousey = 0.9 #Sets starting player position
    $showitems = True

    scene bath_bg #Sets backdrop
    $scene = "bathroom" #Informs the stagehand of which scene to dress for
    $scenecall = 3 #Names scene so that scene initiation jump can navigate back here
    show playerbig at Position(xpos = mousex, ypos = mousey) onlayer sudo#Places player sprite on canvas
    
    while 1>0: #Gameplay loop (not infinite if 0 becomes greater than 1)
        jump stagehand #Stagehand is a section of code that adds all images to the scene
        label setstage3:
        
        show playerbig at Position(xpos = mousex, ypos = mousey) onlayer sudo#Places player sprite on canvas
            
        #Defines instructions for relevant buttons
        
        #Back Button
        if result == 0:
            $mousex, mousey = 0.9, 0.9
            show playerbig at Position(xpos = mousex, ypos = mousey) onlayer sudo#Places player sprite on canvas at this location
            hide playerbig onlayer sudo
            $mousex, mousey = 0.8, 0.6
            jump dropin1
            
        #Alive Spider
        elif result == 9:
            $mousex, mousey = 0.3, 0.9
            show playerbig at Position(xpos = mousex, ypos = mousey) onlayer sudo#Places player sprite on canvas at this location
            j "Urghhhh, I’m not touching it while it’s still alive."
            $clickeditem = "Spider"
            $call = "3"
            jump prophandler
            label setprops3:
            if selected == "Newspaper":
                j "I'll give it a good whack..."
                "*you hit the spider with the force of Thor's hammer*"
                $items.append("Spider")
                $items.remove("Newspaper")
                $useditems.append("Newspaper")
            elif selected == "0":
                j "..."
            elif selected == "Fire Extinguisher":
                j "That seems a little overkill..."
            elif selected == "Glass":
                j "Um... no... I'm planning on drinking out of that"
            else:
                j "That seems pointless"
                
        #Sink
        elif result == 10:
            $mousex, mousey = 0.35, 0.9
            show playerbig at Position(xpos = mousex, ypos = mousey) onlayer sudo#Places player sprite on canvas at this location
            j "Turns out both taps in this place are dry..."
            
        #Soap
        elif result == 11:
            $mousex, mousey = 0.35, 0.9
            show playerbig at Position(xpos = mousex, ypos = mousey) onlayer sudo#Places player sprite on canvas at this location
            j "Soap: the most important invention in history..."
            j "... not that anyone actually uses it..."
            j "... hold up, this is non-pharmaceutical!"
            $clickeditem = "Soap"
            $call = "4"
            jump prophandler
            label setprops4:
            if selected == "Pint of Water":
                "*you add the soap to the mixture*"
                $items.append("Soapy Water in a Mug")
                $items.remove("Pint of Water")
                $useditems.append("Pint of Water")
                $useditems.append("Soap")
                $peeps = True
            elif selected == "0":
                j "..."
            elif selected == "Glass":
                j "I need some liquid in that first..."
            else:
                j "What would that accomplish?"
        
        #Stall
        elif result == 12:
            $mousex, mousey = 0.55, 0.9
            show playerbig at Position(xpos = mousex, ypos = mousey) onlayer sudo#Places player sprite on canvas at this location
            if toiletlocked == True:
                j "*knock knock* Anyone in there?"
                a "Occu...*puff* ..."
                a "... pied"
            elif toiletlocked == False:
                j "The air still hangs heavy with a strange-smelling smoke..."
            
        #Toilet 1
        elif result == 13:
            $mousex, mousey = 0.6, 0.9
            hide playerbig onlayer sudo
            show playerbigrev at Position(xpos = mousex, ypos = mousey) onlayer sudo#Places player sprite on canvas at this location
            j "NOOOOOOPE!"
            j "The smell coming from that toilet is like satan's infant's feces!"
            
        #Sprinkler
        elif result == 14:
            $mousex, mousey = 0.7, 0.9
            hide playerbig onlayer sudo
            show playerbigrev at Position(xpos = mousex, ypos = mousey) onlayer sudo#Places player sprite on canvas at this location
            j "Fire safety is the best kind of safety..."
            j "... it's a wonder that it hasn't gone off with all this smoke..."
            j "... maybe it's heat sensitive?"
            $clickeditem = "Sprinkler"
            $call = "5"
            jump prophandler
            label setprops5:
            if selected == "Matchbook":
                "*The fire alarm goes off*"
                a "BLOODY HELL!!!"
                a "My lighter wont work in this rain..."
                "*Alia leaves the bathroom stall*"
                $items.remove("Matchbook")
                $useditems.append("Matchbook")
                $toiletlocked = False
            elif selected == "0":
                j "..."
            elif selected == "Glass":
                j "I'm not planning on drinking out of that, at all."
            else:
                j "Yeah, that's not a thing... that can... happen."
                
        #Toilet2
        elif result == 15:
            $mousex, mousey = 0.55, 0.9
            show playerbig at Position(xpos = mousex, ypos = mousey) onlayer sudo#Places player sprite on canvas at this location
            j "Hey, this one has some water in it!"
            $clickeditem = "Toilet"
            $call = "6"
            jump prophandler
            label setprops6:
            if selected == "Glass":
                "*You fill the glass*"
                j "Ok, now I need to make this non-pharmaceutical."
                $items.remove("Glass")
                $useditems.append("Glass")
                $items.append("Pint of Water")
            elif selected == "0":
                j "..."
            else:
                j "I'm not sure what that would do..."
            