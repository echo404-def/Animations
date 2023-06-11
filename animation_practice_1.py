#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 11 15:12:51 2023

@author: echo.
"""

import tkinter as tk

class Main:
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry("500x300")
        
        self.ch_r = tk.PhotoImage(file="cha1.png")
        self.ch_l = tk.PhotoImage(file="cha2.png")
        self.bg_b = tk.PhotoImage(file="bg1.png")
        self.bg_f = tk.PhotoImage(file="bg2.png")
        
        self.canvas = tk.Canvas(self.root, width=500, height=300)
        self.canvas.pack()
        
        self.speed = 10
        self.x = 100
        self.y = 220
        
        self.state = {"x": self.speed, "y": 0, "image": self.ch_r}
        
        self.update()
        
    def update(self):
        self.canvas.create_image(250, 150, image=self.bg_b)
        self.move_character()
        self.canvas.create_image(250, 150, image=self.bg_f)
        self.root.after(500, self.update)
        
    def move_character(self):
        if self.x >= 450:
            self.state["x"] = self.speed * -1
            self.state["image"] = self.ch_l
        elif self.x <= 50:
            self.state["x"] = self.speed
            self.state["image"] = self.ch_r
            
        self.x += self.state["x"]
        self.canvas.create_image(self.x, self.y, image=self.state["image"])
        
if __name__ == "__main__":
    f = Main()
    f.root.mainloop()
