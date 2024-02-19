import tkinter as tk
from tkinter import messagebox
import webbrowser
import json

class ReverseConverterGUI:
    def __init__(self, master):
        self.master = master
        master.title("Конвертер из TraderPlus в Expansion")
        master.geometry("900x700")
        master.configure(bg="#333")

        text_split_ratio = 0.7

        self.text_frame = tk.Frame(master, bg="#fff")
        self.text_frame.place(relx=0, rely=0, relwidth=text_split_ratio, relheight=1)

        self.text_widget = tk.Text(self.text_frame, bg="white", fg="#000", insertbackground="black")
        self.text_widget.place(relx=0, rely=0, relwidth=1, relheight=1)

        # Create a scrollbar for the text widget
        scrollbar = tk.Scrollbar(self.text_frame, orient=tk.VERTICAL, command=self.text_widget.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.text_widget.config(yscrollcommand=scrollbar.set)

        self.button_frame = tk.Frame(master, bg="#222")
        self.button_frame.place(relx=text_split_ratio, rely=0, relwidth=1 - text_split_ratio, relheight=1)

        self.convert_button = tk.Button(self.button_frame, text="Конвертировать", bg="#222", fg="#fff",
                                        activebackground="#555",
                                        activeforeground="#fff", borderwidth=2, relief="groove",
                                        font=("Comic Sans MS", 14),
                                        command=self.reverse_convert)
        self.convert_button.place(relx=0.5, rely=0.05, relwidth=0.85, relheight=0.1, anchor="n")

    def reverse_convert(self):
        input_str = self.text_widget.get("1.0", tk.END)

        if not input_str.strip():
            messagebox.showerror(title="Ошибка", message="Поле ввода пусто")
            return

        try:
            data = json.loads(input_str)
        except json.JSONDecodeError:
            messagebox.showerror(title="Ошибка", message="Некорректный JSON")
            return

        category_name = data.get("CategoryName", "")
        products = data.get("Products", [])

        items = []

        for product in products:
            product_data = product.split(',')
            if len(product_data) != 6:
                messagebox.showerror(title="Ошибка", message="Некорректный формат продукта")
                return

            class_name, _, _, _, max_price, min_price = product_data

            if product_data[-2] == "-1":
                max_price = int(product_data[-1]) * 4  # Умножаем последнее значение на 4
            else:
                max_price = int(max_price)

            min_price = max_price  # Устанавливаем MinPriceThreshold равным MaxPriceThreshold
            sell_price_percent = round(int(product_data[-1]) / max_price * 100)  # Округляем SellPricePercent

            # Автоматическая коррекция значения SellPricePercent
            if sell_price_percent < -1:
                sell_price_percent = -1

            max_stock_threshold = 100
            min_stock_threshold = 10
            spawn_attachments = []
            variants = []

            item = {
                "ClassName": class_name,
                "MaxPriceThreshold": max_price,
                "MinPriceThreshold": min_price,
                "SellPricePercent": sell_price_percent,
                "MaxStockThreshold": max_stock_threshold,
                "MinStockThreshold": min_stock_threshold,
                "SpawnAttachments": spawn_attachments,
                "Variants": variants
            }

            items.append(item)

        output_data = {
            "m_Version": 12,
            "DisplayName": category_name,
            "Icon": "Deliver",
            "Color": "FBFCFEFF",
            "IsExchange": 0,
            "InitStockPercent": 75.0,
            "Items": items
        }

        output_str = json.dumps(output_data, indent=4, ensure_ascii=False)

        self.text_widget.delete("1.0", tk.END)
        self.text_widget.insert("1.0", output_str)

root = tk.Tk()
gui = ReverseConverterGUI(root)
root.mainloop()