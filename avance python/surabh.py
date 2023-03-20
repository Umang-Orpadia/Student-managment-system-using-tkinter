import tkinter as tk
from tkinter import messagebox
import tkinter.ttk as ttk
import datetime
from tabulate import tabulate

class BillingSystem:
    def __init__(self, master):
        self.master = master
        master.title("Billing System")

        # Create widgets
        self.label_customer_name = tk.Label(master, text="Customer Name:")
        self.label_customer_name.grid(row=0, column=0)
        self.entry_customer_name = tk.Entry(master)
        self.entry_customer_name.grid(row=0, column=1)

        self.label_date = tk.Label(master, text="Date:")
        self.label_date.grid(row=1, column=0)
        self.entry_date = tk.Entry(master)
        self.entry_date.insert(0, datetime.date.today().strftime("%m/%d/%Y"))
        self.entry_date.grid(row=1, column=1)

        self.label_amount = tk.Label(master, text="Amount:")
        self.label_amount.grid(row=2, column=0)
        self.entry_amount = tk.Entry(master)
        self.entry_amount.grid(row=2, column=1)

        self.label_medication = tk.Label(master, text="Medication:")
        self.label_medication.grid(row=3, column=0)
        self.selected_medication = tk.StringVar()
        medication_options = ["paracetamol", "folic acid"]
        self.medication_menu = ttk.Menubutton(master, textvariable=self.selected_medication, direction="below")
        self.medication_menu.grid(row=3, column=1)
        self.medication_menu.menu = tk.Menu(self.medication_menu, tearoff=0)
        for option in medication_options:
            self.medication_menu.menu.add_command(label=option, command=lambda value=option: self.selected_medication.set(value))
        self.medication_menu["menu"] = self.medication_menu.menu

        self.button_save = tk.Button(master, text="Save", command=self.save_data)
        self.button_save.grid(row=4, column=1)

        # Create file if it does not exist
        with open("billing_data.txt", "a+") as f:
            f.seek(0)
            if len(f.read()) == 0:
                f.write("Customer Name,Date,Amount,Medication\n")

    def save_data(self):
        customer_name = self.entry_customer_name.get()
        date = self.entry_date.get()
        amount = self.entry_amount.get()
        medication = self.selected_medication.get()

        # Error checks
        if len(customer_name) == 0:
            tk.messagebox.showerror("Error", "Please enter customer name")
            return
        
        try:
            datetime.datetime.strptime(date, "%m/%d/%Y")
        except ValueError:
            tk.messagebox.showerror("Error", "Incorrect date format. Please enter date in MM/DD/YYYY format")
            return
        
        if len(amount) == 0:
            tk.messagebox.showerror("Error", "Please enter amount")
            return
        
        try:
            float(amount)
        except ValueError:
            tk.messagebox.showerror("Error", "Invalid amount. Please enter a valid number")
            return

        #for making a table in the file.
        data = [[customer_name,date,amount,medication]]
        headers = ["customer_name", "date", "amount","Medication"]
        table = tabulate(data, headers=headers, tablefmt="grid")

        # Append data to file
        with open("billing_data.txt", "a") as f:
            f.write(table)

        # Clear input fields
        self.entry_customer_name.delete(0, tk.END)
        self.entry_date.delete(0, tk.END)
        self.entry_date.insert(0, datetime.date.today().strftime("%m/%d/%Y"))
        self.entry_amount.delete(0, tk.END)

root = tk.Tk()
billing_system = BillingSystem(root)
root.mainloop()
