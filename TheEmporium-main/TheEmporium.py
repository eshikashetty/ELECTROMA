from tkinter import *
from tkinter import messagebox
import PIL as p
import PIL.ImageTk as ptk
import os
from datetime import datetime
root=Tk()
root.title("Electroma.in")
root.geometry("1360x1100")
Heading=LabelFrame(root,bd=2,relief="groove",bg="orange")
Heading.place(x=0,y=0,width=1380,height=55)
image_logo=p.Image.open("Images\Logo.png")
image_logo_1=ptk.PhotoImage(image_logo)
label_logo=Label(Heading,image=image_logo_1)
label_logo.grid(row=0,column=0)
image_logo_large=ptk.PhotoImage(p.Image.open("Images\cart.png"))
HomeAppliances1_image=ptk.PhotoImage(p.Image.open("Images\HomeAppliances_1.jpg"))
HomeAppliances2_image=ptk.PhotoImage(p.Image.open("Images\HomeAppliances_2.jpeg"))
HomeAppliances3_image=ptk.PhotoImage(p.Image.open("Images\HomeAppliances_3.jpeg"))
HomeAppliances4_image=ptk.PhotoImage(p.Image.open("Images\HomeAppliances_4.jpeg"))
HomeAppliances5_image=ptk.PhotoImage(p.Image.open("Images\HomeAppliances_5.jpeg"))
HomeAppliances6_image=ptk.PhotoImage(p.Image.open("Images\HomeAppliances_6.jpeg"))
HomeAppliances7_image=ptk.PhotoImage(p.Image.open("Images\HomeAppliances_7.jpeg"))
HomeAppliances8_image=ptk.PhotoImage(p.Image.open("Images\HomeAppliances_8.jpeg"))
HomeAppliances9_image=ptk.PhotoImage(p.Image.open("Images\HomeAppliances_9.jpeg"))
HomeAppliances10_image=ptk.PhotoImage(p.Image.open("Images\HomeAppliances_10.jpg"))
Televisions1_image=ptk.PhotoImage(p.Image.open("Images\Televisions_1.jpeg"))
Televisions2_image=ptk.PhotoImage(p.Image.open("Images\Televisions_2.jpeg"))
Televisions3_image=ptk.PhotoImage(p.Image.open("Images\Televisions_3.jpeg"))
Televisions4_image=ptk.PhotoImage(p.Image.open("Images\Televisions_4.jpeg"))
Televisions5_image=ptk.PhotoImage(p.Image.open("Images\Televisions_5.jpeg"))
Televisions6_image=ptk.PhotoImage(p.Image.open("Images\Televisions_6.jpeg"))
Televisions7_image=ptk.PhotoImage(p.Image.open("Images\Televisions_7.jpeg"))
Televisions8_image=ptk.PhotoImage(p.Image.open("Images\Televisions_8.jpeg"))
Televisions9_image=ptk.PhotoImage(p.Image.open("Images\Televisions_9.jpeg"))
Televisions10_image=ptk.PhotoImage(p.Image.open("Images\Televisions_10.jpeg"))
Cameraandaccessories1_image=ptk.PhotoImage(p.Image.open("Images\Cameraandaccessories_1.jpeg"))
Cameraandaccessories2_image=ptk.PhotoImage(p.Image.open("Images\Cameraandaccessories_2.jpeg"))
Cameraandaccessories3_image=ptk.PhotoImage(p.Image.open("Images\Cameraandaccessories_3.jpeg"))
Cameraandaccessories4_image=ptk.PhotoImage(p.Image.open("Images\Cameraandaccessories_4.jpeg"))
Cameraandaccessories5_image=ptk.PhotoImage(p.Image.open("Images\Cameraandaccessories_5.jpeg"))
Cameraandaccessories6_image=ptk.PhotoImage(p.Image.open("Images\Cameraandaccessories_6.jpeg"))
Cameraandaccessories7_image=ptk.PhotoImage(p.Image.open("Images\Cameraandaccessories_7.jpeg"))
Cameraandaccessories8_image=ptk.PhotoImage(p.Image.open("Images\Cameraandaccessories_8.jpeg"))
Cameraandaccessories9_image=ptk.PhotoImage(p.Image.open("Images\Cameraandaccessories_9.jpeg"))
Cameraandaccessories10_image=ptk.PhotoImage(p.Image.open("Images\Cameraandaccessories_10.jpeg"))
Computerandtablets1_image=ptk.PhotoImage(p.Image.open("Images\Computerandtablets_1.jpeg"))
Computerandtablets2_image=ptk.PhotoImage(p.Image.open("Images\Computerandtablets_2.jpeg"))
Computerandtablets3_image=ptk.PhotoImage(p.Image.open("Images\Computerandtablets_3.jpeg"))
Computerandtablets4_image=ptk.PhotoImage(p.Image.open("Images\Computerandtablets_4.jpeg"))
Computerandtablets5_image=ptk.PhotoImage(p.Image.open("Images\Computerandtablets_5.jpeg"))
Computerandtablets6_image=ptk.PhotoImage(p.Image.open("Images\Computerandtablets_6.jpeg"))
Computerandtablets7_image=ptk.PhotoImage(p.Image.open("Images\Computerandtablets_7.jpeg"))
Computerandtablets8_image=ptk.PhotoImage(p.Image.open("Images\Computerandtablets_8.jpeg"))
Computerandtablets9_image=ptk.PhotoImage(p.Image.open("Images\Computerandtablets_9.jpeg"))
Computerandtablets10_image=ptk.PhotoImage(p.Image.open("Images\Computerandtablets_10.jpeg"))

mobile1_image=ptk.PhotoImage(p.Image.open("Images\Mobile_1.jpeg"))
mobile2_image=ptk.PhotoImage(p.Image.open("Images\Mobile_2.jpeg"))
mobile3_image=ptk.PhotoImage(p.Image.open("Images\Mobile_3.jpeg"))
mobile4_image=ptk.PhotoImage(p.Image.open("Images\Mobile_4.jpeg"))
mobile5_image=ptk.PhotoImage(p.Image.open("Images\Mobile_5.jpeg"))
mobile6_image=ptk.PhotoImage(p.Image.open("Images\Mobile_6.jpeg"))
mobile7_image=ptk.PhotoImage(p.Image.open("Images\Mobile_7.jpeg"))
mobile8_image=ptk.PhotoImage(p.Image.open("Images\Mobile_8.jpeg"))
mobile9_image=ptk.PhotoImage(p.Image.open("Images\Mobile_9.jpeg"))
mobile10_image=ptk.PhotoImage(p.Image.open("Images\Mobile_10.jpeg"))




#HomeAppliances Variables
'''clicked_HomeAppliances1=StringVar()
clicked_HomeAppliances1.set("45000")
clicked_HomeAppliances2=StringVar()
clicked_HomeAppliances2.set("21500")
clicked_HomeAppliances3=StringVar()
clicked_HomeAppliances3.set("38490")
clicked_HomeAppliances4=StringVar()
clicked_HomeAppliances4.set("5000")
clicked_HomeAppliances5=StringVar()
clicked_HomeAppliances5.set("11590")
clicked_HomeAppliances6=StringVar()
clicked_HomeAppliances6.set("32900")
clicked_HomeAppliances7=StringVar()
clicked_HomeAppliances7.set("10000")
clicked_HomeAppliances8=StringVar()
clicked_HomeAppliances8.set("7000")
clicked_HomeAppliances9=StringVar()
clicked_HomeAppliances9.set("3649")
clicked_HomeAppliances10=StringVar()
clicked_HomeAppliances10.set("43790")'''
HomeAppliances_list=[]
#Televisions Variables
clicked_Televisions1=StringVar()
clicked_Televisions1.set("Aurora Blue")
clicked_Televisions2=StringVar()
clicked_Televisions2.set("Aquamarine Green")
clicked_Televisions3=StringVar()
clicked_Televisions3.set("Black")
clicked_Televisions4=StringVar()
clicked_Televisions4.set("Black")
clicked_Televisions5=StringVar()
clicked_Televisions5.set("Charcoal Grey")
clicked_Televisions6=StringVar()
clicked_Televisions6.set("Shadow Black")
clicked_Televisions7=StringVar()
clicked_Televisions7.set("Black")
clicked_Televisions8=StringVar()
clicked_Televisions8.set("Black")
clicked_Televisions9=StringVar()
clicked_Televisions9.set("Jet Black")
clicked_Televisions10=StringVar()
clicked_Televisions10.set("Blue & White")
Televisions_list=[]
#Sports and Gym variables
Cameraandaccessories_list=[]
#Computerandtablets variables
Computerandtablets_list=[]
#Appliances variables
mobile_list=[]
name=Label(Heading,text="Electroma",font="arial 20 bold italic",bg="orange",fg="white").grid(row=0,column=1)
tagline=Label(Heading,text="Shopping made easier!",font="arial 16 bold italic",fg="white",bg="orange").grid(row=0,column=2,padx=280)
Products_frame=LabelFrame(root,bd=2,relief="groove",text="Products",font="arial 16 bold",fg="orangered")
Products_frame.place(x=310,y=60,width=1040,height=620)
label_logo_large=Label(Products_frame,image=image_logo_large,bd=2).place(x=250,y=100)
label_enjoy=Label(Products_frame,text="Enjoy Shopping",font="castellar 20 bold").place(x=370,y=370)
Button_frame=LabelFrame(root,bd=2,relief="groove")
Button_frame.place(x=2,y=60,width=300,height=380)

import webbrowser

def show_second_button():
    save_invoice.config(state=Tk.NORMAL)

def ordernow(text):
    op = messagebox.askyesno("Order Confirmation", "Confirm your order")
    if op:
        messagebox.showinfo("Confirmation", "Order confirmed")
        proceed = messagebox.askyesno("Payment", "Proceed to payment?")
        if proceed:
            webbrowser.open_new("https://paytm.com/")
        else:
            messagebox.showinfo("Payment", "Payment cancelled.")
    else:
        messagebox.showinfo("Order Cancelled", "Your order has been cancelled.")
    

        

def save_invoice(text):
    op = messagebox.askyesno("Invoice Saving Confirmation", "Do you want to save the invoice in a file?")
    if op:
        t = datetime.now()
        s = str(t.day) + str(t.month) + str(t.year) + str(t.hour) + str(t.minute) + str(t.second)
        if not os.path.exists("Invoices"):
            os.mkdir("Invoices")
        with open("Invoices/" + s + ".txt", "w") as f:
            f.write(text)
        messagebox.showinfo("Invoice Saving Status", "Invoice is saved successfully as a text document with name " + s + ".txt")
    else:
        messagebox.showinfo("Invoice Saving Status", "The invoice is not saved into a file.")
def HideAllFrames():
    for widget in Products_frame.winfo_children():
        widget.destroy()
def Spaces(n,s1=" "):
    s=""
    for i in range(n):
        s+=s1
    return s
