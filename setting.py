import curses
import keyboard
from curses import wrapper


def main(stdscr):
    curses.init_pair(1, curses.COLOR_WHITE,curses.COLOR_RED)
    RED_AND_WHITE= curses.color_pair(1)
    arrow_y = 0
    while True:
        stdscr.clear()
        stdscr.addstr(arrow_y , 12, "➤ ",RED_AND_WHITE)
        stdscr.addstr(0, 15, "DAS",RED_AND_WHITE) 
        stdscr.addstr(1, 15,"ARR",RED_AND_WHITE)
        stdscr.addstr(2, 15,"SDF",RED_AND_WHITE)
        stdscr.addstr(3,15,'EXIT',RED_AND_WHITE)
        stdscr.refresh()
    
        if keyboard.is_pressed('esc'):
            break

        if keyboard.is_pressed('down'):
            # if not arrow_flag:
            arrow_y = (arrow_y + 1) % 4
                # arrow_flag = True

        if keyboard.is_pressed('enter'):
            if (arrow_y) % 4 == 0:
                pass
            elif (arrow_y)%4==1:   
                pass
            elif (arrow_y)%4==2:
                pass
            else:
                pass

        # keyboard.on_release_key('down', InitArrowFlag)
        

    



wrapper(main)