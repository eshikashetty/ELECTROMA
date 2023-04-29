import tkinter as tk
from tkinter import messagebox
import os

# Function to check login credentials
def login():
    username = entry_username.get()
    password = entry_password.get()

    # Check if username and password match
    if username == "admin" and password == "password":
        # Successful login, open invoices folder
        invoices_folder = "C:/Users/eshik/Downloads/TheEmporium-main/TheEmporium-main/InvoicesInvoices"
        os.startfile("C:/Users/eshik/Downloads/TheEmporium-main")
    else:
        # Invalid login, show error message
        messagebox.showerror("Error", "Invalid username or password")

# Create main window
root = tk.Tk()
root.title("Admin Login")

# Create username label and entry
label_username = tk.Label(root, text="Username:")
label_username.pack()
entry_username = tk.Entry(root)
entry_username.pack()

# Create password label and entry
label_password = tk.Label(root, text="Password:")
label_password.pack()
entry_password = tk.Entry(root, show="*")
entry_password.pack()

# Create login button
btn_login = tk.Button(root, text="Login", command=login)
btn_login.pack()

# Run the Tkinter event loop
root.mainloop()
