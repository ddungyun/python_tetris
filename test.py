import curses
import keyboard
from curses import wrapper

def main(stdscr):
    while True:
        if keyboard.is_pressed('a'):
            break
        stdscr.clear()
        for i in range(10):
            stdscr.addstr(0,i,'a')
        stdscr.refresh()

wrapper(main)