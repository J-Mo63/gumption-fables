*Identification of the Problem*

The game is called "The Ballad of Gumption", and is a point and click adventure game based on the Gumption Tomes from chapters 1 through 10. The gameplay is reminiscent of the original Monkey Island series, with a modern, intuitive inventory system. The project fills the market gap for entertainment, where the market has a lack of 2D, point and click adventure games done in a retro, 8bit pixel-art style.

The requirements and features for this project include the following:

    - Graphical user interface
    - Python 3.0
    - Self-contained .app file
    - Multiple chapters
    - Pointing
    - Clicking
    - Save files
    - Hint systems
    - Two chapters
    - Tutorial
    
    - Targets system requirements:
        - Memory: 1GB
        - Processor: 2.6 GHz
        - Graphics: Intel Iris 1536MB
        - Storage: 200MB GB
        
Also would like to add some stretch goals to my project:

    - The addition of chapters 3 to 10 and maybe think about chapters 1 to 3 from volume two.
    - Voice acting
    - Bonus TBA content

The game mechanics consist of solving puzzles by combining actions or objects with other objects or entities. The successful progression of combinations serve to advance the games plot and bring on new sets of puzles until the completion of all the content that the game has to offer. At this point, I am considering using pixel art for characters and objects, but leave the background in the original art style, altough this is subject to change.

At this point, the way in which I will be able to implement this is by using one image as a background and another as a definition of movement boudaries. Clicking on any part of the background image will give the program coordinates of the clicked location, which will then move the player character sprite to that location. Apat from this, there will also be clickable locations on the screen, which will be triggered by onclick events.

The game is ultimately event driven, and will not do anything that isnt a reaction to user input. I decided to work on this project as many point and click games have complicated and unintuative inventory and action systems. This game will simplify gameplay by infering all actions. An example will be clicking on a character will assume the "talk to..." action, or clicking on certain objects will assume "pick up..." or "examine..." on other objects.