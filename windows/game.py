import curses
from curses import wrapper

def PrintGameMap(stdscr):

    box_x1 = 0
    box_y1 = 0
    while True:
        stdscr.clear()
        
        # 맨 왼쪽 사각형 12 x 6 가로 하나당 2로 계산
        stdscr.addstr(0, 3, '┏━━━━━━━━┓') 
        stdscr.addstr(1,3,'┃        ┃')
        stdscr.addstr(2,3,'┃        ┃')
        stdscr.addstr(3,3,'┃        ┃')
        stdscr.addstr(4,3,'┃        ┃')
        stdscr.addstr(5,3,'┗━━━━━━━━┛')     


        # 24x 22 가로x세로
        stdscr.addstr(0,15,'┏━━━━━━━━━━━━━━━━━━━━┓') 
        stdscr.addstr(1,15,'┃                    ┃')
        stdscr.addstr(2,15,'┃                    ┃')
        stdscr.addstr(3,15,'┃                    ┃')
        stdscr.addstr(4,15,'┃                    ┃')
        stdscr.addstr(5,15,'┃                    ┃')
        stdscr.addstr(6,15,'┃                    ┃')
        stdscr.addstr(7,15,'┃                    ┃')
        stdscr.addstr(8,15,'┃                    ┃')
        stdscr.addstr(9,15,'┃                    ┃')
        stdscr.addstr(10,15,'┃                    ┃')
        stdscr.addstr(11,15,'┃                    ┃')
        stdscr.addstr(12,15,'┃                    ┃')
        stdscr.addstr(13,15,'┃                    ┃')
        stdscr.addstr(14,15,'┃                    ┃')
        stdscr.addstr(15,15,'┃                    ┃')
        stdscr.addstr(16,15,'┃                    ┃')
        stdscr.addstr(17,15,'┃                    ┃')
        stdscr.addstr(18,15,'┃                    ┃')
        stdscr.addstr(19,15,'┃                    ┃')
        stdscr.addstr(20,15,'┃                    ┃')
        stdscr.addstr(21,15,'┗━━━━━━━━━━━━━━━━━━━━┛')    



        #  12x18
        stdscr.addstr(0,40,'┏━━━━━━━━┓') 
        stdscr.addstr(1,40,'┃        ┃')
        stdscr.addstr(2,40,'┃        ┃')
        stdscr.addstr(3,40,'┃        ┃')
        stdscr.addstr(4,40,'┃        ┃') 
        stdscr.addstr(5,40,'┃        ┃')              
        stdscr.addstr(6,40,'┃        ┃') 
        stdscr.addstr(7,40,'┃        ┃') 
        stdscr.addstr(8,40,'┃        ┃') 
        stdscr.addstr(9,40,'┃        ┃') 
        stdscr.addstr(10,40,'┃        ┃') 
        stdscr.addstr(11,40,'┃        ┃')
        stdscr.addstr(12,40,'┃        ┃')
        stdscr.addstr(13,40,'┃        ┃')
        stdscr.addstr(14,40,'┃        ┃')
        stdscr.addstr(15,40,'┃        ┃')
        stdscr.addstr(16,40,'┃        ┃')
        stdscr.addstr(17,40,'┗━━━━━━━━┛')         
        stdscr.refresh()

if __name__ == 'main':
    wrapper(PrintGameMap)
