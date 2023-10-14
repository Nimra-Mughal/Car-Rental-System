from tkinter import *
from PIL import Image,ImageTk
from tkinter import ttk
import random
import pymysql
from tkinter import messagebox



class about:
    def __init__(self,root):
        self.root=root
        self.root.title("Customer")
        self.root.geometry("1400x610+225+218")

        lbltitle = Label(self.root, text="About OUR SYSTEM", font=("times new roman", 18, "bold"), bg="black",fg="gold", bd=4, relief=RIDGE)
        lbltitle.place(x=0, y=0, width=1370, height=50)

        img2 = Image.open("Images\\logo.png")
        img2 = img2.resize((100, 45), Image.ANTIALIAS)
        self.photoimg2 = ImageTk.PhotoImage(img2)
        lblimg = Label(self.root, image=self.photoimg2, bd=0, relief=RIDGE)
        lblimg.place(x=5, y=2, width=100, height=45)

        labelframeleft = LabelFrame(self.root, bd=2, relief=RIDGE, text="About Us ",font=("times new roman", 18, "bold"), padx=5)
        labelframeleft.place(x=20, y=50, width=1320, height=550)



if __name__ == '__main__':
    root=Tk()
    obj=about(root)
    root.mainloop()