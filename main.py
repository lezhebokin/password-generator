from tkinter import Tk, ttk, IntVar, BooleanVar, messagebox, END
import secrets
import string


def block_input(event):
    if event.state & 0x0004 and event.keycode == 65:
        event.widget.event_generate("<<SelectAll>>")
        return "break"
    if event.state & 0x0004 and event.keycode == 67:
        event.widget.event_generate("<<Copy>>")
        return "break"
    return "break"


def character():
    char = []
    if uppercase.get():
        char.extend(string.ascii_uppercase)
    if lowercase.get():
        char.extend(string.ascii_lowercase)
    if digit.get():
        char.extend(string.digits)
    if symbol.get():
        char.extend(string.punctuation)
    return char


def change(*args):
    label["text"] = f"Длина: {length.get()}"


def regulator(delta):
    current = length.get()
    nvalue = (current + delta)
    if 4 <= nvalue <= 64:
        length.set(nvalue)
        change()


def generate():
    char = character()
    if not char:
        messagebox.showerror(title="Ошибка", message="Не выбраны данные")
        return

    password = []
    for _ in range(length.get()):
        password.append(secrets.choice(char))
    entry.delete(0, END)
    entry.insert(0, ''.join(password))


def copy():
    if not entry.get():
        messagebox.showerror(title="Ошибка", message="Нечего копировать")
    else:
        root.clipboard_clear()
        root.clipboard_append(entry.get())


root = Tk()
root.title("Password Generator")
root.geometry("600x120")
root.resizable(width=False, height=False)

ttk.Frame(relief="solid").place(x=5, y=5, width=590, height=55)

uppercase = BooleanVar(value=True)
lowercase = BooleanVar(value=True)
digit = BooleanVar(value=True)
symbol = BooleanVar(value=True)
ttk.Checkbutton(text="[A-Z] Прописные", variable=uppercase).place(x=10, y=10, width=120)
ttk.Checkbutton(text="[a-z] Строчные", variable=lowercase).place(x=10, y=35, width=120)
ttk.Checkbutton(text="[0-9] Цифры", variable=digit).place(x=135, y=10, width=120)
ttk.Checkbutton(text="[#$%] Cимволы", variable=symbol).place(x=135, y=35, width=120)

length = IntVar(value=24)
label = ttk.Label(text=f"Длина: {length.get()}")
label.place(x=260, y=10, width=60)
ttk.Button(text="<", command=lambda: regulator(-1), width=1).place(x=260, y=30)
ttk.Scale(from_=4, to=64, orient="horizontal", variable=length, command=change, length=301).place(x=275, y=30)
ttk.Button(text=">", command=lambda: regulator(1), width=1).place(x=574, y=30)

entry = ttk.Entry()
entry.bind("<Key>", block_input)
entry.place(x=5, y=65, width=590)

ttk.Button(text="ГЕНЕРИРОВАТЬ", command=generate).place(x=5, y=90, width=293)
ttk.Button(text="КОПИРОВАТЬ", command=copy).place(x=302, y=90, width=293)

root.mainloop()
