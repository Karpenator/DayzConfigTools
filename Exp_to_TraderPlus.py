import tkinter as tk
from tkinter import messagebox
import webbrowser
import json


class ConverterGUI:
    def __init__(self, master):
        self.master = master
        master.title("Конвертер конфига из Exp в TraderPlus")
        master.geometry("800x600")
        master.configure(bg="#333")

        text_split_ratio = 0.7

        self.text_frame = tk.Frame(master, bg="#fff")
        self.text_frame.place(relx=0, rely=0, relwidth=text_split_ratio, relheight=1)

        self.text_widget = tk.Text(self.text_frame, bg="white", fg="#000", insertbackground="black")
        self.text_widget.place(relx=0, rely=0, relwidth=1, relheight=1)

        self.button_frame = tk.Frame(master, bg="#222")
        self.button_frame.place(relx=text_split_ratio, rely=0, relwidth=1 - text_split_ratio, relheight=1)        

        self.convert_button = tk.Button(self.button_frame, text="Конвертировать", bg="#222", fg="#fff",
                                        activebackground="#555",
                                        activeforeground="#fff", borderwidth=2, relief="groove",
                                        font=("Comic Sans MS", 14),
                                        command=self.convert)
        self.convert_button.place(relx=0.5, rely=0.05, relwidth=0.85, relheight=0.1, anchor="n")

    def convert(self):
        input_str = self.text_widget.get("1.0", tk.END)

        if not input_str.strip():
            messagebox.showerror(title="Ошибка", message="Поле ввода пусто")
            return

        try:
            data = json.loads(input_str)
        except json.JSONDecodeError:
            messagebox.showerror(title="Ошибка", message="Некорректный JSON")
            return

        display_name = data.get("DisplayName", "")
        items = data.get("Items", [])

        products = []

        for item in items:
            class_name = item["ClassName"]
            max_price = item["MaxPriceThreshold"]
            sell_price_percent = item["SellPricePercent"] * 0.01
            min_price = int(max_price * sell_price_percent)

            products.append(f"{class_name},1,-1,1,{max_price},{min_price}")

        output_data = {
            "CategoryName": display_name,
            "Products": products
        }

        output_str = json.dumps(output_data, indent=4, ensure_ascii=False)

        self.text_widget.delete("1.0", tk.END)
        self.text_widget.insert("1.0", output_str)


root = tk.Tk()

gui = ConverterGUI(root)

root.mainloop()
