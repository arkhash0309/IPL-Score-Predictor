import tkinter as tk

# Create a new window
window = tk.Tk()

# Set the window title
window.title("IPL Score Predictor")

# Set the window size
window.geometry("400x300")

# Create a label widget
label = tk.Label(window, text="Welcome to IPL Score Predictor!")
label.pack()

# Create a button widget
button = tk.Button(window, text="Predict", command=lambda: print("Button clicked!"))
button.pack()

# Run the main event loop
window.mainloop()