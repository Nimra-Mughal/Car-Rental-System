from tkinter import *
from PIL import Image,ImageTk
from tkinter import ttk
import random
import pymysql
from tkinter import messagebox
from tkinter import filedialog


class reg:
    def __init__(self,root):
        self.root=root
        self.root.title("RegisterUser")
        self.root.geometry("1370x610+225+218")
        uploaded_img = Label(root)


        # ==============Table Frame ===================
        Table_Frame=LabelFrame(self.root,bd=2,relief=RIDGE,text="View Details And Search System", font=("times new roman", 14, "bold"),padx=5)
        Table_Frame.place(x=100,y=50,width=920,height=550)

        lblSearchBy=Label(Table_Frame,font=("times new roman", 12, "bold"),text="Search By : ",bg="red",fg="white")
        lblSearchBy.grid(row=0,column=0,sticky=W,padx=2)

        combo_Search = ttk.Combobox(Table_Frame, font=("times new roman", 15, "bold"), width=24, state="readonly")
        combo_Search['values'] = ("fname","lname","contact","email")
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

        self.Cust_Details_Table=ttk.Treeview(details_table,column=("fname","lname","contact","email"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.Cust_Details_Table.xview)
        scroll_y.config(command=self.Cust_Details_Table.yview)

        self.Cust_Details_Table.heading("fname",text="First Name")
        self.Cust_Details_Table.heading("lname",text=" Last Name")
        self.Cust_Details_Table.heading("contact",text="Contact")
        self.Cust_Details_Table.heading("email",text="Email")


        self.Cust_Details_Table["show"]="headings"
        self.Cust_Details_Table.column("fname",width=10)
        self.Cust_Details_Table.column("lname",width=100)
        self.Cust_Details_Table.column("contact",width=100)
        self.Cust_Details_Table.column("email",width=100)



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


    def fetch_data(self):

        try:
            con = pymysql.connect(host="localhost", user="root", password="", database="carRentalSystem")
            cursor = con.cursor()
            cursor.execute("select * from register")
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
    obj=reg(root)
    root.mainloop()
