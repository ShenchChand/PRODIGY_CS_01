import tkinter as tk
from tkinter import messagebox

def caesar_cipher(text, shift, mode):
    shift %= 26
    shift = -shift if mode == 'Decrypt' else shift
    return ''.join(
        chr((ord(c) - (65 if c.isupper() else 97) + shift) % 26 + (65 if c.isupper() else 97))
        if c.isalpha() else c for c in text
    )

def process_cipher():
    text, shift, mode = entry_text.get(), entry_shift.get(), selected_mode.get()
    if not text:
        return messagebox.showerror("Input Error", "Text cannot be empty!")
    try:
        shift = int(shift)
    except ValueError:
        return messagebox.showerror("Input Error", "Shift must be an integer!")
    entry_result.config(state='normal')
    entry_result.delete(0, tk.END)
    entry_result.insert(0, caesar_cipher(text, shift, mode))
    entry_result.config(state='readonly')

def clear_inputs():
    for entry in (entry_text, entry_shift, entry_result):
        entry.delete(0, tk.END)
    entry_result.config(state='readonly')

root = tk.Tk()
root.title("Caesar Cipher")
root.geometry("400x300")

# Create and arrange widgets
tk.Label(root, text="Enter Text:").pack()
entry_text = tk.Entry(root, width=50)
entry_text.pack()

tk.Label(root, text="Shift Value:").pack()
entry_shift = tk.Entry(root, width=10)
entry_shift.pack()

selected_mode = tk.StringVar(value="Encrypt")
tk.Radiobutton(root, text="Encrypt", variable=selected_mode, value="Encrypt").pack()
tk.Radiobutton(root, text="Decrypt", variable=selected_mode, value="Decrypt").pack()

tk.Label(root, text="Result:").pack()
entry_result = tk.Entry(root, width=50, state='readonly')
entry_result.pack()

tk.Button(root, text="Process", command=process_cipher).pack(pady=5)
tk.Button(root, text="Clear", command=clear_inputs).pack(pady=5)

root.mainloop()
