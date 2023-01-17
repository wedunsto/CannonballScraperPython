# Objective: Build the UI for the web scraper
import tkinter as tk

class UIWindow:
    def __init__(self):
        self.window = tk.Tk() # Create the main window
        
        title_text = tk.Label(text="Cannonball Finder")
        title_text.pack() # Add title text to the UI window
        
        self.results_text = tk.Label(text=" ")
        self.results_text.pack()
        
        search_button = tk.Button(
            text="Search",
            width=10,
            height=3,
            command=self.search
        )
        search_button.pack() # Add search button to the UI window
    
    def search(self):
        # Method stub
        self.results_text["text"] = "Found"