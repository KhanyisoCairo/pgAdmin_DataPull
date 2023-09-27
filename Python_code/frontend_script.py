import tkinter as tk
from tkinter import ttk
from datetime import datetime
import backend_script  # Import your backend script

# Create a Tkinter window
window = tk.Tk()
window.title("Data Retrieval")

# Function to retrieve and process data when the button is clicked


def retrieve_data():
    start_date = start_date_entry.get()
    end_date = end_date_entry.get()
    table_name = table_name_var.get()

    # Call the backend script to retrieve and process data
    backend_script.retrieve_and_process_data(start_date, end_date, table_name)


# Create and configure UI elements
start_date_label = ttk.Label(window, text="Start Date:")
start_date_label.pack()
start_date_entry = ttk.Entry(window)
start_date_entry.pack()

end_date_label = ttk.Label(window, text="End Date:")
end_date_label.pack()
end_date_entry = ttk.Entry(window)
end_date_entry.pack()

table_name_label = ttk.Label(window, text="Table Name:")
table_name_label.pack()
table_name_var = tk.StringVar()
table_name_entry = ttk.Entry(window, textvariable=table_name_var)
table_name_entry.pack()

retrieve_button = ttk.Button(
    window, text="Retrieve Data", command=retrieve_data)
retrieve_button.pack()

# Start the Tkinter main loop
window.mainloop()
