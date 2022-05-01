
from pizzeria import Terminal as term, Terminal

if __name__ == '__main__':
    ter = Terminal()

    while True:
        ter.show_menu()
        ter.proceed_input(input())

