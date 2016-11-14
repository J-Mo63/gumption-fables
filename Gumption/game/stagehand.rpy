#Begins stagehand actions
label stagehand: #Places and defines buttons + images
    if scene == "bar": #Checks whether the area is the bar or the bathroom
        if deadspider == True:
            show dead_spider at Position(xpos = 0.8, ypos = 0.85) onlayer sudo #Places dead spider on counter
            
        python: #Interprets code as Python
            
            #Smoke
            ui.frame(xalign=1.1,yalign=0.05)
            ui.imagebutton(im.Scale("images/items/smoke.png", 700, 400), im.Scale("images/items/smoke.png", 720, 420), clicked=ui.returns(6))
            
            #Extinguisher
            if "Fire Extinguisher" not in items:
                if "Fire Extinguisher" not in useditems: #Checks if the item should exist onscreen
                    ui.frame(xalign=0.8,yalign=0.37) #Creates frame for button
                    ui.imagebutton(im.Scale("images/items/extinuisher.png", 170, 170), im.Scale("images/items/extinuisher.png", 180, 180), clicked=ui.returns(4)) #Creates button from image

            #Briefcase
            if "Briefcase" not in items:
                if "Briefcase" not in useditems:
                    ui.frame(xalign=0.05,yalign=0.4)
                    ui.imagebutton(im.Scale("images/items/suitcase.png", 170, 170), im.Scale("images/items/suitcase.png", 180, 180), clicked=ui.returns(5))

        show player at Position(xpos = mousex, ypos = mousey) #Places player sprite on canvas
        if opening == False:
            show blackbar at Position(xpos = 0.0, ypos = 0.06) #Places a background for inventory

        python:  
            #Counter
            ui.frame(xalign=1.095,yalign=1.015)
            ui.imagebutton(im.Scale("images/items/counter.png", 1450, 180), im.Scale("images/items/counter.png", 1470, 190), clicked=ui.returns(3))

            #Bartender
            if bartending == True:
                ui.frame(xalign=1.02,yalign=1.015)
                ui.imagebutton(im.Scale("images/items/bartender.png", 130, 230), im.Scale("images/items/bartender.png", 135, 240), clicked=ui.returns(1))

            #Glass
            if "Glass" not in items:
                if "Glass" not in useditems:
                    ui.frame(xalign=0.7,yalign=0.85)
                    ui.imagebutton(im.Scale("images/items/glass.png", 70, 70), im.Scale("images/items/glass.png", 72, 72), clicked=ui.returns(2))

            #Matches
            if "Matchbook" not in items:
                if "Matchbook" not in useditems:
                    ui.frame(xalign=0.2,yalign=0.85)
                    ui.imagebutton(im.Scale("images/items/matchbook.png", 30, 30), im.Scale("images/items/matchbook.png", 32, 32), clicked=ui.returns(8))

            #Newspaper
            if "Newspaper" not in items:
                if "Newspaper" not in useditems:
                    ui.frame(xalign=0.35,yalign=0.97)
                    ui.imagebutton(im.Scale("images/items/newspaper.png", 150, 150), im.Scale("images/items/newspaper.png", 152, 152), clicked=ui.returns(7))
              
            if peeps == True:
                #Nathan
                ui.frame(xalign=0.25,yalign=0.2)
                ui.imagebutton(im.Scale("images/items/nathan.png", 370, 370), im.Scale("images/items/nathan.png", 380, 380), clicked=ui.returns(16))
                #Matt
                ui.frame(xalign=0.6,yalign=0.1)
                ui.imagebutton(im.Scale("images/items/matt.png", 520, 520), im.Scale("images/items/matt.png", 530, 530), clicked=ui.returns(17))
                #Sash
                ui.frame(xalign=0.8,yalign=0.18)
                ui.imagebutton(im.Scale("images/items/sash.png", 370, 370), im.Scale("images/items/sash.png", 380, 380), clicked=ui.returns(18))
                #Gumption
                if "Gumption" not in items:
                    ui.frame(xalign=0.5,yalign=0.28)
                    ui.imagebutton(im.Scale("images/items/gump.png", 40, 40), im.Scale("images/items/gump.png", 42, 42), clicked=ui.returns(19))

            result = ui.interact() #Sets pressed button as a result
    
    
    
    
    elif scene == "bathroom":
        show smoke at Position(xpos = 0.3, ypos = 0.3) #Smoke effect
        show blackbar at Position(xpos = 0.0, ypos = 0.06) #Places a background for inventory
        python: #Interprets code as Python
            
            #Back
            ui.frame(xalign=1.01,yalign=1.015)
            ui.imagebutton(im.Scale("images/items/back.png", 150, 150), im.Scale("images/items/back.png", 160, 160), clicked=ui.returns(0))
            
            #AliveSpider
            if "Spider" not in items:
                if "Spider" not in useditems:
                    ui.frame(xalign=0.1,yalign=0.3)
                    ui.imagebutton(im.Scale("images/items/spider.png", 30, 30), im.Scale("images/items/spider.png", 32, 32), clicked=ui.returns(9))
            
            #Sink
            ui.frame(xalign=0.05,yalign=0.7)
            ui.imagebutton(im.Scale("images/items/sink.png", 500, 300), im.Scale("images/items/sink.png", 505, 305), clicked=ui.returns(10))
            
            #Soap
            if "Soap" not in useditems:
                ui.frame(xalign=0.3,yalign=0.55)
                ui.imagebutton(im.Scale("images/items/soap.png", 50, 50), im.Scale("images/items/soap.png", 52, 52), clicked=ui.returns(11))
            
            #Stall
            if toiletlocked == True:
                ui.frame(xalign=0.8,yalign=0.55)
                ui.imagebutton(im.Scale("images/items/stallclosed.png", 800, 600), im.Scale("images/items/stallclosed.png", 810, 610), clicked=ui.returns(12))
            elif toiletlocked == False:
                ui.frame(xalign=0.8,yalign=0.55)
                ui.imagebutton(im.Scale("images/items/stallopen.png", 800, 600), im.Scale("images/items/stallopen.png", 810, 610), clicked=ui.returns(12))
                ui.frame(xalign=0.52,yalign=0.7)
                ui.imagebutton(im.Scale("images/items/toilet.png", 250, 400), im.Scale("images/items/toilet.png", 255, 405), clicked=ui.returns(15))
            
            #Toilet1
            ui.frame(xalign=0.8,yalign=0.7)
            ui.imagebutton(im.Scale("images/items/toiletbrown.png", 250, 400), im.Scale("images/items/toiletbrown.png", 255, 405), clicked=ui.returns(13))
            
            #Sprinkler
            ui.frame(xalign=0.9,yalign=0.05)
            ui.imagebutton(im.Scale("images/items/sprinkler.png", 30, 30), im.Scale("images/items/sprinkler.png", 32, 32), clicked=ui.returns(14))
            
        $result = ui.interact() #Sets pressed button as a result
        

hide playerbigrev onlayer sudo
#Returns to location of call in game
if scenecall == 1:
    jump setstage1
elif scenecall == 2:
    jump setstage2
elif scenecall == 3:
    jump setstage3