def HomeAppliancesCall():
    HideAllFrames()
    HomeAppliances_Label=Label(Products_frame,text="HomeAppliances",font="times 15 bold",fg="darkorange",bg="white").grid(row=0,column=0,padx=20)
    lf_HomeAppliances1=LabelFrame(Products_frame,bd=2,relief="groove")
    lf_HomeAppliances1.place(x=5,y=35,width=180,height=280)
    lf_HomeAppliances2=LabelFrame(Products_frame,bd=2,relief="groove")
    lf_HomeAppliances2.place(x=210,y=35,width=180,height=280)
    lf_HomeAppliances3=LabelFrame(Products_frame,bd=2,relief="groove")
    lf_HomeAppliances3.place(x=415,y=35,width=180,height=280)
    lf_HomeAppliances4=LabelFrame(Products_frame,bd=2,relief="groove")
    lf_HomeAppliances4.place(x=620,y=35,width=180,height=280)
    lf_HomeAppliances5=LabelFrame(Products_frame,bd=2,relief="groove")
    lf_HomeAppliances5.place(x=825,y=35,width=180,height=280)
    lf_HomeAppliances6=LabelFrame(Products_frame,bd=2,relief="groove")
    lf_HomeAppliances6.place(x=5,y=310,width=180,height=280)
    lf_HomeAppliances7=LabelFrame(Products_frame,bd=2,relief="groove")
    lf_HomeAppliances7.place(x=210,y=310,width=180,height=280)
    lf_HomeAppliances8=LabelFrame(Products_frame,bd=2,relief="groove")
    lf_HomeAppliances8.place(x=415,y=310,width=180,height=280)
    lf_HomeAppliances9=LabelFrame(Products_frame,bd=2,relief="groove")
    lf_HomeAppliances9.place(x=620,y=310,width=180,height=280)
    lf_HomeAppliances10=LabelFrame(Products_frame,bd=2,relief="groove")
    lf_HomeAppliances10.place(x=825,y=310,width=180,height=280)
    label_HomeAppliances_1=Label(lf_HomeAppliances1,image=HomeAppliances1_image,bd=2).grid(row=0,column=0)
    label_HomeAppliances_2=Label(lf_HomeAppliances2,image=HomeAppliances2_image,bd=2).grid(row=0,column=0)
    label_HomeAppliances_3=Label(lf_HomeAppliances3,image=HomeAppliances3_image,bd=2).grid(row=0,column=0,padx=13)
    label_HomeAppliances_4=Label(lf_HomeAppliances4,image=HomeAppliances4_image,bd=2).grid(row=0,column=0)
    label_HomeAppliances_5=Label(lf_HomeAppliances5,image=HomeAppliances5_image,bd=2).grid(row=0,column=0)
    label_HomeAppliances_6=Label(lf_HomeAppliances6,image=HomeAppliances6_image,bd=2).grid(row=0,column=0)
    label_HomeAppliances_7=Label(lf_HomeAppliances7,image=HomeAppliances7_image,bd=2).grid(row=0,column=0)
    label_HomeAppliances_8=Label(lf_HomeAppliances8,image=HomeAppliances8_image,bd=2).grid(row=0,column=0)
    label_HomeAppliances_9=Label(lf_HomeAppliances9,image=HomeAppliances9_image,bd=2).grid(row=0,column=0)
    label_HomeAppliances_10=Label(lf_HomeAppliances10,image=HomeAppliances10_image,bd=2).grid(row=0,column=0)
    name_HomeAppliances1=Label(lf_HomeAppliances1,text="LG Refrigerator,260L",font="arial 9").grid(row=1,column=0)
    name_HomeAppliances2=Label(lf_HomeAppliances2,text="Samsung  Washing Machine 8kg",font="arial 9",justify="center").grid(row=1,column=0,padx=15)
    name_HomeAppliances3=Label(lf_HomeAppliances3,text="Hitachi Split AC,1.5 Ton",font="arial 9",justify="center").grid(row=1,column=0)
    name_HomeAppliances4=Label(lf_HomeAppliances4,text="Aquagard neo UF+UV,6.2 L ",font="arial 9",justify="center").grid(row=1,column=0,padx=9)
    name_HomeAppliances5=Label(lf_HomeAppliances5,text="Samsung 28L Microwave",font="arial 9",justify="center").grid(row=1,column=0,padx=9)
    name_HomeAppliances6=Label(lf_HomeAppliances6,text="Dyson V8 Vacuum Cleaner",font="arial 9",justify="center").grid(row=1,column=0,padx=15)
    name_HomeAppliances7=Label(lf_HomeAppliances7,text="Philips Air Purifier",font="arial 9",justify="center").grid(row=1,column=0)
    name_HomeAppliances8=Label(lf_HomeAppliances8,text="Havells 3L Geyser",font="arial 9",justify="center").grid(row=1,column=0,padx=20)
    name_HomeAppliances9=Label(lf_HomeAppliances9,text="Symphony Air Cooler",font="arial 9",justify="center").grid(row=1,column=0,padx=2)
    name_HomeAppliances10=Label(lf_HomeAppliances10,text="Bosch 14 Setting Place Dishwasher",font="arial 9",justify="center").grid(row=1,column=0)
    price_HomeAppliances1=Label(lf_HomeAppliances1,text="Price: Rs.45,000",font="arial 9 bold").place(x=5,y=245)
    price_HomeAppliances2=Label(lf_HomeAppliances2,text="Price: Rs.21,500",font="arial 9 bold").place(x=5,y=245)
    price_HomeAppliances3=Label(lf_HomeAppliances3,text="Price: Rs.38,490",font="arial 9 bold").place(x=5,y=245)
    price_HomeAppliances4=Label(lf_HomeAppliances4,text="Price: Rs.5,000",font="arial 9 bold").place(x=5,y=245)
    price_HomeAppliances5=Label(lf_HomeAppliances5,text="Price: Rs.11,590",font="arial 9 bold").place(x=5,y=245)
    price_HomeAppliances6=Label(lf_HomeAppliances6,text="Price: Rs.32,900",font="arial 9 bold").place(x=5,y=245)
    price_HomeAppliances7=Label(lf_HomeAppliances7,text="Price: Rs.10,000",font="arial 9 bold").place(x=5,y=245)
    price_HomeAppliances8=Label(lf_HomeAppliances8,text="Price: Rs.7,000",font="arial 9 bold").place(x=5,y=245)
    price_HomeAppliances9=Label(lf_HomeAppliances9,text="Price: Rs.3,649",font="arial 9 bold").place(x=5,y=245)
    price_HomeAppliances10=Label(lf_HomeAppliances10,text="Price: Rs.43,790",font="arial 9 bold").place(x=5,y=245)
    def AddG1():
        global HomeAppliances_list
        op=messagebox.askyesno("Purchase Confirmation","Are you sure that you want to add this item to the cart?")
        if op:
            HomeAppliances_list.append(["LG Refrigerator,260L",45000,"45,000",Spaces(40-len("LG Refrigerator,260L"))])
            messagebox.showinfo("Product Status","LG Refrigerator,260L  is successfully added to the cart.")
        else:
            messagebox.showinfo("Product Status","LG Refrigerator,260L  is not added to the cart.")
    def AddG2():
        global HomeAppliances_list
        op=messagebox.askyesno("Purchase Confirmation","Are you sure that you want to add this item to the cart?")
        if op:
            HomeAppliances_list.append(["Samsung Washing Machine 8kg",21500,"21500",Spaces(40-len("Samsung Washing Machine 8kg"))])
            messagebox.showinfo("Product Status","Samsung Washing Machine 8kg is successfully added to the cart.")
        else:
            messagebox.showinfo("Product Status","Samsung Washing Machine 8kg is not added to the cart.")
    def AddG3():
        global HomeAppliances_list
        op=messagebox.askyesno("Purchase Confirmation","Are you sure that you want to add this item to the cart?")
        if op:
            HomeAppliances_list.append(["Hitachi Split AC,1.5 Ton",38490,"38,490",Spaces(40-len("Hitachi Split AC,1.5 Ton"))])
            messagebox.showinfo("Product Status","Hitachi Split AC,1.5 Ton is successfully added to the cart.")
        else:
            messagebox.showinfo("Product Status","Hitachi Split AC,1.5 Ton is not added to the cart.")
    def AddG4():
        global HomeAppliances_list
        op=messagebox.askyesno("Purchase Confirmation","Are you sure that you want to add this item to the cart?")
        if op:
            HomeAppliances_list.append(["Aquagard neo UF+UV,6.2 L",5000,"5000",Spaces(40-len("Aquagard neo UF+UV,6.2 L"))])
            messagebox.showinfo("Product Status","Aquagard neo UF+UV,6.2 L is successfully added to the cart.")
        else:
            messagebox.showinfo("Product Status","Aquagard neo UF+UV,6.2 L is not added to the cart.")
    def AddG5():
        global HomeAppliances_list
        op=messagebox.askyesno("Purchase Confirmation","Are you sure that you want to add this item to the cart?")
        if op:
            HomeAppliances_list.append(["Samsung 28L Microwave",11590,"11,590",Spaces(40-len("Samsung 28L Microwave"))])
            messagebox.showinfo("Product Status","Samsung 28L Microwave is successfully added to the cart.")
        else:
            messagebox.showinfo("Product Status","Samsung 28L Microwave is not added to the cart.")
    def AddG6():
        global HomeAppliances_list
        op=messagebox.askyesno("Purchase Confirmation","Are you sure that you want to add this item to the cart?")
        if op:
            HomeAppliances_list.append(["Dyson V8 Vacuum Cleaner",32900,"32,900",Spaces(40-len("Dyson V8 Vacuum Cleaner"))])
            messagebox.showinfo("Product Status","Dyson V8 Vacuum Cleaner is successfully added to the cart.")
        else:
            messagebox.showinfo("Product Status","Dyson V8 Vacuum Cleaner is not added to the cart.")
    def AddG7():
        global HomeAppliances_list
        op=messagebox.askyesno("Purchase Confirmation","Are you sure that you want to add this item to the cart?")
        if op:
            HomeAppliances_list.append(["Philips Air Purifier",10000,"10,000",Spaces(40-len("Philips Air Purifier"))])
            messagebox.showinfo("Product Status","Philips Air Purifier is successfully added to the cart.")
        else:
            messagebox.showinfo("Product Status","Philips Air Purifier is not added to the cart.")
    def AddG8():
        global HomeAppliances_list
        op=messagebox.askyesno("Purchase Confirmation","Are you sure that you want to add this item to the cart?")
        if op:
            HomeAppliances_list.append(["Havells 3L Geyser",7000,"7,000",Spaces(40-len("Havells 3L Geyser"))])
            messagebox.showinfo("Product Status","Havells 3L Geyser is successfully added to the cart.")
        else:
            messagebox.showinfo("Product Status","Havells 3L Geyser is not added to the cart.")
    def AddG9():
        global HomeAppliances_list
        op=messagebox.askyesno("Purchase Confirmation","Are you sure that you want to add this item to the cart?")
        if op:
            HomeAppliances_list.append(["Symphony Air Cooler",3649,"3,649",Spaces(40-len("Symphony Air Cooler"))])
            messagebox.showinfo("Product Status","Symphony Air Cooler is successfully added to the cart.")
        else:
            messagebox.showinfo("Product Status","Symphony Air Cooler is not added to the cart.")
    def AddG10():
        global HomeAppliances_list
        op=messagebox.askyesno("Purchase Confirmation","Are you sure that you want to add this item to the cart?")
        if op:
            HomeAppliances_list.append(["Bosch 14 Setting Place Dishwasher",43790,"43,790",Spaces(40-len("Bosch 14 Setting Place Dishwasher"))])
            messagebox.showinfo("Product Status","Bosch 14 Setting Place Dishwasher is successfully added to the cart.")
        else:
            messagebox.showinfo("Product Status","Bosch 14 Setting Place Dishwasher is not added to the cart.")

    add_HomeAppliances1=Button(lf_HomeAppliances1,text="Add Item",bg="orangered",fg="white",font="times 9 bold",command=AddG1).place(x=120,y=245)
    add_HomeAppliances2=Button(lf_HomeAppliances2,text="Add Item",bg="orangered",fg="white",font="times 9 bold",command=AddG2).place(x=120,y=245)
    add_HomeAppliances3=Button(lf_HomeAppliances3,text="Add Item",bg="orangered",fg="white",font="times 9 bold",command=AddG3).place(x=120,y=245)
    add_HomeAppliances4=Button(lf_HomeAppliances4,text="Add Item",bg="orangered",fg="white",font="times 9 bold",command=AddG4).place(x=120,y=245)
    add_HomeAppliances5=Button(lf_HomeAppliances5,text="Add Item",bg="orangered",fg="white",font="times 9 bold",command=AddG5).place(x=120,y=245)
    add_HomeAppliances6=Button(lf_HomeAppliances6,text="Add Item",bg="orangered",fg="white",font="times 9 bold",command=AddG6).place(x=120,y=245)
    add_HomeAppliances7=Button(lf_HomeAppliances7,text="Add Item",bg="orangered",fg="white",font="times 9 bold",command=AddG7).place(x=120,y=245)
    add_HomeAppliances8=Button(lf_HomeAppliances8,text="Add Item",bg="orangered",fg="white",font="times 9 bold",command=AddG8).place(x=120,y=245)
    add_HomeAppliances9=Button(lf_HomeAppliances9,text="Add Item",bg="orangered",fg="white",font="times 9 bold",command=AddG9).place(x=120,y=245)
    add_HomeAppliances10=Button(lf_HomeAppliances10,text="Add Item",bg="orangered",fg="white",font="times 9 bold",command=AddG10).place(x=120,y=245)
