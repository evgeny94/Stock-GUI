import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
import pandas as pd

# Create the root window
root = tk.Tk()

# Function to open the file explorer when the "Browse" button is clicked
def open_file_explorer():
  # Open the file explorer
  file_path = filedialog.askopenfilename(title="Select an Excel file", filetypes=[("Excel files", "*.xlsx")])

  # Check if a file was selected
  if file_path:
    # Open the Excel file using pandas
    df = pd.read_excel(file_path)

    # Get the list of column names
    column_names = df.columns.tolist()

    # Create a dropdown menu with the column names
    tk.OptionMenu(root, tk.StringVar(root), *column_names).pack()

    # Show a success message
    messagebox.showinfo("Success", "Column names have been loaded successfully.")
  else:
    # Show an error message
    messagebox.showerror("Error", "Please select a valid Excel file.")

# Create a button to open the file explorer
tk.Button(root, text="Browse", command=open_file_explorer).pack()

# Run the main loop
root.mainloop()
