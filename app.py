import tkinter as tk
from script import generate_password

app = tk.Tk()

HEIGHT = 500
WIDTH = 600


def print_password(length):
    try:
        password = generate_password(int(length))
        output_label["text"] = f"Your new password is:\n{password}"
    except:
        print("Invalid format")



def copy_to_clipboard():
    password = str(output_label["text"][23:])
    app.clipboard_clear()
    app.clipboard_append(password)





canvas = tk.Canvas(app, height=HEIGHT, width=WIDTH)
canvas.pack()

frame = tk.Frame(app, bg="#1C2C54")
frame.place(relx=0.0125, rely=0.0125,relwidth=0.975, relheight=0.975)

input_bar = tk.Frame(frame, bg="#0480FC")
input_bar.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.2)

output = tk.Frame(frame, bg="#0480FC")
output.place(relx=0.1, rely=0.4, relwidth=0.8, relheight=0.5)

output_label = tk.Label(output, font=("Verdana",13), justify="center")
output_label.place(relx=0.025, rely=0.05, relheight=0.75, relwidth=0.95)

button = tk.Button(input_bar, text="Create password",font=("Verdana",10), command=lambda: print_password(entry.get()))
button.place(relx=0.675, rely=0.2, relwidth=0.3, relheight=0.6)

label = tk.Label(input_bar, text="Input password's lenght (6-32 characters)",font=("Verdana",10),justify="center", bg="#B4BECC")
label.place(relx=0.025, rely=0.2, relwidth=0.6, relheight=0.3)

entry = tk.Entry(input_bar, bg="#F4F4F4",justify="center")
entry.place(relx=0.025, rely=0.5, relwidth=0.6, relheight=0.3)

copy_button = tk.Button(output, text="Copy password",font=("Verdana",10), command=copy_to_clipboard)
copy_button.place(relx=0.35, rely= 0.85, relwidth=0.3, relheight=0.1)

app.mainloop()


