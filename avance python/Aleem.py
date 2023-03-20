from tkinter import *

class RailwayTicketBooking:
    def __init__(self, master):
        self.master = master
        master.title("Railway Ticket Booking")

        self.train_label = Label(master, text="Select Train:")
        self.train_label.grid(row=0, column=0)

        self.train_listbox = Listbox(master, height=3)
        self.train_listbox.grid(row=0, column=1)
        self.train_listbox.insert(END, "Shatabdi Express")
        self.train_listbox.insert(END, "Rajdhani Express")
        self.train_listbox.insert(END, "Duronto Express")

        self.from_label = Label(master, text="From:")
        self.from_label.grid(row=1, column=0)

        self.from_entry = Entry(master)
        self.from_entry.grid(row=1, column=1)

        self.to_label = Label(master, text="To:")
        self.to_label.grid(row=2, column=0)

        self.to_entry = Entry(master)
        self.to_entry.grid(row=2, column=1)

        self.class_label = Label(master, text="Class:")
        self.class_label.grid(row=3, column=0)

        self.class_var = StringVar()
        self.class_var.set("2AC")
        self.class_radiobutton1 = Radiobutton(master, text="2AC", variable=self.class_var, value="2AC")
        self.class_radiobutton1.grid(row=3, column=1)
        self.class_radiobutton2 = Radiobutton(master, text="3AC", variable=self.class_var, value="3AC")
        self.class_radiobutton2.grid(row=3, column=2)
        self.class_radiobutton3 = Radiobutton(master, text="Sleeper", variable=self.class_var, value="Sleeper")
        self.class_radiobutton3.grid(row=3, column=3)

        self.book_button = Button(master, text="Book", command=self.book_ticket)
        self.book_button.grid(row=4, column=1)

        self.quit_button = Button(master, text="Quit", command=master.quit)
        self.quit_button.grid(row=4, column=2)

    def book_ticket(self):
        train = self.train_listbox.get(self.train_listbox.curselection())
        frm = self.from_entry.get()
        to = self.to_entry.get()
        ticket_class = self.class_var.get()

        print(f"Train: {train}")
        print(f"From: {frm}")
        print(f"To: {to}")
        print(f"Class: {ticket_class}")
        print("Ticket booked successfully.")

root = Tk()
my_ticket_booking = RailwayTicketBooking(root)
root.mainloop()
