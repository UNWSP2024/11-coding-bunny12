# Author: Abrielle Nyei
# Date: 2026-04-17
# Title: Favorite Saying GUI Program

import tkinter as tk

def main():
    # Create main window
    root = tk.Tk()
    root.title("Favorite Saying")
    root.geometry("400x200")

    # Label with favorite saying
    message = tk.Label(
        root,
        text="“Success is not final, failure is not fatal: it is the courage to continue that counts.”",
        wraplength=350,
        justify="center",
        font=("Arial", 12)
    )
    message.pack(expand=True)

    # Run the GUI loop
    root.mainloop()

if __name__ == "__main__":
    main()