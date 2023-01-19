# Objective: Build the UI for the web scraper
import tkinter as tk
import webbrowser
import ScraperLogic

parseLogic = ScraperLogic.Parser()

class UIWindow:
    def __init__(self):
        self.window = tk.Tk() # Create the main window
        
        title_text = tk.Label(text="Cannonball Finder")
        title_text.pack() # Add title text to the UI window
        
        search_button = tk.Button(
            text="Search",
            width=10,
            height=3,
            command=self.search
        )
        search_button.pack() # Add search button to the UI window

    #Define a callback function
    def callback(self, url):
        webbrowser.open_new_tab(url)
    
    def search(self): # Event handler for the search button
        parseLogic.parse() # Parse for Cannonball pipes

        for result in parseLogic.results: # Dynamically create result Labels
            results_text = tk.Label(text= parseLogic.results[result], font=('Helveticabold', 15), fg="blue", cursor="hand2")
            results_text.pack()
            results_text.bind("<Button-1>", lambda e:
                self.callback(result))

uiWindow = UIWindow()

uiWindow.window.mainloop() # Keep the window up