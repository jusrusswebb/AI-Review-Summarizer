import tkinter as tk
import QuickSum as qs
from tkinter import messagebox
from tkinter import *
import re
import tkinter.font as font

 # if E1.get() != None and E1.get() is re.match(r"https?://(?:www\.)?amazon\..*/dp/.*", entry):
# else:
#     button.config(font=("Arial", 12,"bold"))

def reviews_summary(entry):
    if not entry:
        text_area.delete('1.0', tk.END)
        text_area.insert(tk.END, "Please enter a URL above")
        return

    elif not re.match(r"https?://(?:www\.)?amazon\..*/dp/.*", entry):
        text_area.delete('1.0', tk.END)
        text_area.insert(tk.END, "Invalid URL")
        return
    else:
      button.config(font=("Arial", 12,"bold"))

    # Get the URL entered by the user
    reviews = qs.scrape_amazon_reviews(qs.get_product_id(entry))
    final_prompt = qs.prompt.format(list=reviews)
    output = qs.llm(final_prompt)

    try:

        # Display the summary
        text_area.delete('1.0', tk.END)
        text_area.insert(tk.END, output)

    except Exception as e:
        messagebox.showerror('Error', str(e))

# Create the main window
window = tk.Tk()
window.title("Amazon Review Summary")

window.geometry("490x250")

# Create an entry field to enter the product page URL
L1 = tk.Label(window, text = "Input URL:")
L1.place(x = 30, y =15)

E1 = tk.Entry(window, bd = 5)
E1.place(x = 110, y = 10)

# Create a button to fetch and display the summary
button = tk.Button(window, text="Get Summary", command=lambda: reviews_summary(E1.get()))
button.place(x = 320, y = 11)


# Create a text area to display the summary
text_area = tk.Text(window, height=10, width=60, wrap=WORD, padx=5)
text_area.place(x = 20, y = 65)

# Start the Tkinter event loop
window.mainloop()