def TelevisionsCall():
    HideAllFrames()
    Televisions_Label=Label(Products_frame,text="Televisions",font="times 15 bold",fg="darkorange",bg="white").grid(row=0,column=0,padx=10)
    lf_Televisions1=LabelFrame(Products_frame,bd=2,relief="groove")
    lf_Televisions1.place(x=5,y=35,width=200,height=280)
    lf_Televisions2=LabelFrame(Products_frame,bd=2,relief="groove")
    lf_Televisions2.place(x=210,y=35,width=200,height=280)
    lf_Televisions3=LabelFrame(Products_frame,bd=2,relief="groove")
    lf_Televisions3.place(x=415,y=35,width=200,height=280)
    lf_Televisions4=LabelFrame(Products_frame,bd=2,relief="groove")
    lf_Televisions4.place(x=620,y=35,width=200,height=280)
    lf_Televisions5=LabelFrame(Products_frame,bd=2,relief="groove")
    lf_Televisions5.place(x=825,y=35,width=200,height=280)
    lf_Televisions6=LabelFrame(Products_frame,bd=2,relief="groove")
    lf_Televisions6.place(x=5,y=310,width=200,height=280)
    lf_Televisions7=LabelFrame(Products_frame,bd=2,relief="groove")
    lf_Televisions7.place(x=210,y=310,width=200,height=280)
    lf_Televisions8=LabelFrame(Products_frame,bd=2,relief="groove")
    lf_Televisions8.place(x=415,y=310,width=200,height=280)
    lf_Televisions9=LabelFrame(Products_frame,bd=2,relief="groove")
    lf_Televisions9.place(x=620,y=310,width=200,height=280)
    lf_Televisions10=LabelFrame(Products_frame,bd=2,relief="groove")
    lf_Televisions10.place(x=825,y=310,width=200,height=280)
    label_Televisions_1=Label(lf_Televisions1,image=Televisions1_image,bd=2,justify="center").grid(row=0,column=0)
    label_Televisions_2=Label(lf_Televisions2,image=Televisions2_image,bd=2,justify="center").grid(row=0,column=0)
    label_Televisions_3=Label(lf_Televisions3,image=Televisions3_image,bd=2,justify="center").grid(row=0,column=0)
    label_Televisions_4=Label(lf_Televisions4,image=Televisions4_image,bd=2,justify="center").grid(row=0,column=0)
    label_Televisions_5=Label(lf_Televisions5,image=Televisions5_image,bd=2,justify="center").grid(row=0,column=0)
    label_Televisions_6=Label(lf_Televisions6,image=Televisions6_image,bd=2,justify="center").grid(row=0,column=0)
    label_Televisions_7=Label(lf_Televisions7,image=Televisions7_image,bd=2,justify="center").grid(row=0,column=0,padx=8)
    label_Televisions_8=Label(lf_Televisions8,image=Televisions8_image,bd=2,justify="center").grid(row=0,column=0,padx=7)
    label_Televisions_9=Label(lf_Televisions9,image=Televisions9_image,bd=2,justify="center").grid(row=0,column=0)
    label_Televisions_10=Label(lf_Televisions10,image=Televisions10_image,bd=2,justify="center").grid(row=0,column=0,padx=7)
    name_Televisions1=Label(lf_Televisions1,text="Samsung QN90A Neo QLED TV",font="arial 9",justify="center").grid(row=1,column=0,padx=3)
    name_Televisions2=Label(lf_Televisions2,text="LG OLED C1 Series TV",font="arial 9",justify="center").grid(row=1,column=0,padx=6)
    name_Televisions3=Label(lf_Televisions3,text="Sony Bravia X90J Series TV",font="arial 9",justify="center").grid(row=1,column=0)
    name_Televisions4=Label(lf_Televisions4,text="Vizio OLED TV",font="arial 9",justify="center").grid(row=1,column=0,padx=3)
    name_Televisions5=Label(lf_Televisions5,text="TCL 6-Series 4K HDR TV",font="arial 9",justify="center").grid(row=1,column=0,padx=9)
    name_Televisions6=Label(lf_Televisions6,text="Hisense U8G Series TV",font="arial 9",justify="center").grid(row=1,column=0)
    price_Televisions6=Label(lf_Televisions6,text="Price: Rs.67,900",font="arial 9 bold",justify="center").grid(row=4,column=0)
    name_Televisions7=Label(lf_Televisions7,text="Philips OLED 805 TV",font="arial 9",justify="center").grid(row=1,column=0)
    price_Televisions7=Label(lf_Televisions7,text="Price: Rs.49,990",font="arial 9 bold",justify="center").grid(row=4,column=0)
    name_Televisions8=Label(lf_Televisions8,text="OnePlus Y Series Full HD",font="arial 9",justify="center").grid(row=1,column=0)
    price_Televisions8=Label(lf_Televisions8,text="Price: Rs.30,499  Inches: 32",font="arial 9 bold",justify="center").grid(row=3,column=0)
    name_Televisions9=Label(lf_Televisions9,text="Xiaomi Mi TV Q1 75",font="arial 9",justify="center").grid(row=1,column=0,padx=6)
    name_Televisions10=Label(lf_Televisions10,text="Sharp Aquos R5G TV",font="arial 9",justify="center").grid(row=1,column=0)
    price_Televisions10=Label(lf_Televisions10,text="Price: Rs.23,250",font="arial 9 bold",justify="center").grid(row=3,column=0)
    label_clr_Televisions1=Label(lf_Televisions1,text="Colour:",bd=1,font="arial 9",justify="left").place(x=5,y=218)
    label_clr_Televisions2=Label(lf_Televisions2,text="Colour:",bd=1,font="arial 9",justify="left").place(x=5,y=218)
    label_clr_Televisions3=Label(lf_Televisions3,text="Colour:",bd=1,font="arial 9",justify="left").place(x=5,y=218)
    label_clr_Televisions4=Label(lf_Televisions4,text="Colour:",bd=1,font="arial 9",justify="left").place(x=5,y=218)
    label_clr_Televisions5=Label(lf_Televisions5,text="Colour:",bd=1,font="arial 9",justify="left").place(x=5,y=218)
    label_clr_Televisions6=Label(lf_Televisions6,text="Colour:",bd=1,font="arial 9",justify="left").place(x=5,y=218)
    label_clr_Televisions7=Label(lf_Televisions7,text="Colour:",bd=1,font="arial 9",justify="left").place(x=5,y=218)
    label_clr_Televisions8=Label(lf_Televisions8,text="Colour:",bd=1,font="arial 9",justify="left").place(x=5,y=218)
    label_clr_Televisions9=Label(lf_Televisions9,text="Colour:",bd=1,font="arial 9",justify="left").place(x=5,y=218)
    label_clr_Televisions10=Label(lf_Televisions10,text="Colour:",bd=1,font="arial 9",justify="left").place(x=5,y=218)
    options_Televisions1=["Aurora Blue","Interstellar Black","Glacier White","Champagne Gold"]
    options_Televisions2=["Aquamarine Green","Lunar Silver"]
    options_Televisions3=["Black","Forest Green","Molten Orange","Neon Lime"]
    options_Televisions4=["Black","Blue","White"]
    options_Televisions5=["Charcoal Grey","Red","Blue"]
    options_Televisions6=["Shadow Black","Fiery Red"]
    options_Televisions7=["Black"]
    options_Televisions8=["Black"]
    options_Televisions9=["Jet Black","Cherry Red","Mist Grey","Royal Blue"]
    options_Televisions10=["Blue & White"]
    global clicked_Televisions1,clicked_Televisions2,clicked_Televisions3,clicked_Televisions4,clicked_Televisions5,Televisions_list
    global clicked_Televisions6,clicked_Televisions7,clicked_Televisions8,clicked_Televisions9,clicked_Televisions10
    drop_Televisions1=OptionMenu(lf_Televisions1,clicked_Televisions1,*options_Televisions1).place(x=48,y=212)
    drop_Televisions2=OptionMenu(lf_Televisions2,clicked_Televisions2,*options_Televisions2).place(x=48,y=212)
    drop_Televisions3=OptionMenu(lf_Televisions3,clicked_Televisions3,*options_Televisions3).place(x=48,y=212)
    drop_Televisions4=OptionMenu(lf_Televisions4,clicked_Televisions4,*options_Televisions4).place(x=48,y=212)
    drop_Televisions5=OptionMenu(lf_Televisions5,clicked_Televisions5,*options_Televisions5).place(x=48,y=212)
    drop_Televisions6=OptionMenu(lf_Televisions6,clicked_Televisions6,*options_Televisions6).place(x=48,y=212)
    drop_Televisions7=OptionMenu(lf_Televisions7,clicked_Televisions7,*options_Televisions7).place(x=48,y=212)
    drop_Televisions8=OptionMenu(lf_Televisions8,clicked_Televisions8,*options_Televisions8).place(x=48,y=212)
    drop_Televisions9=OptionMenu(lf_Televisions9,clicked_Televisions9,*options_Televisions9).place(x=48,y=212)
    drop_Televisions10=OptionMenu(lf_Televisions10,clicked_Televisions10,*options_Televisions10).place(x=48,y=212)
    def AddE1():
        global Televisions_list
        op=messagebox.askyesno("Purchase Confirmation","Are you sure that you want to add this item to the cart?")
        if op:
            Televisions_list.append(["Samsung QN90A Neo QLED TV",34650,"34,650",clicked_Televisions1.get(),Spaces(40-len("Redmi Note 9 Pro"))])
            messagebox.showinfo("Product Status","Samsung QN90A Neo QLED TV ("+clicked_Televisions1.get()+") is successfully added to the cart.")
        else:
            messagebox.showinfo("Product Status","Samsung QN90A Neo QLED TV ("+clicked_Televisions1.get()+") is not added to the cart.")
    def AddE2():
        global Televisions_list
        op=messagebox.askyesno("Purchase Confirmation","Are you sure that you want to add this item to the cart?")
        if op:
            Televisions_list.append(["LG OLED C1 Series TV",42999,"42,999",clicked_Televisions2.get(),Spaces(40-len("OnePlus 8T 5G"))])
            messagebox.showinfo("Product Status","LG OLED C1 Series TV ("+clicked_Televisions2.get()+") is successfully added to the cart.")
        else:
            messagebox.showinfo("Product Status","LG OLED C1 Series TV ("+clicked_Televisions2.get()+") is not added to the cart.")
    def AddE3():
        global Televisions_list
        op=messagebox.askyesno("Purchase Confirmation","Are you sure that you want to add this item to the cart?")
        if op:
            Televisions_list.append(["Sony Bravia X90J Series TV",34499,"34,4499",clicked_Televisions3.get(),Spaces(40-len("boAt Earphones"))])
            messagebox.showinfo("Product Status","Sony Bravia X90J Series TV ("+clicked_Televisions3.get()+") is successfully added to the cart.")
        else:
            messagebox.showinfo("Product Status","Sony Bravia X90J Series TV ("+clicked_Televisions3.get()+") is not added to the cart.")
    def AddE4():
        global Televisions_list
        op=messagebox.askyesno("Purchase Confirmation","Are you sure that you want to add this item to the cart?")
        if op:
            Televisions_list.append(["Vizio OLED TV",22799,"22,799",clicked_Televisions4.get(),Spaces(40-len("JBL Headphones"))])
            messagebox.showinfo("Product Status","Vizio OLED TV ("+clicked_Televisions4.get()+") is successfully added to the cart.")
        else:
            messagebox.showinfo("Product Status","Vizio OLED TV ("+clicked_Televisions4.get()+") is not added to the cart.")
    def AddE5():
        global Televisions_list
        op=messagebox.askyesno("Purchase Confirmation","Are you sure that you want to add this item to the cart?")
        if op:
            Televisions_list.append(["TCL 6-Series 4K HDR TV",45699,"45,699",clicked_Televisions5.get(),Spaces(40-len("Logitech Mouse"))])
            messagebox.showinfo("Product Status","TCL 6-Series 4K HDR TV ("+clicked_Televisions5.get()+") is successfully added to the cart.")
        else:
            messagebox.showinfo("Product Status","TCL 6-Series 4K HDR TV ("+clicked_Televisions5.get()+") is not added to the cart.")
    def AddE6():
        global Televisions_list
        op=messagebox.askyesno("Purchase Confirmation","Are you sure that you want to add this item to the cart?")
        if op:
            Televisions_list.append(["Hisense U8G Series TV",67900,"67,900",clicked_Televisions6.get(),Spaces(40-len("HP Pavilion Laptop"))])
            messagebox.showinfo("Product Status","Hisense U8G Series TV ("+clicked_Televisions6.get()+") is successfully added to the cart.")
        else:
            messagebox.showinfo("Product Status","Hisense U8G Series TV ("+clicked_Televisions6.get()+") is not added to the cart.")
    def AddE7():
        global Televisions_list
        op=messagebox.askyesno("Purchase Confirmation","Are you sure that you want to add this item to the cart?")
        if op:
            Televisions_list.append(["Philips OLED 805 TV",49990,"49,990",clicked_Televisions7.get(),Spaces(40-len("Skyworth Q71 Series TV"))])
            messagebox.showinfo("Product Status","Philips OLED 805 TV ("+clicked_Televisions7.get()+") is successfully added to the cart.")
        else:
            messagebox.showinfo("Product Status","Philips OLED 805 TV ("+clicked_Televisions7.get()+") is not added to the cart.")
    def AddE8():
        global Televisions_list
        op=messagebox.askyesno("Purchase Confirmation","Are you sure that you want to add this item to the cart?")
        if op:
            Televisions_list.append(["OnePlus Android TV",30499,"30,499",clicked_Televisions8.get(),Spaces(40-len("OnePlus Android TV"))])
            messagebox.showinfo("Product Status","OnePlus Android TV ("+clicked_Televisions8.get()+") is successfully added to the cart.")
        else:
            messagebox.showinfo("Product Status","OnePlus Android TV ("+clicked_Televisions8.get()+") is not added to the cart.")
    def AddE9():
        global Televisions_list
        op=messagebox.askyesno("Purchase Confirmation","Are you sure that you want to add this item to the cart?")
        if op:
            Televisions_list.append(["Xiaomi Mi TV Q1 75",23999,"23,999",clicked_Televisions9.get(),Spaces(40-len("Xiaomi Mi TV Q1 75"))])
            messagebox.showinfo("Product Status","Xiaomi Mi TV Q1 75 ("+clicked_Televisions9.get()+") is successfully added to the cart.")
        else:
            messagebox.showinfo("Product Status","Xiaomi Mi TV Q1 75 ("+clicked_Televisions9.get()+") is not added to the cart.")
    def AddE10():
        global Televisions_list
        op=messagebox.askyesno("Purchase Confirmation","Are you sure that you want to add this item to the cart?")
        if op:
            Televisions_list.append(["Sharp Aquos R5G TV",23250,"23,250",clicked_Televisions10.get(),Spaces(40-len("Sharp Aquos R5G TV"))])
            messagebox.showinfo("Product Status","Sharp Aquos R5G TV ("+clicked_Televisions10.get()+") is successfully added to the cart.")
        else:
            messagebox.showinfo("Product Status","Sharp Aquos R5G TV ("+clicked_Televisions10.get()+") is not added to the cart.")
    price_Televisions1=Label(lf_Televisions1,text="Price: Rs.34,650",font="arial 9 bold").place(x=5,y=245)
    price_Televisions2=Label(lf_Televisions2,text="Price: Rs.42,999",font="arial 9 bold").place(x=5,y=245)
    price_Televisions3=Label(lf_Televisions3,text="Price: Rs.34,499",font="arial 9 bold").place(x=5,y=245)
    price_Televisions4=Label(lf_Televisions4,text="Price: Rs.22,799",font="arial 9 bold").place(x=5,y=245)
    price_Televisions5=Label(lf_Televisions5,text="Price: Rs.45,699",font="arial 9 bold").place(x=5,y=245)
    price_Televisions9=Label(lf_Televisions9,text="Price: Rs.23,999",font="arial 9 bold").place(x=5,y=245)
    add_Televisions1=Button(lf_Televisions1,text="Add Item",bg="darkorange",fg="white",font="times 9 bold",command=AddE1).place(x=120,y=245)
    add_Televisions2=Button(lf_Televisions2,text="Add Item",bg="darkorange",fg="white",font="times 9 bold",command=AddE2).place(x=120,y=245)
    add_Televisions3=Button(lf_Televisions3,text="Add Item",bg="darkorange",fg="white",font="times 9 bold",command=AddE3).place(x=120,y=245)
    add_Televisions4=Button(lf_Televisions4,text="Add Item",bg="darkorange",fg="white",font="times 9 bold",command=AddE4).place(x=120,y=245)
    add_Televisions5=Button(lf_Televisions5,text="Add Item",bg="darkorange",fg="white",font="times 9 bold",command=AddE5).place(x=120,y=245)
    add_Televisions6=Button(lf_Televisions6,text="Add Item",bg="darkorange",fg="white",font="times 9 bold",command=AddE6).place(x=60,y=245)
    add_Televisions7=Button(lf_Televisions7,text="Add Item",bg="darkorange",fg="white",font="times 9 bold",command=AddE7).place(x=60,y=245)
    add_Televisions8=Button(lf_Televisions8,text="Add Item",bg="darkorange",fg="white",font="times 9 bold",command=AddE8).place(x=60,y=245)
    add_Televisions9=Button(lf_Televisions9,text="Add Item",bg="darkorange",fg="white",font="times 9 bold",command=AddE9).place(x=120,y=245)
    add_Televisions10=Button(lf_Televisions10,text="Add Item",bg="darkorange",fg="white",font="times 9 bold",command=AddE10).place(x=60,y=245)
