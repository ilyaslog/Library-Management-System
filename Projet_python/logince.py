import tkinter as tk
from tkinter import ttk, messagebox


# Function to check login credentials
def login():
    entered_login = login_entry.get()
    entered_password = password_entry.get()

    # Check if login and password are correct (replace this with your actual login logic)
    if entered_login == "user" and entered_password == "password":
        messagebox.showinfo("Login Successful", "Welcome, " + entered_login + "!")
    else:
        messagebox.showerror("Login Failed", "Invalid login or password")


# Creating the main window
root = tk.Tk()
root.title("Login")

# Creating labels and entries for login and password using ttk style
style = ttk.Style()
style.configure("TEntry", padding=(10, 5, 10, 5))

login_label = ttk.Label(root, text="Login:")
login_label.pack(pady=5)
login_entry = ttk.Entry(root)
login_entry.pack(pady=5)

password_label = ttk.Label(root, text="Password:")
password_label.pack(pady=5)
password_entry = ttk.Entry(root, show="*")  # Show '*' for password input
password_entry.pack(pady=5)

# Creating a login button
login_button = ttk.Button(root, text="Login", command=login)
login_button.pack(pady=10)

root.mainloop()
