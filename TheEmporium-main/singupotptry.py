from tkinter import*
from PIL import ImageTk
import mysql.connector
from tkinter import messagebox
from twilio.rest import Client


account_sid = "AC563c4715fe1a4e6f6e0dad8d0db8ab0c"
auth_token = "c9ac4313d66736a964e592f18590f609"
verify_sid = "VAd89e7f513cee045f88717e335b57123b"

client = Client(account_sid, auth_token)
class Signup:
    
    def __init__(self, root):
        self.root = root
        self.root.title("Sign Up")
        self.root.geometry("1299x600+200+150")
        self.root.resizable(True, True)
        self.bg = ImageTk.PhotoImage(file="Images\990.jpg")
        self.bg_image = Label(self.root, image=self.bg).place(x=0, y=0, relwidth=1, relheight=1)
        self.username = StringVar()
        self.password = StringVar()
        self.phone_no=StringVar()
        self.email = StringVar()
        self.otp = StringVar()
        self.Frame_signup = Frame(self.root, bg="white")
        self.Frame_signup.place(x=150, y=150, height=500, width=600)
     

        title = Label(self.Frame_signup, text="ELECTROMA", font=("Impact", 35, "bold"), fg="#d77337", bg="white").place(
            x=90, y=30)
        lbl_signup=Label(self.Frame_signup, text="Sign Up:", font=("new times roman", 15, "bold"), fg="black", bg="white").place(
            x=90, y=95)

        lbl_user = Label(self.Frame_signup, text="Username", font=("Goudy old style", 15, "bold"), fg="gray",
                          bg="white").place(x=90, y=140)
        self.txt_user = Entry(self.Frame_signup, font=("times new roman", 15), bg="lightgray", textvariable=self.username)
        self.txt_user.place(x=90, y=170, width=350, height=35)

        lbl_pass = Label(self.Frame_signup, text="Password", font=("Goudy old style", 15, "bold"), fg="gray",
                          bg="white").place(x=90, y=210)
        self.txt_pass = Entry(self.Frame_signup, font=("times new roman", 15), bg="lightgray", show="*", textvariable=self.password)
        self.txt_pass.place(x=90, y=240, width=350, height=35)

        lbl_email = Label(self.Frame_signup, text="Email", font=("Goudy old style", 15, "bold"), fg="gray",
                          bg="white").place(x=90, y=280)
        self.txt_email = Entry(self.Frame_signup, font=("times new roman", 15), bg="lightgray", textvariable=self.email)
        self.txt_email.place(x=90, y=310, width=350, height=35)
        
        lbl_phone_no = Label(self.Frame_signup, text="Contact Number", font=("Goudy old style", 15, "bold"), fg="gray",
                          bg="white").place(x=90, y=360)
        self.txt_phone_no = Entry(self.Frame_signup, font=("times new roman", 15), bg="lightgray", textvariable=self.phone_no)
        self.txt_phone_no.place(x=90, y=390, width=350, height=35)

        def enable_button():
                submit_btn.config(state="normal")
        
        signup_btn = Button(self.root, text="Sign Up", fg="white", bg="#d77337", font=("times new roman", 20), command=self.signup)
        signup_btn.place(x=300, y=680, width=180, height=40)
        submit_btn = Button(self.root, text="Submit", fg="white", bg="#d77337", font=("times new roman", 20), command=self.check_otp)
        submit_btn.place(x=500, y=680, width=180, height=40)
        submit_btn.config(state="disabled")
        root.after(22000, enable_button)
       

    
    def signup(self):
        # Send OTP via SMS
        verification = client.verify.v2.services(verify_sid) \
            .verifications \
            .create(to=self.phone_no.get(), channel="sms")
        if verification.status != 'pending':
            messagebox.showerror("Error", "Failed to send OTP")
            return

        # Display OTP field
        lbl_otp = Label(self.Frame_signup, text="Enter OTP", font=("Goudy old style", 15, "bold"), fg="gray", bg="white")
        lbl_otp.place(x=90, y=430)
        self.txt_otp = Entry(self.Frame_signup, font=("times new roman", 15), bg="lightgray", show="*", state="normal")
        self.txt_otp.place(x=90, y=460, width=350, height=35)
        self.txt_otp.focus_set()
        messagebox.showinfo("Success", "OTP sent successfully!")

        # Verify OTP
    def check_otp(self):
        verification_check = client.verify.v2.services(verify_sid) \
            .verification_checks \
            .create(to=self.phone_no.get(), code=self.txt_otp.get())
        if verification_check.status == "approved":
            messagebox.showinfo("Success", "OTP verified successfully!")
        else:
            messagebox.showerror("Error", "Invalid OTP, try again!")
                

        # Insert user details into MySQL database
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Root@123",
            database="mpr"
        )
        mycursor = mydb.cursor()
        sql = "INSERT INTO users (username, password, email, phone_no) VALUES (%s, %s, %s, %s)"
        val = (self.username.get(), self.password.get(), self.email.get(), self.phone_no.get())
        mycursor.execute(sql, val)
        mydb.commit()
        messagebox.showinfo("Success", "User registered successfully!")
        self.txt_user.delete(0, END)
        self.txt_pass.delete(0, END)
        self.txt_email.delete(0, END)
        self.txt_phone_no.delete(0, END)
        self.txt_otp.delete(0, END)
        self.root.destroy()

        

        #messagebox.showinfo("Success", "otp send successfully!")

          

        #self.txt_user.delete(0, END)
        #self.txt_pass.delete(0, END)
        #self.txt_email.delete(0, END)
        #self.txt_phone_no.delete(0,END)
        #self.txt_otp.delete(0, END)
        #self.txt_otp.destroy()
        #lbl_otp.destroy()
        #self.signup_clicked = False
        #self.root.destroy()
        
        import loginreal
        loginreal.Login

root = Tk()
obj = Signup(root)
root.mainloop()
