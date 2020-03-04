#count = 0  # Survival count needs to be implemented in all definitions
#inventory = ""
# All Story related texts have to be in seperate def function()
# This in order to not repeat unwanted text and only repeat 'count and questions + if-solutions'
# 'count and questions + if-solutions' have to be able to get called seperately ('in def function()')
# Calling needs to be more precise depending on importance of function
def Firstscene(count):
    userInput1 = input("What do you do? a) Walk out of room b) Stay in room ( <enter> a) or b) )\n:")
    count = count + 1
    if userInput1 == "a)":  # Solution Path1
        WalkoutRoom(count)
    elif userInput1 == "b)":  # Will return to Walkoutroom()
        StayinRoom(count)
def StayinRoom(count):   # Go back to the Firstscene()
        print("no one coming return to door")
        Firstscene(count)
def WalkoutRoom(count):#solution path
    count = count + 1
    userInput2 = input("The corona Zombie is coming for u, What do you do(A = fight, B = Run, C = Lock door)\n:")
    if userInput2 == "A":
        FightZombie(count)
    elif userInput2 == "B": #solution path2
        RunAwayZombie(count)
    elif userInput == "C":
        WalkoutRoom(count)  # has to include text so maybe make seperate TextPart function = 1 more step
def FightZombie(count):  # graphics with objects
    userInput3 = input("Which of the objects could help you? ( A)Crutches, B)Wheelchair, C)Gun )\n:")
    if userInput3 == "Crutches":  # put to inventory
        count = count + 1
        print("You pick up crutches and want to use them but how?")
        userInput5 = input("How u wanna use crutch?(A = Hit, B = Use)")
        Inventory = Inventory + "Crutch"
        if userInput5 == "Hit":
            print("big fight but no effect")
            RunAwayZombie(count)
        elif userInput5 == "Use":
            print("kick had no effect on the corona zombie")
            RunAwayZombie(count)  # going back to
    elif userInput3 == "Wheelchair":  # put to inventory
        count = count + 1
        Inventory = Inventory + "Wheelchair"
        print("You tried to take advantage of the wheelchair but no effect on zombie")
        WalkoutRoom(count)
    elif userInput3 == "Gun":  # put to inventory
        count = count + 1
        print("Tricky ToyGun is no helping")
        WalkoutRoom(count)

def RunAwayZombie(count):
    userInput4 = input("You want to find out of the hospital ( a = Right, b = Left)\n:")
    if userInput4 == "Right": #going to count more
        if Inventory == "Crutches":
            print("you can defend yourself with your crutches")  # here no count
            print("txt")
            userInput6 = input("selecthowtousecrutches")
            if userInput6 == "Hit":
                print("You escape without a survival point")
                return RunAwayZombie(count)
        elif Inventory != "Crutches":  # if inventory does not contain 'crutches' return to runawayzombie() to pick left
            count = count + 1
            print("txt")
            RunAwayZombie(count)
    elif userInput4 == "Left":  #solution path3
        count = count + 1
        ShowCorridor(count)
def ShowCorridor(count):
    userInput7 = input("Show corridor")  # choose graphical corridor or room
    count = count + 1
    if userInput7 == "Continue running":  # solutions path4
        ContinueRunning(count)
    elif userInput7 == "Hide in Room":  # you are locked in with zombies and need to return to Left- Show_Corridor graphics
        print("The Corona Zombie is smelling you, there is only one possibility:") #goback to graphical window
        ShowCorridor(count)
def ContinueRunning(count):  # solutions path
    userInput8 = input('Look or hide')  # graphical reception or text with items to pick up
    count = count + 1
    if userInput8 == "Look":   #solution path5 # look for items
        print("search for something")
        PickupMap(count)
    elif userInput8 == "Hide behind desk":
        print("Zombie is coming")
        ContinueRunning(count)
def PickupMap(count):
    UserInput9 = input("Pick up Map, Pencils ,Paper ,Staple ,paperclip,")  # look for items in reception desk#Maybe str() need
    while UserInput9 != "Map":
        count = count + 1
        print("This item will not help you")
        return PickupMap(count)
    if UserInput9 == "Map": #solution path6
        count = count + 1
        RuntoQuiz(count)
def RuntoQuiz(count):
    userInput10 = input("Hide or Run?:")
    count = count + 1
    if userInput10 == "Hide":
        RuntoQuiz(count)
    elif userInput10 == "Run": #solutions path 7 #Graphical window quiz# select a)b)c) of pictures Final door
        FinalDoor(count) #Input in graphics
def FinalDoor(count):
    userInput22 = input("Left door to freedom or Right door to freedom?")
    count = count + 1
    if userInput22 == "Left":
        print("HAHA Almost")
        FinaDoor(count)
    elif userInput22 == "Right":
        print("WIN")  # insert graphics picture win a nice finish
        print("your survival count is:",count)
def main():
    count = 0
    Inventory = []
    Firstscene(count)
    StayinRoom(count)
    WalkoutRoom(count)
    FightZombie(count)
    RunAwayZombie(count)
    ShowCorridor(count)
    ContinueRunning(count)
    PickupMap(count)
    RuntoQuiz(count)
    FinalDoor(count)
main()