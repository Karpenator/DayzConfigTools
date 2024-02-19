import os
import json
import tkinter as tk
import tkinter.ttk as ttk
from tkinter import filedialog

def convert_params():
    ultima_path = ultima_path_entry.get()
    save_folder = save_folder_entry.get()

    if not os.path.exists(ultima_path):
        info_label.config(text='Ошибка: Укажите путь к папке файлов KR_BANKING', fg='red')
        return

    if not os.path.exists(save_folder):
        os.makedirs(save_folder)

    files_list = [f for f in os.listdir(ultima_path) if f.endswith('.json')]
    files_count = len(files_list)
    progress_bar.config(maximum=files_count, value=0)
    progress_label.config(text='{} из {}'.format(0, files_count))

    for index, file_name in enumerate(files_list):
        with open(os.path.join(ultima_path, file_name), 'r') as file:
            data = json.load(file)
            steam64_id = data['m_Steam64ID']
            player_name = data['m_PlayerName']
            money_amount = data['m_OwnedCurrency']
            new_data = {
                'Version': '2.5',
                'SteamID64': steam64_id,
                'Name': player_name,
                'MoneyAmount': money_amount,
                'MaxAmount': 100000000,
                'Licences': [],
                'Insurances': {}
            }
            new_file_name = f'Account_{steam64_id}.json'
            file_path = os.path.join(save_folder, new_file_name)

        with open(file_path, 'w') as file:
            json.dump(new_data, file, indent=4)

        progress_bar.config(value=index + 1)
        progress_label.config(text='{} из {}'.format(index + 1, files_count))

    info_label.config(text='Конвертация завершена', fg='green')



def select_ultima_path():
    path = filedialog.askdirectory()
    ultima_path_entry.delete(0, tk.END)
    ultima_path_entry.insert(0, path)


def select_save_folder():
    path = filedialog.askdirectory()
    save_folder_entry.delete(0, tk.END)
    save_folder_entry.insert(0, path)


root = tk.Tk()
root.title('Конвертер параметров из KR_BANKING в TraderPlus Banking')

# Создаем виджеты и располагаем их на форме
ultima_label = tk.Label(root, text='Путь к KR_BANKING')
ultima_label.grid(row=0, column=0)

ultima_path_entry = tk.Entry(root)
ultima_path_entry.grid(row=0, column=1)

ultima_button = tk.Button(root, text='Выбрать', command=select_ultima_path)
ultima_button.grid(row=0, column=2)

save_label = tk.Label(root, text='Куда сохранять')
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