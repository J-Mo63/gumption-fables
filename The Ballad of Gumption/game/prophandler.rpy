#The Prop Handler code displays options to use items on other items
label prophandler:
        python:
            spacing = 0.4
            ui.vbox(xalign=0.5,yalign=0.35)
            ui.textbutton("Do nothing", clicked=ui.returns("0"), xminimum=250)
            ui.close()
            for item in items:
                ui.vbox(xalign=0.5,yalign=spacing)
                ui.textbutton("Use " + item + " on " + clickeditem, clicked=ui.returns(item), xminimum=250)
                ui.close()
                spacing += 0.05
                if spacing + 0.05 == 1:
                    break
            selected = ui.interact()
        if call == "1":
            jump setprops1
        elif call == "2":
            jump setprops2
        elif call == "3":
            jump setprops3
        elif call == "4":
            jump setprops4
        elif call == "5":
            jump setprops5
        elif call == "6":
            jump setprops6
        elif call == "7":
            jump setprops7
        elif call == "8":
            jump setprops8
        elif call == "9":
            jump setprops9
            
            
            
#This code is from the RenPy cookbook for displaying an inventory in a game
init python: 
        items = []  #Defines the inventory at the beginning of the game
        useditems = [] #Keeps items that have been used
        showitems = False

        def display_items_overlay():
            if showitems:
                    inventory_show = "Inventory: "
                    for i in range(0, len(items)):
                        item_name = items[i].title()
                        if i > 0:
                            inventory_show += ", "
                        inventory_show += item_name
                    ui.frame()
                    ui.text(inventory_show)
        config.overlay_functions.append(display_items_overlay)
        #items.remove("lamp")#when you want to remove items
        #showitems = False #when you don't want to show the inventory onscreen (cutscenes and the like)
        #showitems = True #when you want to reshow the inventory after the cutscene is over
        
        #useditems.remove("lamp")