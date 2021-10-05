
import time
from curses import wrapper
from datetime import datetime
import curses
from subprocess import Popen, PIPE
from pprint import pprint

def stdout(cmd):
    output = Popen(cmd,shell=True,stdout=PIPE).communicate()[0]
    return output.decode()


def makelist(string):
    strg = string.split("\n")
    return strg 


command = "figlet -f small shoaib"


#breh = stdout(command)
#hehe = makelist(breh)

#pprint(hehe)

#print(len(hehe))


def main(stdscr):
    curses.curs_set(0)
    text = "Press AnyKey To Start CountDown"
    #text = stdout(command)
    h,w = stdscr.getmaxyx()
    w = (w // 2) - len(text)//2
    h = h // 2
    print(text)
    #time.sleep(3)
    stdscr.clear()
    stdscr.addstr(h,w,text)
    stdscr.refresh()
    key = stdscr.getch()

    if key != ord('q'):
        i =  0
        v = 0
        while True:
            stdscr.clear()
            timenow = str(datetime.now().strftime("%H : %M : %S") )
            list_string = stdout(f"figlet -f small {timenow}")
            raw_list = makelist(list_string)
    

            for index , text in enumerate(raw_list):
                h,w = stdscr.getmaxyx()
                x  = (w//2)-len(text)//2 
                y =  h//2 - len(raw_list)//2 + index 
            
                curses.init_pair(1, curses.COLOR_CYAN, curses.COLOR_BLACK)

                stdscr.attron(curses.color_pair(1))
                stdscr.addstr(y,x, text)
                stdscr.attroff(curses.color_pair(1))

            stdscr.refresh()
            time.sleep(1)

wrapper(main)


