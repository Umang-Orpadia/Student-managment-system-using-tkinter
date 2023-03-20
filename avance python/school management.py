from tkinter import *
import csv


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~login form~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

root=Tk()
root.title("school management system")
root.geometry("800x600")

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Labels~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

l1=Label(text="Username")
l1.grid(row=0,column=0,padx=10,pady=10)
l2=Label(text="Password")
l2.grid(row=1,column=0,padx=10,pady=10)

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Entry~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

username=Entry(root)
username.grid(row=0,column=1,padx=10,pady=10)
password=Entry(root,show="*")
password.grid(row=1,column=1,padx=10,pady=10)

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Verify login~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


def verify_details():
    if username.get() == "Umang" and password.get() == "12345":
        manage()
    else:
        print("Incorrect username or password")
    
def dis1():
    root3 = Tk()
    root3.geometry("600x750")
    root3.title("Displaying record")
    l1=Label(root3,text="Name   Roll no")
    l1.grid(row=0,column=0)

    listbox = Listbox(root3)
    listbox.grid(row=1, column=0, padx=10, pady=10)

    with open("saveit.csv", "r", newline="") as f:
        reader = csv.reader(f)
        for row in reader:
            listbox.insert(END, row)

    root3.mainloop()

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~`Management(Do not finger here)~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~`
def manage():
    root1=Tk()
    root1.geometry("700x700")
    root1.title("Entery page")
    l1=Label(root1,text='Student name').grid(row=0,column=0)
    sname=Entry(root1)
    sname.grid(row=0,column=1)
    l2=Label(root1,text='Student Rollno').grid(row=1,column=0)
    sroll=Entry(root1)
    sroll.grid(row=1,column=1)

    def record():
        with open("saveit.csv", "a", newline="") as f:
            writer = csv.writer(f)
            writer.writerow([sname.get(), sroll.get()])

    sname.delete(0, END)
    sroll.delete(0, END)
    btn=Button(root1,text="Submit",command=record).grid(row=2,column=1)
    btn=Button(root1,text="show record",command=dis1).grid(row=3,column=1)
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Buttons~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
b1=Button(text="Submit",command=verify_details)
b1.grid(row=5,column=0,padx=10,pady=10)



root.mainloop()

