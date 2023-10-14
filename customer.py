from tkinter import *
from PIL import Image,ImageTk
from tkinter import ttk
import random
import pymysql
from tkinter import messagebox



class cust_win:
    def __init__(self,root):
        self.root=root
        self.root.title("Customer")
        self.root.geometry("1370x610+225+218")

        # ==============Variables============
        self.var_ref=StringVar()
        x=random.randint(1000,9999)
        self.var_ref.set(str(x))

        self.var_cust_name=StringVar()
        self.var_mother=StringVar()
        self.var_gender=StringVar()
        self.var_post=StringVar()
        self.var_mobile=StringVar()
        self.var_email=StringVar()
        self.var_nationality=StringVar()
        self.var_address=StringVar()
        self.var_idProof=StringVar()
        self.var_idNumber=StringVar()

        lbltitle = Label(self.root, text="ADD CUSTOMER DETAILS", font=("times new roman", 18, "bold"), bg="black",fg="gold", bd=4, relief=RIDGE)
        lbltitle.place(x=0, y=0, width=1370, height=50)

        img2 = Image.open("Images\\logo.png")
        img2 = img2.resize((100, 45), Image.ANTIALIAS)
        self.photoimg2 = ImageTk.PhotoImage(img2)
        lblimg = Label(self.root, image=self.photoimg2, bd=0, relief=RIDGE)
        lblimg.place(x=5, y=2, width=100, height=45)

        labelframeleft=LabelFrame(self.root,bd=2,relief=RIDGE,text="Customer Details",font=("times new roman", 18, "bold"),padx=5)
        labelframeleft.place(x=5,y=50,width=425,height=550)

        lbl_cust_ref=Label(labelframeleft,text="Customer Ref",font=("times new roman", 12, "bold"),padx=2,pady=6)
        lbl_cust_ref.grid(row=0,column=0,sticky=W)
        self.entry_ref=ttk.Entry(labelframeleft,textvariable=self.var_ref,width=29,font=("times new roman", 13, "bold"),state="readonly")
        self.entry_ref.grid(row=0,column=1)

        cname = Label(labelframeleft, text="Customer Name", font=("times new roman", 12, "bold"), padx=2, pady=6)
        cname.grid(row=1, column=0, sticky=W)
        self.txt_cname = ttk.Entry(labelframeleft,textvariable=self.var_cust_name, width=29, font=("times new roman", 13, "bold"))
        self.txt_cname.grid(row=1, column=1)

        mname = Label(labelframeleft, text="Mother Name", font=("times new roman", 12, "bold"), padx=2, pady=6)
        mname.grid(row=2, column=0, sticky=W)
        self.txt_mname = ttk.Entry(labelframeleft,textvariable=self.var_mother, width=29, font=("times new roman", 13, "bold"))
        self.txt_mname.grid(row=2, column=1)

        # mname = Label(labelframeleft, text="Mother Name", font=("times new roman", 12, "bold"), padx=2, pady=6)
        # mname.grid(row=2, column=0, sticky=W)
        # txt_mname = ttk.Entry(labelframeleft, width=29, font=("times new roman", 13, "bold"))
        # txt_mname.grid(row=2, column=1)

        labelgender = Label(labelframeleft, text="Gender", font=("times new roman", 12, "bold"), padx=2, pady=6)
        labelgender.grid(row=3, column=0, sticky=W)
        self.combo_gender=ttk.Combobox(labelframeleft,textvariable=self.var_gender, font=("times new roman", 13, "bold"),width=27,state="readonly")
        self.combo_gender['values'] = ("Others","Male","Female")
        self.combo_gender.current(0)
        self.combo_gender.grid(row=3,column=1)

        lblpostcode = Label(labelframeleft, text="PostCode", font=("times new roman", 12, "bold"), padx=2, pady=6)
        lblpostcode.grid(row=4, column=0, sticky=W)
        self.txt_lblpostcode = ttk.Entry(labelframeleft,textvariable=self.var_post, width=29, font=("times new roman", 13, "bold"))
        self.txt_lblpostcode.grid(row=4, column=1)

        lblmobile = Label(labelframeleft, text="Mobile", font=("times new roman", 12, "bold"), padx=2, pady=6)
        lblmobile.grid(row=5, column=0, sticky=W)
        self.txt_lblmobile = ttk.Entry(labelframeleft,textvariable=self.var_mobile, width=29, font=("times new roman", 13, "bold"))
        self.txt_lblmobile.grid(row=5, column=1)

        lblemail = Label(labelframeleft, text="Email", font=("times new roman", 12, "bold"), padx=2, pady=6)
        lblemail.grid(row=6, column=0, sticky=W)
        self.txt_lblemail = ttk.Entry(labelframeleft,textvariable=self.var_email, width=29, font=("times new roman", 13, "bold"))
        self.txt_lblemail.grid(row=6, column=1)

        lblNationality = Label(labelframeleft, text="Nationality", font=("times new roman", 12, "bold"), padx=2, pady=6)
        lblNationality.grid(row=7, column=0, sticky=W)
        self.combo_Nationality = ttk.Combobox(labelframeleft,textvariable=self.var_nationality, font=("times new roman", 13, "bold"), width=27, state="readonly")
        self.combo_Nationality['values'] = ("Pakistani", "Indian", "Americans", "British")
        self.combo_Nationality.current(0)
        self.combo_Nationality.grid(row=7, column=1)

        lblIdProof = Label(labelframeleft, text="Id Proof Type", font=("times new roman", 12, "bold"), padx=2, pady=6)
        lblIdProof.grid(row=8, column=0, sticky=W)
        self.combo_id = ttk.Combobox(labelframeleft,textvariable=self.var_idProof, font=("times new roman", 13, "bold"), width=27,state="readonly")
        self.combo_id['values'] = ("NIC","DrivindLicence",  "Passport")
        self.combo_id.current(0)
        self.combo_id.grid(row=8, column=1)

        lblIdNumber = Label(labelframeleft, text="Id Number", font=("times new roman", 12, "bold"), padx=2, pady=6)
        lblIdNumber.grid(row=9, column=0, sticky=W)
        self.lblIdNumber = ttk.Entry(labelframeleft,textvariable=self.var_idNumber, width=29, font=("times new roman", 13, "bold"))
        self.lblIdNumber.grid(row=9, column=1)

        lblAddress = Label(labelframeleft, text="Address", font=("times new roman", 12, "bold"), padx=2, pady=6)
        lblAddress.grid(row=10, column=0, sticky=W)
        self.lblAddress = ttk.Entry(labelframeleft,textvariable=self.var_address, width=29, font=("times new roman", 13, "bold"))
        self.lblAddress.grid(row=10, column=1)

        btn_frame=Frame(labelframeleft,bd=2,relief=RIDGE)
        btn_frame.place(x=0,y=400,width=412,height=40)

        btnAdd=Button(btn_frame,text="Add",command=self.add_data,font=("times new roman",13, "bold"),bg="black",fg="gold",width=9)
        btnAdd.grid(row=0,column=0,padx=1)

        btnUpdate = Button(btn_frame, text="Update", font=("times new roman", 13, "bold"), bg="black", fg="gold", width=9)
        btnUpdate.grid(row=0, column=1, padx=1)

        btnDelete = Button(btn_frame, text="Delete", font=("times new roman", 13, "bold"), bg="black", fg="gold", width=9)
        btnDelete.grid(row=0, column=2, padx=1)

        btnReset = Button(btn_frame, text="Reset", font=("times new roman", 13, "bold"), bg="black", fg="gold", width=9)
        btnReset.grid(row=0, column=3, padx=1)

        # ==============Table Frame ===================
        Table_Frame=LabelFrame(self.root,bd=2,relief=RIDGE,text="View Details And Search System", font=("times new roman", 14, "bold"),padx=5)
        Table_Frame.place(x=435,y=50,width=920,height=550)

        lblSearchBy=Label(Table_Frame,font=("times new roman", 12, "bold"),text="Search By : ",bg="red",fg="white")
        lblSearchBy.grid(row=0,column=0,sticky=W,padx=2)

        combo_Search = ttk.Combobox(Table_Frame, font=("times new roman", 15, "bold"), width=24, state="readonly")
        combo_Search['values'] = ("Mobile", "Ref")
        combo_Search.current(0)
        combo_Search.grid(row=0, column=1,padx=2)

        txtSearch = ttk.Entry(Table_Frame, width=24, font=("times new roman", 17, "bold"))
        txtSearch.grid(row=0, column=2,padx=2)

        btnSearch = Button(Table_Frame, text="Search", font=("times new roman", 13, "bold"), bg="black", fg="gold", width=9)
        btnSearch.grid(row=0, column=3, padx=2)

        btnShowAll = Button(Table_Frame, text="Show All", font=("times new roman", 13, "bold"), bg="black", fg="gold",width=9)
        btnShowAll.grid(row=0, column=4, padx=2)

        # ================= show data table ==========
        details_table=Frame(Table_Frame,bd=2,relief=RIDGE)
        details_table.place(x=0,y=50,width=910,height=350)

        scroll_x=ttk.Scrollbar(details_table,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(details_table,orient=VERTICAL)

        self.Cust_Details_Table=ttk.Treeview(details_table,column=("ref","name","mother","gender","post","mobile",
                                                                   "email","nationality","idproof","idnumber","address"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.Cust_Details_Table.xview)
        scroll_y.config(command=self.Cust_Details_Table.yview)

        self.Cust_Details_Table.heading("ref",text="Refer No")
        self.Cust_Details_Table.heading("name",text="Name")
        self.Cust_Details_Table.heading("mother",text="Mother Name")
        self.Cust_Details_Table.heading("gender",text="Gender")
        self.Cust_Details_Table.heading("post",text="Post Code")
        self.Cust_Details_Table.heading("mobile",text="Mobile")
        self.Cust_Details_Table.heading("email",text="Email")
        self.Cust_Details_Table.heading("nationality",text="Nationality")
        self.Cust_Details_Table.heading("idproof",text="Id Proof")
        self.Cust_Details_Table.heading("idnumber",text="Id Number")
        self.Cust_Details_Table.heading("address",text="Address")

        self.Cust_Details_Table["show"]="headings"
        self.Cust_Details_Table.column("ref",width=100)
        self.Cust_Details_Table.column("name",width=100)
        self.Cust_Details_Table.column("mother",width=100)
        self.Cust_Details_Table.column("gender",width=100)
        self.Cust_Details_Table.column("post",width=100)
        self.Cust_Details_Table.column("mobile",width=100)
        self.Cust_Details_Table.column("email",width=100)
        self.Cust_Details_Table.column("nationality",width=100)
        self.Cust_Details_Table.column("idproof",width=100)
        self.Cust_Details_Table.column("idnumber",width=100)
        self.Cust_Details_Table.column("address",width=100)

        self.Cust_Details_Table.pack(fill=BOTH,expand=1)
        self.Cust_Details_Table.bind("<ButtonRelease-1>",self.get_cursor)
        self.fetch_data()

    def add_data(self):
        if self.var_mobile.get()=="" or self.var_mother.get()=="":
            messagebox.showerror("Error","All field are required ")
        else:
            # messagebox.showinfo("Error","Sucessfully registerd",parent=self.root)
            try:
                con = pymysql.connect(host="localhost", user="root", password="", database="carRentalSystem")
                cursor = con.cursor()
                cursor.execute(
                    "insert into customer (Ref,Name,Mother,Gender,PostCode,Mobile,Email,Nationality,IdProof,IdNumber,Address) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
                    (
                        self.var_ref.get(),
                        self.var_cust_name.get(),
                        self.var_mother.get(),
                        self.var_gender.get(),
                        self.var_post.get(),
                        self.var_mobile.get(),
                        self.var_email.get(),
                        self.var_nationality.get(),
                        self.var_idProof.get(),
                        self.var_idNumber.get(),
                        self.var_address.get()))
                con.commit()
                self.fetch_data()
                con.close()
                messagebox.showinfo("Success", "Add Successfully", parent=self.root)
                self.ClearData()
            except Exception as ex:
                messagebox.showerror("Error", f"Error due to {str(ex)}", parent=self.root)

    def fetch_data(self):

        try:
            con = pymysql.connect(host="localhost", user="root", password="", database="carRentalSystem")
            cursor = con.cursor()
            cursor.execute("select * from customer" )
            rows=cursor.fetchall()
            if len(rows)!=0:
                self.Cust_Details_Table.delete(*self.Cust_Details_Table.get_children())
                for i in rows:
                    self.Cust_Details_Table.insert("",END,values=i)
                con.commit()
            con.close()
            self.ClearData()
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}", parent=self.root)

    def get_cursor(self):
        cursor_row=self.Cust_Details_Table.focus()
        content=self.Cust_Details_Table.item(cursor_row)
        r=content["values"]

        self.var_ref.set(r[0]),
        self.var_cust_name.set(r[1]),
        self.var_mother.set(r[2]),
        self.var_gender.set(r[3]),
        self.var_post.set(r[4]),
        self.var_mobile.set(r[5]),
        self.var_email.set(r[6]),
        self.var_nationality.set(r[7]),
        self.var_idProof.set(r[8]),
        self.var_idNumber.set(r[9]),
        self.var_address.set(r[10])


    def ClearData(self):
        self.entry_ref.delete(0, END),
        self.txt_cname.delete(0, END),
        self.txt_mname.delete(0, END),
        self.combo_gender.current(0),
        self.txt_lblpostcode.delete(0, END),
        self.txt_lblmobile.delete(0, END),
        self.txt_lblemail.delete(0, END),
        self.combo_Nationality.current(0),
        self.combo_id.current(0),
        self.lblIdNumber.delete(0, END),
        self.lblAddress.delete(0, END)



if __name__ == '__main__':
    root=Tk()
    obj=cust_win(root)
    root.mainloop()
