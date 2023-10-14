import tkinter
from tkinter import ttk, messagebox
import pymysql
import json

from PIL import Image,ImageTk

class Registration:
    def __init__(self,root):
        self.root=root
        self.root.title("Registration Form")
        self.root.geometry("350x700+0+0")
        self.bg=ImageTk.PhotoImage(file="images/bigger.png")
        bg=tkinter.Label(self.root, image=self.bg).place(x=0, y=0, relheight=1, relwidth=1)


        frame1=tkinter.Frame(self.root, background="white")
        frame1.place(x=700,y=130,width=640,height=500)
        tkinter.Label(frame1, text="Register Here", font=("Impact", 25, "bold"), bg="white", fg="#d77337").place(x=50, y=20)

        self.img = ImageTk.PhotoImage(file="images/reg.png")
        tkinter.Label(frame1, image=self.img, bg="white").place(x=280, y=10)

        f_name=tkinter.Label(frame1, text="Firstname", font=("Roboto", 12, "bold"), bg="white", fg="black").place(x=50, y=80)
        self.txt_fname=tkinter.Entry(frame1, font=("Roboto", 12,), bg="light grey")
        self.txt_fname.place(x=50, y=110, width=250,height=35)

        lastname=tkinter.Label(frame1, text="Lastname", font=("Roboto", 12, "bold"), bg="white", fg="black").place(x=370, y=80)
        self.txt_lname = tkinter.Entry(frame1, font=("Roboto", 12,), bg="light grey")
        self.txt_lname.place(x=370, y=110, width=250,height=35)

        contact=tkinter.Label(frame1, text="Contact", font=("Roboto", 12, "bold"), bg="white", fg="black").place(x=50, y=150)
        self.txt_contact = tkinter.Entry(frame1, font=("Roboto", 12,), bg="light grey")
        self.txt_contact.place(x=50, y=180, width=250,height=35)

        email=tkinter.Label(frame1, text="Email", font=("Roboto", 12, "bold"), bg="white", fg="black").place(x=370, y=150)
        self.txt_email = tkinter.Entry(frame1, font=("Roboto", 12,), bg="light grey")
        self.txt_email.place(x=370, y=180, width=250,height=35)

        # file = open("MyApi.json", "r")
        # x = file.read()
        # result = json.loads(x)
        # # print(result)
        # for i in result:
        #     print(i["country_name"])
        question = tkinter.Label(frame1, text="Security Question", font=("Roboto", 12, "bold"), bg="white", fg="black").place(x=50, y=220)
        self.cmb_question = ttk.Combobox(frame1, font=("Roboto", 9), state="read only")
        self.cmb_question['values'] = ("Select your answer", "Your pet name","Your Father name")
        self.cmb_question.place(x=50, y=250, width=250, height=35)
        self.cmb_question.current(0)


        Answer=tkinter.Label(frame1, text="Answer", font=("Roboto", 12, "bold"), bg="white", fg="black").place(x=370, y=220)
        self.txt_answer = tkinter.Entry(frame1, font=("Roboto", 12,), bg="light grey")
        self.txt_answer.place(x=370, y=250, width=250,height=35)

        password = tkinter.Label(frame1, text="Password", font=("Roboto", 12, "bold"), bg="white", fg="black").place(x=50, y=290)
        self.txt_password = tkinter.Entry(frame1, font=("Roboto", 12,), bg="light grey")
        self.txt_password.place(x=50, y=320, width=250,height=35)


        Cpassword= tkinter.Label(frame1, text="Confirm Password", font=("Roboto", 12, "bold"), bg="white", fg="black").place(x=370, y=290)
        self.txt_cpassword = tkinter.Entry(frame1, font=("Roboto", 12,), bg="light grey")
        self.txt_cpassword.place(x=370, y=320, width=250,height=35)
        self.chk=tkinter.IntVar()
        chk=tkinter.Checkbutton(frame1, text="I agree Terms and conditions", onvalue=1, offvalue=0, font=("Robot", 12), bg="White").place(x=50, y=380)

        btn=tkinter.Button(frame1, text="Register", font=("Roboto", 10, "bold"), foreground="white", command=self.RegData, bg="#d77337", bd=0, cursor="hand2").place(x=50, y=430, width=100, height=40)
    def RegData(self):
        if self.txt_fname.get()=="" or self.txt_lname.get()=="" or self.txt_contact.get()=="" or self.txt_answer.get()=="" or self.txt_email.get()=="" or self.txt_password.get()=="" or self.txt_cpassword.get()=="":
            messagebox.showerror("Error","All feilds are mendatory",parent=self.root)
        elif self.txt_password.get()!= self.txt_cpassword.get():
            messagebox.showerror("Error","Password confirm password does not match",parent=self.root)
        else:
            # messagebox.showinfo("Error","Sucessfully registerd",parent=self.root)
            try:
                con = pymysql.connect(host="localhost", user="root", password="", database="regdb")
                cursor = con.cursor()
                cursor.execute(
                    "insert into employee (fname,lname,contact,email,answer,password,cpassword) values (%s,%s,%s,%s,%s,%s,%s)",
                    (
                        self.txt_fname.get(),
                        self.txt_lname.get(),
                        self.txt_contact.get(),
                        self.txt_email.get(),
                        self.txt_answer.get(),
                        self.txt_password.get(),
                        self.txt_cpassword.get()))
                con.commit()
                con.close()
                messagebox.showinfo("Success", "Registered Successfully", parent=self.root)
                self.ClearData()
            except Exception as ex:
                messagebox.showerror("Error", f"Error due to {str(ex)}", parent=self.root)

    def ClearData(self):
        self.txt_fname.delete(0, tkinter.END),
        self.txt_lname.delete(0, tkinter.END),
        self.txt_contact.delete(0, tkinter.END),
        self.txt_email.delete(0, tkinter.END),
        self.txt_answer.delete(0, tkinter.END),
        self.txt_password.delete(0, tkinter.END),
        self.txt_cpassword.delete(0, tkinter.END),
        self.chk.set(0),
        self.cmb_question.set(0)


root=tkinter.Tk()
object=Registration(root)
root.mainloop()






#
# root=Tk()
# object=Registration(root)
# root.mainloop()

