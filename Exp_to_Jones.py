import tkinter as tk
from tkinter import filedialog
import json
import webbrowser

def load_config():
    filename = filedialog.askopenfilename(filetypes=[("JSON Files", "*.json")])
    with open(filename, 'r') as file:
        config = json.load(file)
    left_text.delete("1.0", tk.END)
    left_text.insert(tk.END, json.dumps(config, indent=4))

def convert_config():
    config = json.loads(left_text.get("1.0", tk.END))
    converted_values = []
    for item in config["Items"]:
        converted_values.append(item["ClassName"])
    filename = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt")])
    with open(filename, 'w') as file:
        file.write("<Category> Escape From Tarkov\n")
        file.write('\n'.join(value + ", *, " + str(item["MaxPriceThreshold"]) + ", " + str(item["MinPriceThreshold"]) for item, value in zip(config["Items"], converted_values)))


root = tk.Tk()
root.title("DayZ Trader Config Converter")
root.configure(background="#1C1C1C")

root.config(bg="#1C1C1C")  # Установка темного фона

load_button = tk.Button(root, text="Load Config", command=load_config, font=("Comic Sans MS", 14))
load_button.grid(row=0, column=0)

convert_button = tk.Button(root, text="Convert", command=convert_config, font=("Comic Sans MS", 14))
convert_button.grid(row=0, column=1)


left_text = tk.Text(root)
left_text.grid(row=1, column=0, columnspan=4)

root.mainloop()