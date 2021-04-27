import turtle
import random
hexchars = list(map(chr, range(48, 58))) + list(map(chr, range(97, 103)))
def randhex(n):
    hexchars = list(map(chr, range(48, 58))) + list(map(chr, range(97, 103)))
    hexv = ''
    for i in range(n):
        hexv += hexchars[random.randint(0,len(hexchars)-1)]
    return hexv

def HexConvert(h1):
    new = 0
    for i in range(len(h1)):
        char = h1[-1]
        chardec = hexchars.index(char)
        if((chardec != 0) and (i != 0)):
            new += chardec *(16**i)
        elif (i == 0):
            new += chardec
        h1 = h1[:-1]
    return new

def hex_add_1(h1):
    hexchars = list(map(chr, range(48, 58))) + list(map(chr, range(97, 103)))
    a=h1
    for i in range(1,(len(h1) + 1)):
        if((i == len(a))and(a[-i] == 'f')):
            h1 = '1' + '0'*i
            return h1
        if(a[-i] != 'f' ):
            new = hexchars[hexchars.index(a[-i])+1]
            for j in range(i):
                h1 = h1[:-1]
            h1 += new
            h1 += '0'*(i-1)
            return h1
def hexplusH(h1,h2):
    for i in range (HexConvert(h2)):
        h1=hex_add_1(h1)
    return h1


def nxtclr(clr):
    return '#'+hexplusH(clr[1:],'5')

def crcl(n,clr):
    for i in range(24):
        for j in range(4):
            t.forward(n)
            t.right(90)
        t.right(15)
        clr=nxtclr(clr)
        t.pencolor(clr)
    
        

t= turtle.Turtle()
t.speed('fastest')
t.screen.bgcolor("black")
clr='#' + randhex(6)
t.pencolor(clr)      
count=40

for i in range(20):
    if (i%5 == 0):
        count+=20*i/5
    else:
        count+=5
    clr='#'+hexplusH(clr[1:],'78')
    print(clr)
    crcl(count,clr)
    
    
    
