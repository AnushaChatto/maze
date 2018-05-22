print "hello player 1\n\n\n\n"


print "select the number of rows of your palace"

n = input()
print "\n\nyour stage is set with", n, " x", n, "output"
print "\n\n\n press y when ready, press anything else to save yourself"

test = raw_input()
if test == 'y':
    print "your funeral"
else:
    print "i guess i scared you :-( sorry, but bye bye "
    exit()

print "\n\n\nit has begun"

a= []

def m_b(place):                     #generating the field
    for i in range(n):
        place.append(["O"] * n)

m_b(a)

print "so here's your goal \n you are at position 1,1 \n you have to move to position",n,",",n
print "\n \n simple enough right?"

print "\n choose r for right l for left, d for down u for up \n\n enter your input"
x= raw_input()          #this input will not matter
print "\n wait wait wait.... i think you should see something first"
del x

h= n*1.5                #health calculator is just 1.5 into diagonal
l=h;

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
    print("That's out of range, you just hit a wall")
    h= h - 0.1;
    health()
    char_y = prev_char_y
    char_x = prev_char_x
    a[char_y][char_x] = "X"
    visual(a)

