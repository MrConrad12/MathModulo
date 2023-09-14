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

