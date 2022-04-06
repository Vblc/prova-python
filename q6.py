orig = "abcdefghijklmnopqrstuvwxyz"
dest = "nvxkrgpszdeailyuhfbocqjmwt"

# Pergunte uma mensagem para o usuário
msg = input("mensagem original: ")

msglist = list(msg.lower())
newlist = []

while len(msglist) > 0:
    if msglist[0] == 'a':
        newlist.append('n')
        msglist.remove('a')
    elif msglist[0] == 'b':
        newlist.append('v')
        msglist.remove('b')
    elif msglist[0] == 'c':
        newlist.append('x')
        msglist.remove('c')
    elif msglist[0] == 'd':
        newlist.append('k')
        msglist.remove('d')
    elif msglist[0] == 'e':
        newlist.append('r')
        msglist.remove('e')
    elif msglist[0] == 'f':
        newlist.append('g')
        msglist.remove('f')
    elif msglist[0] == 'g':
        newlist.append('p')
        msglist.remove('g')
    elif msglist[0] == 'h':
        newlist.append('s')
        msglist.remove('h')
    elif msglist[0] == 'i':
        newlist.append('z')
        msglist.remove('i')
    elif msglist[0] == 'j':
        newlist.append('d')
        msglist.remove('j')
    elif msglist[0] == 'k':
        newlist.append('e')
        msglist.remove('k')
    elif msglist[0] == 'l':
        newlist.append('a')
        msglist.remove('l')
    elif msglist[0] == 'm':
        newlist.append('i')
        msglist.remove('m')
    elif msglist[0] == 'n':
        newlist.append('l')
        msglist.remove('n')
    elif msglist[0] == 'o':
        newlist.append('y')
        msglist.remove('o')
    elif msglist[0] == 'p':
        newlist.append('u')
        msglist.remove('p')
    elif msglist[0] == 'q':
        newlist.append('h')
        msglist.remove('q')
    elif msglist[0] == 'r':
        newlist.append('f')
        msglist.remove('r')
    elif msglist[0] == 's':
        newlist.append('b')
        msglist.remove('s')
    elif msglist[0] == 't':
        newlist.append('o')
        msglist.remove('t')
    elif msglist[0] == 'u':
        newlist.append('c')
        msglist.remove('u')
    elif msglist[0] == 'v':
        newlist.append('q')
        msglist.remove('v')
    elif msglist[0] == 'w':
        newlist.append('j')
        msglist.remove('w')
    elif msglist[0] == 'x':
        newlist.append('m')
        msglist.remove('x')
    elif msglist[0] == 'y':
        newlist.append('w')
        msglist.remove('y')
    elif msglist[0] == 'z':
        newlist.append('t')
        msglist.remove('z')
    elif msglist[0] == ',':
        newlist.append(',')
        msglist.remove(',')
    elif msglist[0] == '.':
        newlist.append('.')
        msglist.remove('.')
    elif msglist[0] == ' ':
        newlist.append(' ')
        msglist.remove(' ')
    elif msglist[0] == '?':
        newlist.append('?')
        msglist.remove('?')    
    elif msglist[0] == '!':
        newlist.append('!')
        msglist.remove('!')
    else:
        break

# Codifique a mensagem e imprime

str1 = ''.join(newlist)

print(str1)
