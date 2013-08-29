#!/usr/bin/python

import curses

class Box:
  def __init__(self,screen):
    self.scr=screen
    self.getmax()
    self.reset()
    
  def reset(self):
    self.x=self.maxx/2
    self.y=self.maxy/2
    self.pen(False)
    self.scr.addstr(0,0,"squDOODLER  [d: Pen down  s: Pen up  a: Delete  c: Reset]")
    self.scr.move(self.y,self.x)
  
  def pen(self,val):
    if not val:
      self.pen_off=True
      self.scr.addstr(0,60,"[PEN: OFF]")
      self.scr.move(self.y,self.x)
    elif val:
      self.pen_off=False
      self.scr.addstr(0,60,"[PEN:  ON]")
      self.scr.move(self.y,self.x)
  
  def getmax(self):
    (self.maxy,self.maxx)=self.scr.getmaxyx()

  def show(self):
    try: self.scr.addch(self.y,self.x,43)
    except curses.error: pass
    self.scr.refresh()
  
  def move(self,side):
    if side=='up':  self.y-=1
    elif side=='dwn': self.y+=1
    elif side=='lft': self.x-=1
    elif side=='rht': self.x+=1
    
    if self.x<0: self.x=0
    if self.y<1: self.y=1
    if self.scr.is_wintouched(): self.getmax()
    if self.x>=self.maxx-1: self.x=self.maxx-1
    if self.y>self.maxy-1: self.y=self.maxy-1
    
    self.scr.move(self.y,self.x)
  
  def rem(self):
    self.scr.addch(ord(' '))
    
def game(self,scr):
  b=Box(scr)
  while True:
    if not b.pen_off:
      b.show()
      scr.refresh()
    c=scr.getch()
    if c==curses.KEY_UP:
      b.move('up')
    elif c==curses.KEY_DOWN:
      b.move('dwn')
    elif c==curses.KEY_LEFT:
      b.move('lft')
    elif c==curses.KEY_RIGHT:
      b.move('rht')
    elif c==ord('s'):
      b.pen(False)
      curses.curs_set(1)
    elif c==ord('d'):
      b.pen(True)
    elif c==ord('a'):
      b.rem()
    elif c==ord('c'):
      b.scr.erase()
      b.reset()  
    else: break
    
    
if __name__=='__main__':
  stdscr=curses.initscr()
  curses.wrapper(game,stdscr)
    
