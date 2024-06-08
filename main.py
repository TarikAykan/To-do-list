import tkinter as tk
from tkinter import messagebox

tasks = []

def add_task():
    task = task_entry.get()
    if task:
        tasks.append({"task": task, "completed": False})
        update_task_list()
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Uyarı", "Lütfen bir görev girin.")

def update_task_list():
    task_listbox.delete(0, tk.END)
    for idx, task in enumerate(tasks):
        status = "Tamamlandı" if task["completed"] else "Tamamlanmadı"
        task_listbox.insert(tk.END, f"{idx + 1}. {task['task']} - {status}")

def complete_task():
    try:
        index = int(task_entry.get()) - 1
        if 0 <= index < len(tasks):
            tasks[index]["completed"] = True
            update_task_list()
            task_entry.delete(0, tk.END)
        else:
            messagebox.showerror("Hata", "Geçersiz görev numarası.")
    except ValueError:
        messagebox.showerror("Hata", "Lütfen geçerli bir sayı giriniz.")

def delete_task():
    try:
        index = int(task_entry.get()) - 1
        if 0 <= index < len(tasks):
            tasks.pop(index)
            update_task_list()
            task_entry.delete(0, tk.END)
        else:
            messagebox.showerror("Hata", "Geçersiz görev numarası.")
    except ValueError:
        messagebox.showerror("Hata", "Lütfen geçerli bir sayı giriniz.")

root = tk.Tk()
root.title("To-Do List Uygulaması")

task_entry = tk.Entry(root, width=50)
task_entry.pack(pady=10)

add_button = tk.Button(root, text="Görev Ekle", command=add_task)
add_button.pack(pady=5)

complete_button = tk.Button(root, text="Görevi Tamamla", command=complete_task)
complete_button.pack(pady=5)

delete_button = tk.Button(root, text="Görev Sil", command=delete_task)
delete_button.pack(pady=5)

task_listbox = tk.Listbox(root, width=50, height=10)
task_listbox.pack(pady=10)

root.mainloop()
