import tkinter as tk
from tkinter import filedialog, Text
import os

# helps creating GUI
# filedialog will help us pick the apps and text to desplay some text
# os imports apps


# all the attribute will be attached to the main.
main = tk.Tk()
apps = []

#in order to remove empty space whenever user does not pick an app to execute
if os.path.isfile('save.txt'):
    with open('save.txt', 'r') as f:
        tempApps = f.read()
        tempApps = tempApps.split(',')
        application = [x for x in tempApps if x.strip()]
mainHeight = main.winfo_height()
mainWidth = main.winfo_width()


def addApp():
    # inorder to delete previous apps
    for widget in frame.winfo_children():
        widget.destroy()

    filename = filedialog.askopenfilename(initialdir="/", title="Select File",
                                          filetypes=(("executables", "*.exe"), ("all files", "*.*")))
    apps.append(filename)
    print(filename)

    for app in apps:
        label = tk.label = tk.Label(frame, text=app, bg="Grey")
        label.pack()


def runApps():
    for app in apps:
        os.startfile(app)
    # creating a canvas and attaching it to main


canvas = tk.Canvas(main, height=500, width=500, bg="Yellow")
canvas.pack()

frame = tk.Frame(main, bg="white", height=mainHeight - 50, width=mainWidth - 50)
frame.place(relx=0.1, rely=0.1)
open_file = tk.Button(main, text="Open File", fg="Black", bg="Grey", command=addApp)
open_file.pack()

run = tk.Button(main, text="Run", fg="Black", bg="Grey", command=runApps)
run.pack()


for app in apps:
    label = tk.Label(frame, text = app)
    label.pack()
main.mainloop()

# inorder to save previous mem
with open('save.txt', 'w') as f:
    for app in apps:
        f.write(app + ',')
