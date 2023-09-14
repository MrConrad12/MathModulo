from tkinter import *
import time


class Input(Frame):
    """input for setting value of modulo or multi"""
    def __init__(self, *args, text='', optionlabel='able', command=None, **kwargs):
        super().__init__(*args, **kwargs)
        self._apply = IntVar()
        self._inputs = {}

        Label(self, text=text, width=10).pack(side=LEFT)

        self._inputs['input'] = Spinbox(
            self, from_=2, to=3000, state=NORMAL, 
            justify=CENTER, command=command)
            
        self._inputs['check'] = Checkbutton(
            self, text=optionlabel,variable=self._apply, width=20,
            offvalue=0, onvalue=1, command=self.activing)

        self._inputs['input'].pack(side=LEFT)
        self._inputs['check'].pack(side=LEFT)
        self.pack( expand=YES, padx=5, pady=5)

    def activing(self):
        """active the input"""
        (state, text)= (NORMAL, 'able') if self._apply.get() else (DISABLED, 'disable')
        self._inputs['check'].configure(text=text)
        self._inputs['input'].configure(state=state)

    @property
    def value(self):
        """return value in the input"""
        val = self._inputs['input'].get()
        return int(val)

    def abled(self):
        for val in self._inputs.values():
            val.configure(state=NORMAL)
    
    def disable(self):
        for val in self._inputs.values():
            val.configure(state=DISABLED)


class Control(LabelFrame):
    """controler for manual configuration"""
    def __init__(self, *args, **kwargs):
        super().__init__(*args,**kwargs)
        self.configure(text='Manual config')

        self.modulo = 1
        self.multi = 0
        self._max_modulo = 200
        self._max_multi = 300
        self.command = []

        frame = Frame(self)
        self.input_modulo = Input(self, text='modulo : ', command=self.spin_value)
        self.input_mutli = Input(self, text='multi : ', command=self.spin_value)
        frame.pack(fill=X, padx=5, pady=5,ipadx=5, ipady=5, side=TOP)

        #scale for module
        self.command.append(Scale(
            self, length=300, orient=HORIZONTAL, sliderlength=10,
            label='modulo :', from_=0, to=self._max_modulo,
            command=self.set_modulo,relief=GROOVE, bd=2
            ).pack(fill=X, padx=5, pady=5,ipadx=5, ipady=5, side=TOP))

        # scale for multi
        self.command.append(Scale(
            self, length=300, orient=HORIZONTAL, sliderlength=10, 
            label='multi :', from_=0, to=self._max_multi, 
            command=self.set_multi,relief=GROOVE, bd=2
            ).pack(fill=X, padx=5, pady=5,ipadx=5, ipady=5,side=TOP))
    
    def spin_value(self):
        self.event_generate('<Control-Z>')
        self.multi = self.input_mutli.value
        self.modulo = self.input_modulo.value

    def set_multi(self, multi=0):
        self.multi = int(multi)
        self.event_generate('<Control-Z>')

    def set_modulo(self, modulo=1):
        self.modulo = int(modulo)
        self.event_generate('<Control-Z>')


class Auto(LabelFrame):
    """configuration for automatic animation"""
    def __init__(self, *args, graph=None, **kwargs):
        super().__init__(*args,**kwargs)
        self.configure(text='Auto config')
        self.running = False
        self._graph = graph
        self._modulo = 2
        self._multi = 2
        self._speed = 1
        self._input_modulo = Input(self, text='modulo')
        self._input_multi = Input(self, text='multi')
        
        self._multi_ind = 1
        self._modulo_ind = 1

        frame = Frame(self, width=40)
        Label(frame, text='Speed', width=10).pack(side=LEFT)
        self.speed_spin = Spinbox(frame, from_=1, to=7)
        self.speed_spin.pack(side=LEFT, expand=NO)
        frame.pack(side=TOP, expand=YES, padx=5, pady=5)

        Button(frame, text='STOP', width=10, command=self.stop).pack(side=RIGHT, expand=YES, padx=3)
        Button(frame, text='RUN', width=10, command=self.run).pack(side=RIGHT, expand=YES, padx=3)
        

    def run(self):
        """run animation"""
        self._multi_ind = 1
        self._modulo_ind = 1
        self._modulo = self._input_modulo.value
        self._multi = self._input_multi.value
        self._speed = int(self.speed_spin.get())
        self.running = True
        self.event_generate('<Control-A>')

    def stop(self):
        """stop animation"""
        self.running = False
        self.event_generate('<Control-A>')


class Command(Frame):
    """command for automatic and manual configuration"""
    def __init__(self, *args, graph = None, **kwargs):
        super().__init__(*args, **kwargs)
        self.configure(relief=GROOVE, bd=4)
        self.graph = graph
        self.choice = IntVar()

        self.radio1 = Radiobutton(self, text='activate', variable=self.choice, value=1)
        self.radio2 = Radiobutton(self, text='activate', variable=self.choice, value=0)
        self.auto = Auto(self,graph=graph)
        self.control = Control(self)

        self.radio1.pack(side=TOP)
        self.auto.pack(fill=X)
        self.radio2.pack(side=TOP)
        self.control.pack(fill=X)

        self.master.bind('<Control-A>', self.animation)
        self.master.bind('<Control-Z>', self.draw)

    def draw(self, event):
        """draw lines in the canvas"""
        self.auto.running = False       
        self.graph.show_modulo(
            multi = self.control.multi + 1,
            modulo = self.control.modulo + 1
        )

    def animation(self, event=None):
        if self.auto.running:
            self.graph.show_modulo(
                multi = self.auto._multi_ind,
                modulo = self.auto._modulo_ind
            )
            if self.auto._multi_ind <= self.auto._multi:
                self.auto._multi_ind += 0.1
            if self.auto._modulo_ind <= self.auto._modulo:
                self.auto._modulo_ind += 1
            if not(
                self.auto._multi_ind == self.auto._multi and 
                self.auto._modulo_ind == self.auto._modulo):
                self.after(int(500/self.auto._speed), self.animation)
            else: 
                self.auto.running = False
                self.graph.delete(ALL)
