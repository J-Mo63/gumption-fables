import math
x = 1.10
y = 1.10
xclick = 40.70
yclick = 40.70

def MoveCharacter(x,y,xclick,yclick): #Defines movement function
    print (y)
    d = math.sqrt((xclick - x)**2 + (yclick - y)**2) #Gets the ‘D’ (distance formula)
    for i in range(1, int(d + 1)): #For-loop to distance as an integer
        xstep = 0.5*(xclick - x)/d #Gets vector in direction of click divided for x-coordinate
        ystep = 0.5*(yclick - y)/d #Gets vector in direction of click divided for y-coordinate
        x = x + xstep #Adds x-vector to character position
        y = y + ystep #Adds y-vector to character position
        print (x)
        print (y)

MoveCharacter(x,y,xclick,yclick)