def CameraandaccessoriesCall():
    HideAllFrames()
    Cameraandaccessories_Label=Label(Products_frame,text="Camera and Accessories",font="times 15 bold",fg="orange",bg="white").grid(row=0,column=0,padx=10)
    lf_Cameraandaccessories1=LabelFrame(Products_frame,bd=2,relief="groove")
    lf_Cameraandaccessories1.place(x=5,y=35,width=200,height=280)
    lf_Cameraandaccessories2=LabelFrame(Products_frame,bd=2,relief="groove")
    lf_Cameraandaccessories2.place(x=210,y=35,width=200,height=280)
    lf_Cameraandaccessories3=LabelFrame(Products_frame,bd=2,relief="groove")
    lf_Cameraandaccessories3.place(x=415,y=35,width=200,height=280)
    lf_Cameraandaccessories4=LabelFrame(Products_frame,bd=2,relief="groove")
    lf_Cameraandaccessories4.place(x=620,y=35,width=200,height=280)
    lf_Cameraandaccessories5=LabelFrame(Products_frame,bd=2,relief="groove")
    lf_Cameraandaccessories5.place(x=825,y=35,width=200,height=280)
    lf_Cameraandaccessories6=LabelFrame(Products_frame,bd=2,relief="groove")
    lf_Cameraandaccessories6.place(x=5,y=310,width=200,height=280)
    lf_Cameraandaccessories7=LabelFrame(Products_frame,bd=2,relief="groove")
    lf_Cameraandaccessories7.place(x=210,y=310,width=200,height=280)
    lf_Cameraandaccessories8=LabelFrame(Products_frame,bd=2,relief="groove")
    lf_Cameraandaccessories8.place(x=415,y=310,width=200,height=280)
    lf_Cameraandaccessories9=LabelFrame(Products_frame,bd=2,relief="groove")
    lf_Cameraandaccessories9.place(x=620,y=310,width=200,height=280)
    lf_Cameraandaccessories10=LabelFrame(Products_frame,bd=2,relief="groove")
    lf_Cameraandaccessories10.place(x=825,y=310,width=200,height=280)
    label_Cameraandaccessories_1=Label(lf_Cameraandaccessories1,image=Cameraandaccessories1_image,bd=2,justify="center").grid(row=0,column=0)
    label_Cameraandaccessories_2=Label(lf_Cameraandaccessories2,image=Cameraandaccessories2_image,bd=2,justify="center").grid(row=0,column=0,padx=7)
    label_Cameraandaccessories_3=Label(lf_Cameraandaccessories3,image=Cameraandaccessories3_image,bd=2,justify="center").grid(row=0,column=0)
    label_Cameraandaccessories_4=Label(lf_Cameraandaccessories4,image=Cameraandaccessories4_image,bd=2,justify="center").grid(row=0,column=0,padx=8)
    label_Cameraandaccessories_5=Label(lf_Cameraandaccessories5,image=Cameraandaccessories5_image,bd=2,justify="center").grid(row=0,column=0)
    label_Cameraandaccessories_6=Label(lf_Cameraandaccessories6,image=Cameraandaccessories6_image,bd=2,justify="center").grid(row=0,column=0,padx=8)
    label_Cameraandaccessories_7=Label(lf_Cameraandaccessories7,image=Cameraandaccessories7_image,bd=2,justify="center").grid(row=0,column=0)
    label_Cameraandaccessories_8=Label(lf_Cameraandaccessories8,image=Cameraandaccessories8_image,bd=2,justify="center").grid(row=0,column=0,padx=8)
    label_Cameraandaccessories_9=Label(lf_Cameraandaccessories9,image=Cameraandaccessories9_image,bd=2,justify="center").grid(row=0,column=0)
    label_Cameraandaccessories_10=Label(lf_Cameraandaccessories10,image=Cameraandaccessories10_image,bd=2,justify="center").grid(row=0,column=0)
    name_Cameraandaccessories1=Label(lf_Cameraandaccessories1,text="Nikon Handcam",font="arial 9",justify="center").grid(row=1,column=0,padx=13)
    name_Cameraandaccessories2=Label(lf_Cameraandaccessories2,text="GoPro Hero11 Black",font="arial 9",justify="center").grid(row=1,column=0)
    name_Cameraandaccessories3=Label(lf_Cameraandaccessories3,text="Sony Alpha ILCE",font="arial 9",justify="center").grid(row=1,column=0)
    name_Cameraandaccessories4=Label(lf_Cameraandaccessories4,text="Tamron 17",font="arial 9",justify="center").grid(row=1,column=0)
    name_Cameraandaccessories5=Label(lf_Cameraandaccessories5,text="Samyang AF24",font="arial 9",justify="center").grid(row=1,column=0,padx=14)
    name_Cameraandaccessories6=Label(lf_Cameraandaccessories6,text="Cannon EOS",font="arial 9",justify="center").grid(row=1,column=0)
    name_Cameraandaccessories7=Label(lf_Cameraandaccessories7,text="GoPro CHDHC",font="arial 9",justify="center").grid(row=1,column=0,padx=4)
    name_Cameraandaccessories8=Label(lf_Cameraandaccessories8,text="Nikon Z50",font="arial 9",justify="center").grid(row=1,column=0)
    name_Cameraandaccessories9=Label(lf_Cameraandaccessories9,text="FujiFilm Insta X",font="arial 9",justify="center").grid(row=1,column=0,padx=12)
    name_Cameraandaccessories10=Label(lf_Cameraandaccessories10,text="Sanyipace Digital",font="arial 9",justify="center").grid(row=1,column=0,padx=5)
    price_Cameraandaccessories1=Label(lf_Cameraandaccessories1,text="Price: Rs.40,970",font="arial 9 bold").grid(row=2,column=0)
    price_Cameraandaccessories2=Label(lf_Cameraandaccessories2,text="Price: Rs.34,160",font="arial 9 bold").grid(row=2,column=0)
    price_Cameraandaccessories3=Label(lf_Cameraandaccessories3,text="Price: Rs.39,550",font="arial 9 bold").grid(row=2,column=0)
    price_Cameraandaccessories4=Label(lf_Cameraandaccessories4,text="Price: Rs.20,350",font="arial 9 bold").grid(row=2,column=0)
    price_Cameraandaccessories5=Label(lf_Cameraandaccessories5,text="Price: Rs.20,980",font="arial 9 bold").grid(row=2,column=0)
    price_Cameraandaccessories6=Label(lf_Cameraandaccessories6,text="Price: Rs.58,990",font="arial 9 bold").grid(row=3,column=0)
    price_Cameraandaccessories7=Label(lf_Cameraandaccessories7,text="Price: Rs.23,949",font="arial 9 bold").grid(row=4,column=0)
    price_Cameraandaccessories8=Label(lf_Cameraandaccessories8,text="Price: Rs.60,799",font="arial 9 bold").grid(row=3,column=0)
    price_Cameraandaccessories9=Label(lf_Cameraandaccessories9,text="Price: Rs.55,999",font="arial 9 bold").grid(row=2,column=0)
    price_Cameraandaccessories10=Label(lf_Cameraandaccessories10,text="Price: Rs.45,999",font="arial 9 bold").grid(row=2,column=0)
    def AddS1():
        global Cameraandaccessories_list
        op=messagebox.askyesno("Purchase Confirmation","Are you sure that you want to add this item to the cart?")
        if op:
            Cameraandaccessories_list.append(["GM Cricket Bat",40970,"40,970",Spaces(40-len("GM Cricket Bat"))])
            messagebox.showinfo("Product Status","Nikon Handcam is successfully added to the cart.")
        else:
            messagebox.showinfo("Product Status","Nikon Handcam is not added to the cart.")
    def AddS2():
        global Cameraandaccessories_list
        op=messagebox.askyesno("Purchase Confirmation","Are you sure that you want to add this item to the cart?")
        if op:
            Cameraandaccessories_list.append(["GoPro Hero11 Black",34160,"34,160",Spaces(40-len("GTS Leather Ball"))])
            messagebox.showinfo("Product Status","GoPro Hero11 Black is successfully added to the cart.")
        else:
            messagebox.showinfo("Product Status","GoPro Hero11 Black is not added to the cart.")
    def AddS3():
        global Cameraandaccessories_list
        op=messagebox.askyesno("Purchase Confirmation","Are you sure that you want to add this item to the cart?")
        if op:
            Cameraandaccessories_list.append(["Sony Alpha ILCE",39550,"39,550",Spaces(40-len("Yonex Badminton Racquet"))])
            messagebox.showinfo("Product Status","Sony Alpha ILCE is successfully added to the cart.")
        else:
            messagebox.showinfo("Product Status","Sony Alpha ILCE is not added to the cart.")
    def AddS4():
        global Cameraandaccessories_list
        op=messagebox.askyesno("Purchase Confirmation","Are you sure that you want to add this item to the cart?")
        if op:
            Cameraandaccessories_list.append(["Tamron 17",20350,"20,350",Spaces(40-len("Strauss Shuttlecock"))])
            messagebox.showinfo("Product Status","Tamron 17 is successfully added to the cart.")
        else:
            messagebox.showinfo("Product Status","Tamron 17 is not added to the cart.")
    def AddS5():
        global Cameraandaccessories_list
        op=messagebox.askyesno("Purchase Confirmation","Are you sure that you want to add this item to the cart?")
        if op:
            Cameraandaccessories_list.append(["Samyang AF24",20980,"20,980",Spaces(40-len("Table Tennis Kit"))])
            messagebox.showinfo("Product Status","Samyang AF24 is successfully added to the cart.")
        else:
            messagebox.showinfo("Product Status","Samyang AF24 is not added to the cart.")
    def AddS6():
        global Cameraandaccessories_list
        op=messagebox.askyesno("Purchase Confirmation","Are you sure that you want to add this item to the cart?")
        if op:
            Cameraandaccessories_list.append(["Cannon EOS",58990,"58,990",Spaces(40-len("Cockatoo Treadmill"))])
            messagebox.showinfo("Product Status","Cannon EOS  with Auto-Incline is successfully added to the cart.")
        else:
            messagebox.showinfo("Product Status","Cannon EOS  with Auto-Incline is not added to the cart.")
    def AddS7():
        global Cameraandaccessories_list
        op=messagebox.askyesno("Purchase Confirmation","Are you sure that you want to add this item to the cart?")
        if op:
            Cameraandaccessories_list.append(["GoPro CHDHC",23949,"23,949",Spaces(40-len("Aurion Dumbbells"))])
            messagebox.showinfo("Product Status","GoPro CHDHC is successfully added to the cart.")
        else:
            messagebox.showinfo("Product Status","GoPro CHDHC is not added to the cart.")
    def AddS8():
        global Cameraandaccessories_list
        op=messagebox.askyesno("Purchase Confirmation","Are you sure that you want to add this item to the cart?")
        if op:
            Cameraandaccessories_list.append(["Nikon Z50",60799,"60,799",Spaces(40-len("Bench Press Machine"))])
            messagebox.showinfo("Product Status","Nikon Z50 is successfully added to the cart.")
        else:
            messagebox.showinfo("Product Status","Nikon Z50 is not added to the cart.")
    def AddS9():
        global Cameraandaccessories_list
        op=messagebox.askyesno("Purchase Confirmation","Are you sure that you want to add this item to the cart?")
        if op:
            Cameraandaccessories_list.append(["FujiFilm Insta X",55999,"55,999",Spaces(40-len("Reach Exercise Cycle"))])
            messagebox.showinfo("Product Status","FujiFilm Insta X is successfully added to the cart.")
        else:
            messagebox.showinfo("Product Status","FujiFilm Insta X is not added to the cart.")
    def AddS10():
        global Cameraandaccessories_list
        op=messagebox.askyesno("Purchase Confirmation","Are you sure that you want to add this item to the cart?")
        if op:
            Cameraandaccessories_list.append(["Sanyipace Digital",45999,"45,999",Spaces(40-len("RMOUR Punch Bag"))])
            messagebox.showinfo("Product Status","Sanyipace Digital is successfully added to the cart.")
        else:
            messagebox.showinfo("Product Status","Sanyipace Digital is not added to the cart.")
    add_Cameraandaccessories1=Button(lf_Cameraandaccessories1,text="Add Item",bg="orange",fg="white",font="times 9 bold",command=AddS1).place(x=68,y=245)
    add_Cameraandaccessories2=Button(lf_Cameraandaccessories2,text="Add Item",bg="orange",fg="white",font="times 9 bold",command=AddS2).place(x=68,y=245)
    add_Cameraandaccessories3=Button(lf_Cameraandaccessories3,text="Add Item",bg="orange",fg="white",font="times 9 bold",command=AddS3).place(x=68,y=245)
    add_Cameraandaccessories4=Button(lf_Cameraandaccessories4,text="Add Item",bg="orange",fg="white",font="times 9 bold",command=AddS4).place(x=68,y=245)
    add_Cameraandaccessories5=Button(lf_Cameraandaccessories5,text="Add Item",bg="orange",fg="white",font="times 9 bold",command=AddS5).place(x=68,y=245)
    add_Cameraandaccessories6=Button(lf_Cameraandaccessories6,text="Add Item",bg="orange",fg="white",font="times 9 bold",command=AddS6).place(x=68,y=245)
    add_Cameraandaccessories7=Button(lf_Cameraandaccessories7,text="Add Item",bg="orange",fg="white",font="times 9 bold",command=AddS7).place(x=68,y=245)
    add_Cameraandaccessories8=Button(lf_Cameraandaccessories8,text="Add Item",bg="orange",fg="white",font="times 9 bold",command=AddS8).place(x=68,y=245)
    add_Cameraandaccessories9=Button(lf_Cameraandaccessories9,text="Add Item",bg="orange",fg="white",font="times 9 bold",command=AddS9).place(x=68,y=245)
    add_Cameraandaccessories10=Button(lf_Cameraandaccessories10,text="Add Item",bg="orange",fg="white",font="times 9 bold",command=AddS10).place(x=68,y=245)
