import tkinter as tk
import pygame
from tkinter.font import Font
from PIL import Image, ImageTk

class Countdown(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        #images:
        self.empty_blue= ImageTk.PhotoImage(Image.open("CoreScreenBlueEmpty.png"))
        self.empty_blue_happy= ImageTk.PhotoImage(Image.open("CoreScreenBlueHappy.png"))
        self.empty_red= ImageTk.PhotoImage(Image.open("CoreScreenRedEmpty.png"))
        self.empty_red_angry= ImageTk.PhotoImage(Image.open("CoreScreenRedAngry.png"))
        self.current_background = self.empty_blue
        blank = ImageTk.PhotoImage(Image.open("Blank.png"))
        #Background Image:
        self.background_label = tk.Label(self, image=self.current_background)
        self.background_label.photo=self.current_background
        self.background_label.place(x=0, y=0, relwidth=1, relheight=1)
        #Default Settings
        self.wm_attributes('-fullscreen', 1)
        self.start = False
        self.text_size = 11
        pygame.init()
        pygame.mixer.init()
        

        
        self.label = tk.Label(self, image=blank, text="", compound=tk.CENTER, height=0, width=0)
        self.label.photo = blank
        self.label.pack()
        self.configure(background="black")
        #Total time
        self.remaining = 35
        #Key bindings
        self.bind('<Escape>', self.escape_key)
        self.bind('<Control-b>', self.bl_key)
        self.bind('<Control-s>', self.br_key)
        self.bind('<Control-q>', self.q_key)
        self.bind('<Control-w>', self.w_key)
        self.bind('<Control-e>', self.e_key)
        self.bind('<Control-n>', self.n_key)
        self.bind('<Control-h>', self.h_key)
        self.bind('<Control-t>', self.t_key)
        self.bind('<Control-c>', self.c_key)
        self.bind('<Control-p>', self.p_key)
     
        # Colors
        self.foreground_color = "white"

        # Sounds
        self.background_sound = None
        self.text = None
        #self.text = tk.Text(self, foreground=self.foreground_color,
                            #background="black", insertbackground="green",
                            #font=("Courier",self.text_size))
        #self.text.insert("end", raven)
        #self.text.focus()
        #self.text.pack(fill="both", expand=True)
        #Text Box
        self.text = tk.Text(self, foreground="white", height= 10, width = 50,
                            background="black", insertbackground="green",
                            font=("Calibri",30))

        self.text.focus()

        self.display_time()

    def countdown(self):
        sound = None
        if self.remaining <= 0:
            self.label.configure(text="time's up!", font=("Times New Roman", 44),
                                 foreground="white")
            self.text = ""
        elif self.start:
            self.display_time()
            self.remaining -= 1
            self.after(1000, self.countdown)

    def display_time(self):
        x = self.remaining
        seconds = x % 60
        x //= 60
        minutes = x % 60
        x //= 60
        hours = x % 24
        self.label.configure(text= "%02d:%02d:%02d" % (hours,minutes,seconds),
                             background="black", foreground=self.foreground_color,
                             font=("Calibri", 44))
        #if self.start:
            #if self.text_size != 44:
                #self.text_size = 44
                #self.text.delete(1.0,"end")
                #self.text.configure(font=("Courier", self.text_size))

    def escape_key(self,event):
        print("Quitting...")
        self.destroy()
    def bl_key(self,event):
        print("True...")
        if not self.start:
            self.start = True
            self.countdown()
        #self.remaining -=1
    def br_key(self,event):
        print("False...")
        if self.start:
            self.start = False
    def q_key(self,event):
        self.background_label.configure(image=self.empty_blue_happy)
    def w_key(self,event):
        self.background_label.configure(image=self.empty_red)
    def e_key(self,event):
        self.background_label.configure(image=self.empty_red_angry)
    def n_key(self,event):
        sound = pygame.mixer.Sound("corevo-a2-Alex.wav")
        sound.set_volume(1.0)
        sound.play()
    def h_key(self,event):
        if self.background_sound: 
            self.background_sound.stop()
        self.background_sound = pygame.mixer.Sound("happy_space.wav")
        self.background_sound.set_volume(.7)
        self.background_sound.play()
    def t_key(self,event):
        if self.background_sound: 
            self.background_sound.stop()
        self.background_sound = pygame.mixer.Sound("dark_space.wav")
        self.background_sound.set_volume(.7)
        self.background_sound.play()
    def c_key(self,event):
        self.text.pack()
    def p_key(self,event):
        if self.text:
            self.text.delete(1.0,"end")
            self.text.pack_forget()


if __name__ == "__main__":

    app = Countdown()

    app.mainloop()
