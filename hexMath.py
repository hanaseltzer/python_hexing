hexchars = list(map(chr, range(48, 58))) + list(map(chr, range(97, 103)))
import random

#random 6 digit hex
def randhex(n):
    hexchars = list(map(chr, range(48, 58))) + list(map(chr, range(97, 103)))
    hexv = ''
    for i in range(n):
        hexv += hexchars[random.randint(0,len(hexchars)-1)]
    return hexv


#hex + 1
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

def hex_minus_1(h1):
    dec = HexConvert(h1)
    dec-=1
    return toHex(dec)

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

def hexplusH(h1,h2):
    for i in range (HexConvert(h2)):
        h1=hex_add_1(h1)
    return h1

def hexplusD(h,d):
    for i in range (d):
        h=hex_add_1(h)
    return h
def toHex(d):
    h=''
    r=1
    endsum=0
    while((d/(16**r))>16):
        r+=1
    for i in range(r):
        subsum = d-(16**r)
        endsum+=subsum
        h+=hexchars[int(d/(16**r))]
    return h
    


        


