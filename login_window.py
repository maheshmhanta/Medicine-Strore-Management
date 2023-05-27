import tkinter as tk
from tkinter import *
from PIL import ImageTk, Image
import mysql.connector
import tkinter.messagebox
from tkinter import ttk

def submitact():
	user = Username.get()
	passw = password.get()
# Function for login button on the login screen
def submit():
    global username, password, actual
    username = Username.get()
    password =str(password.get())
    query = "SELECT Password from dbusers where Username = %s"
    values = (username,)
    mycursor.execute(query, values)
    actualPassword = mycursor.fetchall()
    try:
        actual = actualPassword[0][0]
        mainFun()
    except:
        tkinter.messagebox.showinfo("Error", "Invalid Username", parent = root)


def Add():
    item = e1.get()
    quantity = (e2.get())
    price = (e3.get())
    

    mysqldb=mysql.connector.connect(host="localhost",user="root",password="akash",database="medicine",auth_plugin="mysql_native_password")
    mycursor=mysqldb.cursor()

    try:
       sql = "INSERT INTO  store VALUES (%s, %s, %s)"
       val = (item,quantity,price)
       mycursor.execute(sql, val)
       mysqldb.commit()
       lastid = mycursor.lastrowid
       tkinter.messagebox.showinfo("information", "Medicine inserted successfully...")
       e1.delete(0, END)
       e2.delete(0, END)
       e3.delete(0, END)
       e1.focus_set()
    except Exception as e:
       print(e)
       mysqldb.rollback()
       mysqldb.close()

def delete():
    item = e1.get()

    mysqldb=mysql.connector.connect(host="localhost",user="root",password="akash",database="medicine",auth_plugin="mysql_native_password")
    mycursor=mysqldb.cursor()

    try:
       sql = "delete from store where item = %s"
       val = (item,)
       mycursor.execute(sql, val)
       mysqldb.commit()
       tkinter.messagebox.showinfo("information", "Record Deleteeeee successfully...")

       e1.delete(0, END)
       e2.delete(0, END)
       e3.delete(0, END)
       e1.focus_set()

    except Exception as e:

       print(e)
       mysqldb.rollback()
       mysqldb.close()

def update():
    item = e1.get()
    quantity = e2.get()
    price = e3.get()
    mysqldb=mysql.connector.connect(host="localhost",user="root",password="akash",database="medicine",auth_plugin="mysql_native_password")
    mycursor=mysqldb.cursor()

    try:
       sql = "Update  store set quantity= %s,price= %s where item = %s"
       val = (quantity,price,item)
       mycursor.execute(sql, val)
       mysqldb.commit()
       tkinter.messagebox.showinfo("information", "Record Updateddddd successfully...")

       e1.delete(0, END)
       e2.delete(0, END)
       e3.delete(0, END)
       e1.focus_set()

    except Exception as e:

       print(e)
       mysqldb.rollback()
       mysqldb.close()

def mainFun():
    global root
    if password == actual:
        root.withdraw()
        main()
    else:
        tkinter.messagebox.showinfo("Error", "Please enter correct password", parent = root)

def main():
    root = tk.Tk()
    root.geometry("700x450")
    global e1
    global e2
    global e3
    tk.Label(root,text="Medicine Store",fg="black",font=('times new roman',36)).place(x=300,y=0)
            
    tk.Label(root,text="Item Name").place(x=10,y=10)
    Label(root,text="Quantity").place(x=10,y=40)
    Label(root,text="Price").place(x=10,y=70)

    e1=Entry(root)
    e1.place(x=140,y=10)
    e2=Entry(root)
    e2.place(x=140,y=40)
    e3=Entry(root)
    e3.place(x=140,y=70)

    Button(root,text="Add",height=2,width=9,command=Add).place(x=30,y=130)
    Button(root,text="Update",height=2,width=9,command=update).place(x=140,y=130)
    Button(root,text="Delete",height=2,width=9,command=delete).place(x=250,y=130)
    Button(root,text="Refresh",height=2,width=9,command=refresh).place(x=350,y=130)

    cols = ('ITEM', 'Quantity', 'Price')
    global listBox
    listBox = ttk.Treeview(root, columns=cols, show='headings' )
    
    for col in cols:
        listBox.heading(col, text=col)
        listBox.grid(row=1, column=0, columnspan=2)
        listBox.place(x=10, y=200)

    show()
    
    
    root.mainloop()


def refresh():
    #Clear the treeview list items
    for item in listBox.get_children():
        listBox.delete(item)
    show()


def show():
        mysqldb = mysql.connector.connect(host="localhost", user="root", password="akash",database="medicine",auth_plugin="mysql_native_password")
        mycursor = mysqldb.cursor()
        mycursor.execute("SELECT * FROM store")
        records = mycursor.fetchall()
        print(records)

        for i, (stname, course,fee) in enumerate(records, start=1):
            listBox.insert("", "end", values=(stname, course, fee))
            mysqldb.close()



root = tk.Tk()
root.geometry("800x500")

root.title("Login Page")


#Database connection - To access the username and password from a table
conn = mysql.connector.connect(host="localhost", user="root", password="akash", database="medicine",port=3306,auth_plugin='mysql_native_password')
mycursor = conn.cursor()

# Defining the first row
lblfrstrow = tk.Label(root, text ="Username -",font=('times new roman',25))
lblfrstrow.place(x = 100, y = 100, width = 300)

Username = tk.Entry(root, width = 15,font=('times new roman',25))
Username.place(x = 400, y = 100,)

lblsecrow = tk.Label(root, text ="Password -",font=('times new roman',25))
lblsecrow.place(x = 100, y = 200, width = 300)

password = tk.Entry(root, width = 15,font=('times new roman',25))
password.place(x = 400, y = 200,)

submitbtn = tk.Button(root, text ="Login",font=('times new roman',20),
					fg="white",bg ='green', command = submit,width=20)
submitbtn.place(x = 250, y = 300,)


root.mainloop()