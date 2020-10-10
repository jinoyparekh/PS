# Simple console program to convert string or int to char


def lister(*args):
    while True:
        greetings = 'This is a simple console program to convert input to char'
        exit = 'press quit or esc exit'
        l_greetings = len(greetings)
        l_sep = '\n'+'*'*l_greetings+'\n'
        print(l_sep, greetings, l_sep)
        print(l_sep, exit, l_sep)
        name = input("Please enter your name: ")

        if name.lower() == 'quit' or name.lower() == 'esc':
            break

        n = list(name)
        print(f'your name in list : {n}')
        print(f'your name is : {name}')


lister()
