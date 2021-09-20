'''
Вгадати задане число з 5 попиток!
'''
import sys

while True:
    x = int(input('Введіть число: '))
    if x <= 4:
        print(x)
    elif x == 5:
        print('STOP')
        break