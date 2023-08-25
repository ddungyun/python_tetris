

#-*- coding: utf-8 -*-

import curses
from curses import wrapper
import time
import keyboard
import tetrimino
from windows import game, setting, start

class Tetris:

    def __init__(self):
        self.map = [
            [0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0],
            ]

        self.score = 0
        self.rotate = 0
        self.block_type = 0
        self.block_x = 4
        self.block_y = 0
        self.drop_speed = 1
        self.st_speed = 1
        self.das = 0.131
        self.das_flag = False
        self.arr = 0.015
        self.arr_flag = False
        self.sdf = 0.01
        self.stop = 2
        self.map_height = 20
        self.map_width = 10
        self.game_box_x = 16
        self.game_box_y = 1
        
    def Game(self, stdscr):
        curses.curs_set(0)

        start_win = curses.newwin(30, 120, 0, 0)
        start_arrow = start.PrintStartMap(start_win)

        if start_arrow:
            setting.PrintSettingMap(stdscr)

        self.InitTimer()
        stdscr.erase()

        while True:

            self.down_end_timer = time.time()
            self.drop_speed = self.st_speed

            if keyboard.is_pressed('esc'):
                break

            if keyboard.is_pressed('down'):
                self.drop_speed = self.sdf

            if keyboard.is_pressed('left'):
                if not self.IsLeftWall():
                    if not self.CheckWidthObstacle(-1):
                        if not self.arr_flag:
                            if not self.das_flag:
                                self.InitDASTimer()
                                self.MoveBlock(-1)
                                self.das_flag = True
                            
                            elif self.das_flag:
                                self.DAS_end_timer = time.time()
                                DAS_elapsed_time = self.GetElapsedDASTime()

                                if  DAS_elapsed_time > self.das:
                                    self.InitARRTimer()
                                    self.MoveBlock(-1)
                                    self.arr_flag = True
                        else:
                            self.ARR_end_timer = time.time()
                            ARR_elapsed_time = self.GetElapsedARRTime()

                            if  ARR_elapsed_time > self.arr:
                                self.ARR_start_timer = self.ARR_end_timer
                                self.MoveBlock(-1)
            
            elif keyboard.is_pressed('right'):
                if not self.IsRightWall():
                    if not self.CheckWidthObstacle(1):
                        if not self.arr_flag:
                            if not self.das_flag:
                                self.InitDASTimer()
                                self.MoveBlock(1)
                                self.das_flag = True
                            
                            elif self.das_flag:
                                self.DAS_end_timer = time.time()
                                DAS_elapsed_time = self.GetElapsedDASTime()

                                if  DAS_elapsed_time > self.das:
                                    self.InitARRTimer()
                                    self.MoveBlock(1)
                                    self.arr_flag = True
                        else:
                            self.ARR_end_timer = time.time()
                            ARR_elapsed_time = self.GetElapsedARRTime()

                            if  ARR_elapsed_time > self.arr:
                                self.ARR_start_timer = self.ARR_end_timer
                                self.MoveBlock(1)

            keyboard.on_release_key('left', self.InitRelease)
            keyboard.on_release_key('right', self.InitRelease)
            
            down_elapsed_time = self.GetElapsedDownTime()

            # 일반적인 드랍 타이머
            if down_elapsed_time > self.drop_speed:
                if not self.IsFloor():
                    if not self.CheckHeightObstacle(1):
                        self.down_start_timer = self.down_end_timer
                        self.DownBlock()

            # 바닥에서 굳히는 타이머
            if self.stop > self.drop_speed:
                if down_elapsed_time > self.stop:
                    self.map[self.block_y][self.block_x] = 1
                    self.block_x = 4
                    self.block_y = 0
                    self.InitDownTimer()

            self.PrintMap(stdscr, self.game_box_y, self.game_box_x)

    def CheckLines(self):
        line_count = 0
        
        for y in range(self.map_height):
            line_flag = True
            for x in range(self.map_width):
                if not self.map[y][x]:
                    line_flag = False
            if line_flag:
                line_count += 1
        
        return line_count
                
    
    def CheckWidthObstacle(self, dir):
        if self.map[self.block_y][self.block_x + dir]:
            return True
        return False
    
    def CheckHeightObstacle(self, dir):
        if self.map[self.block_y + dir][self.block_x]:
            return True
        return False
    
    def IsFloor(self):
        if self.block_y < (self.map_height - 1):
            return False
        return True

    def IsLeftWall(self):
        if self.block_x > 0:
            return False
        return True

    def IsRightWall(self):
        if self.block_x < (self.map_width - 1):
            return False
        return True

    def InitRelease(self, evt):
        self.das_flag = False
        self.arr_flag = False

        self.InitDASTimer()
        self.InitARRTimer()

    def InitTimer(self):
        self.InitDownTimer()
        self.InitDASTimer()
        self.InitARRTimer()

    def InitDownTimer(self):
        self.down_start_timer = time.time()
        self.down_end_timer = time.time()

    def InitDASTimer(self):
        self.DAS_start_timer = time.time()
        self.DAS_end_timer = time.time()

    def InitARRTimer(self):
        self.ARR_start_timer = time.time()
        self.ARR_end_timer = time.time()
        
    def GetElapsedDownTime(self):
        return self.down_end_timer - self.down_start_timer

    def GetElapsedDASTime(self):
        return self.DAS_end_timer - self.DAS_start_timer

    def GetElapsedARRTime(self):
        return self.ARR_end_timer - self.ARR_start_timer

    def DownBlock(self):
        self.block_y += 1

    def MoveBlock(self, dir):
        self.block_x += dir

    def PrintMap(self, stdscr, begin_y=0, begin_x=0):

        stdscr.clear()
        game.PrintGameMap(stdscr)

        for y in range(20):
            for x in range(10):
                if self.map[y][x] != 0:
                    stdscr.addstr(y + begin_y, x * 2 + begin_x, u'▣')

                if (y == self.block_y) and (x == self.block_x):
                    stdscr.addstr(y + begin_y, x * 2 + begin_x, u'⭘')
        stdscr.refresh()


t = Tetris()

wrapper(t.Game)