from functools import partial
import tkinter as tk

def on_click(button_text):
    if button_text == "=":
        try:
            result = eval(entry.get())
            entry.delete(0, tk.END)
            entry.insert(tk.END, str(result))
        except Exception as e:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")
    elif button_text == "C":
        entry.delete(0, tk.END)
    elif button_text == "X":
        current_text = entry.get()
        new_text = current_text[:-1]  
        entry.delete(0, tk.END)    
        entry.insert(0, new_text)
        

    else:
        entry.insert(tk.END, button_text)


# Create the main application window
root = tk.Tk()
root.title("Simple Calculator")
root.configure(background='grey')

# Entry widget to display the result
entry = tk.Entry(root, width=21, font=("Arial", 20))
entry.grid(row=0, column=0, columnspan=4,sticky='ns',pady=10)

# Define the calculator buttons
buttons = [
    "X", "(", ")", "/",
    "7", "8", "9", "*",
    "4", "5", "6", "-",
    "1", "2", "3", "+",
    "C", "0", ".", "="
]

def dis():
    print('hello')
# Add buttons to the window
row, col = 1, 0

for button_text in buttons:
    if(button_text=='X'):
        clr='red'
    elif(button_text=='='):
        clr='green'
    else:
        clr='grey'
        
    cmd = partial(on_click, button_text)
    button = tk.Button(root, text=button_text, font=("Arial", 20),width=4,height=2,bg=clr,
                       command=cmd)
    button.grid(row=row, column=col)
    col += 1
    if col > 3:
        col = 0
        row += 1

# Start the main event loop
root.mainloop()