def ComputerandtabletsCall():
    HideAllFrames()
    Computerandtablets_Label=Label(Products_frame,text="Computer and Tablets",font="times 15 bold",fg="salmon",bg="white").grid(row=0,column=0,padx=20)
    lf_Computerandtablets1=LabelFrame(Products_frame,bd=2,relief="groove")
    lf_Computerandtablets1.place(x=5,y=35,width=200,height=280)
    lf_Computerandtablets2=LabelFrame(Products_frame,bd=2,relief="groove")
    lf_Computerandtablets2.place(x=210,y=35,width=200,height=280)
    lf_Computerandtablets3=LabelFrame(Products_frame,bd=2,relief="groove")
    lf_Computerandtablets3.place(x=415,y=35,width=200,height=280)
    lf_Computerandtablets4=LabelFrame(Products_frame,bd=2,relief="groove")
    lf_Computerandtablets4.place(x=620,y=35,width=200,height=280)
    lf_Computerandtablets5=LabelFrame(Products_frame,bd=2,relief="groove")
    lf_Computerandtablets5.place(x=825,y=35,width=200,height=280)
    lf_Computerandtablets6=LabelFrame(Products_frame,bd=2,relief="groove")
    lf_Computerandtablets6.place(x=5,y=310,width=200,height=280)
    lf_Computerandtablets7=LabelFrame(Products_frame,bd=2,relief="groove")
    lf_Computerandtablets7.place(x=210,y=310,width=200,height=280)
    lf_Computerandtablets8=LabelFrame(Products_frame,bd=2,relief="groove")
    lf_Computerandtablets8.place(x=415,y=310,width=200,height=280)
    lf_Computerandtablets9=LabelFrame(Products_frame,bd=2,relief="groove")
    lf_Computerandtablets9.place(x=620,y=310,width=200,height=280)
    lf_Computerandtablets10=LabelFrame(Products_frame,bd=2,relief="groove")
    lf_Computerandtablets10.place(x=825,y=310,width=200,height=280)
    label_Computerandtablets_1=Label(lf_Computerandtablets1,image=Computerandtablets1_image,bd=2,justify="center").grid(row=0,column=0)
    label_Computerandtablets_2=Label(lf_Computerandtablets2,image=Computerandtablets2_image,bd=2,justify="center").grid(row=0,column=0,padx=8)
    label_Computerandtablets_3=Label(lf_Computerandtablets3,image=Computerandtablets3_image,bd=2,justify="center").grid(row=0,column=0,padx=8)
    label_Computerandtablets_4=Label(lf_Computerandtablets4,image=Computerandtablets4_image,bd=2,justify="center").grid(row=0,column=0,padx=8)
    label_Computerandtablets_5=Label(lf_Computerandtablets5,image=Computerandtablets5_image,bd=2,justify="center").grid(row=0,column=0,padx=8)
    label_Computerandtablets_6=Label(lf_Computerandtablets6,image=Computerandtablets6_image,bd=2,justify="center").grid(row=0,column=0)
    label_Computerandtablets_7=Label(lf_Computerandtablets7,image=Computerandtablets7_image,bd=2,justify="center").grid(row=0,column=0)
    label_Computerandtablets_8=Label(lf_Computerandtablets8,image=Computerandtablets8_image,bd=2,justify="center").grid(row=0,column=0,padx=8)
    label_Computerandtablets_9=Label(lf_Computerandtablets9,image=Computerandtablets9_image,bd=2,justify="center").grid(row=0,column=0,padx=8)
    label_Computerandtablets_10=Label(lf_Computerandtablets10,image=Computerandtablets10_image,bd=2,justify="center").grid(row=0,column=0,padx=8)
    name_Computerandtablets1=Label(lf_Computerandtablets1,text="Samsung led monitor",font="arial 9",justify="center").grid(row=1,column=0,padx=10)
    name_Computerandtablets2=Label(lf_Computerandtablets2,text="Frontech Led Monitor",font="arial 9",justify="center").grid(row=1,column=0)
    name_Computerandtablets3=Label(lf_Computerandtablets3,text="HP Pavillion",font="arial 9",justify="center").grid(row=1,column=0)
    name_Computerandtablets4=Label(lf_Computerandtablets4,text="Lenovo Ideapad Gaming",font="arial 9",justify="center").grid(row=1,column=0)
    name_Computerandtablets5=Label(lf_Computerandtablets5,text="Lenovo intel core i3",font="arial 9",justify="center").grid(row=1,column=0)
    name_Computerandtablets6=Label(lf_Computerandtablets6,text="Samsung galaxy",font="arial 9",justify="center").grid(row=1,column=0,padx=2)
    name_Computerandtablets7=Label(lf_Computerandtablets7,text="Redmi pad 4",font="arial 9",justify="center").grid(row=1,column=0,padx=5)
    name_Computerandtablets8=Label(lf_Computerandtablets8,text="Xiaomi pad 5",font="arial 9",justify="center").grid(row=1,column=0)
    name_Computerandtablets9=Label(lf_Computerandtablets9,text="realme pad",font="arial 9",justify="center").grid(row=1,column=0)
    name_Computerandtablets10=Label(lf_Computerandtablets10,text="Apple IPad",font="arial 9",justify="center").grid(row=1,column=0)
    
    price_Computerandtablets1=Label(lf_Computerandtablets1,text="Price: Rs.6,990",font="arial 9 bold").grid(row=2,column=0)
    price_Computerandtablets2=Label(lf_Computerandtablets2,text="Price: Rs.17,390",font="arial 9 bold").grid(row=3,column=0)
    price_Computerandtablets3=Label(lf_Computerandtablets3,text="Price: Rs.34,999",font="arial 9 bold").grid(row=3,column=0)
    price_Computerandtablets4=Label(lf_Computerandtablets4,text="Price: Rs.12,290",font="arial 9 bold").grid(row=4,column=0)
    price_Computerandtablets5=Label(lf_Computerandtablets5,text="Price: Rs.13,640",font="arial 9 bold").grid(row=3,column=0)
    price_Computerandtablets6=Label(lf_Computerandtablets6,text="Price: Rs.6,590",font="arial 9 bold").grid(row=2,column=0)
    price_Computerandtablets7=Label(lf_Computerandtablets7,text="Price: Rs.14,999",font="arial 9 bold").grid(row=3,column=0)
    price_Computerandtablets8=Label(lf_Computerandtablets8,text="Price: Rs.24,490",font="arial 9 bold").grid(row=3,column=0)
    price_Computerandtablets9=Label(lf_Computerandtablets9,text="Price: Rs.36,854",font="arial 9 bold").grid(row=4,column=0)
    price_Computerandtablets10=Label(lf_Computerandtablets10,text="Price: Rs.26,999",font="arial 9 bold").grid(row=3,column=0)
    def AddF1():
        global Computerandtablets_list
        op=messagebox.askyesno("Purchase Confirmation","Are you sure that you want to add this item to the cart?")
        if op:
            Computerandtablets_list.append(["Samsung led monitor",6990,"6,990",Spaces(40-len("Julian 2 Door Wardrobe"))])
            messagebox.showinfo("Product Status","Samsung led monitor is successfully added to the cart.")
        else:
            messagebox.showinfo("Product Status","Samsung led monitor is not added to the cart.")
    def AddF2():
        global Computerandtablets_list
        op=messagebox.askyesno("Purchase Confirmation","Are you sure that you want to add this item to the cart?")
        if op:
            Computerandtablets_list.append(["Frontech Led Monitor",17390,"17,390",Spaces(40-len("Zuari 3 Door Wardrobe"))])
            messagebox.showinfo("Product Status","Frontech Led Monitor is successfully added to the cart.")
        else:
            messagebox.showinfo("Product Status","Frontech Led Monitor is not added to the cart.")
    def AddF3():
        global Computerandtablets_list
        op=messagebox.askyesno("Purchase Confirmation","Are you sure that you want to add this item to the cart?")
        if op:
            Computerandtablets_list.append(["HP Pavillion",34999,"34,999",Spaces(40-len("TADesign 3 Door Wardrobe"))])
            messagebox.showinfo("Product Status","HP Pavillion is successfully added to the cart.")
        else:
            messagebox.showinfo("Product Status","HP Pavillion is not added to the cart.")
    def AddF4():
        global Computerandtablets_list
        op=messagebox.askyesno("Purchase Confirmation","Are you sure that you want to add this item to the cart?")
        if op:
            Computerandtablets_list.append(["Lenovo Ideapad Gaming",12290,"12,290",Spaces(40-len("Opus Queen Box Bed"))])
            messagebox.showinfo("Product Status","Lenovo Ideapad Gaming is successfully added to the cart.")
        else:
            messagebox.showinfo("Product Status","Lenovo Ideapad Gaming is not added to the cart.")
    def AddF5():
        global Computerandtablets_list
        op=messagebox.askyesno("Purchase Confirmation","Are you sure that you want to add this item to the cart?")
        if op:
            Computerandtablets_list.append(["Lenovo intel core i3",13640,"13,640",Spaces(40-len("Jasper King Box Bed"))])
            messagebox.showinfo("Product Status","Lenovo intel core i3 is successfully added to the cart.")
        else:
            messagebox.showinfo("Product Status","Lenovo intel core i3 is not added to the cart.")
    def AddF6():
        global Computerandtablets_list
        op=messagebox.askyesno("Purchase Confirmation","Are you sure that you want to add this item to the cart?")
        if op:
            Computerandtablets_list.append(["Samsung galaxy",6590,"6,590",Spaces(40-len("Zuari TV Unit"))])
            messagebox.showinfo("Product Status","Samsung galaxy is successfully added to the cart.")
        else:
            messagebox.showinfo("Product Status","Samsung galaxy is not added to the cart.")
    def AddF7():
        global Computerandtablets_list
        op=messagebox.askyesno("Purchase Confirmation","Are you sure that you want to add this item to the cart?")
        if op:
            Computerandtablets_list.append(["Redmi pad 4",14999,"14,999",Spaces(40-len("Forzza TV Unit"))])
            messagebox.showinfo("Product Status","Redmi pad 4 TV is successfully added to the cart.")
        else:
            messagebox.showinfo("Product Status","Redmi pad 4 TV is not added to the cart.")
    def AddF8():
        global Computerandtablets_list
        op=messagebox.askyesno("Purchase Confirmation","Are you sure that you want to add this item to the cart?")
        if op:
            Computerandtablets_list.append(["Xiaomi pad 5",24490,"24,490",Spaces(40-len("Kurlon Black Sofa Set"))])
            messagebox.showinfo("Product Status","Xiaomi pad 5 is successfully added to the cart.")
        else:
            messagebox.showinfo("Product Status","Xiaomi pad 5 is not added to the cart.")
    def AddF9():
        global Computerandtablets_list
        op=messagebox.askyesno("Purchase Confirmation","Are you sure that you want to add this item to the cart?")
        if op:
            Computerandtablets_list.append(["realme pad",36854,"36,854",Spaces(40-len("Suncrown Cream Sofa Set"))])
            messagebox.showinfo("Product Status","realme pad Fabric 6 Set is successfully added to the cart.")
        else:
            messagebox.showinfo("Product Status","realme pad Fabric 6 is not added to the cart.")
    def AddF10():
        global Computerandtablets_list
        op=messagebox.askyesno("Purchase Confirmation","Are you sure that you want to add this item to the cart?")
        if op:
            Computerandtablets_list.append(["Apple IPad",26999,"26,999",Spaces(40-len("Allie 6 Seater Dining Set"))])
            messagebox.showinfo("Product Status","Apple IPad 6 is successfully added to the cart.")
        else:
            messagebox.showinfo("Product Status","Apple IPad 6 is not added to the cart.")
    add_Computerandtablets1=Button(lf_Computerandtablets1,text="Add Item",bg="salmon",fg="white",font="times 9 bold",command=AddF1).place(x=68,y=245)
    add_Computerandtablets2=Button(lf_Computerandtablets2,text="Add Item",bg="salmon",fg="white",font="times 9 bold",command=AddF2).place(x=68,y=245)
    add_Computerandtablets3=Button(lf_Computerandtablets3,text="Add Item",bg="salmon",fg="white",font="times 9 bold",command=AddF3).place(x=68,y=245)
    add_Computerandtablets4=Button(lf_Computerandtablets4,text="Add Item",bg="salmon",fg="white",font="times 9 bold",command=AddF4).place(x=68,y=245)
    add_Computerandtablets5=Button(lf_Computerandtablets5,text="Add Item",bg="salmon",fg="white",font="times 9 bold",command=AddF5).place(x=68,y=245)
    add_Computerandtablets6=Button(lf_Computerandtablets6,text="Add Item",bg="salmon",fg="white",font="times 9 bold",command=AddF6).place(x=68,y=245)
    add_Computerandtablets7=Button(lf_Computerandtablets7,text="Add Item",bg="salmon",fg="white",font="times 9 bold",command=AddF7).place(x=68,y=245)
    add_Computerandtablets8=Button(lf_Computerandtablets8,text="Add Item",bg="salmon",fg="white",font="times 9 bold",command=AddF8).place(x=68,y=245)
    add_Computerandtablets9=Button(lf_Computerandtablets9,text="Add Item",bg="salmon",fg="white",font="times 9 bold",command=AddF9).place(x=68,y=245)
    add_Computerandtablets10=Button(lf_Computerandtablets10,text="Add Item",bg="salmon",fg="white",font="times 9 bold",command=AddF10).place(x=68,y=245)
