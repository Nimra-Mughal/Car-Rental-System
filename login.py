from tkinter import*
from tkinter import ttk

import pymysql
from PIL import Image,ImageTk
from tkinter import messagebox
from dashboardAdmin import adminDashboard

class Login_window:
    def __init__(self,root):
        self.root=root
        self.root.title("Login")
        self.root.geometry("340x450+600+200")

        # self.bg=ImageTk.PhotoImage(file="Images\sidecar2.png")
        #
        # lbl_bg=Label(self.root,image=self.bg)
        # lbl_bg.place(x=0,y=0,relwidth=1,relheight=1)

        frame=Frame(self.root,bg="black")
        frame.place(x=0,y=0,width=340,height=450)

        img1=Image.open("Images\permission.png")
        img1=img1.resize((100,100),Image.ANTIALIAS)
        self.photoimage1=ImageTk.PhotoImage(img1)
        lblimg1=Label(image=self.photoimage1,bg="black",borderwidth=0)
        lblimg1.place(x=120,y=10,width=100,height=100)

        get_str=Label(frame,text="Get Started",font=("Times New Roman",20,"bold"),fg="gold",bg="black")
        get_str.place(x=95,y=100)

        email=lbl=Label(frame,text="Email",font=("Times New Roman",15,"bold"),fg="gold",bg="black")
        email.place(x=70,y=155)

        self.txtuser=ttk.Entry(frame,font=("Times New Roman",15,"bold"))
        self.txtuser.place(x=40,y=180,width=270)

        Password = lbl = Label(frame, text="Password", font=("Times New Roman", 15, "bold"), fg="gold", bg="black")
        Password.place(x=70, y=225)

        self.txtpass = ttk.Entry(frame, font=("Times New Roman", 15, "bold"))
        self.txtpass.place(x=40, y=250, width=270)

        img2 = Image.open("Images\profile.png")
        img2 = img2.resize((25, 25), Image.ANTIALIAS)
        self.photoimage2 = ImageTk.PhotoImage(img2)
        lblimg1 = Label(image=self.photoimage2, bg="black", borderwidth=0)
        lblimg1.place(x=38, y=150, width=25, height=25)

        img3 = Image.open("Images\password.png")
        img3 = img3.resize((25, 25), Image.ANTIALIAS)
        self.photoimage3 = ImageTk.PhotoImage(img3)
        lblimg1 = Label(image=self.photoimage3, bg="black", borderwidth=0)
        lblimg1.place(x=38, y=220, width=25, height=25)

        loginbtn=Button(frame,text="Login",font=("Times New Roman", 15, "bold"),bd=3,command=self.logindashboard,relief=RIDGE,fg="black",bg="gold",activeforeground="white",activebackground="red")
        loginbtn.place(x=110,y=300,width=120,height=35)

        registerbtn = Button(frame,cursor="hand2", text="New User Register", font=("Times New Roman", 10, "bold"),borderwidth=0, fg="gold",bg="black", activeforeground="white", activebackground="black")
        registerbtn.place(x=15, y=370, width=160)

        registerbtn = Button(frame, text="Forgot Password",command=self.forgot_password_window, font=("Times New Roman", 10, "bold"),borderwidth=0,fg="gold", bg="black", activeforeground="white", activebackground="black")
        registerbtn.place(x=180, y=370, width=160)




    # def logindashboard(self):
    #     if self.txtuser.get()=="" or self.txtpass.get()=="":
    #         messagebox.showerror("Error","All feild required!")
    #
    #     else:
    #         try:
    #             con = pymysql.connect(host="localhost", user="root", password="", database="carRentalSystem")
    #             cur = con.cursor()
    #             cur.execute("select * from register where fname=%s and password=%s",(self.txtuser.get(),self.txtpass.get()))
    #             row=cur.fetchone()
    #             if row==None:
    #                 messagebox.showerror("Error","Invalid UserName & Password")
    #             elif self.txtuser.get() == "admin" and self.txtpass.get() == "1234":
    #                 import dashboardAdmin
    #                 con.close()
    #             else:
    #                 messagebox.showinfo("Sucess","Success login")
    #
    #         except Exception as ex:
    #             messagebox.showerror("Error", f"Error due to {str(ex)}", parent=self.root)

        # def ClearData(self):
        #     self.fname_entry.delete(0, END),
        #     self.txt_lname.delete(0, END),
        #     self.txt_contact.delete(0, END),
        #     self.txt_email.delete(0, END),
        #     self.combo_security_Q.current(0),
        #     self.txt_security.delete(0, END),
        #     self.txt_pswd.delete(0, END),
        #     self.txt_confirm_pswd.delete(0, END),
        #     self.var_check.set(0)

    def reset_pass(self):

        if self.combo_security_Q.get() == "Select":
            # if self.var_SecurityQ.get()=="Select":
            messagebox.showerror("Error", "Select the security Question ")
        elif self.txt_security.get() == "":
            # elif self.var_SecurityA.get() == "":
            messagebox.showerror("Error", "Please enter the answer")
        elif self.txt_newpass.get() == "":
            messagebox.showerror("Erorr", "Please enter the new password")
        else:
            try:
                con = pymysql.connect(host="localhost", user="root", password="", database="carRentalSystem")
                cursor = con.cursor()
                qury = ("select * from register where email=%s and securityQ=%s and securityA=%s")
                vlaue = (self.txtuser.get(), self.combo_security_Q.get(), self.txt_security.get(),)
                cursor.execute(qury, vlaue)
                row = cursor.fetchone()
                if row == None:
                    messagebox.showerror("Error", "Please enter correct Answer")
                else:
                    query = ("update register set password=%s where email=%s")
                    value = (self.txt_newpass.get(), self.txtuser.get())
                    cursor.execute(query, value)
                    con.commit()
                    con.close()
                    messagebox.showinfo("Sucess", "Password Sucessfully Updated")

            except Exception as ex:
                messagebox.showerror("Error", f"Error due to {str(ex)}", parent=self.root)
                # messagebox.showinfo("Info","Your password has been reset , please login new password")

    def forgot_password_window(self):
        if self.txtuser.get() == "":
            messagebox.showerror("Error", "Please Enter the email address to reset Password")
        else:
            con = pymysql.connect(host="localhost", user="root", password="", database="carRentalSystem")
            cursor = con.cursor()
            query = ("select * from register where email=%s")
            value = (self.txtuser.get(),)
            cursor.execute(query, value)
            row = cursor.fetchone()
            # print(row)

            if row == None:
                messagebox.showerror("My Error", "Please enter the valid user name")
            else:
                con.close()
                self.root2 = Toplevel()
                self.root2.title("Forget Password")
                self.root2.geometry("340x450+610+170")

                l = Label(self.root2, text="Forget Password", font=("times new roman", 20, "bold"), fg="red",
                          bg="white")
                l.place(x=0, y=10, relwidth=1)

                security_Q = Label(self.root2, text="Select Security Questions", font=("times new roman", 15, "bold"),
                                   bg="white", fg="black")
                security_Q.place(x=50, y=80)

                self.combo_security_Q = ttk.Combobox(self.root2, font=("times new roman", 15, "bold"), state="readonly")
                self.combo_security_Q["values"] = (
                "Select", "Your Birth Place", "Your Girl Friend Name", "Your Pet Name")
                self.combo_security_Q.place(x=50, y=110, width=250)
                self.combo_security_Q.current(0)

                security_A = Label(self.root2, text="Security Answer", font=("times new roman", 15, "bold"), bg="white",
                                   fg="black")
                # security_A = Label(self.root2, text="Security Answer", font=("times new roman", 15, "bold"), bg="white",fg="black")
                security_A.place(x=50, y=150)

                self.txt_security = ttk.Entry(self.root2, font=("times new roman", 15))
                self.txt_security.place(x=50, y=180, width=250)

                new_password = Label(self.root2, text="New Password", font=("times new roman", 15, "bold"), bg="white",
                                     fg="black")
                new_password.place(x=50, y=220)

                self.txt_newpass = ttk.Entry(self.root2, font=("times new roman", 15))
                self.txt_newpass.place(x=50, y=250, width=250)

                btn = Button(self.root2, text="Reset", command=self.reset_pass, font=("times new roman", 15),
                             fg="white", bg="green")
                btn.place(x=100, y=290)


if __name__ == '__main__':
    root=Tk()
    app=Login_window(root)
    root.mainloop()

