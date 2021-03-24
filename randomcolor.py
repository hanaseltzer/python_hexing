import random
def randclr():
    hexchars = list(map(chr, range(48, 58))) + list(map(chr, range(65, 71)))
    hexv = ''
    for i in range(6):
        hexv += hexchars[random.randint(0,len(hexchars)-1)]
    return "#" + hexv
print(randclr())