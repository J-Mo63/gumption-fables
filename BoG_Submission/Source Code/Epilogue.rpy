#Beginning of Epilogue section
label Epilogue:
    $showitems = False
    scene black_bg #Sets backdrop
    if dead == True: #Secret alternative ending
        while loopcount < 5:
            "And in killing himself, J-Mo broke the time-loop."
            "For it had been centuries that the world had been caught in an infinite loop."
            $loopcount += 1
    else: #Ending dialogue
        "And so the friends left for the airport..."
        "J-Mo brought his non-existent beer..."
        "Nathan slammed his head on the door on the way out..."
        if choice == True:
            "Matt stopped floating after sobering out..."
            "And Sash was somewhat satisfied..."
        elif choice == False:
            "Matt found inner peace within himself..."
            "And Sash still acted 'active-aggressive' towards the world..."

        "Thank you for playing the first chapter of The Ballad of Gumption"
        "NEXT TIME, ON GUMPTION:"
        "It's the same characters and the same puzzles you've seen before..."
        "... but on a plane."
        if DLC == True:
            jump Chapter2_Terminal #If DLC is present, it will jump to the second chapter after chapter 1 ends.
        "plz buy the DLC"
        jump end #Jumps back the the main menu