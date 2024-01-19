import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

def main():
    # Main application window
    global encryption_frame, decryption_frame
    root = tk.Tk()
    root.resizable(False, False)
    root.title("Caesar Cipher")

    # Encryption frame
    encryption_frame = ttk.LabelFrame(root, text="Encryption", padding="10")

    ttk.Label(encryption_frame, text="Plaintext:").grid(column=0, row=0, sticky="w")
    entry_plaintext = ttk.Entry(encryption_frame, width=40)
    entry_plaintext.grid(column=1, row=0)

    ttk.Label(encryption_frame, text="Shifts (comma-separated):").grid(column=0, row=1, sticky="w")
    entry_shifts = ttk.Entry(encryption_frame, width=40)
    entry_shifts.grid(column=1, row=1)

    ttk.Label(encryption_frame, text="Ciphertext:").grid(column=0, row=2, sticky="w")
    entry_ciphertext = ttk.Entry(encryption_frame, width=40, state="readonly")
    entry_ciphertext.grid(column=1, row=2)

    encrypt_button = ttk.Button(encryption_frame, text="Encrypt",
                                command=lambda: encrypt_text(entry_plaintext, entry_shifts, entry_ciphertext))
    encrypt_button.grid(column=1, row=3)

    # Decryption frame
    decryption_frame = ttk.LabelFrame(root, text="Decryption", padding="10")

    ttk.Label(decryption_frame, text="Ciphertext:").grid(column=0, row=0, sticky="w")
    entry_decrypt_ciphertext = ttk.Entry(decryption_frame, width=40)
    entry_decrypt_ciphertext.grid(column=1, row=0)

    ttk.Label(decryption_frame, text="Shifts (comma-separated):").grid(column=0, row=1, sticky="w")
    entry_decrypt_shifts = ttk.Entry(decryption_frame, width=40)
    entry_decrypt_shifts.grid(column=1, row=1)

    ttk.Label(decryption_frame, text="Plaintext:").grid(column=0, row=2, sticky="w")
    entry_decrypt_plaintext = ttk.Entry(decryption_frame, width=40, state="readonly")
    entry_decrypt_plaintext.grid(column=1, row=2)

    decrypt_button = ttk.Button(decryption_frame, text="Decrypt",
                                command=lambda: decrypt_text(entry_decrypt_ciphertext, entry_decrypt_shifts,
                                                             entry_decrypt_plaintext))
    decrypt_button.grid(column=1, row=3)

    # Main window buttons to toggle frames
    encryption_button = ttk.Button(root, text="Encryption", command=toggle_encryption_frame)
    encryption_button.grid(row=1, column=0, padx=10, pady=10)

    decryption_button = ttk.Button(root, text="Decryption", command=toggle_decryption_frame)
    decryption_button.grid(row=1, column=1, padx=10, pady=10)

    # Start the application
    root.mainloop()

# Function to perform Caesar Cipher encryption/decryption
def caesar_cipher(text, shifts, decrypt=False):
    result = ""
    for i, char in enumerate(text):
        if not decrypt:
            shift = shifts[i % len(shifts)]
        else:
            shift = -shifts[i % len(shifts)]

        # Shift every character, not just alphabetic ones
        result += chr((ord(char) + shift - 32) % 95 + 32)
    return result

# Function to get the list of shift values from the input string
def get_shifts(shifts_str):
    try:
        shifts = list(map(int, shifts_str.split(',')))
        if not shifts:
            raise ValueError("Shift list cannot be empty.")
        return shifts
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid comma-separated list of integers for shifts.")
        return None

# Toggle the visibility of the encryption frame
def toggle_encryption_frame():
    if encryption_frame.winfo_ismapped():
        encryption_frame.grid_remove()
    else:
        encryption_frame.grid()
        decryption_frame.grid_remove()

# Toggle the visibility of the decryption frame
def toggle_decryption_frame():
    if decryption_frame.winfo_ismapped():
        decryption_frame.grid_remove()
    else:
        decryption_frame.grid()
        encryption_frame.grid_remove()

# Functions to encrypt and decrypt text, tied to the buttons in the frames
def encrypt_text(entry_plaintext, entry_shifts, entry_ciphertext):
    plaintext = entry_plaintext.get()
    shifts_str = entry_shifts.get()
    shifts = get_shifts(shifts_str)
    if shifts is not None:
        encrypted_text = caesar_cipher(plaintext, shifts)
        entry_ciphertext.config(state=tk.NORMAL)
        entry_ciphertext.delete(0, tk.END)
        entry_ciphertext.insert(0, encrypted_text)
        entry_ciphertext.config(state="readonly")

def decrypt_text(entry_decrypt_ciphertext, entry_decrypt_shifts, entry_decrypt_plaintext):
    ciphertext = entry_decrypt_ciphertext.get()
    shifts_str = entry_decrypt_shifts.get()
    shifts = get_shifts(shifts_str)
    if shifts is not None:
        decrypted_text = caesar_cipher(ciphertext, shifts, decrypt=True)
        entry_decrypt_plaintext.config(state=tk.NORMAL)
        entry_decrypt_plaintext.delete(0, tk.END)
        entry_decrypt_plaintext.insert(0, decrypted_text)
        entry_decrypt_plaintext.config(state="readonly")

if __name__ == "__main__":
    main()
