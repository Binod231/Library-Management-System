from tkinter import *
from PIL import ImageTk,Image
import sqlite3
from tkinter import messagebox
from AddBook import *
from DeleteBook import *
from ViewBooks import *
from IssueBook import *
from ReturnBook import *
from StudentList import *


def createTable():
    con = sqlite3.connect("project.db")
    cur = con.cursor()
    cur.executescript('''
create table if not exists  books (bid text primary key,title text,author text,status text);
create table if not exists books_issued (bid text primary key,
                      issued_to text);
''')
    # con.commit()
# Add your own database name and password here to reflect in the code
mypass = "root"
mydatabase="db"

con = sqlite3.connect("project.db")
cur = con.cursor()

root = Tk()
root.state("zoomed")
root.iconbitmap("library.ico")
root.title("Library")
root.minsize(width=400,height=400)
root.geometry("600x500")

# Take n greater than 0.25 and less than 5
same=True
n=0.25

# Adding a background image
background_image =Image.open("lib.jpg")
#background_image = background_image.resize((root.winfo_screenwidth(), root.winfo_screenheight()), Image.ANTIALIAS)
background_photo = ImageTk.PhotoImage(background_image)
background_label = Label(root, image=background_photo)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

headingFrame1 = Frame(root,bg="#FFBB00",bd=5)
headingFrame1.place(relx=0.2,rely=0.1,relwidth=0.6,relheight=0.16)

headingLabel = Label(headingFrame1, text="Welcome to \n Binod Library", bg='black', fg='white', font=('Courier',15))
headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)

btn1 = Button(root,text="Add Book Details",bg='black', fg='white', command=addBook)
btn1.place(relx=0.28,rely=0.3, relwidth=0.45,relheight=0.1)
    
btn2 = Button(root,text="Delete Book",bg='black', fg='white', command=delete)
btn2.place(relx=0.28,rely=0.4, relwidth=0.45,relheight=0.1)
    
btn3 = Button(root,text="View Book List",bg='black', fg='white', command=View)
btn3.place(relx=0.28,rely=0.5, relwidth=0.45,relheight=0.1)
    
btn4 = Button(root,text="Issue Book to Student",bg='black', fg='white', command = issueBook)
btn4.place(relx=0.28,rely=0.6, relwidth=0.45,relheight=0.1)
    
btn5 = Button(root,text="Return Book",bg='black', fg='white', command = returnBook)
btn5.place(relx=0.28,rely=0.7, relwidth=0.45,relheight=0.1)

btn6 = Button(root, text="View Student List", bg='black', fg='white', command = displayStudentList)
btn6.place(relx=0.28, rely=0.8, relwidth=0.45, relheight=0.1)
createTable()
root.mainloop()