from tkinter import *
import webbrowser
import os
import subprocess

def initialize_main_menu():
    global root, btn_discord, btn_donate, btn_banking, btn_trader_plus, btn_trader_creator, btn_c_converter, btn_exp_to_jones
    root = Tk()
    root.title("Инструменты конфигурации Dayz от Karpenator")
    root.geometry("600x400")  # Установить размер окна
    root.configure(bg="#1C1C1C")
    root.resizable(False, False)

    # Настройка шрифта и цвета переднего плана для кнопок
    btn_font = ("Comic Sans MS", 14)
    btn_fg = "black"  # Цвет переднего плана для белых кнопок
    btn_bg = "green"  # Цвет фона для зеленых кнопок

    bottom_frame = Frame(root, bg="#1C1C1C")
    bottom_frame.pack(side=BOTTOM, fill=X)

    # Создание кнопки "Ultima BANK в BANKING"
    btn_banking = Button(root, text="Ultima BANK в BANKING", command=run_banking_program, font=btn_font, fg=btn_fg, bg="Green")
    btn_banking.place(x=10, y=10)

    # Создание кнопки "Banking to TraderPlus"
    btn_trader_plus = Button(root, text="Banking to TraderPlus", command=run_trader_plus_program, font=btn_font, fg=btn_fg, bg="Green")
    btn_trader_plus.place(x=10, y=70)

    # Создание кнопки "Trader Config Creator"
    btn_trader_creator = Button(root, text="Trader Config Creator", command=run_trader_creator_program, font=btn_font, fg=btn_fg, bg="white")
    btn_trader_creator.place(x=10, y=130)
    
    # Создание кнопки "C to map converter"
    btn_c_converter = Button(root, text="C to map converter", command=run_c_converter_program, font=btn_font, fg=btn_fg, bg="Red")
    btn_c_converter.place(x=10, y=190)
    
    # Создание кнопки "Exp to Jones"
    btn_exp_to_jones = Button(root, text="Exp to Jones", command=run_exp_to_jones_program, font=btn_font, fg=btn_fg, bg="white")
    btn_exp_to_jones.place(x=460, y=10)

    # Создание кнопки "Exp to TraderPlus"
    btn_exp_to_jones = Button(root, text="Exp to TraderPlus", command=run_exp_to_TraderPlus_program, font=btn_font, fg=btn_fg, bg="white")
    btn_exp_to_jones.place(x=416, y=70)

    # Создание кнопки "Jones to Exp"
    btn_exp_to_jones = Button(root, text="Jones to Exp", command=run_Jones_to_Exp_program, font=btn_font, fg=btn_fg, bg="white")
    btn_exp_to_jones.place(x=460, y=130)

    # Создание кнопки "TraderPlus to Exp"
    btn_exp_to_jones = Button(root, text="TraderPlus to Exp", command=run_TraderPlus_to_Exp_program, font=btn_font, fg=btn_fg, bg="white")
    btn_exp_to_jones.place(x=416, y=190)
    
    # Создание кнопки "TraderPlus to Jones"
    btn_exp_to_jones = Button(root, text="TraderPlus to Jones", command=run_TraderPlus_to_Jones_program, font=btn_font, fg=btn_fg, bg="white")
    btn_exp_to_jones.place(x=396, y=250)
    
    # Создание кнопок Discord и Donate
    btn_discord = Button(bottom_frame, text="Дискорд", command=open_discord, font=btn_font, fg=btn_fg, bg=btn_bg)
    btn_discord.pack(side=LEFT, padx=10, pady=10, anchor=CENTER)

    btn_donate = Button(bottom_frame, text="Пожертвовать", command=open_donate, font=btn_font, fg=btn_fg, bg=btn_bg)
    btn_donate.pack(side=RIGHT, padx=10, pady=10, anchor=CENTER)

def open_discord():
    webbrowser.open_new("https://discord.gg/Mj7tFHe8Nz")

def open_donate():
    webbrowser.open_new("https://boosty.to/karpenator/donate")

def run_banking_program():
    subprocess.Popen(['python', 'banking.py'])

def run_trader_plus_program():
    subprocess.Popen(['python', 'banking_to_trader_plus.py'])

def run_trader_creator_program():
    subprocess.Popen(['python', 'Trader_Config_Creator.py'])

def run_c_converter_program():
    subprocess.Popen(['python', 'C_to_map_converter.py'])

def run_exp_to_jones_program():
    subprocess.Popen(['python', 'Exp_to_Jones.py'])

def run_exp_to_TraderPlus_program():
    subprocess.Popen(['python', 'Exp_to_TraderPlus.py'])

def run_Jones_to_Exp_program():
    subprocess.Popen(['python', 'Jones_to_Exp.py'])

def run_TraderPlus_to_Exp_program():
    subprocess.Popen(['python', 'TraderPlus_to_Exp.py'])

def run_TraderPlus_to_Jones_program():
    subprocess.Popen(['python', 'TraderPlus_to_Jones.py'])

initialize_main_menu()
root.mainloop()