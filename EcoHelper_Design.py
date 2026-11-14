# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import tkinter as tk

class EcoHelper: 
    
    def __init__(self, page) :
        self.page = page
        self.page.title("EcoHelper")
        self.page.geometry("393x852")
        self.page.configure(bg="#236476")
        
        self.current_face = None
    
        self.splashPage()
    
    def splashPage(self) :
        if self.current_face is not None :
            self.current_face.destroy()
            
        self.current_face = tk.Frame(self.page)
        self.current_face.pack(expand = True)
            
        #SplashPage
        self.imgWelcomePage = tk.PhotoImage(file = "welcomeScreen.png")
        self.btnWelcomePage = tk.Button(self.current_face, image = self.imgWelcomePage, bg ="#236476",
                                        relief = "flat", bd = 0, highlightthickness= 0, borderwidth= 0,
                                        activebackground= "#236476", command = self.recyclingType)
        self.btnWelcomePage.pack(pady = 5)
        

    def recyclingType(self) : 
        
        if self.current_face is not None :
            self.current_face.destroy()
            
        self.current_face = tk.Frame(self.page, bg="#236476")
        self.current_face.pack(expand = True)

        #Select Type of Recycling
        self.imgHouseholdItems = tk.PhotoImage(file = "btnHousehold.png")
        self.btnHouseholdItems = tk.Button(self.current_face, image = self.imgHouseholdItems, bg="#236476", 
                              relief="flat", bd = 0, highlightthickness = 0, 
                              borderwidth = 0, activebackground="#236476", command = self.scan)
        self.imgElectronics = tk.PhotoImage(file = "btnElectronics.png")
        self.btnElectronics = tk.Button(self.current_face, image = self.imgElectronics, bg = "#236476",
                              relief="flat", bd = 0, highlightthickness = 0, activebackground="#236476",
                              command = self.scan)
        
        self.btnHouseholdItems.pack(pady = 5)
        self.btnElectronics.pack(pady = 5)

        #if btnHouseholdItems.click() :
            #buttonClicked = 'Household'
        #else :
            #buttonClicked = 'Electronics'
    
    def scan(self) :
        
        if self.current_face is not None :
            self.current_face.destroy()
            
        self.current_face = tk.Frame(self.page, bg="#236476")
        self.current_face.pack(expand = True)
        
        self.imgBackArrow = tk.PhotoImage(file = "btnBackArrowButton.png")
        self.btnBackArrow = tk.Button(self.current_face, image = self.imgBackArrow, bg = "#236476",
                                      relief = "flat", bd = 0, highlightthickness = 0, activebackground = "#236476",
                                      command = self.recyclingType)
        self.imgScan = tk.PhotoImage(file = "btnScanButton.png")
        self.btnScan = tk.Button(self.current_face, image=self.imgScan, bg="#236476", 
                                  relief="flat", bd=0, highlightthickness=0, activebackground="#236476")
       
        self.btnBackArrow.pack(pady = 5)
        self.btnScan.pack(pady = 5)
    
page = tk.Tk()
ecoHelper = EcoHelper(page)
page.mainloop()

    

