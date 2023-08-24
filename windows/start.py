import curses
import keyboard
from curses import wrapper



def main(stdscr):
    curses.init_pair(1, curses.COLOR_WHITE,curses.COLOR_RED)
    RED_AND_WHITE= curses.color_pair(1)
    arrow_y = 0
    while True:
        stdscr.clear()
        
        if keyboard.is_pressed('esc'):
            break
        if keyboard.is_pressed('down'):
                arrow_y = (arrow_y + 1) % 2
        
        stdscr.addstr(arrow_y + 1, 0, "➤ ",RED_AND_WHITE)
        
        stdscr.addstr(0, 15, "TETRIS",RED_AND_WHITE) 
        stdscr.addstr(1, 15,"START",RED_AND_WHITE)
        stdscr.addstr(2, 15,"SETTING",RED_AND_WHITE)
        stdscr.refresh()

        if keyboard.is_pressed('enter'):
            if (arrow_y) % 2 == 1:
                pass
            else:
                pass
        
                  
        


wrapper(main)

