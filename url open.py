import webbrowser
import tkinter as tk
from tkinter import messagebox
import time

# Function to open URLs
def open_urls():
    urls = text_box.get("1.0", tk.END).strip().split('\n')
    if not urls:
        messagebox.showerror("Error", "No URLs provided!")
        return
    
    for url in urls:
        url = url.strip()
        if url:
            if not url.startswith('http://') and not url.startswith('https://'):
                url = 'http://' + url
            try:
                webbrowser.open(url, new=2)  # Open in a new tab, if possible
                time.sleep(1)  # Add a 1-second delay between opening each URL
            except Exception as e:
                messagebox.showerror("Error", f"Failed to open URL: {url}\n{e}")

# Create the main window
root = tk.Tk()
root.title("Open URLs")

# Create a text box for URL input
text_box = tk.Text(root, height=10, width=100)
text_box.pack()

# Insert the default URLs
default_urls = """https://www.youtube.com/watch?v=Ge3LBCaqq_c&list=PL7pkSK1xbGD4sSDQ86Pyj-wp2wdEGZ8qE&index=1
https://www.youtube.com/watch?v=PVdu7-ej5-w&list=PL7pkSK1xbGD4sSDQ86Pyj-wp2wdEGZ8qE&index=5
https://www.youtube.com/watch?v=umZbAZxVGxI&list=PL7pkSK1xbGD4sSDQ86Pyj-wp2wdEGZ8qE&index=6
https://www.youtube.com/watch?v=fsODGI87Uok&list=PL7pkSK1xbGD4sSDQ86Pyj-wp2wdEGZ8qE&index=9
https://www.youtube.com/watch?v=JIUXWTs5ZB4&list=PL7pkSK1xbGD4sSDQ86Pyj-wp2wdEGZ8qE&index=14
https://www.youtube.com/watch?v=BQ1IWkhrKfk&list=PL7pkSK1xbGD4sSDQ86Pyj-wp2wdEGZ8qE&index=22"""
text_box.insert(tk.END, default_urls)

# Create an open button
open_button = tk.Button(root, text="Open URLs", command=open_urls)
open_button.pack()

# Run the GUI loop
root.mainloop()
