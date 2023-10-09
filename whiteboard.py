# whiteboard
from tkinter import *
from tkinter.colorchooser import askcolor
from tkinter import ttk
import tkinter as tk

root=Tk()
root.geometry("1050x570+150+50")
root.configure(bg="#f2f3f5")
root.resizable(False,False)
root.title("whiteboard")

current_x=0
current_y=0
color='black'

def locate_xy(work):
 global current_x,current_y
 current_x=work.x
 current_y=work.y

def addLine(work):
 global current_x,current_y
 canvas.create_line((current_x,current_y,work.x,work.y),width=get_current_value(),fill=color,capstyle=ROUND,smooth=TRUE)
 current_x,current_y=work.x,work.y

def show_color(new_color):
 global color
 color=new_color

def new_canvas():
 canvas.delete('all')
 display_pallete()

image_icon=PhotoImage(file="google.png")
root.iconphoto(False,image_icon)

imglgao=PhotoImage(file="cs1.png")
Label(root,image=imglgao).place(x=10,y=10)

eraser=PhotoImage(file="eraser.png")
Button(root,image=eraser,command=new_canvas).place(x=15,y=250)

colors=Canvas(root,bg="#ffffff",width=37,height=200,bd=0)
colors.place(x=15,y=20)


def display_pallete():
 id=colors.create_rectangle((10,10,30,30),fill="black")
 colors.tag_bind(id,'<Button-1>',lambda x: show_color('black'))

 id=colors.create_rectangle((10,40,30,60),fill="red")
 colors.tag_bind(id,'<Button-1>',lambda x: show_color('red'))

 id=colors.create_rectangle((10,70,30,90),fill="green")
 colors.tag_bind(id,'<Button-1>',lambda x: show_color('green'))

 id=colors.create_rectangle((10,100,30,120),fill="blue")
 colors.tag_bind(id,'<Button-1>',lambda x: show_color('blue'))

 id=colors.create_rectangle((10,130,30,150),fill="yellow")
 colors.tag_bind(id,'<Button-1>',lambda x: show_color('yellow'))
 
 id=colors.create_rectangle((10,160,30,180),fill="cyan")
 colors.tag_bind(id,'<Button-1>',lambda x: show_color('cyan'))

display_pallete()

canvas=Canvas(root,width=930,height=500,background="white",cursor="hand2")
canvas.place(x=100,y=10)

canvas.bind('<Button-1>',locate_xy)
canvas.bind('<B1-Motion>', addLine)

current_value=tk.DoubleVar()
def get_current_value():
 return '{: .2f}'.format(current_value.get())

def slider_changed(event):
 value_label.configure(text=get_current_value())

slider=ttk.Scale(root,from_=0,to=100,orient='horizontal',command=slider_changed,variable=current_value)
slider.place(x=30,y=530)

value_label=ttk.Label(root,text=get_current_value())


root.mainloop() 