from tkinter import *
from PIL import Image,ImageTk
from tkinter import ttk
import random
import pymysql
from tkinter import messagebox
from tkinter import filedialog


class add_brands:
    def __init__(self,root):
        self.root=root
        self.root.title("Customer")
        self.root.geometry("1370x610+225+218")
        uploaded_img = Label(root)

        # ==============Variables============
        self.var_ref=StringVar()
        x=random.randint(1000,9999)
        self.var_ref.set(str(x))

        self.var_brand_name=StringVar()


        lbltitle = Label(self.root, text="ADD BRANDS FOR CAR", font=("times new roman", 18, "bold"), bg="black",fg="gold", bd=4, relief=RIDGE)
        lbltitle.place(x=0, y=0, width=1370, height=50)

        img2 = Image.open("Images\\logo.png")
        img2 = img2.resize((100, 45), Image.ANTIALIAS)
        self.photoimg2 = ImageTk.PhotoImage(img2)
        lblimg = Label(self.root, image=self.photoimg2, bd=0, relief=RIDGE)
        lblimg.place(x=5, y=2, width=100, height=45)

        labelframeleft=LabelFrame(self.root,bd=2,relief=RIDGE,text="Brands Details",font=("times new roman", 18, "bold"),padx=5)
        labelframeleft.place(x=5,y=50,width=425,height=550)

        lbl_brand_ref=Label(labelframeleft,text="Brands Id ",font=("times new roman", 13, "bold"),padx=2,pady=6)
        lbl_brand_ref.grid(row=0,column=0,sticky=W)
        entry_brand=ttk.Entry(labelframeleft,textvariable=self.var_ref,width=29,font=("times new roman", 13, "bold"),state="readonly")
        entry_brand.grid(row=1,column=0,padx=80)

        bname = Label(labelframeleft, text="Brand Name", font=("times new roman", 13, "bold"), padx=2, pady=6)
        bname.grid(row=2, column=0, sticky=W)
        txt_bname = ttk.Entry(labelframeleft,textvariable=self.var_brand_name, width=29, font=("times new roman", 13, "bold"))
        txt_bname.grid(row=3, column=0,padx=80)

        # bname = Label(labelframeleft, text="Brand Image", font=("times new roman", 13, "bold"), padx=2, pady=6)
        # bname.grid(row=4, column=0, sticky=W)
        # uploadbtn=Button(labelframeleft,text=" Upload Image ",command=self.upload,font=("times new roman",13, "bold"),bg="grey",fg="black",width=9)
        # uploadbtn.grid(row=5, column=0, padx=80)


        btn_frame=Frame(labelframeleft,bd=2,relief=RIDGE)
        btn_frame.place(x=0,y=300,width=412,height=40)

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
        combo_Search['values'] = ("Brand", "Ref")
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

        self.Cust_Details_Table=ttk.Treeview(details_table,column=("ref","bname"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.Cust_Details_Table.xview)
        scroll_y.config(command=self.Cust_Details_Table.yview)

        self.Cust_Details_Table.heading("ref",text="Refer No")
        self.Cust_Details_Table.heading("bname",text=" BrandName")

        self.Cust_Details_Table["show"]="headings"
        self.Cust_Details_Table.column("ref",width=10)
        self.Cust_Details_Table.column("bname",width=100)


        self.Cust_Details_Table.pack(fill=BOTH,expand=1)
        self.fetch_data()

    # def upload(self):
    #     try:
    #         path = filedialog.askopenfilename()
    #         image = Image.open(path)
    #         img = ImageTk.PhotoImage(image)
    #         self.uploaded_img.configure(image=img)
    #         self.uploaded_img.image = img
    #     except:
    #         pass

    def add_data(self):
        if self.var_brand_name.get()=="" :
            messagebox.showerror("Error","All field are required ")
        else:
            # messagebox.showinfo("Error","Sucessfully registerd",parent=self.root)
            try:
                con = pymysql.connect(host="localhost", user="root", password="", database="carRentalSystem")
                cursor = con.cursor()
                cursor.execute(
                    "insert into brands (ref,bname) values (%s,%s)",
                    (
                        self.var_ref.get(),
                        self.var_brand_name.get()))
                con.commit()
                self.fetch_data()
                con.close()
                messagebox.showinfo("Success", "Add Successfully", parent=self.root)
                # self.ClearData()
            except Exception as ex:
                messagebox.showerror("Error", f"Error due to {str(ex)}", parent=self.root)

    def fetch_data(self):

        try:
            con = pymysql.connect(host="localhost", user="root", password="", database="carRentalSystem")
            cursor = con.cursor()
            cursor.execute("select * from brands")
            rows = cursor.fetchall()
            if len(rows) != 0:
                self.Cust_Details_Table.delete(*self.Cust_Details_Table.get_children())
                for i in rows:
                    self.Cust_Details_Table.insert("", END, values=i)
                con.commit()
            con.close()
            # self.ClearData()
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}", parent=self.root)





if __name__ == '__main__':
    root=Tk()
    obj=add_brands(root)
    root.mainloop()
