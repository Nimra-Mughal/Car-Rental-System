from tkinter import *
from tkinter import messagebox

import pymysql
from PIL import Image,ImageTk
from addbrands import add_brands
from addcars import addcars
from customer import cust_win
from contact import contact
from book import booking
from registerUser import reg
from quiry import qr
from profile import profile


class adminDashboard:
    def __init__(self,root):
        self.root=root
        self.root.title("Car Rental System")
        self.root.geometry("1550x800+0+0")

        self.user=StringVar()




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

        lbltitle=Label(self.root,text="ADMIN DASHBOARD",font=("times new roman",40,"bold"),bg="black",fg="gold",bd=4,relief=RIDGE)
        lbltitle.place(x=0,y=140,width=1650,height=50)

        main_frame=Frame(self.root,bd=4,relief=RIDGE)
        main_frame.place(x=0,y=190,width=1599,height=650)

        lblmenu = Button(main_frame, text="User Profile",command=self.pro, font=("times new roman", 18, "bold"), bg="black",fg="gold", bd=4, relief=RIDGE)
        lblmenu.place(x=0, y=0, width=230)

        btn_frame = Frame(main_frame, bd=4, relief=RIDGE)
        btn_frame.place(x=0, y=38, width=228, height=190)

        # ==================Main Button=====================
        cust_btn=Button(btn_frame,text="QUIRIES",command=self.qr,width=22, font=("times new roman", 14, "bold"), bg="black",fg="gold",bd=0,cursor="hand1")
        cust_btn.grid(row=0,column=0,pady=1)

        room_btn = Button(btn_frame, text="CARS", width=22,command=self.addcars, font=("times new roman", 14, "bold"), bg="black",fg="gold", bd=0, cursor="hand1")
        room_btn.grid(row=1, column=0, pady=1)

        details_btn = Button(btn_frame, text="BRANDS",command=self.add_brands, width=22, font=("times new roman", 14, "bold"), bg="black",fg="gold", bd=0, cursor="hand1")
        details_btn.grid(row=2, column=0, pady=1)

        report_btn = Button(btn_frame, text="BOOKING", width=22,command=self.book, font=("times new roman", 14, "bold"), bg="black",fg="gold", bd=0, cursor="hand1")
        report_btn.grid(row=3, column=0, pady=1)

        logout_btn = Button(btn_frame, text="Reg USER", width=22,command=self.reg, font=("times new roman", 14, "bold"), bg="black",fg="gold", bd=0, cursor="hand1")
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
        admin = Frame(main_frame, bd=4, relief=RIDGE)
        admin.place(x=225, y=0, width=1410, height=690)

        try:
            con = pymysql.connect(host="localhost", user="root", password="", database="carRentalSystem")
            mycursor = con.cursor()
            mycursor.execute("select COUNT(*) from register")
            myresult = mycursor.fetchall()
            print(myresult)
            con.close()
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}", parent=self.root)

        register_user = Frame(admin, bd=4, bg="gold", relief=RIDGE)
        register_user.place(x=50, y=50, width=300, height=180)
        register_userbtn = Button(register_user, text="Registered User", width=22, font=("times new roman", 14, "bold"), bg="black",fg="gold", bd=0, cursor="hand1")
        register_userbtn.grid(row=0, column=0, pady=10,padx=25)
        register_lbl = Label(register_user,text=myresult, font=("times new roman", 50, "bold"), fg="black")
        register_lbl.grid(row=1, column=0, pady=10)

        try:
            con = pymysql.connect(host="localhost", user="root", password="", database="carRentalSystem")
            mycursor = con.cursor()
            mycursor.execute("select COUNT(*) from booking")
            myresult = mycursor.fetchall()
            print(myresult)
            con.close()
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}", parent=self.root)

        total_booking = Frame(admin, bd=4, bg="gold",relief=RIDGE)
        total_booking.place(x=450, y=50, width=300, height=180)
        total_bookingbtn = Button(total_booking, text="Total Booking", width=22, font=("times new roman", 14, "bold"), bg="black", fg="gold", bd=0, cursor="hand1")
        total_bookingbtn.grid(row=0, column=0, pady=10, padx=25)
        booking_lbl=Label(total_booking,text=myresult,font=("times new roman", 50, "bold"), fg="black")
        booking_lbl.grid(row=1,column=0,pady=10)

        total_subscriber = Frame(admin, bd=4, bg="gold", relief=RIDGE)
        total_subscriber.place(x=250, y=300, width=300, height=180)
        total_subscriberbtn = Button(total_subscriber, text="Total Subscribers", width=22,font=("times new roman", 14, "bold"), bg="black", fg="gold", bd=0, cursor="hand1")
        total_subscriberbtn.grid(row=0, column=0, pady=10, padx=25)
        subscriber_lbl = Label(total_subscriber, text="36", font=("times new roman", 50, "bold"), fg="black")
        subscriber_lbl.grid(row=1, column=0, pady=10)

        try:
            con = pymysql.connect(host="localhost", user="root", password="", database="carRentalSystem")
            mycursor = con.cursor()
            mycursor.execute("select COUNT(*) from contact")
            myresult = mycursor.fetchall()
            print(myresult)
            con.close()
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}", parent=self.root)

        total_Queries = Frame(admin, bd=4 , bg="gold", relief=RIDGE)
        total_Queries.place(x=700, y=300, width=300, height=180)
        total_Queriesbtn = Button(total_Queries, text="Total Queries", width=22,font=("times new roman", 14, "bold"), bg="black", fg="gold", bd=0, cursor="hand1")
        total_Queriesbtn.grid(row=0, column=0, pady=10, padx=25)
        Queries_lbl = Label(total_Queries, text=myresult, font=("times new roman", 50, "bold"), fg="black")
        Queries_lbl.grid(row=1, column=0, pady=10)

        total_cars = Frame(admin, bd=4, bg="gold", relief=RIDGE)
        total_cars.place(x=850, y=50, width=300, height=180)
        total_carsbtn = Button(total_cars, text="Total Cars", width=22,font=("times new roman", 14, "bold"), bg="black", fg="gold", bd=0, cursor="hand1")
        total_carsbtn.grid(row=0, column=0, pady=10, padx=25)
        cars_lbl = Label(total_cars, text="36", font=("times new roman", 50, "bold"), fg="black")
        cars_lbl.grid(row=1, column=0, pady=10)





        # img3 = Image.open("Images\\sidecar2.png")
        # img3 = img3.resize((1410, 690), Image.ANTIALIAS)
        # self.photoimg3 = ImageTk.PhotoImage(img3)
        # lblimg1 = Label(main_frame, image=self.photoimg3, bd=4, relief=RIDGE)
        # lblimg1.place(x=225, y=0, width=1410, height=690)


    def add_brands(self):
        self.new_window=Toplevel(self.root)
        self.app=add_brands(self.new_window)

    def addcars(self):
        self.new_window=Toplevel(self.root)
        self.app=addcars(self.new_window)

    def cust_details(self):
        self.new_window=Toplevel(self.root)
        self.app=cust_win(self.new_window)

    def add_quiries(self):
        self.new_window = Toplevel(self.root)
        self.app = contact(self.new_window)

    def book(self):
        self.new_window = Toplevel(self.root)
        self.app = booking(self.new_window)

    def reg(self):
        self.new_window = Toplevel(self.root)
        self.app = reg(self.new_window)

    def qr(self):
        self.new_window = Toplevel(self.root)
        self.app = qr(self.new_window)

    def pro(self):
        self.new_window = Toplevel(self.root)
        self.app = profile(self.new_window)



    # def count_user(self):




if __name__ == '__main__':
    root=Tk()
    obj=adminDashboard(root)
    root.mainloop()