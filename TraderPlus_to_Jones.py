import tkinter as tk
from tkinter import filedialog
import webbrowser
import json

class ConverterGUI:
    def __init__(self, master):
        self.master = master
        master.title("Конвертер текста")
        master.geometry("800x600")
        master.configure(bg="#333")
        
        text_split_ratio = 0.7
        
        self.text_frame = tk.Frame(master, bg="#fff")
        self.text_frame.place(relx=0, rely=0, relwidth=text_split_ratio, relheight=1)

        self.text_widget = tk.Text(self.text_frame, bg="white", fg="#000", insertbackground="black")
        self.text_widget.place(relx=0, rely=0, relwidth=1, relheight=1)

        self.button_frame = tk.Frame(master, bg="#222")
        self.button_frame.place(relx=text_split_ratio, rely=0, relwidth=1-text_split_ratio, relheight=1)
        
        self.convert_button = tk.Button(self.button_frame, text="Конвертировать", bg="#222", fg="#fff", activebackground="#555", 
                                       activeforeground="#fff", borderwidth=2, relief="groove",
                                       font=("Comic Sans MS", 14), 
                                       command=self.convert)
        self.convert_button.place(relx=0.5, rely=0.05, relwidth=0.85, relheight=0.1, anchor="n")

    def convert(self):
        input_str = self.text_widget.get("1.0", tk.END)

        if not input_str.strip():
            tk.messagebox.showerror(title="Ошибка", message="Поле ввода пусто")
            return

        # Добавьте фигурные скобки, если они отсутствуют
        if not input_str.strip().startswith('{'):
            input_str = '{' + input_str
        if not input_str.strip().endswith('}'):
            input_str += '}'

        try:
            data = json.loads(input_str)
        except json.JSONDecodeError:
            tk.messagebox.showerror(title="Ошибка", message="Некорректный JSON")
            return

        trader_categories = data.get("TraderCategories", [])

        output_str = ""
        for category in trader_categories:
            output_str += f"<Category> {category['CategoryName']}\n"
            for product in category["Products"]:
                product_list = product.split(",")
                output_str += f"\t{product_list[0].strip()}, *, {product_list[-2].strip()}, {product_list[-1].strip()}\n"
        
        # Вставляем результат в текстовый виджет вместо удаления его содержимого
        self.text_widget.delete("1.0", tk.END)
        self.text_widget.insert("1.0", output_str)


root = tk.Tk()

gui = ConverterGUI(root)

root.mainloop()