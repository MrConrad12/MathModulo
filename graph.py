from tkinter import * 
from math import *
WIDTH = 500
HEIGHT = 640


class Graph(Canvas):
    '''canvas showing the modulo calcul'''

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.c_width = kwargs.get('width') / 2
        self.c_height = kwargs.get('height') / 2
        self._radius = 250
        self._pos = []
        self.color = 'white'
        
    def show_modulo(self, multi, modulo):
        self.delete(ALL)
        self._pos.clear()
        if not modulo:
            modulo = 1
        modulo *= 10
        pas = 2*pi / modulo
        self.draw_circle()
        
        for n in range(0, modulo):
            ang = n * pas
            x = round(cos(ang - pi/2) * self._radius + self.c_width)
            y = round(sin(ang - pi/2) * self._radius + self.c_height)
            self._pos.append((x, y))
        
        for n in range(0, modulo):
            a = n % modulo
            b = (n * multi) % modulo
            b = int(b) 

            #self.color = 'blue' if n <= (modulo / 2) else 'red'
            if n <= (modulo/4):
                self.color = 'red'
            elif (modulo/4) <= n <= (modulo/2):
                self.color = 'green'
            elif (modulo/2) <= n <= (modulo*3/4):
                self.color = 'blue'
            elif (modulo*3/4) <= n <=  modulo:
                self.color = 'cyan'

            self.create_line(
                self._pos[a][0], 
                self._pos[a][1], 
                self._pos[b][0], 
                self._pos[b][1], 
                fill=self.color)
        
    def draw_circle(self):
        self.create_oval(
            self.c_width - self._radius, 
            self.c_height - self._radius,
            self.c_width + self._radius, 
            self.c_height + self._radius, 
            outline= 'black'
            )

if __name__ == '__main__':
    root = Tk()
    root.update()
    test = Graph(root, width=500, height=700, bg='black')
    test.pack()
    i = 1
    a = 10
    timer = 0
    def add():
        global i, a, timer
        test.show_modulo(multi=i, modulo=a)
        
        timer += 0.05
        # in dual incrementation stop at modulo 175 and multi 17.5
        if a <= 300 :
            
            i += 0.1
            a += 0
            root.after(60, add)
        
    add()
    root.mainloop()