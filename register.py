from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import pymysql
from login import Login_window

class Register:
    def __init__(self,root):
        self.root=root
        self.root.title("Register")
        self.root.geometry("800x500+400+200")

        self.var_fname=StringVar()
        self.var_lname=StringVar()
        self.var_contact=StringVar()
        self.var_email=StringVar()
        self.var_securityQ=StringVar()
        self.var_securityA=StringVar()
        self.var_pass=StringVar()
        self.var_confpass=StringVar()


        # self.bg=ImageTk.PhotoImage(file="Images\sidecar2.png")
        # lbl_bg = Label(self.root, image=self.bg)
        # lbl_bg.place(x=0, y=0, relwidth=1, relheight=1)
        #
        # self.bg1 = ImageTk.PhotoImage(file="Images\img.png")
        # lbl_left = Label(self.root, image=self.bg1)
        # lbl_left.place(x=180, y=120, width=470, height=550)

        frame=Frame(self.root,bg="black")
        frame.place(x=0, y=0, width=800, height=550)

        register_lbl=Label(frame,text="REGISTER HERE",font=("Times New Roman",20,"bold"),fg="gold",bg="black")
        register_lbl.place(x=50,y=30)

        #============Row1==================
        fname=Label(frame,text="First Name",font=("Times New Roman",15,"bold"),fg="gold",bg="black")
        fname.place(x=50,y=100)

        self.fname_entry=ttk.Entry(frame,textvariable=self.var_fname,font=("Times New Roman",15,"bold"))
        self.fname_entry.place(x=50,y=130,width=250)

        lname = Label(frame, text="Last Name", font=("Times New Roman", 15, "bold"),fg="gold",bg="black")
        lname.place(x=370, y=100)

        self.txt_lname = ttk.Entry(frame,textvariable=self.var_lname, font=("Times New Roman", 15, "bold"))
        self.txt_lname.place(x=370, y=130, width=250)

        #============Row2==================
        contact = Label(frame, text="Contact No", font=("Times New Roman", 15, "bold"), fg="gold",bg="black")
        contact.place(x=50, y=170)

        self.txt_contact = ttk.Entry(frame,textvariable=self.var_contact, font=("Times New Roman", 15, "bold"))
        self.txt_contact.place(x=50, y=200, width=250)

        email = Label(frame, text="Email", font=("Times New Roman", 15, "bold"), fg="gold",bg="black")
        email.place(x=370, y=170)

        self.txt_email = ttk.Entry(frame,textvariable=self.var_email, font=("Times New Roman", 15, "bold"))
        self.txt_email.place(x=370, y=200, width=250)


        #============Row3==================
        security_Q=Label(frame, text="Select Security question", font=("Times New Roman", 15, "bold"), fg="gold",bg="black")
        security_Q.place(x=50, y=240)

        self.combo_security_Q=ttk.Combobox(frame,textvariable=self.var_securityQ, font=("Times New Roman", 15, "bold"), state="readonly")

        self.combo_security_Q['values'] = ("Select","Your Birth Place","Your Pet Name","Your Best Friend Name")

        self.combo_security_Q.place(x=50, y=270, width=250)
        self.combo_security_Q.current(0)

        security_A = Label(frame, text="Security Answer", font=("Times New Roman", 15, "bold"), fg="gold",bg="black")
        security_A.place(x=370, y=240)

        self.txt_security = ttk.Entry(frame,textvariable=self.var_securityA, font=("Times New Roman", 15, "bold"))
        self.txt_security.place(x=370, y=270, width=250)

        #============Row4==================
        Pswd = Label(frame, text="Password", font=("Times New Roman", 15, "bold"), fg="gold",bg="black")
        Pswd.place(x=50, y=310)

        self.txt_pswd = ttk.Entry(frame,textvariable=self.var_pass, font=("Times New Roman", 15, "bold"))
        self.txt_pswd.place(x=50, y=340, width=250)

        confirm_Pswd = Label(frame, text="Confirm Password", font=("Times New Roman", 15, "bold"), fg="gold",bg="black")
        confirm_Pswd.place(x=370, y=310)

        self.txt_confirm_pswd = ttk.Entry(frame,textvariable=self.var_confpass, font=("Times New Roman", 15, "bold"))
        self.txt_confirm_pswd.place(x=370, y=340, width=250)

        #============CheckBtn==================
        self.var_check=IntVar()
        checkbtn=Checkbutton(frame,variable=self.var_check,text="I Agree The terms and conditions",font=("Times New Roman", 15, "bold"),fg="gold",bg="black",onvalue=1,offvalue=0)
        checkbtn.place(x=50,y=380)

        #============Button==================
        img=Image.open("Images\\btnreg.png")
        img=img.resize((200,50),Image.ANTIALIAS)
        self.photoimage=ImageTk.PhotoImage(img)
        b1=Button(frame,image=self.photoimage,command=self.RegData,borderwidth=0,cursor="hand2",bg="black")
        b1.place(x=50,y=420,width=200)

        img1 = Image.open("Images\loginbtn.png")
        img1 = img1.resize((200, 50), Image.ANTIALIAS)
        self.photoimage1 = ImageTk.PhotoImage(img1)
        b1 = Button(frame, image=self.photoimage1,command=self.signin, borderwidth=0, cursor="hand2",bg="black")
        b1.place(x=360, y=420, width=200)

    def RegData(self):
        if self.var_fname.get()=="" or self.var_lname.get()=="" or self.var_contact.get()=="" or self.var_email.get()=="" or self.var_securityQ.get()=="" or self.var_securityA.get()=="" or self.var_pass.get()=="":
            messagebox.showerror("Error","All feilds are mendatory",parent=self.root)
        elif self.var_pass.get()!= self.var_confpass.get():
            messagebox.showerror("Error","Password confirm password does not match",parent=self.root)
        else:
            # messagebox.showinfo("Error","Sucessfully registerd",parent=self.root)
            try:
                con = pymysql.connect(host="localhost", user="root", password="", database="carRentalSystem")
                cursor = con.cursor()
                cursor.execute(
                    "insert into register (fname,lname,contact,email,securityQ,securityA,password) values (%s,%s,%s,%s,%s,%s,%s)",
                    (
                        self.var_fname.get(),
                        self.var_lname.get(),
                        self.var_contact.get(),
                        self.var_email.get(),
                        self.var_securityQ.get(),
                        self.var_securityA.get(),
                        self.var_pass.get()))
                con.commit()
                con.close()
                messagebox.showinfo("Success", "Registered Successfully", parent=self.root)
                self.ClearData()
            except Exception as ex:
                messagebox.showerror("Error", f"Error due to {str(ex)}", parent=self.root)


    def signin(self):
        self.new_window = Toplevel(self.root)
        self.app = Login_window(self.new_window)

    def ClearData(self):
        self.fname_entry.delete(0, END),
        self.txt_lname.delete(0, END),
        self.txt_contact.delete(0, END),
        self.txt_email.delete(0, END),
        self.combo_security_Q.current(0),
        self.txt_security.delete(0, END),
        self.txt_pswd.delete(0, END),
        self.txt_confirm_pswd.delete(0, END),
        self.var_check.set(0)












if __name__ == '__main__':
    root=Tk()
    app=Register(root)
    root.mainloop()
