# -*- coding: utf-8 -*-
"""
HackED 2026 - EcoHelper

"""

import tkinter as tk

TITLE = ("Lexend", 35, "bold")

class tkinterApp(tk.Tk):

    def __init__(self, *args, **kwargs): 
        
        tk.Tk.__init__(self, *args, **kwargs)
        
        self.title("EcoHelper")
        self.geometry("393x852")
        self.configure(bg="#236476")
        
        container = tk.Frame(self)  
        container.pack(side = "top", fill = "both", expand = True) 
 
        container.grid_rowconfigure(0, weight = 1)
        container.grid_columnconfigure(0, weight = 1)
 
        self.frames = {}  
 
        for F in (SplashPage, RecyclingType, Scan):
 
            frame = F(container, self)
 
            # initializing frame of that object from
            self.frames[F] = frame 
 
            frame.grid(row = 0, column = 0, sticky ="nsew")
 
        self.show_frame(SplashPage)
 
    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()

class SplashPage(tk.Frame):
    
    def __init__(self, parent, controller): 
        
        tk.Frame.__init__(self, parent, bg="#236476")        
        
        self.lblTitle = tk.PhotoImage(file="EcoHelperTitle.png")
        title = tk.Label(self, image=self.lblTitle, bg="#236476", fg="#FFF")
        title.pack(expand=True)
        
        self.after(1500, lambda: controller.show_frame(RecyclingType))

class RecyclingType(tk.Frame):
    
    def __init__(self, parent, controller): 
        
        tk.Frame.__init__(self, parent, bg="#236476")
        self.columnconfigure(0, weight=1)
        self.rowconfigure((0, 3), weight=1)
        
        self.promptRecycling = tk.PhotoImage(file="PromptRecycling.png")
        lblRecycling = tk.Label(self, image=self.promptRecycling, bg="#236476", fg="#FFF")
        lblRecycling.grid(row=0, column=0, sticky="n")
        
        self.imgHouseholdItems = tk.PhotoImage(file = "btnHousehold.png")
        btnHouseholdItems = tk.Button(self, image=self.imgHouseholdItems, bg="#236476", relief="flat", 
                                      bd=0, highlightthickness=0, activebackground="#236476", 
                                      command = lambda: controller.show_frame(Scan))
        btnHouseholdItems.grid(row=1, column=0, padx=10, pady=10)
        
        self.imgElectronics = tk.PhotoImage(file = "btnElectronics.png")
        btnElectronics = tk.Button(self, image=self.imgElectronics, bg="#236476", relief="flat", 
                                   bd=0, highlightthickness=0, activebackground="#236476",
                                   command = lambda: controller.show_frame(Scan))
        btnElectronics.grid(row=2, column=0, padx=10, pady=10)

class Scan(tk.Frame):
    
    def __init__(self, parent, controller):
        
        tk.Frame.__init__(self, parent, bg="#236476")
        self.columnconfigure(0, weight=1)
        self.rowconfigure((0, 3), weight=1)
        
        self.imgBack = tk.PhotoImage(file = "btnBack.png")
        btnBack = tk.Button(self, image=self.imgBack, bg="#236476", relief="flat", 
                            bd=0, highlightthickness=0, activebackground="#236476", 
                            command = lambda: controller.show_frame(RecyclingType))
        btnBack.grid(row=0, column=0, sticky="nw", padx=10, pady=10)
        
        self.imgScan = tk.PhotoImage(file = "btnScan.png")
        btnScan = tk.Button(self, image=self.imgScan, bg="#236476", relief="flat", 
                            bd=0, highlightthickness=0, activebackground="#236476")
        btnScan.grid(row=3, column=0, padx=10, pady=10)
        
class DataPage(tk.Frame):
    
    def __init__(self, parent, controller):
        
        tk.Frame.__init__(self, parent, bg="#236476")
        

app = tkinterApp()
app.mainloop()
