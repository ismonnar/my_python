from tkinter import *
import tkinter.scrolledtext as scroll
import datetime
import json
from tkinter import messagebox as mb


tasks = []


def click():
    try:
        t = datetime.datetime.strptime(time.get(), '%H %M')
        d = {'Задача': task.get(), 'Катеория': category.get(), 'Время': time.get()}
        to_json(d)
        tasks.append(d)
        task.delete(0, END)
        category.delete(0, END)
        time.delete(0, END)
        return tasks
    except ValueError:
        mistake = Tk()
        mistake.geometry('300x25')
        mistake.title('Ошибка')
        mistake.configure(bg="#EEEEEE")
        Label(mistake, text="Неверный формат задачи времени", bg="#EEEEEE").pack()
        mistake.mainloop()


def show():
    st.delete('1.0', END)
    for i in tasks:
        st.insert(INSERT, str(i)[1:-1]+'\n')


def to_json(data):
    with open("task_list.json", "w", encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False)

def exit1():
    answer = mb.askyesno(title='Внимание!', message='Вы точно хотите выйти из программы?')
    if answer == True:
        root.destroy()
    else:
        pass

root = Tk()
root.geometry('750x200')
root.title('Менеджер задач')
root.configure(bg="#EEEEEE")

Label(text="Задача:", height=1, width=15, bg="#EEEEEE").grid(row=1, column=0)
task = Entry(width=30, bg="#FFFFFF")
task.grid(row=1, column=1)

Label(text="Категория:", height=1, width=15, bg="#EEEEEE").grid(row=2, column=0)
category = Entry(width=30, bg="#FFFFFF")
category.grid(row=2, column=1)

Label(text="Время:", height=1, width=15, bg="#EEEEEE").grid(row=3, column=0)
time = Entry(width=30, bg="#FFFFFF")
time.grid(row=3, column=1)

Button(root, text="Добавить задачу", height=1, width=15, bg="#EEEEEE", command=click).grid(row=4, column=1)

Button(text="Список задач", height=1, width=15, bg="#EEEEEE", command=show).grid(row=5, column=1)

Button(root, text="Выход", height=1, width=15, fg='white', bg="#FF000F", command=exit1).grid(row=6, column=1)

st = scroll.ScrolledText(root, width=35, height=6)
st.grid(row=1, column=5, rowspan=4)

root.mainloop()
