from tkinter import *
from PIL import Image,ImageTk
from tkinter import ttk
import random
import pymysql
from tkinter import messagebox
from tkinter import filedialog


class profile:
    def __init__(self,root):
        self.root=root
        self.root.title("Customer")
        self.root.geometry("1370x610+225+218")
        uploaded_img = Label(root)

        # ==============Variables============



        lbltitle = Label(self.root, text="UPDATE YOUR PROFILE INFO", font=("times new roman", 18, "bold"), bg="black",fg="gold", bd=4, relief=RIDGE)
        lbltitle.place(x=0, y=0, width=1370, height=50)





        #
        # btn_frame=Frame(lbltitle,bd=2,relief=RIDGE)
        # btn_frame.place(x=0,y=300,width=412,height=40)

        # ==============Table Frame ===================
        Table_Frame=LabelFrame(self.root,bd=2,relief=RIDGE,text="Your Profile", font=("times new roman", 14, "bold"),padx=5)
        Table_Frame.place(x=435,y=80,width=550,height=450)

        try:
            con = pymysql.connect(host="localhost", user="root", password="", database="carRentalSystem")
            mycursor = con.cursor()
            mycursor.execute("SELECT fname FROM `register` WHERE fname='admin'")
            myresult = mycursor.fetchall()
            print(myresult)
            con.close()
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}", parent=self.root)
        Queries_lbl = Label(Table_Frame, text="First Name : ", font=("times new roman", 15, "bold"), fg="black")
        Queries_lbl.grid(row=0, column=1, pady=10)
        self.name = StringVar()
        self.name.set(myresult)
        entry_brand = ttk.Entry(Table_Frame, textvariable=self.name, width=20, font=("times new roman", 15, "bold"))
        entry_brand.grid(row=0, column=2, padx=1)

        try:
            con = pymysql.connect(host="localhost", user="root", password="", database="carRentalSystem")
            mycursor = con.cursor()
            mycursor.execute("SELECT lname FROM `register` WHERE fname='admin'")
            lname = mycursor.fetchall()
            print(lname)
            con.close()
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}", parent=self.root)
        Queries_lbl = Label(Table_Frame, text="Last Name : ", font=("times new roman", 15, "bold"), fg="black")
        Queries_lbl.grid(row=1, column=1, pady=10)
        self.lname = StringVar()
        self.lname.set(lname)
        entry_brand = ttk.Entry(Table_Frame, textvariable=self.lname, width=20, font=("times new roman", 15, "bold"))
        entry_brand.grid(row=1, column=2, padx=5)

        try:
            con = pymysql.connect(host="localhost", user="root", password="", database="carRentalSystem")
            mycursor = con.cursor()
            mycursor.execute("SELECT contact FROM `register` WHERE fname='admin'")
            contact = mycursor.fetchall()
            print(contact)
            con.close()
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}", parent=self.root)
        Queries_lbl = Label(Table_Frame, text="Contact No : ", font=("times new roman", 15, "bold"), fg="black")
        Queries_lbl.grid(row=2, column=1, pady=10)
        self.contact = StringVar()
        self.contact.set(contact)
        entry_brand = ttk.Entry(Table_Frame, textvariable=self.contact, width=20, font=("times new roman", 15, "bold"))
        entry_brand.grid(row=2, column=2, padx=5)




        try:
            con = pymysql.connect(host="localhost", user="root", password="", database="carRentalSystem")
            mycursor = con.cursor()
            mycursor.execute("SELECT email FROM `register` WHERE fname='admin'")
            User = mycursor.fetchall()
            print(User)
            con.close()
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}", parent=self.root)
        Queries_lbl = Label(Table_Frame, text="User Email : ", font=("times new roman", 15, "bold"), fg="black")
        Queries_lbl.grid(row=3, column=1, pady=10)
        self.email = StringVar()
        self.email.set(User)
        entry_brand = ttk.Entry(Table_Frame, textvariable=self.email, width=20, font=("times new roman", 15, "bold"))
        entry_brand.grid(row=3, column=2, padx=5)

        try:
            con = pymysql.connect(host="localhost", user="root", password="", database="carRentalSystem")
            mycursor = con.cursor()
            mycursor.execute("SELECT password FROM `register` WHERE fname='admin'")
            password = mycursor.fetchall()
            print(password)
            con.close()
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}", parent=self.root)
        Queries_lbl = Label(Table_Frame, text="User password : ", font=("times new roman", 15, "bold"), fg="black")
        Queries_lbl.grid(row=4, column=1, pady=10)
        self.password = StringVar()
        self.password.set(password)
        self.pwds = ttk.Entry(Table_Frame, textvariable=self.password, show='*',width=20, font=("times new roman", 15, "bold"))
        self.pwds.grid(row=4, column=2, padx=5)

        btnAdd = Button(Table_Frame, text="Update Info",command=self.changePassword,  font=("times new roman", 13, "bold"), bg="black",fg="gold", width=15)
        btnAdd.grid(row=5,column=2,  pady=5)



        self.bg1 = ImageTk.PhotoImage(file="Images\password.png")
        lbl_left = Label(self.root, image=self.bg1)
        lbl_left.place(x=80, y=150,width=300,height=400)




    def changePassword(self):
            if self.pwds.get() == "":
                messagebox.showerror("Error", "Password required ")
            else:
                try:
                    con = pymysql.connect(host="localhost", user="root", password="", database="carRentalSystem")
                    cursor = con.cursor()
                    cursor.execute(
                        "update register set password=%s where fname='admin'",
                        (
                         self.pwds.get()))
                    con.commit()
                    con.close()
                    messagebox.showinfo("Success", "Your Password Changed Successfully", parent=self.root)
                except Exception as ex:
                    messagebox.showerror("Error", f"Error due to {str(ex)}", parent=self.root)

    # =====================RESET PASSWORD =================================
    # def reset_pass(self):
    #
    #     if self.combo_security_Q.get() == "Select":
    #         # if self.var_SecurityQ.get()=="Select":
    #         messagebox.showerror("Error", "Select the security Question ")
    #     elif self.txt_security.get() == "":
    #         # elif self.var_SecurityA.get() == "":
    #         messagebox.showerror("Error", "Please enter the answer")
    #     elif self.txt_newpass.get() == "":
    #         messagebox.showerror("Erorr", "Please enter the new password")
    #     else:
    #         try:
    #             con = pymysql.connect(host="localhost", user="root", password="", database="hotelmanegment")
    #             cursor = con.cursor()
    #             qury = ("select * from register where email=%s and securityQ=%s and securityA=%s")
    #             vlaue = (self.txtuser.get(), self.combo_security_Q.get(), self.txt_security.get(),)
    #             cursor.execute(qury, vlaue)
    #             row = cursor.fetchone()
    #             if row == None:
    #                 messagebox.showerror("Error", "Please enter correct Answer")
    #             else:
    #                 query = ("update register set password=%s where email=%s")
    #                 value = (self.txt_newpass.get(), self.txtuser.get())
    #                 cursor.execute(query, value)
    #
    #                 con.commit()
    #                 con.close()
    #         except Exception as ex:
    #             messagebox.showerror("Error", f"Error due to {str(ex)}", parent=self.root)
    #             # messagebox.showinfo("Info","Your password has been reset , please login new password")






if __name__ == '__main__':
    root=Tk()
    obj=profile(root)
    root.mainloop()
