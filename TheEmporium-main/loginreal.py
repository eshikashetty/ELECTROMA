from tkinter import*
from PIL import ImageTk
from tkinter import messagebox
import mysql.connector
import subprocess
class Login:
    def __init__(self,root):
        self.root=root
        self.root.title("LOGIN")
        self.root.geometry("1299x600+200+150")
        self.root.resizable(True,True)
        self.bg=ImageTk.PhotoImage(file="Images\990.jpg")
        self.bg_image=Label(self.root,image=self.bg).place(x=0,y=0,relwidth=1,relheight=1)
        Frame_login=Frame(self.root,bg="white")
        Frame_login.place(x=150,y=150,height=340,width=500)
        title=Label(Frame_login,text="ELECTROMA",font=("Impact",35,"bold"),fg="#d77337",bg="white") .place(x=90,y=30)
        lbl_login=Label(Frame_login,text="Login Here",font=("times new roman",15,"bold"),fg="black",bg="white") .place(x=90,y=95)
        lbl_user=Label(Frame_login,text="Username",font=("Goudy old style",15,"bold"),fg="gray",bg="white") .place(x=90,y=140)
        self.txt_user=Entry(Frame_login,font=("times new roman",15),bg="lightgray")
        self.txt_user.place(x=90,y=170,width=350,height=35)

        lbl_pass=Label(Frame_login,text="Password",font=("Goudy old style",15,"bold"),fg="gray",bg="white") .place(x=90,y=210)
        self.txt_pass=Entry(Frame_login,font=("times new roman",15),bg="lightgray",show="*")
        self.txt_pass.place(x=90,y=240,width=350,height=35)

        forget_btn=Button(Frame_login,text="Forget Password?",bg="white",fg="#d77337",bd=0,font=("times new roman",12)).place(x=90,y=280)
        login_btn=Button(self.root,text="Login",fg="white",bg="#d77337",font=("times new roman",20), command=self.login).place(x=300,y=470,width=180,height=40)

    def connect_to_database(self):
        mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Root@123",
        database="mpr"
        )
        return mydb

    def login(self):
        username = self.txt_user.get()
        password = self.txt_pass.get()
        mydb = self.connect_to_database()
        mycursor = mydb.cursor()
        mycursor.execute("SELECT * FROM users WHERE username = %s AND password = %s", (username, password))
        result = mycursor.fetchone()
        if result:
            messagebox.showinfo("Success", "Login successful!")
            self.root.destroy()
            subprocess.run(["python", "TheEmporium.py"])
            
            
           
        else:
            messagebox.showerror("Error", "Invalid username or password.")
root=Tk()
obj=Login(root)
root.mainloop()





