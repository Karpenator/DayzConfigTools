import os
import json
import re
import tkinter as tk
import tkinter.ttk as ttk
from tkinter import filedialog

def convert_params():
    ultima_path = ultima_path_entry.get()
    save_folder = save_folder_entry.get()

    if not os.path.exists(ultima_path):
        info_label.config(text='Ошибка: Укажите путь к файлу с маппингом в формате .c', fg='red')
        return

    if not os.path.exists(save_folder):
        os.makedirs(save_folder)

    with open(ultima_path, 'r') as file:
        data = file.readlines()

    if len(data) <= 26:
        info_label.config(text='Ошибка: Менее чем 27 файлов в маппинге', fg='red')
        return

    files_count = len(data) - 26  # Count of files to be processed
    progress_bar.config(maximum=files_count, value=0)
    progress_label.config(text='{} из {}'.format(0, files_count))

    converted_lines = []

    for index, line in enumerate(data[26:]):  # Start from the 27th file
        match = re.match(r'SpawnObject\("(.*?)"\s*,\s*"(.*?)"\s*,\s*"(.*?)"\s*,\s*(.*?)\);', line)

        if match:
            object_name, position, rotation, _ = match.groups()
            formatted_line = f'SpawnerObject | {object_name} | {position} | {rotation} |'
            converted_lines.append(formatted_line)

        progress_bar.config(value=index + 1)
        progress_label.config(text='{} из {}'.format(index + 1, files_count))

    new_file_name = f'Converted_{os.path.basename(ultima_path)}'
    file_path = os.path.join(save_folder, new_file_name)

    with open(file_path, 'w') as file:
        file.write('\n'.join(converted_lines))

    info_label.config(text='Конвертация завершена', fg='green')
    print(f'Conversion completed. File saved at: {file_path}')
    print(f'Converted lines: {converted_lines}')


def select_ultima_path():
    file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.c")])
    ultima_path_entry.delete(0, tk.END)
    ultima_path_entry.insert(0, file_path)


def select_save_folder():
    path = filedialog.askdirectory()
    save_folder_entry.delete(0, tk.END)
    save_folder_entry.insert(0, path)


root = tk.Tk()
root.title('Конвертер параметров')

# Создаем виджеты и располагаем их на форме
ultima_label = tk.Label(root, text='Путь к маппинг файлу в формате .c')
ultima_label.grid(row=0, column=0)

ultima_path_entry = tk.Entry(root)
ultima_path_entry.grid(row=0, column=1)

ultima_button = tk.Button(root, text='Выбрать', command=select_ultima_path)
ultima_button.grid(row=0, column=2)

save_label = tk.Label(root, text='Куда сохранить')
save_label.grid(row=1, column=0)

save_folder_entry = tk.Entry(root)
save_folder_entry.grid(row=1, column=1)

save_button = tk.Button(root, text='Выбрать', command=select_save_folder)
save_button.grid(row=1, column=2)

convert_button = tk.Button(root, text='Конвертировать', command=convert_params)
convert_button.grid(row=2, column=1)

progress_bar = tk.ttk.Progressbar(root, orient='horizontal', length=200)
progress_bar.grid(row=3, column=1)

progress_label = tk.Label(root, text='', width=15)
progress_label.grid(row=3, column=2)

info_label = tk.Label(root, text='', width=30)
info_label.grid(row=4, column=1)

root.mainloop()