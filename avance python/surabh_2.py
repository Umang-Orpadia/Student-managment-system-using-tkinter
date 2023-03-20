import tkinter as tk
import tkinter.ttk as ttk
from tkinter import messagebox
import datetime
from tabulate import tabulate
import random

order_ID  = random.randint(1000 , 9999)
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

        self.label_medication = tk.Label(master, text="Medication:")
        self.label_medication.grid(row=2, column=0)

        # Define the medication dictionary with name and value pairs
        self.medications = {'Aspirin': 10, 'Ibuprofen': 15, 'Paracetamol': 20}

        # Create a list to store the selected medications
        self.selected_medications = []

        # Create a Menubutton for the medications
        self.selected_medication = tk.StringVar()
        self.selected_medication.set("Select medication")
        self.medications_menu = tk.OptionMenu(master, self.selected_medication, *self.medications.keys())
        self.medications_menu.grid(row=2, column=1)

        self.label_amount = tk.Label(master, text="Amount:")
        self.label_amount.grid(row=3, column=0)
        self.entry_amount = tk.Entry(master)
        self.entry_amount.grid(row=3, column=1)

        self.button_add_medication = tk.Button(master, text="Add Medication", command=self.add_medication)
        self.button_add_medication.grid(row=2, column=2)

        self.button_save = tk.Button(master, text="Save", command=self.save_data)
        self.button_save.grid(row=4, column=1)

        # Create file if it does not exist
        with open("billing_data.txt", "a+") as f:
            f.seek(0)
            if len(f.read()) == 0:
                f.write("Customer Name,Date,Amount,Medications,Order ID\n")

    def add_medication(self):
        medication = self.selected_medication.get()
        if medication != "Select medication":
            self.selected_medications.append(medication)
            self.update_total_amount()

    def update_total_amount(self):
        total_amount = 0
        for medication in self.selected_medications:
            total_amount += self.medications[medication]
        self.label_amount.config(text="Total amount: $" + str(total_amount))

    def save_data(self):
        customer_name = self.entry_customer_name.get()
        date = self.entry_date.get()
        amount = self.entry_amount.get()
        medications = ", ".join(self.selected_medications)

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
            tk.messagebox.showerror("Error", "Please  enter amount")
            return
        
        try:
            float(amount)
        except ValueError:
            tk.messagebox.showerror("Error", "Invalid amount. Please enter a valid number")
            return

        #for making a table in the file.
        data = [[customer_name,date,amount,medications,order_ID]]
        headers = ["customer_name", "date", "amount","Medication","order_ID"]
        table = tabulate(data, headers=headers, tablefmt="grid")
        
        # Append data to file
        with open("billing_data.txt", "a") as f:
            f.write(table)
            f.write('\n')

        # Clear input fields
        self.entry_customer_name.delete(0, tk.END)
        self.entry_date.delete(0, tk.END)
        self.entry_date.insert(0, datetime.date.today().strftime("%m/%d/%Y"))
        self.entry_amount.delete(0, tk.END)
        

root = tk.Tk()
billing_system = BillingSystem(root)
root.mainloop()
