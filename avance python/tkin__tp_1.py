import csv
from tkinter import*

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~title,geometry~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
root=Tk()
root.title("parking lot management")
root.geometry("800x600")
root.configure(background="powder blue")
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

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Verify login~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


def verify_details():
    if username.get() == "incharge" and password.get() == "12456":
        root.destroy()
        manage()
        
    else:
        print("Incorrect username or password")
    


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Record~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



def dis1():
    root3 = Tk()
    root3.geometry("600x750")
    root3.title("record display")
    l1=Label(root3,text= "NAME  NUMBER  TIMNG")
    l1.grid(row=0,column=0)

    listbox = Listbox(root3)
    listbox.grid(row=1, column=0, padx=10, pady=10)

    with open("saveit.csv", "r", newline="") as f:
        reader = csv.reader(f)
        for row in reader:
            listbox.insert(END, row)

    root3.mainloop()


def manage():
    root1=Tk()
    root1.geometry("700x700")
    root1.title("Enter details")
    l1=Label(root1,text='CAR NAME',font="lucida 20 bold")
    l1.grid(row=0,column=0)
    sname=Entry(root1,font="lucida 20 bold")
    sname.grid(row=0,column=1)
    l2=Label(root1,text='CAR NUMBER',font="lucida 20 bold")
    l2.grid(row=1,column=0)
    sroll=Entry(root1,font="lucida 20 bold")
    sroll.grid(row=1,column=1)
    l3=Label(root1,text='PARKING TIME',font="lucida 20 bold")
    l3.grid(row=2,column=0)
    stime=Entry(root1,font="lucida 20 bold")
    stime.grid(row=2,column=1)
    
    

    def record():
        with open("saveit.csv", "a", newline="") as f:
            writer = csv.writer(f)
            writer.writerow([sname.get(), sroll.get(),stime.get()])
    def destroyit():
        root1.destroy()
    sname.delete(0, END)
    sroll.delete(0, END)
    stime.delete(0,END)
    btn=Button(root1,text="Submit",command=record).grid(row=3,column=1)
    btn=Button(root1,text="show record",command=dis1).grid(row=4,column=1)
    Button(text="DELETE",command=destroyit).grid(row=5,column=1)

   
    
    root1.mainloop()

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Buttons~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
b1=Button(root,text="Login",command=verify_details,padx=100,font="lucida 20 bold",bg="powder blue",relief=SUNKEN,bd=10)
b1.grid(row=2,column=1,padx=10,pady=10)
root.mainloop()