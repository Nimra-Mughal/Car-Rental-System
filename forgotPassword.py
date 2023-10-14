from tkinter import*
from tkinter import ttk

import pymysql
from PIL import Image,ImageTk
from tkinter import messagebox

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

        get_str=Label(frame,text="Forgot Password",font=("Times New Roman",20,"bold"),fg="gold",bg="black")
        get_str.place(x=75,y=100)


        # Security Questions
        security_Q = Label(frame, text="Select Security question", font=("Times New Roman", 15, "bold"), fg="gold",bg="black")
        security_Q.place(x=50, y=150)

        self.combo_security_Q = ttk.Combobox(frame,font=("Times New Roman", 15, "bold"), state="readonly")

        self.combo_security_Q['values'] = ("Select", "Your Birth Place", "Your Pet Name", "Your Best Friend Name")

        self.combo_security_Q.place(x=50, y=180, width=250)
        self.combo_security_Q.current(0)

        security_A = Label(frame, text="Security Answer", font=("Times New Roman", 15, "bold"), fg="gold", bg="black")
        security_A.place(x=370, y=240)

        self.txt_security = ttk.Entry(frame,font=("Times New Roman", 15, "bold"))
        self.txt_security.place(x=370, y=270, width=250)

        # img2 = Image.open("Images\profile.png")
        # img2 = img2.resize((25, 25), Image.ANTIALIAS)
        # self.photoimage2 = ImageTk.PhotoImage(img2)
        # lblimg1 = Label(image=self.photoimage2, bg="black", borderwidth=0)
        # lblimg1.place(x=38, y=150, width=25, height=25)

        # img3 = Image.open("Images\password.png")
        # img3 = img3.resize((25, 25), Image.ANTIALIAS)
        # self.photoimage3 = ImageTk.PhotoImage(img3)
        # lblimg1 = Label(image=self.photoimage3, bg="black", borderwidth=0)
        # lblimg1.place(x=38, y=220, width=25, height=25)

        loginbtn=Button(frame,text="Login",font=("Times New Roman", 15, "bold"),bd=3,command=self.logindashboard,relief=RIDGE,fg="black",bg="gold",activeforeground="white",activebackground="red")
        loginbtn.place(x=110,y=300,width=120,height=35)

        registerbtn = Button(frame,cursor="hand2", text="New User Register", font=("Times New Roman", 10, "bold"),borderwidth=0, fg="gold",bg="black", activeforeground="white", activebackground="black")
        registerbtn.place(x=15, y=370, width=160)

        registerbtn = Button(frame, text="Forgot Password", font=("Times New Roman", 10, "bold"),borderwidth=0,fg="gold", bg="black", activeforeground="white", activebackground="black")
        registerbtn.place(x=180, y=370, width=160)




    def logindashboard(self):
        if self.txtuser.get()=="" or self.txtpass.get()=="":
            messagebox.showerror("Error","All feild required!")

        else:
            try:
                con = pymysql.connect(host="localhost", user="root", password="", database="carRentalSystem")
                cur = con.cursor()
                cur.execute("select * from register where fname=%s and password=%s",(self.txtuser.get(),self.txtpass.get()))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","Invalid UserName & Password")
                elif self.txtuser.get() == "admin" and self.txtpass.get() == "1234":
                    messagebox.showinfo("Sucess", "Successfully Login Admin")
                    self.root.destroy()
                    import dashboardAdmin
                    con.close()
                else:
                    messagebox.showinfo("Sucess","Success login")

            except Exception as ex:
                messagebox.showerror("Error", f"Error due to {str(ex)}", parent=self.root)

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


if __name__ == '__main__':
    root=Tk()
    app=Login_window(root)
    root.mainloop()

