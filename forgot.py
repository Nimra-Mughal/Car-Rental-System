# =====================RESET PASSWORD =================================
    def reset_pass(self):

        if self.combo_security_Q.get()=="Select":
        # if self.var_SecurityQ.get()=="Select":
            messagebox.showerror("Error","Select the security Question ")
        elif self.txt_security.get()=="":
        # elif self.var_SecurityA.get() == "":
            messagebox.showerror("Error","Please enter the answer")
        elif self.txt_newpass.get()=="":
            messagebox.showerror("Erorr","Please enter the new password")
        else:
            try:
                con = pymysql.connect(host="localhost", user="root", password="", database="hotelmanegment")
                cursor = con.cursor()
                qury=("select * from register where email=%s and securityQ=%s and securityA=%s")
                vlaue=(self.txtuser.get(),self.combo_security_Q.get(),self.txt_security.get(),)
                cursor.execute(qury,vlaue)
                row=cursor.fetchone()
                if row==None:
                    messagebox.showerror("Error","Please enter correct Answer")
                else:
                    query=("update register set password=%s where email=%s")
                    value=(self.txt_newpass.get(),self.txtuser.get())
                    cursor.execute(query,value)

                    con.commit()
                    con.close()
            except Exception as ex:
                messagebox.showinfo("Info","Your password has been reset , please login new password")

    # =====================FORGOT PASSWORD WINDOW =================================
    def forgot_password_window(self):
        if  self.txtuser.get()=="":
            messagebox.showerror("Error","Please Enter the email address to reset Password")
        else:
            con = pymysql.connect(host="localhost", user="root", password="", database="hotelmanegment")
            cursor = con.cursor()
            query=("select * from register where email=%s")
            value=(self.txtuser.get(),)
            cursor.execute(query,value)
            row=cursor.fetchone()
            # print(row)

            if row==None:
                messagebox.showerror("My Error","Please enter the valid user name")
            else:
                con.close()
                self.root2=Toplevel()
                self.root2.title("Forget Password")
                self.root2.geometry("340x450+610+170")

                l=Label(self.root2,text="Forget Password",font=("times new roman",20,"bold"),fg="red",bg="white")
                l.place(x=0,y=10,relwidth=1)

                security_Q = Label(self.root2, text="Select Security Questions", font=("times new roman", 15, "bold"),bg="white", fg="black")
                security_Q.place(x=50, y=80)

                self.combo_security_Q = ttk.Combobox(self.root2,font=("times new roman", 15, "bold"), state="readonly")
                self.combo_security_Q["values"] = ("Select", "Select Your Birth Place", "Your Girl Friend Name", "Your Pet Name")
                self.combo_security_Q.place(x=50, y=110, width=250)
                self.combo_security_Q.current(0)

                security_A = Label(self.root2, text="Security Answer", font=("times new roman", 15, "bold"), bg="white",fg="black")
                security_A.place(x=50, y=150)

                self.txt_security = ttk.Entry(self.root2, font=("times new roman", 15))
                self.txt_security.place(x=50, y=180, width=250)

                new_password = Label(self.root2, text="New Password", font=("times new roman", 15, "bold"), bg="white",fg="black")
                new_password.place(x=50, y=220)

                self.txt_newpass = ttk.Entry(self.root2, font=("times new roman", 15))
                self.txt_newpass.place(x=50, y=250, width=250)

                btn=Button(self.root2,text="Reset", font=("times new roman", 15),fg="white",bg="green")
                btn.place(x=100,y=290)

