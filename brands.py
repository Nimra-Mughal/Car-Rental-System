from tkinter import *
from PIL import Image,ImageTk
from tkinter import ttk
import random
import pymysql
from tkinter import messagebox


class brands:
    def __init__(self,root):
        self.root=root
        self.root.title("Customer")
        self.root.geometry("1370x610+225+218")

        lbltitle = Label(self.root, text="OUR BRANDS DETAILS", font=("times new roman", 18, "bold"), bg="black",fg="gold", bd=4, relief=RIDGE)
        lbltitle.place(x=0, y=0, width=1370, height=50)

        img2 = Image.open("Images\\logo.png")
        img2 = img2.resize((100, 45), Image.ANTIALIAS)
        self.photoimg2 = ImageTk.PhotoImage(img2)
        lblimg = Label(self.root, image=self.photoimg2, bd=0, relief=RIDGE)
        lblimg.place(x=5, y=2, width=100, height=45)

        labelframeleft = LabelFrame(self.root, bd=2, relief=RIDGE, text="Available Brands",font=("times new roman", 18, "bold"), padx=5)
        labelframeleft.place(x=20, y=50, width=1320, height=550)

        # data = con.execute("select * from student")
        # print("id","Name","class","email")
        # for a in data:
        #     print(a[0],a[1],a[2],a[3])
        # con.close()

        # ================= show data table ==========
        details_table = Frame(labelframeleft, bd=2, relief=RIDGE)
        details_table.place(x=80, y=80, width=510, height=350)

        # scroll_x = ttk.Scrollbar(details_table, orient=HORIZONTAL)
        # scroll_y = ttk.Scrollbar(details_table, orient=VERTICAL)

        self.Cust_Details_Table = ttk.Treeview(details_table, column=("ref", "bname"))
        # scroll_x.pack(side=BOTTOM, fill=X)
        # scroll_y.pack(side=RIGHT, fill=Y)
        #
        # scroll_x.config(command=self.Cust_Details_Table.xview)
        # scroll_y.config(command=self.Cust_Details_Table.yview)

        self.Cust_Details_Table.heading("ref", text="Refer No")
        self.Cust_Details_Table.heading("bname", text=" BrandName")

        self.Cust_Details_Table["show"] = "headings"
        self.Cust_Details_Table.column("ref")
        self.Cust_Details_Table.column("bname")

        self.Cust_Details_Table.pack(fill=BOTH, expand=1)
        self.fetch_data()


        self.bg1 = ImageTk.PhotoImage(file="Images\\brands.png")
        lbl_left = Label(self.root, image=self.bg1)
        lbl_left.place(x=680, y=130, width=570,height=400)

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
    obj=brands(root)
    root.mainloop()