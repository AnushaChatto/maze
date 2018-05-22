from os import system, name
from time import sleep

def clear():
    # for windows
    if name == 'nt':
        _ = system('cls')

    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')


print "hello player 1\n\n\n\n"


print "select the number of rows of your palace"

n = input()
print "\n\nyour stage is set with", n, " x", n, "output"
print "\n\n\n press y when ready, press anything else to save yourself"

test = raw_input()

clear()
if test == 'y':
    print "your funeral"
else:
    print "i guess i scared you :-( sorry, but bye bye "
    exit()

sleep(4)

print "\n\n\nit has begun...."

sleep(4)

clear()

a= []
def m_b(place):
    for i in range(n):
        place.append(["O"] * n)

m_b(a)

print "so here's your goal \n you are at position 1,1 \n you have to move to position",n,",",n
print "\n \n simple enough right?"

print "\n choose r for right l for left, d for down u for up \n\n enter your input"
x= raw_input()

clear()

print "\n wait wait wait.... i think you should see something first"
del x

sleep(4)

clear()

h= n*1.5            #calculating health which is just diagonal into 1.5
l=h;                #maximum health

def health( ):
    print "\n\n\n***********************"
    print "\n health =", l, "/", h ;
    print "\n***********************"
    return[0]

health()

def visual(x):
    for i in x:
        print(" ".join(i))

visual(a)


prev_char_y = 0
prev_char_x = 0
char_y = 0
char_x = 0
a[char_x][char_y] = "X"
visual(a)
go = True
try:
    while go:
        print  "move l, r, d, u or stop"
        control = raw_input()

        print control

        if control == "l":
            char_x = char_x -1
        elif control == "r":
            char_x = char_x +1
        elif control == "d":
            char_y = char_y + 1
        elif control == "u":
            char_y = char_y -1
        elif control == "stop":
            go = False
        else:
            print ("do it again idiot")
        clear()
        a[prev_char_y][prev_char_x] = "O"
        a[char_y][char_x] = "X"
        prev_char_y = char_y
        prev_char_x = char_x
        visual(a)

        if char_x== n-1 & char_y== n-1:
            print "you suceeded!"
            print "\n health is"
            health()
            go = False
except IndexError:
    print("That's out of range, you just hit a wall, full of spikes, you dead")
    h= h - h;
    health()
    char_y = prev_char_y
    char_x = prev_char_x
    a[char_y][char_x] = "X"
    visual(a)

