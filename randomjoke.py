import tkinter as tk
import pyjokes

def get_joke():
    joke = pyjokes.get_joke()
    joke_label.config(text=joke)

# Create the main window
root = tk.Tk()
root.title("Random Joke App")
root.geometry("400x200")

# Joke display label
joke_label = tk.Label(root, text="Click below for a joke!", wraplength=350, font=("Arial", 12))
joke_label.pack(pady=20)

# Button to get a joke
joke_button = tk.Button(root, text="Tell me a joke", command=get_joke, font=("Arial", 12))
joke_button.pack(pady=10)

# Run the app
root.mainloop()