def mobileCall():
    HideAllFrames()
    mobile_Label=Label(Products_frame,text="Mobile",font="times 15 bold",fg="lightsalmon",bg="white").grid(row=0,column=0,padx=20)
    lf_mobile1=LabelFrame(Products_frame,bd=2,relief="groove")
    lf_mobile1.place(x=5,y=35,width=200,height=280)
    lf_mobile2=LabelFrame(Products_frame,bd=2,relief="groove")
    lf_mobile2.place(x=210,y=35,width=200,height=280)
    lf_mobile3=LabelFrame(Products_frame,bd=2,relief="groove")
    lf_mobile3.place(x=415,y=35,width=200,height=280)
    lf_mobile4=LabelFrame(Products_frame,bd=2,relief="groove")
    lf_mobile4.place(x=620,y=35,width=200,height=280)
    lf_mobile5=LabelFrame(Products_frame,bd=2,relief="groove")
    lf_mobile5.place(x=825,y=35,width=200,height=280)
    lf_mobile6=LabelFrame(Products_frame,bd=2,relief="groove")
    lf_mobile6.place(x=5,y=310,width=200,height=280)
    lf_mobile7=LabelFrame(Products_frame,bd=2,relief="groove")
    lf_mobile7.place(x=210,y=310,width=200,height=280)
    lf_mobile8=LabelFrame(Products_frame,bd=2,relief="groove")
    lf_mobile8.place(x=415,y=310,width=200,height=280)
    lf_mobile9=LabelFrame(Products_frame,bd=2,relief="groove")
    lf_mobile9.place(x=620,y=310,width=200,height=280)
    lf_mobile10=LabelFrame(Products_frame,bd=2,relief="groove")
    lf_mobile10.place(x=825,y=310,width=200,height=280)
    label_mobile_1=Label(lf_mobile1,image=mobile1_image,bd=2,justify="center").grid(row=0,column=0)
    label_mobile_2=Label(lf_mobile2,image=mobile2_image,bd=2,justify="center").grid(row=0,column=0)
    label_mobile_3=Label(lf_mobile3,image=mobile3_image,bd=2,justify="center").grid(row=0,column=0,padx=7)
    label_mobile_4=Label(lf_mobile4,image=mobile4_image,bd=2,justify="center").grid(row=0,column=0)
    label_mobile_5=Label(lf_mobile5,image=mobile5_image,bd=2,justify="center").grid(row=0,column=0,padx=7)
    label_mobile_6=Label(lf_mobile6,image=mobile6_image,bd=2,justify="center").grid(row=0,column=0)
    label_mobile_7=Label(lf_mobile7,image=mobile7_image,bd=2,justify="center").grid(row=0,column=0,padx=8)
    label_mobile_8=Label(lf_mobile8,image=mobile8_image,bd=2,justify="center").grid(row=0,column=0)
    label_mobile_9=Label(lf_mobile9,image=mobile9_image,bd=2,justify="center").grid(row=0,column=0,padx=22)
    label_mobile_10=Label(lf_mobile10,image=mobile10_image,bd=2,justify="center").grid(row=0,column=0,padx=6)
    name_mobile1=Label(lf_mobile1,text="Vivo Y21",font="arial 9",justify="center").grid(row=1,column=0)
    name_mobile2=Label(lf_mobile2,text="OnePlus Nord",font="arial 9",justify="center").grid(row=1,column=0)
    name_mobile3=Label(lf_mobile3,text="RealMe C31",font="arial 9",justify="center").grid(row=1,column=0)
    name_mobile4=Label(lf_mobile4,text="Technospark 9",font="arial 9",justify="center").grid(row=1,column=0)
    name_mobile5=Label(lf_mobile5,text="Oppo K3",font="arial 9",justify="center").grid(row=1,column=0)
    name_mobile6=Label(lf_mobile6,text="Samsung Galaxy",font="arial 9",justify="center").grid(row=1,column=0,padx=12)
    name_mobile7=Label(lf_mobile7,text="Motorola E40",font="arial 9",justify="center").grid(row=1,column=0)
    name_mobile8=Label(lf_mobile8,text="Iphone 10",font="arial 9",justify="center").grid(row=1,column=0)
    name_mobile9=Label(lf_mobile9,text="Iphone 13",font="arial 9",justify="center").grid(row=1,column=0)
    name_mobile10=Label(lf_mobile10,text="Iphone 14",font="arial 9",justify="center").grid(row=1,column=0)
    price_mobile1=Label(lf_mobile1,text="Price: Rs.24,990",font="arial 9 bold").grid(row=2,column=0)
    price_mobile2=Label(lf_mobile2,text="Price: Rs.33,790",font="arial 9 bold").grid(row=2,column=0)
    price_mobile3=Label(lf_mobile3,text="Price: Rs.34,999",font="arial 9 bold").grid(row=3,column=0)
    price_mobile4=Label(lf_mobile4,text="Price: Rs.25,290",font="arial 9 bold").grid(row=2,column=0)
    price_mobile5=Label(lf_mobile5,text="Price: Rs.19,690",font="arial 9 bold").grid(row=3,column=0)
    price_mobile6=Label(lf_mobile6,text="Price: Rs.19,999",font="arial 9 bold").grid(row=2,column=0)
    price_mobile7=Label(lf_mobile7,text="Price: Rs.42,879",font="arial 9 bold").grid(row=2,column=0)
    price_mobile8=Label(lf_mobile8,text="Price: Rs.34,999",font="arial 9 bold").grid(row=3,column=0)
    price_mobile9=Label(lf_mobile9,text="Price: Rs.42,499",font="arial 9 bold").grid(row=2,column=0)
    price_mobile10=Label(lf_mobile10,text="Price: Rs.53,249",font="arial 9 bold").grid(row=3,column=0)
    def AddA1():
        global mobile_list
        op=messagebox.askyesno("Purchase Confirmation","Are you sure that you want to add this item to the cart?")
        if op:
            mobile_list.append(["Vivo Y21",24990,"24,990",Spaces(40-len("Whirlpool Top Load"))])
            messagebox.showinfo("Product Status","Vivo Y21 is successfully added to the cart.")
        else:
            messagebox.showinfo("Product Status","Vivo Y21 is not added to the cart.")
    def AddA2():
        global mobile_list
        op=messagebox.askyesno("Purchase Confirmation","Are you sure that you want to add this item to the cart?")
        if op:
            mobile_list.append(["OnePlus Nord",33790,"33,790",Spaces(40-len("IFB Front Load"))])
            messagebox.showinfo("Product Status","OnePlus Nord is successfully added to the cart.")
        else:
            messagebox.showinfo("Product Status","OnePlus Nord is not added to the cart.")
    def AddA3():
        global mobile_list
        op=messagebox.askyesno("Purchase Confirmation","Are you sure that you want to add this item to the cart?")
        if op:
            mobile_list.append(["RealMe C31",34999,"34,999",Spaces(40-len("Samsung Inverter AC"))])
            messagebox.showinfo("Product Status","RealMe C31 is successfully added to the cart.")
        else:
            messagebox.showinfo("Product Status","RealMe C31 is not added to the cart.")
    def AddA4():
        global mobile_list
        op=messagebox.askyesno("Purchase Confirmation","Are you sure that you want to add this item to the cart?")
        if op:
            mobile_list.append(["Technospark 9",25290,"25,290",Spaces(40-len("LG 260L Refrigerator"))])
            messagebox.showinfo("Product Status","Technospark 9 is successfully added to the cart.")
        else:
            messagebox.showinfo("Product Status","Technospark 9 is not added to the cart.")
    def AddA5():
        global mobile_list
        op=messagebox.askyesno("Purchase Confirmation","Are you sure that you want to add this item to the cart?")
        if op:
            mobile_list.append(["Oppo K3",19690,"19,690",Spaces(40-len("IFB Microwave Oven"))])
            messagebox.showinfo("Product Status","Oppo K3 is successfully added to the cart.")
        else:
            messagebox.showinfo("Product Status","Oppo K3 is not added to the cart.")
    def AddA6():
        global mobile_list
        op=messagebox.askyesno("Purchase Confirmation","Are you sure that you want to add this item to the cart?")
        if op:
            mobile_list.append(["Samsung Galaxy",19999,"19,999",Spaces(40-len("Bajaj Mixer Grinder"))])
            messagebox.showinfo("Product Status","Samsung Galaxy is successfully added to the cart.")
        else:
            messagebox.showinfo("Product Status","Samsung Galaxy is not added to the cart.")
    def AddA7():
        global mobile_list
        op=messagebox.askyesno("Purchase Confirmation","Are you sure that you want to add this item to the cart?")
        if op:
            mobile_list.append(["Motorola E40",42879,"42,879",Spaces(40-len("Balzano Electric Kettle"))])
            messagebox.showinfo("Product Status","Motorola E40 is successfully added to the cart.")
        else:
            messagebox.showinfo("Product Status","Motorola E40 is not added to the cart.")
    def AddA8():
        global mobile_list
        op=messagebox.askyesno("Purchase Confirmation","Are you sure that you want to add this item to the cart?")
        if op:
            mobile_list.append(["Iphone 10",34999,"34,999",Spaces(40-len("Elica Wall Mounted Chimney"))])
            messagebox.showinfo("Product Status","Iphone 10 is successfully added to the cart.")
        else:
            messagebox.showinfo("Product Status","Iphone 10 is not added to the cart.")
    def AddA9():
        global mobile_list
        op=messagebox.askyesno("Purchase Confirmation","Are you sure that you want to add this item to the cart?")
        if op:
            mobile_list.append(["Iphone 11",42499,"42,499",Spaces(40-len("Kent Ace Water Purifier"))])
            messagebox.showinfo("Product Status","Iphone 11 is successfully added to the cart.")
        else:
            messagebox.showinfo("Product Status","Iphone 11 is not added to the cart.")
    def AddA10():
        global mobile_list
        op=messagebox.askyesno("Purchase Confirmation","Are you sure that you want to add this item to the cart?")
        if op:
            mobile_list.append(["Iphone 13",53249,"53,249",Spaces(40-len("Eureka Dry Vacuum Cleaner"))])
            messagebox.showinfo("Product Status","Iphone 13 is successfully added to the cart.")
        else:
            messagebox.showinfo("Product Status","Iphone 13 is not added to the cart.")
    add_mobile1=Button(lf_mobile1,text="Add Item",bg="lightsalmon",fg="white",font="times 9 bold",command=AddA1).place(x=68,y=245)
    add_mobile2=Button(lf_mobile2,text="Add Item",bg="lightsalmon",fg="white",font="times 9 bold",command=AddA2).place(x=68,y=245)
    add_mobile3=Button(lf_mobile3,text="Add Item",bg="lightsalmon",fg="white",font="times 9 bold",command=AddA3).place(x=68,y=245)
    add_mobile4=Button(lf_mobile4,text="Add Item",bg="lightsalmon",fg="white",font="times 9 bold",command=AddA4).place(x=68,y=245)
    add_mobile5=Button(lf_mobile5,text="Add Item",bg="lightsalmon",fg="white",font="times 9 bold",command=AddA5).place(x=68,y=245)
    add_mobile6=Button(lf_mobile6,text="Add Item",bg="lightsalmon",fg="white",font="times 9 bold",command=AddA6).place(x=68,y=245)
    add_mobile7=Button(lf_mobile7,text="Add Item",bg="lightsalmon",fg="white",font="times 9 bold",command=AddA7).place(x=68,y=245)
    add_mobile8=Button(lf_mobile8,text="Add Item",bg="lightsalmon",fg="white",font="times 9 bold",command=AddA8).place(x=68,y=245)
    add_mobile9=Button(lf_mobile9,text="Add Item",bg="lightsalmon",fg="white",font="times 9 bold",command=AddA9).place(x=68,y=245)
    add_mobile10=Button(lf_mobile10,text="Add Item",bg="lightsalmon",fg="white",font="times 9 bold",command=AddA10).place(x=68,y=245)
