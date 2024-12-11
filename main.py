import tkinter as tk
from tkinter import messagebox
import hashlib

# Dictionary to store original and shortened URLs
url_mapping = {}

def shorten_url():
    original_url = url_input.get().strip()
    if not original_url:
        messagebox.showerror("Error", "Please enter a URL to shorten.")
        return
    
    # Generate a hash-based key
    hash_object = hashlib.md5(original_url.encode())
    short_key = hash_object.hexdigest()[:8]  # Use the first 8 characters of the hash
    
    # Create the shortened URL
    shortened = f"http://short.ly/{short_key}"
    url_mapping[shortened] = original_url  # Map shortened URL to original URL
    
    shortened_url.set(shortened)

def open_url():
    shortened = shortened_url.get().strip()
    if shortened in url_mapping:
        original_url = url_mapping[shortened]
        messagebox.showinfo("Original URL", f"Redirecting to: {original_url}")
        # Open the URL in the default browser
        import webbrowser
        webbrowser.open(original_url)
    else:
        messagebox.showerror("Error", "Invalid shortened URL. Cannot open.")

# Create the main application window
root = tk.Tk()
root.title("Custom URL Shortener")
root.geometry("500x250")
root.resizable(False, False)

# Define StringVars for user input and output
url_input = tk.StringVar()
shortened_url = tk.StringVar()

# Create and place widgets
tk.Label(root, text="Enter URL to Shorten:", font=("Arial", 12)).pack(pady=10)
tk.Entry(root, textvariable=url_input, width=60, font=("Arial", 10)).pack()

tk.Button(root, text="Shorten URL", font=("Arial", 12), command=shorten_url).pack(pady=10)

tk.Label(root, text="Shortened URL:", font=("Arial", 12)).pack(pady=5)
tk.Entry(root, textvariable=shortened_url, width=60, font=("Arial", 10), state="readonly").pack()

tk.Button(root, text="Open Shortened URL", font=("Arial", 12), command=open_url).pack(pady=10)

# Run the application
root.mainloop()
