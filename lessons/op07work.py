import tkinter as tk


def on_key_press():
    numbers = entry1.get().split()
    result = 0
    for number in numbers:
        result += float(number)
    label2.config(text=str(result))

root = tk.Tk()
root.title('hello_python')

root.geometry('300x200')
#root.resizable(False, False)


label1 = tk.Label(root, text='input numbers. whitespace is delimiter')
label1.pack()
entry1 = tk.Entry(root)
entry1.pack()

button1 = tk.Button(root, text='Press me', command=on_key_press)
button1.pack()

label2 = tk.Label(root, text='')
label2.pack()

root.mainloop()
