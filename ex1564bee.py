#versão final
import sys

for line in sys.stdin:
    try:
        complain_user = int(line.strip())
        if complain_user == 0:
            print('vai ter copa!')
        else:
            print('vai ter duas!')
    except ValueError:
        pass

#versão inicial
while True:
    complain_user = int(input())
    if complain_user > 0:
        print('vai ter duas!')
    else:
        print('vai ter copa!')