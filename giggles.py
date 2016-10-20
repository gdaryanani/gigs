from graphics import *
import time

def main():
    win = GraphWin("test",1280,710)
    win.setBackground("green")
    message = Text(Point(300,400), "Hello!")
    message.setSize(100)
    message.setTextColor("blue")
    message.draw(win)
    c = Circle(Point(500,500), 100)
    c.draw(win)
    win.getMouse()
    time.sleep(1)

main()
