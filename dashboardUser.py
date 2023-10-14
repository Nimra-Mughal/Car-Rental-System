from tkinter import *
from PIL import Image,ImageTk
from brands import brands
from cars import cars
from customer import cust_win
from addbookings import booking


class userDashboard:
    def __init__(self,root):
        self.root=root
        self.root.title("Car Rental System")
        self.root.geometry("1550x800+0+0")

        img1=Image.open("Images\\rentacar.jpg")
        img1=img1.resize((1650,140),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)
        lblimg=Label(self.root,image=self.photoimg1,bd=4,relief=RIDGE)
        lblimg.place(x=0,y=0,width=1650,height=140)

        img2 = Image.open("Images\\logo.png")
        img2 = img2.resize((230, 140), Image.ANTIALIAS)
        self.photoimg2 = ImageTk.PhotoImage(img2)
        lblimg = Label(self.root, image=self.photoimg2, bd=4, relief=RIDGE)
        lblimg.place(x=0, y=0, width=230, height=140)

        lbltitle=Label(self.root,text="USER DASHBOARD",font=("times new roman",40,"bold"),bg="black",fg="gold",bd=4,relief=RIDGE)
        lbltitle.place(x=0,y=140,width=1650,height=50)

        main_frame=Frame(self.root,bd=4,relief=RIDGE)
        main_frame.place(x=0,y=190,width=1599,height=650)

        lblmenu = Label(main_frame, text="User Profile", font=("times new roman", 20, "bold"), bg="black",fg="gold", bd=4, relief=RIDGE)
        lblmenu.place(x=0, y=0, width=230)

        btn_frame = Frame(main_frame, bd=4, relief=RIDGE)
        btn_frame.place(x=0, y=38, width=228, height=190)

        # ==================Main Button=====================
        cust_btn=Button(btn_frame,text="CUSTOMER",command=self.cust_details,width=22, font=("times new roman", 14, "bold"), bg="black",fg="gold",bd=0,cursor="hand1")
        cust_btn.grid(row=0,column=0,pady=1)

        room_btn = Button(btn_frame, text="CARS", width=22,command=self.addcars, font=("times new roman", 14, "bold"), bg="black",fg="gold", bd=0, cursor="hand1")
        room_btn.grid(row=1, column=0, pady=1)

        details_btn = Button(btn_frame, text="BRANDS",command=self.add_brands, width=22, font=("times new roman", 14, "bold"), bg="black",fg="gold", bd=0, cursor="hand1")
        details_btn.grid(row=2, column=0, pady=1)

        report_btn = Button(btn_frame, text="BOOKING",command=self.booking, width=22, font=("times new roman", 14, "bold"), bg="black",fg="gold", bd=0, cursor="hand1")
        report_btn.grid(row=3, column=0, pady=1)

        logout_btn = Button(btn_frame, text="LOGOUT", width=22, font=("times new roman", 14, "bold"), bg="black",fg="gold", bd=0, cursor="hand1")
        logout_btn.grid(row=4, column=0, pady=1)

        img4 = Image.open("Images\\sidecar1.png")
        img4 = img4.resize((230, 230), Image.ANTIALIAS)
        self.photoimg4 = ImageTk.PhotoImage(img4)
        lblimg1 = Label(main_frame, image=self.photoimg4, bd=4, relief=RIDGE)
        lblimg1.place(x=0, y=225, width=230, height=230)

        img5 = Image.open("Images\\sidecar2.png")
        img5 = img5.resize((1410, 690), Image.ANTIALIAS)
        self.photoimg5 = ImageTk.PhotoImage(img5)
        lblimg1 = Label(main_frame, image=self.photoimg5, bd=4, relief=RIDGE)
        lblimg1.place(x=0, y=420, width=230, height=210)

        # ==================admin Dashboard============





        img3 = Image.open("Images\\img_1.png")
        img3 = img3.resize((1410, 690), Image.ANTIALIAS)
        self.photoimg3 = ImageTk.PhotoImage(img3)
        lblimg1 = Label(main_frame, image=self.photoimg3, bd=4, relief=RIDGE)
        lblimg1.place(x=225, y=0, width=1410, height=690)


    def add_brands(self):
        self.new_window=Toplevel(self.root)
        self.app=brands(self.new_window)

    def addcars(self):
        self.new_window=Toplevel(self.root)
        self.app=cars(self.new_window)

    def cust_details(self):
        self.new_window=Toplevel(self.root)
        self.app=cust_win(self.new_window)
    def booking(self):
        self.new_window = Toplevel(self.root)
        self.app = booking(self.new_window)


if __name__ == '__main__':
    root=Tk()
    obj=userDashboard(root)
    root.mainloop()