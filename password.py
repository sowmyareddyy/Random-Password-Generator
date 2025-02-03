import random
import string
import tkinter as tk
from tkinter import messagebox

def generate_password():
    try:
        length = int(length_entry.get())
        if low_var.get():
            chars = string.ascii_lowercase
        elif medium_var.get():
            chars = string.ascii_letters + string.digits
        elif strong_var.get():
            chars = string.ascii_letters + string.digits + string.punctuation
        else:
            raise ValueError("Please select a password strength.")

        password = ''.join(random.choice(chars) for _ in range(length))
        password_entry.delete(0, tk.END)
        password_entry.insert(0, password)
    except ValueError as e:
        messagebox.showerror("Error", str(e))

def copy_to_clipboard():
    root.clipboard_clear()
    root.clipboard_append(password_entry.get())
    root.update()


root = tk.Tk()
root.title("Random Password Generator")
root.configure(bg="skyblue")


tk.Label(root, text="Random Password Generator", font=("Arial", 16, "bold"), bg="skyblue").grid(row=0, column=0, columnspan=2, pady=10)


tk.Label(root, text="Password:", font=("Arial", 10, "bold"), bg="skyblue").grid(row=1, column=0, padx=5, pady=5)
password_entry = tk.Entry(root, width=30)
password_entry.grid(row=1, column=1, padx=5, pady=5)

tk.Label(root, text="Length:", font=("Arial", 10, "bold"), bg="skyblue").grid(row=2, column=0, padx=5, pady=5)
length_entry = tk.Entry(root, width=10)
length_entry.grid(row=2, column=1, padx=5, pady=5)


tk.Label(root, text="Strength:", font=("Arial", 10, "bold"), bg="skyblue").grid(row=3, column=0, padx=5, pady=5)
low_var = tk.BooleanVar()
medium_var = tk.BooleanVar()
strong_var = tk.BooleanVar()

low_button = tk.Radiobutton(root, text="Low", variable=low_var, value=True, bg="skyblue", font=("Arial", 10))
low_button.grid(row=3, column=1, sticky="w")
medium_button = tk.Radiobutton(root, text="Medium", variable=medium_var, value=True, bg="skyblue", font=("Arial", 10))
medium_button.grid(row=4, column=1, sticky="w")
strong_button = tk.Radiobutton(root, text="Strong", variable=strong_var, value=True, bg="skyblue", font=("Arial", 10))
strong_button.grid(row=5, column=1, sticky="w")

generate_button = tk.Button(root, text="Generate", command=generate_password, font=("Arial", 10, "bold"))
generate_button.grid(row=6, column=0, padx=5, pady=10)
copy_button = tk.Button(root, text="Copy", command=copy_to_clipboard, font=("Arial", 10, "bold"))
copy_button.grid(row=6, column=1, padx=5, pady=10)

root.mainloop()
