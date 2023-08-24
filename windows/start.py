import curses
import keyboard
from curses import wrapper

def PrintStartMap(stdscr):
    curses.init_pair(1, curses.COLOR_WHITE,curses.COLOR_RED)
    RED_AND_WHITE= curses.color_pair(1)

    global arrow_flag
    arrow_flag= False

    def InitArrowFlag(evt):
        global arrow_flag
        arrow_flag = False

    arrow_y = 0
    while True:
        stdscr.clear()
        
        if keyboard.is_pressed('esc'):
            break
        if keyboard.is_pressed('down'):
            if not arrow_flag:
                arrow_y = (arrow_y + 1) % 2
                arrow_flag = True

        keyboard.on_release_key('down', InitArrowFlag)
        
        stdscr.addstr(arrow_y + 1, 0, "➤ ",RED_AND_WHITE)
        
        stdscr.addstr(0, 15, "TETRIS",RED_AND_WHITE) 
        stdscr.addstr(1, 15,"START",RED_AND_WHITE)
        stdscr.addstr(2, 15,"SETTING",RED_AND_WHITE)
        stdscr.refresh()

        if keyboard.is_pressed('enter'):
            return (arrow_y) % 2
            
        
                  
        

if __name__ == 'main':
    wrapper(PrintStartMap)

