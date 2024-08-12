'''

from getpass import getpass

username = input("enter your user name : ")
password = getpass("enter your password : ")
'''

import tkinter as tk
from tkinter import ttk
from pymongo import MongoClient

# MongoDB connection setup
client = MongoClient("mongodb://localhost:27017/")  # Change the URL if using a remote database
db = client['user_database']
collection = db['users']

def save_to_database(username, password):
    user_data = {"username": username, "password": password}
    collection.insert_one(user_data)
    print(f"Username: {username} and Password stored in MongoDB.")

def toggle_password():
    if password_entry.cget('show') == '':
        password_entry.config(show='*')
        toggle_button.config(text='Show Password')
    else:
        password_entry.config(show='')
        toggle_button.config(text='Hide Password')

def submit():
    username = username_entry.get()
    password = password_entry.get()
    save_to_database(username, password)

# Create the main window
root = tk.Tk()
root.title("Login")

# Username label and entry
username_label = ttk.Label(root, text="Username:")
username_label.grid(row=0, column=0, padx=10, pady=10)
username_entry = ttk.Entry(root, width=30)
username_entry.grid(row=0, column=1, padx=10, pady=10)

# Password label and entry
password_label = ttk.Label(root, text="Password:")
password_label.grid(row=1, column=0, padx=10, pady=10)
password_entry = ttk.Entry(root, width=30, show='*')
password_entry.grid(row=1, column=1, padx=10, pady=10)

# Show/Hide password button
toggle_button = ttk.Button(root, text="Show Password", command=toggle_password)
toggle_button.grid(row=1, column=2, padx=10, pady=10)

# Remember me radio buttons
remember_var = tk.StringVar()
remember_var.set("no")

remember_yes = ttk.Radiobutton(root, text="Remember Me", variable=remember_var, value="yes")
remember_yes.grid(row=2, column=0, padx=10, pady=10)

remember_no = ttk.Radiobutton(root, text="Don't Remember Me", variable=remember_var, value="no")
remember_no.grid(row=2, column=1, padx=10, pady=10)

# Submit button
submit_button = ttk.Button(root, text="Submit", command=submit)
submit_button.grid(row=3, column=1, pady=10)

# Add border to entries
style = ttk.Style()
style.configure("TEntry", borderwidth=2, relief="solid")

# Start the GUI loop
root.mainloop()

