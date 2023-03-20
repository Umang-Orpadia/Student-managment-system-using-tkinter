from tkinter import*
from tkinter import ttk
import csv
from tkinter import messagebox
import mysql.connector



#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~login form~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

root=Tk()
root.title("parking lot management")
root.geometry("1800x900")

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Labels~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
f1=Frame(root,bd=20,relief=RIDGE)
f1.place(x=0,y=0,width=400,height=300)

f2=Frame(root,bd=20,relief=RIDGE)
f2.place(x=440,y=0,width=400,height=300)

f3=Label(root,bd=15,relief=RIDGE)
f3.place(x=0,y=350,height=100,width=800)

f4=Frame(root,bd=20,relief=RIDGE)
f4.place(x=0,y=500,height=300,width=800)

text1=Text(f2,width=45,height=16)
text1.grid(row=0,column=0)

def manage():
    if L1=="" or L2=="":
        messagebox.showerror("Error","All field are required")
    else :
        conn=mysql.connector.connect(host="localhost",username="root",password="khushi@5885",database="Mydata")
        my_cursor=conn.cursor()
        my_cursor.execute("*input into details values(%s,%s)",(L1.get(),L2.get()))
        conn.commit()
        conn.close()

btn1=Button(f3,text="Submit",command=manage)
btn1.grid(row=0,column=0)



l1=Label(f1,text="Username")
l1.grid(row=0,column=0)
L1=StringVar()

e1=Entry(f1,textvariable=L1)
e1.grid(row=0,column=1)


l2=Label(f1,text="password")
l2.grid(row=1,column=0)
L2=StringVar()

e2=Entry(f1,textvariable=L2)
e2.grid(row=1,column=1)

scrollx=ttk.Scrollbar(f4,orient=HORIZONTAL)
scrolly=ttk.Scrollbar(f4,orient=VERTICAL)
he1=ttk.Treeview(f4,columns=("l1","l2"),xscrollcommand=scrolly.set,yscrollcommand=scrollx.set)


scrollx.pack(side=BOTTOM,fill=X)
scrolly.pack(side=RIGHT,fill=Y)

scrollx=ttk.Scrollbar(command=he1.xview)
scrolly=ttk.Scrollbar(command=he1.yview)

he1.heading("l1",text="username")
he1.heading("l2",text="password")
he1["show"]="headings"

he1.pack(fill=BOTH,expand=1)
he1.column("l1",width=100)
he1.column("l2",width=100)





# l1=Label(text="username")
# l1.grid(row=0,column=0,padx=10,pady=10)
# l2=Label(text="Password")
# l2.grid(row=1,column=0,padx=10,pady=10)

# #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Entry~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# username=Entry(root)
# username.grid(row=0,column=1,padx=10,pady=10)
# password=Entry(root,show="*")
# password.grid(row=1,column=1,padx=10,pady=10)

# text1=Text( )


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Verify login~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
 

# def verify_details():
#     if username.get() == "incharge" and password.get() == "12456":
#         manage()
#     else:
#         print("Incorrect username or password")
    
# def dis1():
#     root3 = Tk()
#     root3.geometry("900x900")
#     root3.title("enter car info")
#     l1=Label(root3,text="NAME   NUMBER   TIMING")
#     l1.grid(row=0,column=0)  

#     listbox = Listbox(root3)
#     listbox.grid(row=1, column=0, padx=10, pady=10)

#     with open("saveit.csv", "r", newline="") as f:
#         reader = csv.reader(f)
#         for row in reader:
#             listbox.insert(END, row)

#     root3.mainloop()


# def manage():
#     root1=Tk()
#     root1.geometry("700x700")
#     root1.title("Entry page")
#     l1=Label(root1,text='CAR NAME').grid(row=0,column=0)
#     sname=Entry(root1)
#     sname.grid(row=0,column=1)
#     l2=Label(root1,text='CAR NUMBER').grid(row=1,column=0)
#     sroll=Entry(root1)
#     sroll.grid(row=1,column=1)
#     l3=Label(root1,text='TIMING PARKED').grid(row=2,column=0)
#     stime=Entry(root1)
#     stime.grid(row=2,column=1)
    

#     def record():
#         with open("saveit.csv", "a", newline="") as f:
#             writer = csv.writer(f)
#             writer.writerow([sname.get(), sroll.get(),stime.get()])

#     sname.delete(0, END)
#     sroll.delete(0, END)
#     btn=Button(root1,text="Submit",command=record).grid(row=3,column=1)
#     btn=Button(root1,text="show record",command=dis1).grid(row=4,column=1)
# #~~~~~~~~~~~~~~~~~~~~~~~~~~~~Buttons~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# b1=Button(text="Submit",command=verify_details)
# b1.grid(row=6,column=0,padx=10,pady=10)



root.mainloop()
