from tkinter import *
from tkinter import filedialog, messagebox
from PIL import ImageTk, Image
import pytesseract
import pymysql

pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files (x86)\\Tesseract-OCR\\tesseract.exe'

root = Tk()
root.title('TechVidvan Text from image project')
uploaded_img=Label(root)


def RegData(self):

    try:
        con = pymysql.connect(host="localhost", user="root", password="", database="carRentalSystem")
        cursor = con.cursor()
        cursor.execute(
            "insert into Images (Photo) values (%s)",
            (
                self.uploadbtn))
        con.commit()
        con.close()
        messagebox.showinfo("Success", "Registered Successfully", parent=self.root)
        # self.ClearData()
    except Exception as ex:
        messagebox.showerror("Error", f"Error due to {str(ex)}", parent=self.root)


# myCursor.execute("CREATE TABLE IF NOT EXISTS Images(id INTEGERS(45) NOT NULL AUTO_INCREMENT PRIMARY KEY, Photo LONGBLOB NOT NULL")

def InsertBlob(FilePath):
    con = pymysql.connect(host="localhost", user="root", password="", database="carRentalSystem")
    myCursor = con.cursor()
    with open(FilePath, "rb") as File:
        BinaryData = File.read()
    SQLStatement = "INSERT INTO Images (Photo) VALUES (%s)"
    myCursor.execute(SQLStatement, (BinaryData, ))
    con.commit()


# def RetrieveBlob(ID):
#     con = pymysql.connect(host="localhost", user="root", password="", database="carRentalSystem")
#     myCursor = con.cursor()
#     SQLStatement2 = "SELECT * FROM Images WHERE id = '{0}'"
#     myCursor.execute(SQLStatement2.format(str(ID)))
#     myResult = myCursor.fetchone()[1]
#     StoreFilePath = "ImageOutputs/img{0}.jpg".format(str(ID))
#     print(myResult)
#     with open(StoreFilePath, "wb") as File:
#         File.write(myResult)
#         File.close()


def upload():
    try:
        path=filedialog.askopenfilename()
        image=Image.open(path)
        img=ImageTk.PhotoImage(image)
        uploaded_img.configure(image=img)
        uploaded_img.image=img
    except:
        pass


uploadbtn = Button(root,text="Upload an image",command=upload,bg="#2f2f77",fg="gray",height=2,width=20,font=('Times',15,'bold')).pack()

uploaded_img.pack()

root.mainloop()