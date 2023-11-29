import datetime
import tkinter as tk
from tkinter import filedialog
from tkVideoPlayer import TkinterVideo
from video import video
from tkinter import *
import matplotlib.pyplot as plt
#import matplotlib.image as mpimg
import numpy as np
import cv2
import os
import glob
from moviepy.video.io.VideoFileClip import VideoFileClip
from tkinter import ttk
import subprocess
import sys
import PIL
import tkinter as tk
import pyttsx3
from PIL import ImageTk
from PIL import Image
import tkinter
import PIL.Image
import PIL.ImageTk
from moviepy.editor import VideoFileClip
#Import everything needed to edit/save/watch video clips
#from moviepy import *
from IPython.display import HTML
#from IPython.display import Image
import win32gui, win32con
import tkinter as tk
from tkVideoPlayer import TkinterVideo


hide = win32gui.GetForegroundWindow()
win32gui.ShowWindow(hide , win32con.SW_HIDE)
def ani():
    
    window = tk.Toplevel()
   
    window.wm_title("Process is Running")
    file="loading.gif"

    info = Image.open(file)

    frames = info.n_frames  # gives total number of frames that gif contains

    # creating list of PhotoImage objects for each frames
    im = [tk.PhotoImage(file=file,format=f"gif -index {i}") for i in range(frames)]

    count = 0
    anim = None
    def animation(count):
        global anim
        im2 = im[count]

        gif_label.configure(image=im2)
        count += 1
        if count == frames:
            count = 0
        anim = window.after(50,lambda :animation(count))

    gif_label = tk.Label(window,image="")
    gif_label.pack()
    animation(count)
    process = subprocess.Popen([ 'python.exe',"main.py"])
    
    def check_process():
        if process.poll() is None:
            # process is still running, check again 100ms later
            window.after(100, check_process)
        else:
            # prcoess is completed, destroy the window
            window.destroy()
    check_process() # start the checking
    
#([ 'python.exe',"LCDSS.py"])
def exit1():
    root2.destroy()


#-----------
def v1():
    process = subprocess.Popen([ 'python.exe',"video.py"])
    
    def check_process():
        if process.poll() is None:
            # process is still running, check again 100ms later
            window.after(100, check_process)
        else:
            # prcoess is completed, destroy the window
            window.destroy()
    check_process() # start the checking
    

#-----------
    
root2 = Tk()
root2.geometry("1100x700")
root2.configure(bg='white')
root2.title("Parking Lot Counter")
#Define the PhotoImage Constructor by passing the image file
img= PhotoImage(file='img_final.png', master= root2)
img_label= Label(root2,image=img)
#define the position of the image
img_label.grid(row=0,column=1)
button_publish=Button(root2,text=" START ",padx=42,pady=10,bg="green",fg="white",command=ani)
button_publish.grid(row=1,column=1)
button_=Button(root2,text=" VIDEO  ",padx=41,pady=10,bg="yellow",fg="black",command=v1)
button_.grid(row=2,column=1)
button_return1=Button(root2,text=" EXIT ",padx=42,pady=10,bg="red",fg="black",command=exit1)
button_return1.grid(row=3,column=1)
root2.mainloop()
