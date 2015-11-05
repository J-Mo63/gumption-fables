#Beginning of Chapter 1 (with bartender)
label Chapter1_Bar:
    $mousex = 0.9
    $mousey = 0.9 #Sets starting player position
    $showitems = True
    
    j "Now, where to get some non-alcoholic non-pharmaceutical pro-vegan beer?" #This is how RenPy delivers dialogue
    
    label dropin1:

    scene bar_bg #Sets backdrop
    $scene = "bar" #Informs the stagehand of which scene to dress for
    $scenecall = 2 #Names scene so that scene initiation jump can navigate back here
    
    show player at Position(xpos = mousex, ypos = mousey) #Places player sprite on canvas
    
    if peeps == True:
        if seen == False:
            s "was da mata wit u?"
            j "Sorry?"
            s "You gave Matt gumption and he spread it all over the walls and floor of my apartment"
            m "gumption gumption gumption"
            j "damnit, Matt you told me your pans were burnt"
            m "they were, but then it got out of hand and I saw the walls and floor were dusty"
            s "erghnh"
            s "FIX THIS"
            "*Nathan suddenly bursts through the door of the bar*"
            n "won a comp and I’m taking you all to Gumption Land, Bolivia"
            j "*sigh* I should get packed..."
            $seen = True
        else:
            n "J-Mo, let's go!"
            s "NOT UNTIL YOU GET THAT GUMPTION AWAY FROM MATT"
            j "urgh... what should I do...?"
    
    while 1>0: #Gameplay loop (not infinite if 0 becomes greater than 1)
        jump stagehand #Stagehand is a section of code that adds all images to the scene
        label setstage2:
            
        #Defines instructions for relevant buttons
        #Bartender
        if result == 1:
            $mousex, mousey = 0.9, 0.9
            show player at Position(xpos = mousex, ypos = mousey) #Places player sprite on canvas at this location
            b "Busting for the loo right now..."
            b "... did you see that gigantic-bloody spider in the bathroom?"
            b "... I haven't been able to go to the toilet all day - freaks me out."
            $clickeditem = "Bartender" #Sets the clicked item name for inventory use
            $call = "2" #Names location so that scene inventory jump can navigate back here
            jump prophandler #Provides onscreen options to use items on other items
            label setprops2:
            if selected == "0": #Actions based on result of prophandler
                j "... I'll... go check that out..."
            elif selected == "Spider":
                j "I feel like he’ll know it’s dead if I just hand it to him."
                j "I should put it down near him on the counter."
            else:
                j "It wouldn't do anything THAT interesting."
            if deadspider == True:
                j "He doesn't quite see the spider, I should move it towards him."
        
        #Glass
        elif result == 2:
            $mousex, mousey = 0.7, 0.85
            show player at Position(xpos = mousex, ypos = mousey) #Places player sprite on canvas
            if bartending == True:
                b "Hey! Those aren't free, you know?"
                j "Hmm, I need to get him away from the counter."
            elif bartending == False:
                j "Was this glass really worth the death of a minor character?..."
                j "... Nah, I can’t be having an existential crisis in a video game."
                $items.append("Glass")
                j "Now I need some non-alcoholic liquids."
                
         
        #Matchbook
        elif result == 8:
            $mousex, mousey = 0.2, 0.85
            show player at Position(xpos = mousex, ypos = mousey) #Places player sprite on canvas
            j "People usually don't allow me to touch matches..."
            j "… but I don’t think I’m going to do IT again."
            $items.append("Matchbook")
        
        #Smoke
        elif result == 6:
            $mousex, mousey = 0.8, 0.6
            show player at Position(xpos = mousex, ypos = mousey) #Places player sprite on canvas
            if toiletlocked == True:
                j "Seems like all this smoke is coming from the bathroom..."
            elif toiletlocked == True:
                j "Alia's smoke really lingers, huh?"
            hide dead_spider onlayer sudo
            jump Chapter1_Bathroom
           
        #Fire Extinguisher
        elif result == 4:
            $mousex, mousey = 0.8, 0.5
            show player at Position(xpos = mousex, ypos = mousey) #Places player sprite on canvas
            j "Since when has a fire extinguisher not been useful?"
            $items.append("Fire Extinguisher")
            
        #Counter
        elif result == 3:
            $mousex, mousey = 0.8, 0.9
            show player at Position(xpos = mousex, ypos = mousey) #Places player sprite on canvas
            if deadspider == False:
                j "This is some quality wood..."
            elif deadspider == True:
                j "I need to move it towards him - he doesnt notice it..."
            $clickeditem = "Counter"
            $call = "1"
            jump prophandler
            label setprops1:
            if selected == "Spider":
                j "I'll just leave this here"
                j "Now, I should move it towards him"
                $items.remove("Spider")
                $useditems.append("Spider")
                $deadspider = True
            elif selected == "0":
                j "..."
            elif selected == "Fire Extinguisher":
                if deadspider == True:
                    j "Ok, here it goes..."
                    "*The bartender is so startled by a cold wind of spiders that he ignites on the stove behind him*"
                    "*... while burning, he runs into the wall in panic, knocking himself out.*"
                    $items.remove("Fire Extinguisher")
                    $useditems.append("Fire Extinguisher")
                    $deadspider = False
                    $bartending = False
                elif deadspider == False:
                    j "I guess I could blow something towards him with this..."
                    j "... but I’m missing something to blow."
            else:
                j "At least it didnt light on fire..."
        
        #Briefcase
        elif result == 5:
            $mousex, mousey = 0.16, 0.55
            show player at Position(xpos = mousex, ypos = mousey) #Places player sprite on canvas
            if peeps == True:
                j "That is so convenient that I found this bag just lying here..."
                $clickeditem = "Briefcase" #Sets the clicked item name for inventory use
                $call = "9" #Names location so that scene inventory jump can navigate back here
                jump prophandler #Provides onscreen options to use items on other items
                label setprops9:
                if selected == "0": #Actions based on result of prophandler
                    if "Gun" not in items:
                        j "Hey, there's a gun in here..."
                        $items.append("Gun")
                    j "..."
                elif selected == "Non-Alcoholic Non-Pharmaceutical Pro-Vegan Beer":
                    $items.remove("Non-Alcoholic Non-Pharmaceutical Pro-Vegan Beer")
                    $items.append("Briefcase")
            
            else:
                j "I'm not really planning on going anywhere..."
        
        #Newspaper
        elif result == 7:
            $mousex, mousey = 0.3, 0.85
            show player at Position(xpos = mousex, ypos = mousey) #Places player sprite on canvas
            $article = renpy.random.randint(0, 4)
            if article == 0:
                j 'It reads "RBA claims interest rates fall to new high...'
                j ' ... - RBA members fail drug-test"  '
            elif article == 1:
                j 'It reads "Print media dead!"'
            elif article == 2:
                j 'It reads "Apple patents iPatent"'
                j 'It also says "Inquest into RBA after "totaling" Future Fund on Doritos and Mountain Dew"'
            elif article == 3:
                j 'It reads "Midget porn double of Gordon Ramsay found dead in badger hole"'
                j ' ... RBA members still fail drug-test"  '
            else:
                j 'It reads "Dick Smith has an opinion on something!"'
            $items.append("Newspaper")
            
        #Nathan
        elif result == 16:
            $mousex, mousey = 0.35, 0.49
            show player at Position(xpos = mousex, ypos = mousey) #Places player sprite on canvas
            n "Pack up and get ready to go"
            if "Gumption" not in items:
                n "If you want to help Sash get that Gumption off Matt..."
                n "Use your powers of lawyering to get it back from him"
            $clickeditem = "Nathan"
            $call = "7"
            jump prophandler
            label setprops7:
            if selected == "Briefcase":
                n "Great, let's head to the airport."
                jump Epilogue
            elif selected == "Gun":
                n "Let's head to the airport."
                j "I don't think so, Nathan."
                "*bang*"
                $dead = True
                jump Epilogue
            else:
                n "That's... great J-Mo."
                n "We really should get going."
                j "I should make my beer, pack it up and go now..."

            
        #Matt
        elif result == 17:
            $mousex, mousey = 0.4, 0.49
            show player at Position(xpos = mousex, ypos = mousey) #Places player sprite on canvas
            m "Gumption"
            m "Gumption gumption gumption"
            m "Gumption"
            j "Uhuh"
            j "Matt, can I have the gumption?"
            m "Gumption."
            j "Ok, you... keep doing that floating thing in that case."
            $clickeditem = "Matt"
            $call = "8"
            jump prophandler
            label setprops8:
            if selected == "Contract":
                j "Matt, this is the contract for your lease."
                j "It prohibits smearing of gumption all over the walls and floor of your apartment... sexually..."
                j "Give me the gumption"
                m "*sad* gumption..."
                $items.append("Gumption")
                $items.remove("Contract")
                $choice = True
            elif selected == "Soapy Water in a Mug":
                j "Now Matt, as a vegan, I need you to bless this to become beer"
                m "Gumption"
                j "Thanks"
                $items.append("Non-Alcoholic Non-Pharmaceutical Pro-Vegan Beer")
                $items.remove("Soapy Water in a Mug")
            else:
                j "He seems... busy right now..."
            
        #Sash
        elif result == 18:
            $mousex, mousey = 0.8, 0.49
            show player at Position(xpos = mousex, ypos = mousey) #Places player sprite on canvas
            if contractbool == False:
                    s "HE WONT LISTEN TO ME"
                    s "WHY DID YOU GIVE IT TO HIM"
                    j "urgh..."
                    s "I CANT BELIEVE YOU"
                    j "umm..."
                    s "Here, take this. It's our lease contract"
                    s "Maybe he'll listen to his lawyer"
                    j "ahh..."
                    j "... ok."
                    $items.append("Contract")
                    $contractbool = True
            s "FIX THIS"
            
        #Gumption
        elif result == 19:
            $mousex, mousey = 0.4, 0.49
            show player at Position(xpos = mousex, ypos = mousey) #Places player sprite on canvas
            $article = renpy.random.randint(0, 4)
            m "GUMPTION!"
            j "Oh, sorry."
            j "He seems pretty attached to that can of Gumption..."
            
        else:
            j "I’m sorry, Dave. I'm afraid I can't do that."