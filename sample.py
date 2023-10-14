from tkinter import *
from PIL import Image,ImageTk
from customer import cust_win
from brands import brands
from cars import cars
from about import about
from contact import contact
from login import Login_window
from register import Register


class adminDashboard:
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

        lbltitle=Label(self.root,text="CAR RENTAL SYSTEM",font=("times new roman",40,"bold"),bg="black",fg="gold",bd=4,relief=RIDGE)
        lbltitle.place(x=0,y=140,width=1650,height=50)

        signin = Button(self.root, text="SignIn",command=self.signin, font=("times new roman", 15, "bold"), bg="black",fg="gold", bd=0, relief=RIDGE)
        signin.place(x=1350, y=150, width=100, height=30)

        signup = Button(self.root, text="SignUp",command=self.signup, font=("times new roman", 15, "bold"), bg="black",fg="gold", bd=0, relief=RIDGE)
        signup.place(x=1440, y=150, width=100, height=30)

        main_frame=Frame(self.root,bd=4,relief=RIDGE)
        main_frame.place(x=0,y=190,width=1599,height=650)

        lblmenu = Label(main_frame, text="MENU", font=("times new roman", 20, "bold"), bg="black",fg="gold", bd=4, relief=RIDGE)
        lblmenu.place(x=0, y=0, width=230)

        btn_frame = Frame(main_frame, bd=4, relief=RIDGE)
        btn_frame.place(x=0, y=38, width=228, height=190)

        # ==================Main Button=====================
        cust_btn=Button(btn_frame,text="Home",command=self.cust_details,width=22, font=("times new roman", 14, "bold"), bg="black",fg="gold",bd=0,cursor="hand1")
        cust_btn.grid(row=0,column=0,pady=1)

        room_btn = Button(btn_frame, text="BRANDS",command=self.brand_details, width=22, font=("times new roman", 14, "bold"), bg="black",fg="gold", bd=0, cursor="hand1")
        room_btn.grid(row=1, column=0, pady=1)

        details_btn = Button(btn_frame, text="CARS",command=self.car_details, width=22, font=("times new roman", 14, "bold"), bg="black",fg="gold", bd=0, cursor="hand1")
        details_btn.grid(row=2, column=0, pady=1)

        # report_btn = Button(btn_frame, text="ABOUTUS",command=self.about_details, width=22, font=("times new roman", 14, "bold"), bg="black",fg="gold", bd=0, cursor="hand1")
        # report_btn.grid(row=3, column=0, pady=1)

        logout_btn = Button(btn_frame, text="CONTACTUS",command=self.contact_details, width=22, font=("times new roman", 14, "bold"), bg="black",fg="gold", bd=0, cursor="hand1")
        logout_btn.grid(row=3, column=0, pady=1)

        img3 = Image.open("Images\\sidecar2.png")
        img3 = img3.resize((1410, 690), Image.ANTIALIAS)
        self.photoimg3 = ImageTk.PhotoImage(img3)
        lblimg1 = Label(main_frame, image=self.photoimg3, bd=4, relief=RIDGE)
        lblimg1.place(x=225, y=0, width=1410, height=690)

        img4 = Image.open("Images\\sidecar1.png")
        img4 = img4.resize((230, 250), Image.ANTIALIAS)
        self.photoimg4 = ImageTk.PhotoImage(img4)
        lblimg1 = Label(main_frame, image=self.photoimg4, bd=4, relief=RIDGE)
        lblimg1.place(x=0, y=180, width=230, height=260)

        img5 = Image.open("Images\\sidecar2.png")
        img5 = img5.resize((230, 250), Image.ANTIALIAS)
        self.photoimg5 = ImageTk.PhotoImage(img5)
        lblimg1 = Label(main_frame, image=self.photoimg5, bd=4, relief=RIDGE)
        lblimg1.place(x=0, y=420, width=230, height=250)

    def cust_details(self):
        self.new_window=Toplevel(self.root)
        self.app=adminDashboard(self.new_window)

    def brand_details(self):
        self.new_window=Toplevel(self.root)
        self.app=brands(self.new_window)

    def car_details(self):
        self.new_window=Toplevel(self.root)
        self.app=cars(self.new_window)

    def contact_details(self):
        self.new_window=Toplevel(self.root)
        self.app=contact(self.new_window)

    def about_details(self):
        self.new_window=Toplevel(self.root)
        self.app=about(self.new_window)

    def signin(self):
        self.new_window = Toplevel(self.root)
        self.app = Login_window(self.new_window)

    def signup(self):
        self.new_window = Toplevel(self.root)
        self.app = Register(self.new_window)



if __name__ == '__main__':
    root=Tk()
    obj=adminDashboard(root)
    root.mainloop()