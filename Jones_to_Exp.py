import tkinter as tk
from tkinter import filedialog
import json
import webbrowser

def load_config():
    filename = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])
    if filename:
        with open(filename, 'r') as file:
            lines = file.readlines()
        #category = lines[0].strip()  Get the category from the first line
        items = "\n".join(line.strip() for line in lines[1:])
        formatted_items = []
        for line in items.split("\n"):
            parts = line.strip().split(",")
            class_name = parts[0].strip()
            values = [value.strip() for value in parts[1:]]
            max_price_threshold = values[1]
            if max_price_threshold != "*":
                max_price_threshold = int(max_price_threshold)
            min_price_threshold = int(values[2])
            formatted_items.append(f"{class_name}, {max_price_threshold}, {min_price_threshold}")
        formatted_text = f"\n".join(formatted_items)
        left_text.delete("1.0", tk.END)
        left_text.insert(tk.END, formatted_text)

def convert_config():
    config = {
        "m_Version": 12,
        "DisplayName": "Syndicate Guild",
        "Icon": "Deliver",
        "Color": "FBFCFEFF",
        "IsExchange": 0,
        "InitStockPercent": 75.0,
        "Items": []
    }

    lines = left_text.get("1.0", tk.END).splitlines()

    for line in lines[1:]:
        parts = line.strip().split(",")
        class_name = parts[0].strip()

        # Get the values after the class name
        values = [value.strip() for value in parts[1:]]

        # Assign the values to the corresponding variables
        max_price_threshold = values[0]
        if max_price_threshold != "*":
            max_price_threshold = int(max_price_threshold)

        min_price_threshold = int(values[1])

        item = {
            "ClassName": class_name,
            "MaxPriceThreshold": max_price_threshold,
            "MinPriceThreshold": min_price_threshold,
            "SellPricePercent": -1,
            "MaxStockThreshold": 99,
            "MinStockThreshold": 1,
            "SpawnAttachments": [],
            "Variants": []
        }

        config["Items"].append(item)

    formatted_text = json.dumps(config, indent=4, separators=(",", ": "))
    left_text.config(state="normal")  # Enable editing of the text widget
    left_text.delete("1.0", tk.END)
    left_text.insert(tk.END, formatted_text)

    # Save the JSON file
    file_path = filedialog.asksaveasfilename(defaultextension=".json", filetypes=[("JSON Files", "*.json")])
    if file_path:
        with open(file_path, "w") as file:
            file.write(formatted_text)



root = tk.Tk()
root.title("DayZ Trader Config Converter")
root.configure(background="#1C1C1C")

# Установка темного фона
root.config(bg="#1C1C1C")

# Создание кнопок
button_frame = tk.Frame(root, bg="#1C1C1C")
button_frame.pack()

load_button = tk.Button(button_frame, text="Load Config", command=load_config, font=("Comic Sans MS", 14))
load_button.pack(side=tk.LEFT, padx=10, pady=10)

convert_button = tk.Button(button_frame, text="Convert", command=convert_config, font=("Comic Sans MS", 14))
convert_button.pack(side=tk.LEFT, padx=10, pady=10)

# Создание текстового поля
left_text = tk.Text(root)
left_text.pack(fill=tk.BOTH, expand=True)

root.mainloop()