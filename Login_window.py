import tkinter as tk
import mysql.connector
from tkinter import *


def submitact():
	
	user = Username.get()
	passw = password.get()

	print(f"The name entered by you is {user} {passw}")

	logintodb(user, passw)


def logintodb(user, passw):
	
	# If password is entered by the
	# user
	if passw:
		db = mysql.connector.connect(host ="localhost",
									user = user,
									password = passw,
									db ="College")
		cursor = db.cursor()
		
	# If no password is entered by the
	# user
	else:
		db = mysql.connector.connect(host ="localhost",
									user = user,
									db ="College")
		cursor = db.cursor()
		
	# A Table in the database
	savequery = "select * from STUDENT"
	
	try:
		cursor.execute(savequery)
		myresult = cursor.fetchall()
		
		# Printing the result of the
		# query
		for x in myresult:
			print(x)
		print("Query Executed successfully")
		
	except:
		db.rollback()
		print("Error occurred")


root = tk.Tk()
root.geometry("900x500+200+00")
root.title("DBMS Login Page")


# Defining the first row
lblfrstrow = tk.Label(root, text ="Username -",font=('times new roman',25))
lblfrstrow.place(x = 100, y = 100, width = 500)

Username = tk.Entry(root, width = 15,font=('times new roman',25))
Username.place(x = 500, y = 100,)

lblsecrow = tk.Label(root, text ="Password -",font=('times new roman',25))
lblsecrow.place(x = 100, y = 200, width = 500)

password = tk.Entry(root, width = 15,font=('times new roman',25))
password.place(x = 500, y = 200,)

submitbtn = tk.Button(root, text ="Login",font=('times new roman',20),
					fg="white",bg ='green', command = submitact,width=20)
submitbtn.place(x = 350, y = 300,)

root.mainloop()
