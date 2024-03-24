import tkinter as tk


def on_key_press():
    text = entry1.get()
    label2.config(text=f"Nice to meet you, {text}!")

root = tk.Tk()
root.title('hello_python')

root.geometry('300x200')
#root.resizable(False, False)


label1 = tk.Label(root, text='What is your name?')
label1.pack()
entry1 = tk.Entry(root)
entry1.pack()

button1 = tk.Button(root, text='Press me', command=on_key_press)
button1.pack()

label2 = tk.Label(root, text='')
label2.pack()

root.mainloop()
