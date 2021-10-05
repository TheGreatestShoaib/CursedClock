
import time
from curses import wrapper
from datetime import datetime
import curses

def main(stdscr):
    curses.curs_set(0)
    text = "Press AnyKey To Start CountDown"
    h,w = stdscr.getmaxyx()
    w = (w // 2) - len(text)//2
    h = h // 2
    stdscr.clear()
    stdscr.addstr(h,w,text)
    stdscr.refresh()
    key = stdscr.getch()

    if key != ord('q'):
        i =  0
        v = 0
        while True:
            stdscr.clear()
            timenow = str(datetime.now().strftime("%H:%M:%S") )
            h,w = stdscr.getmaxyx()
            x  = (w//2)-len(timenow)//2 
            y =  h//2
            
            curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_CYAN)

            stdscr.attron(curses.color_pair(1))
            stdscr.addstr(y,x, timenow)
            stdscr.attroff(curses.color_pair(1))

            stdscr.refresh()
            time.sleep(1)

wrapper(main)

