from tkinter import *
from PIL import Image,ImageTk
from tkinter import ttk
import random
import pymysql
from tkinter import messagebox



class contact:
    def __init__(self,root):
        self.root=root
        self.root.title("Customer")
        self.root.geometry("1400x610+225+218")

        lbltitle = Label(self.root, text="CONTACT HERE", font=("times new roman", 18, "bold"), bg="black",fg="gold", bd=4, relief=RIDGE)
        lbltitle.place(x=0, y=0, width=1370, height=50)

        img2 = Image.open("Images\\logo.png")
        img2 = img2.resize((100, 45), Image.ANTIALIAS)
        self.photoimg2 = ImageTk.PhotoImage(img2)
        lblimg = Label(self.root, image=self.photoimg2, bd=0, relief=RIDGE)
        lblimg.place(x=5, y=2, width=100, height=45)

        labelframeleft = LabelFrame(self.root, bd=2, relief=RIDGE, text="Contact Us",font=("times new roman", 18, "bold"), padx=5)
        labelframeleft.place(x=30, y=50, width=1320, height=550)

        #===================================================

        contact_frame = Frame(labelframeleft, bd=2, relief=RIDGE)
        contact_frame.place(x=100, y=35, width=600, height=400)

        head = Label(contact_frame, text="SEND MESSAGE", font=("times new roman", 20, "bold"), padx=2, pady=6)
        head.grid(row=0, column=0,padx=180,pady=20, sticky=W)

        name = Label(contact_frame, text="Full Name", font=("times new roman", 12, "bold"), padx=2, pady=6)
        name.grid(row=1, column=0,padx=150, sticky=W)
        self.name = ttk.Entry(contact_frame, width=35, font=("times new roman", 13, "bold"))
        self.name.grid(row=2, column=0,padx=150)

        email = Label(contact_frame, text="Email", font=("times new roman", 12, "bold"), padx=2, pady=6)
        email.grid(row=3, column=0,padx=150, sticky=W)
        self.email = ttk.Entry(contact_frame, width=35, font=("times new roman", 13, "bold"))
        self.email.grid(row=4, column=0, padx=150)

        msg = Label(contact_frame, text="Your Message", font=("times new roman", 12, "bold"), padx=2, pady=6)
        msg.grid(row=5, column=0,pady=5,padx=150, sticky=W)
        self.msg = ttk.Entry(contact_frame, width=35, font=("times new roman", 13, "bold"))
        self.msg.grid(row=6, column=0,padx=150)


        submit=Button(contact_frame,text="SEND",command=self.RegData,font=("times new roman",13, "bold"),bg="black",fg="gold",width=9)
        submit.grid(row=7,column=0,padx=150,pady=5)

    def RegData(self):
        if self.name.get()=="" or self.email.get()=="" or self.msg.get()=="":
            messagebox.showerror("Error","All feilds are mendatory",parent=self.root)
        else:
            # messagebox.showinfo("Error","Sucessfully registerd",parent=self.root)
            try:
                con = pymysql.connect(host="localhost", user="root", password="", database="carRentalSystem")
                cursor = con.cursor()
                cursor.execute(
                    "insert into contact (name,email,msg) values (%s,%s,%s)",
                    (
                        self.name.get(),
                        self.email.get(),
                        self.msg.get()))
                con.commit()
                con.close()
                messagebox.showinfo("Success", "Registered Successfully", parent=self.root)
                self.ClearData()
            except Exception as ex:
                messagebox.showerror("Error", f"Error due to {str(ex)}", parent=self.root)

    def ClearData(self):
        self.name.delete(0, END),
        self.email.delete(0, END),
        self.msg.delete(0, END)


if __name__ == '__main__':
    root=Tk()
    obj=contact(root)
    root.mainloop()