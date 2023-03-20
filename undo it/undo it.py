import csv
from tkinter import*
from tkinter import ttk





#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~title,geometry~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
root=Tk()
root.title("school management system")
root.geometry("800x600")
root.configure(background="powder blue")
#name=Label(text="Hello",font="arial 18 bold",bg="red",fg="white")
# name.grid(row=0,column=0,padx=10,pady=20)
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Labels~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


l1=Label(text="Username",font="lucida 20 bold",bg="powder blue")
l1.grid(row=0,column=0,padx=10,pady=10)
l2=Label(text="Password",font="lucida 20 bold",bg="powder blue")
l2.grid(row=1,column=0,padx=10,pady=10)

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Entery~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
username=Entry(root,font="lucida 20 bold",bg="powder blue",relief=SUNKEN,bd=10)
username.grid(row=0,column=1,padx=10,pady=10)
password=Entry(root,show="*",font="lucida 20 bold",bg="powder blue",relief=SUNKEN,bd=10)
password.grid(row=1,column=1,padx=10,pady=10)




#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Command and functions~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# def getdetails():
#     print(username.get())
#     print(password.get())

# user=username.get()
# passw=password.get()

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Verify login~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


def verify_details():
    if username.get() == "Umang" and password.get() == "12345":
        root.destroy()
        manage()
        
    else:
        print("Incorrect username or password")
    


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Record~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#sname=StringVar()

# def record():
#     f=open("saveit.txt","a")
#     f.write(username.get())
#     f.close()



#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Management (Do not finger here)~~~~~~~~~~~~~~~~~~~~~~~~~~
# def dis1():
#     root3=Tk()
#     root3.geometry("600x750")
#     root3.title("Displaying record")
#     listbox=Listbox(root3)
#     listbox.grid(row=0,column=0,padx=10,pady=10)
#     with open("saveit.txt","r")as f:
#         for line in f:
#             listbox.insert(END,line.split("-"))

#     root3.mainloop()

def dis1():
    root3 = Tk()
    root3.geometry("1100x950+5+5")
    root3.title("Displaying record")

    f1=Frame(root3,bd=10,relief=GROOVE)
    f1.place(x=0,y=0,height=100,width=800)

    f2=Frame(root3,bd=10,relief=GROOVE)
    f2.place(x=0,y=150,height=500,width=800)


#~~~~~~~~~~~~~~~name,roll no,contact no,dob,emailid

    # l1=Label(f1,text="Name",font="lucida 20 bold")
    # l1.grid(row=0,column=0)
    la1=Label(f1,text="displayes records are",font="lucida 30 bold")
    la1.pack(fill=BOTH)
    # l2=Label(f1,text="roll",font="lucida 20 bold")
    # l2.grid(row=0,column=1)

    # scrollx=ttk.Scrollbar(f2,orient=HORIZONTAL)
    # scrolly=ttk.Scrollbar(f2,orient=VERTICAL)
    # he1=ttk.Treeview(f2,columns=("l1","l2","l3","l4","l5"),xscrollcommand=scrolly.set,yscrollcommand=scrollx.set)


    # scrollx.pack(side=BOTTOM,fill=X)
    # scrolly.pack(side=RIGHT,fill=Y)

    # scrollx=ttk.Scrollbar(command=he1.xview)
    # scrolly=ttk.Scrollbar(command=he1.yview)

    # scrollx=ttk.Scrollbar(f2,orient=HORIZONTAL, command=he1.xview)
    # scrolly=ttk.Scrollbar(f2,orient=VERTICAL, command=he1.yview)
    # he1=ttk.Treeview(f2,columns=("l1","l2","l3","l4","l5"),xscrollcommand=scrollx.set,yscrollcommand=scrolly.set)
    
    # scrollx.pack(side=BOTTOM,fill=X)
    # scrolly.pack(side=RIGHT,fill=Y)

    # he1.heading("l1",text="Name")
    # he1.heading("l2",text="Rollno")
    # he1.heading("l3",text="D.O.B")
    # he1.heading("l4",text="Contact")
    # he1.heading("l5",text="Email")
    # he1["show"]="headings"

    # he1.pack(fill=BOTH,expand=1)
    # # he1.column("l1",width=100)
    # # he1.column("l2",width=100)
    # scrollx.config(command=he1.xview)
    # scrolly.config(command=he1.yview)

    he1 = ttk.Treeview(f2, columns=("l1", "l2", "l3", "l4", "l5"))
    he1.heading("l1", text="Name")
    he1.heading("l2", text="Rollno")
    he1.heading("l3", text="D.O.B")
    he1.heading("l4", text="Contact")
    he1.heading("l5", text="Email")
    he1["show"] = "headings"
    he1.pack(fill=BOTH, expand=1)

    scrollx = ttk.Scrollbar(f2, orient=HORIZONTAL, command=he1.xview)
    scrolly = ttk.Scrollbar(f2, orient=VERTICAL, command=he1.yview)
    scrollx.pack(side=BOTTOM, fill=X)
    scrolly.pack(side=RIGHT, fill=Y)
    he1.configure(xscrollcommand=scrollx.set, yscrollcommand=scrolly.set)

    with open("saveit.csv", "r") as f:
        reader=csv.reader(f)
        for i, row in enumerate(reader):
            if i == 0:
                continue  # skip header row
            he1.insert("", "end", text=i, values=row)


    # listbox = Listbox(f2,width=50,height=20)
    # listbox.grid(row=0, column=0)

    # with open("saveit.csv", "r", newline="") as f:
    #     reader = csv.reader(f)
    #     for row in reader:
    #         Listbox.insert(END, row)

    root3.mainloop()


