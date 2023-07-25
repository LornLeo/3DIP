from tkinter import *
from csv import writer
import csv
from tkinter import messagebox
import subprocess
def submit(Username,Password,confirm_password):
    if Username and Password and confirm_password:
        if len(Password)<8:
            messagebox.showerror("Error", "Password at least 8 digits")
        elif Password!=confirm_password:
            messagebox.showerror("Error","Please match the password")
        else:
            User_ID=0
            with open("user_database.csv", 'r') as file:
                csvreader = csv.reader(file)
                rows=list(csvreader)
            error=False
            for row in rows:
                User_ID=User_ID+1
                if row[1]==Username:
                    messagebox.showerror("Error","Username has already been registered")
                    error=True
            if error==False:
                List=[User_ID,Username,Password,"offline"]
                with open('user_database.csv', 'a',newline='') as f_object:
                    writer_object = writer(f_object)
                    writer_object.writerow(List)
                    f_object.close()
                List=[User_ID,"1","0","unpaid"]
                with open('order_database.csv', 'a',newline='') as f_object:
                    writer_object = writer(f_object)
                    writer_object.writerow(List)
                    f_object.close()
                messagebox.showinfo("showinfo", "Successful")
                newWindow.destroy()
    else:
        if Username and Password:
            messagebox.showerror("Error","Please enter the confirmed password")
        elif Username and confirm_password:
            messagebox.showerror("Error","Please first enter the password")
        elif Username:
            messagebox.showerror("Error","Please enter the password")
        else:
            messagebox.showerror("Error","Please enter the username")

newWindow = Tk()
newWindow.title("Create account")
newWindow.geometry("500x250")
newWindow.resizable(0, 0)
newWindow.configure(bg="white")
menu_title = Label(newWindow,text="Create account",font=('Rockwell 21'),bg='#fcc302',fg="white",width=9,padx=30,pady=2)
menu_title.grid(row=0,column=0,columnspan=2,sticky=W)
Username_lbl=Label(newWindow,text="Username: ",bg="white",font=('Arial 13'))
Username_lbl.grid(row=1,column=0,sticky=W,pady=(30,0))
Username_ent1= Entry(newWindow,bd=3,width=30,font=('Arial 13'))
Username_ent1.grid(row=1, column=1,sticky=W,pady=(30,0))

Password_lbl=Label(newWindow,text="Password: ",bg="white",font=('Arial 13'))
Password_lbl.grid(row=2,column=0,sticky=W,pady=(15,0))
Password_ent1= Entry(newWindow,show="*",bd=3,width=30,font=('Arial 13'))
Password_ent1.grid(row=2, column=1,sticky=W,pady=(15,0))
    
CPassword_lbl=Label(newWindow,text="Confirmed password: ",bg="white",font=('Arial 13'))
CPassword_lbl.grid(row=3,column=0,sticky=W,pady=(15,0))
CPassword_ent1= Entry(newWindow,bd=3,show="*",width=30,font=('Arial 13'))
CPassword_ent1.grid(row=3, column=1,sticky=W,pady=(15,0))
    
submit_button = Button(newWindow, text="Sign up",width=20,font=('serif 13'),fg="white",bg="black",command=lambda: submit(Username_ent1.get(),Password_ent1.get(),CPassword_ent1.get()))
submit_button.grid(row=6,column=1,pady=(15,0))

newWindow.mainloop()