# Author: Abrielle Nyei
# Date: 2026-04-17
# Title: Show Info GUI Program

import tkinter as tk

def show_info():
    info_label.config(
        text="Name: John Doe\nAddress: 123 Maple Street\nSpringfield, USA"
    )

def main():
    # Create main window
    root = tk.Tk()
    root.title("Personal Info")
    root.geometry("400x250")

    # Label to display info
    global info_label
    info_label = tk.Label(root, text="", font=("Arial", 12), justify="center")
    info_label.pack(pady=20)

    # Show Info button
    show_button = tk.Button(root, text="Show Info", command=show_info)
    show_button.pack(pady=10)

    # Quit button
    quit_button = tk.Button(root, text="Quit", command=root.destroy)
    quit_button.pack(pady=10)

    # Run GUI loop
    root.mainloop()

if __name__ == "__main__":
    main()