def manage():
    root1=Tk()
    root1.geometry("1100x900+10+10")
    root1.title("Entery page")

    f1=Frame(root1,bd=10,relief=GROOVE)
    f1.place(x=0,y=0,width=800,height=400)

    f2=Frame(root1,bd=10,relief=GROOVE)
    f2.place(x=0,y=450,width=800,height=100)

    l1=Label(f1,text='Student name',font="lucida 20 bold")
    l1.grid(row=0,column=0)
    sname=Entry(f1,font="lucida 20 bold")
    sname.grid(row=0,column=1)

    l2=Label(f1,text='Student Rollno',font="lucida 20 bold")
    l2.grid(row=1,column=0)
    sroll=Entry(f1,font="lucida 20 bold")
    sroll.grid(row=1,column=1)

    l3=Label(f1,text='Date of Birth',font="lucida 20 bold")
    l3.grid(row=2,column=0)
    sdob=Entry(f1,font="lucida 20 bold")
    sdob.grid(row=2,column=1)

    l4=Label(f1,text='Contact no',font="lucida 20 bold")
    l4.grid(row=3,column=0)
    scontact=Entry(f1,font="lucida 20 bold")
    scontact.grid(row=3,column=1)

    l5=Label(f1,text='Email-id',font="lucida 20 bold")
    l5.grid(row=4,column=0)
    semail=Entry(f1,font="lucida 20 bold")
    semail.grid(row=4,column=1)
    
    # def record():
    #     f=open("saveit.txt","a")
    #     f.write(sname.get()+"-"+sroll.get()+"\n")
    #     #f.write(sroll.get()+"\n")
    #     f.close()
    def record():
        with open("saveit.csv", "a", newline="") as f:
            writer = csv.writer(f)
            writer.writerow([sname.get(), sroll.get(), sdob.get(), scontact.get(), semail.get()])
    def destroyit():
        root1.destroy()
    sname.delete(0, END)
    sroll.delete(0, END)
    btn1=Button(f2,text="Submit",command=record,font="lucida 20 bold",bg="light green",fg="red").grid(row=0,column=0,padx=5)
    btn2=Button(f2,text="show record",command=dis1,font="lucida 20 bold",bg="light green",fg="red").grid(row=0,column=1,padx=5)
    btn3=Button(f2,text="Close",command=destroyit,font="lucida 20 bold",bg="light green",fg="red").grid(row=0,column=2,padx=5)


    # def record():
    #     f=open("saveit.txt","a")
    #     f.write(username.get())
    #     f.close()
    
    root1.mainloop()


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Buttons~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
b1=Button(root,text="Login",command=verify_details,padx=100,font="lucida 20 bold",bg="powder blue",relief=SUNKEN,bd=10)
b1.grid(row=2,column=1,padx=10,pady=10)



root.mainloop()