HomeAppliances_button=Button(Button_frame,text="HomeAppliances",font="times 20 bold",width=17,bd=6,bg="orangered",fg="white",activebackground="coral",command=HomeAppliancesCall)
HomeAppliances_button.grid(row=0,column=0,padx=5,pady=5)
Televisions_button=Button(Button_frame,text="Televisions",font="times 20 bold",width=17,bd=6,bg="darkorange",fg="white",activebackground="coral",command=TelevisionsCall)
Televisions_button.grid(row=1,column=0,padx=5,pady=5)
Cameraandaccessories_button=Button(Button_frame,text="Camera and Accessories",font="times 20 bold",width=17,bd=6,bg="orange",fg="white",activebackground="coral",command=CameraandaccessoriesCall)
Cameraandaccessories_button.grid(row=2,column=0,padx=5,pady=5)
Computerandtablets_button=Button(Button_frame,text="Computer and Tablets",font="times 20 bold",width=17,bd=6,bg="salmon",fg="white",activebackground="coral",command=ComputerandtabletsCall)
Computerandtablets_button.grid(row=3,column=0,padx=5,pady=5)
mobile_button=Button(Button_frame,text="Mobile",font="times 20 bold",width=17,bd=6,bg="lightsalmon",fg="white",activebackground="coral",command=mobileCall)
mobile_button.grid(row=4,column=0,padx=5,pady=5)
Coupon_frame=LabelFrame(root,bd=2,relief="groove",text="MEGA SALE!!!",fg="red",font="arial 16 bold")
Coupon_frame.place(x=2,y=450,width=300,height=230)
Coupon_1=Label(Coupon_frame,text="Get 15% Off on your purchase(upto Rs.100000)",font="times 11",fg="white",bg="red")
Coupon_2=Label(Coupon_frame,text="Get 10% Off on your purchase(upto Rs.25000.0)",font="times 11",fg="white",bg="tomato")
Coupon_3=Label(Coupon_frame,text="Get 5% Off on your purchase(upto Rs.5000.00)",font="times 11",fg="white",bg="salmon")
Coupon_1.grid(row=0,column=0,padx=10,pady=17)
Coupon_2.grid(row=1,column=0,padx=10,pady=17)
Coupon_3.grid(row=2,column=0,padx=10,pady=17)
def Bill():
    op=messagebox.askyesno("Bill Generation Confirmation","Products cannot be added or removed during bill generation. Are you sure that you have finished shopping?")
    if op:
        Products_frame.destroy()
        Button_frame.destroy()
        Coupon_frame.destroy()
        bill_gen_button.destroy()
        HomeAppliances_price=0
        Televisions_price=0
        Cameraandaccessories_price=0
        Computerandtablets_price=0
        mobile_price=0
        for i in range(len(HomeAppliances_list)):
            HomeAppliances_price+=HomeAppliances_list[i][1]
        for i in range(len(Televisions_list)):
            Televisions_price+=Televisions_list[i][1]
        for i in range(len(Cameraandaccessories_list)):
            Cameraandaccessories_price+=Cameraandaccessories_list[i][1]
        for i in range(len(Computerandtablets_list)):
            Computerandtablets_price+=Computerandtablets_list[i][1]
        for i in range(len(mobile_list)):
            mobile_price+=mobile_list[i][1]
        total_price=HomeAppliances_price+Televisions_price+Cameraandaccessories_price+Computerandtablets_price+mobile_price
        discount=[0,0,0]
        if 0.15*total_price<100000:
            discount[0]=0.15*total_price
        else:
            discount[0]=100000
        if 0.1*total_price<25000:
            discount[1]=0.1*total_price
        else:
            discount[1]=25000
        if 0.05*total_price<5000:
            discount[2]=0.05*total_price
        else:
            discount[2]=5000
        max_discount=max(discount)
        if max_discount==discount[0]:
            suggest=Label(root,bd=1,text="Suggested : 15% Off upto Rs.100000",font="times 12",fg="red").place(x=545,y=480)
        elif max_discount==discount[1]:
            suggest=Label(root,bd=1,text="Suggested : 10% Off upto Rs.25000",font="times 12",fg="red").place(x=545,y=480)
        else:
            suggest=Label(root,bd=1,text="Suggested : 5% Off upto Rs.5000",font="times 12",fg="red").place(x=545,y=480)
        def GenBill(d,choice):
            bill_area=LabelFrame(root,bd=2,relief="groove")
            bill_area.place(x=305,y=80,width=750,height=600)
            bill_title=Label(bill_area,text="INVOICE",font="arial 15 bold",bd=4,relief="groove").pack(fill=X)
            scroll_y=Scrollbar(bill_area,orient=VERTICAL)
            bill_txt_area=Text(bill_area,yscrollcommand=scroll_y.set)
            scroll_y.pack(side=RIGHT,fill=Y)
            scroll_y.config(command=bill_txt_area.yview)
            bill_txt_area.pack(fill=BOTH,expand=1)
            bill_txt_area.insert(END,Spaces(40)+"ELECTROMA\n"+Spaces(90,'*')+"\n")
            if len(HomeAppliances_list)>0:
                bill_txt_area.insert(END,"HomeAppliances Product(s)\n\nProduct Name"+Spaces(28)+"Price"+Spaces(25)+"Price\n")
                for i in HomeAppliances_list:
                    bill_txt_area.insert(END,i[0]+i[3]+"Rs."+str(i[1])+Spaces(27-len(str(i[1])))+i[2]+"\n")
                bill_txt_area.insert(END,"\nTotal HomeAppliances Price : Rs."+str(HomeAppliances_price)+"\n"+Spaces(90,'*')+"\n")
            if len(Televisions_list)>0:
                bill_txt_area.insert(END,"Televisions Product(s)\n\nProduct Name"+Spaces(28)+"Price"+Spaces(25)+"Colour\n")
                for i in Televisions_list:
                    bill_txt_area.insert(END,i[0]+i[4]+"Rs."+i[2]+Spaces(27-len(i[2]))+i[3]+"\n")
                bill_txt_area.insert(END,"\nTotal Televisions Price : Rs."+str(Televisions_price)+"\n"+Spaces(90,'*')+"\n")
            if len(Cameraandaccessories_list)>0:
                bill_txt_area.insert(END,"Camera and accessories(s)\n\nProduct Name"+Spaces(28)+"Price\n")
                for i in Cameraandaccessories_list:
                    bill_txt_area.insert(END,i[0]+i[3]+"Rs."+i[2]+"\n")
                bill_txt_area.insert(END,"\nTotal Camera and accessories Price : Rs."+str(Cameraandaccessories_price)+"\n"+Spaces(90,'*')+"\n")
            if len(Computerandtablets_list)>0:
                bill_txt_area.insert(END,"Computerandtablets Product(s)\n\nProduct Name"+Spaces(28)+"Price\n")
                for i in Computerandtablets_list:
                    bill_txt_area.insert(END,i[0]+i[3]+"Rs."+i[2]+"\n")
                bill_txt_area.insert(END,"\nTotal Computerandtablets Price : Rs."+str(Computerandtablets_price)+"\n"+Spaces(90,'*')+"\n")
            if len(mobile_list)>0:
                bill_txt_area.insert(END,"mobile(s)\n\nProduct Name"+Spaces(28)+"Price\n")
                for i in mobile_list:
                    bill_txt_area.insert(END,i[0]+i[3]+"Rs."+i[2]+"\n")
                bill_txt_area.insert(END,"\nTotal mobile Price : Rs."+str(mobile_price)+"\n"+Spaces(90,'*'))
            bill_txt_area.insert(END,"\nTotal Price(before discount) = Rs."+str(total_price))
            if choice==1:
                bill_txt_area.insert(END,"\nCoupon Applied : 15% Off upto Rs.100000")
            elif choice==2:
                bill_txt_area.insert(END,"\nCoupon Applied : 10% Off upto Rs.25000")
            else:
                bill_txt_area.insert(END,"\nCoupon Applied : 5% Off upto Rs.5000")
            bill_txt_area.insert(END,"\nDiscount Offered : Rs."+str(d))
            bill_txt_area.insert(END,"\nTotal Price(after discount) = Rs."+str(total_price-d))
            def enable_button():
                save_button.config(state="normal")
            save_button=Button(root,text="Save Invoice",font="times 20 bold",bd=6,bg="salmon",width=10,fg="white",command=lambda:save_invoice(bill_txt_area.get("1.0",END)))
            save_button.place(x=1120,y=600)
            save_button.config(state="disabled")
            root.after(10000, enable_button)
            #save_button=Button(root,text="Save Invoice",font="times 20 bold",bd=6,bg="salmon",width=10,fg="white",command=lambda:save_invoice(bill_txt_area.get("1.0",END)))
            #save_button.place(x=1120,y=600)
            ordernow_button=Button(root,text="Order now",font="times 20 bold",bd=6,bg="salmon",width=10,fg="white",command=lambda:ordernow(bill_txt_area.get("1.0",END)))
            ordernow_button.place(x=1120,y=500)
        Coupon_frame_2=LabelFrame(root,bd=2,relief="groove",text="Apply a Coupon",fg="red",font="arial 16 bold").place(x=500,y=150,width=380,height=300)
        Coupon_apply1=Button(Coupon_frame_2,text="15% Off upto Rs.100000",font="times 19 bold",width=17,bd=6,bg="orange",fg="white",activebackground="coral",command=lambda:GenBill(discount[0],1))
        Coupon_apply1.place(x=540,y=190)
        Coupon_apply2=Button(Coupon_frame_2,text="10% Off upto Rs.25000",font="times 20 bold",width=17,bd=6,bg="orange",fg="white",activebackground="coral",command=lambda:GenBill(discount[1],2))
        Coupon_apply2.place(x=540,y=280)
        Coupon_apply3=Button(Coupon_frame_2,text="5% Off upto Rs.5000",font="times 20 bold",width=17,bd=6,bg="orange",fg="white",activebackground="coral",command=lambda:GenBill(discount[2],3))
        Coupon_apply3.place(x=540,y=370)
    else:
        messagebox.showinfo("Bill Generation Confirmation","You can continue shopping now.")
#bill_gen_button=Button(Heading,bd=4,text="Proceed to Checkout",font="times 17 bold",bg="red",fg="white",activebackground="coral",command=Bill)
bill_gen_button = Button(Heading, bd=4, text="Proceed to Checkout", font="times 17 bold", bg="red", fg="white", activebackground="coral", command=Bill)
bill_gen_button.grid(row=0, column=1, padx=120, pady=10)
bill_gen_button.grid(row=0,column=3)
root.mainloop()
