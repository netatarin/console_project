import customtkinter as ctk
import logic

#виджеты для 1 окна
def show_window_1():
    global okno, zagolovok, opisanie, widget_button
    rows, columns = 3, 1
    for i in range(rows):
        okno.rowconfigure(index=i, weight=1)
    for i in range(columns):
        okno.columnconfigure(index=i, weight=1)
    zagolovok.grid(row=0, column=0, ipadx=4, ipady=4, sticky="news", padx=20, pady=20)
    opisanie.grid(row=1, column=0, ipadx=4, ipady=4, sticky="news", padx=20, pady=20)
    widget_button.grid(row=2, column=0, ipadx=4, ipady=4, sticky="news", padx=390, pady=120)

def forget_window_1():
    global zagolovok, opisanie, widget_button
    zagolovok.grid_forget()
    opisanie.grid_forget()
    widget_button.grid_forget()
    rows, columns = 3, 1
    for i in range(rows):
        okno.rowconfigure(index=i, weight=0)
    for i in range(columns):
        okno.columnconfigure(index=i, weight=0)
#--------------------------------------------------------------------------
def show_window_2():
    global okno, widget_combobox, widget_textbox, knopka
    row,columns=3,1
    for i in range(row):
        okno.rowconfigure(index=i,weight=1)
    for i in range(columns):
        okno.columnconfigure(index=i,weight=1)
    widget_combobox.grid(row=0,column=0, sticky="ew", padx=20, pady=20)
    widget_textbox.grid(row=1, column=0, ipadx=4, ipady=4, sticky="news", padx=20, pady=20)
    knopka.grid(row=2, column=0, ipadx=4, ipady=4, sticky="news", padx=420, pady=5)

def forget_window_2():
    global widget_combobox, widget_textbox, knopka
    widget_combobox.grid_forget()
    widget_textbox.grid_forget()
    knopka.grid_forget()
    rows, columns = 3, 1
    for i in range(rows):
        okno.rowconfigure(index=i, weight=0)
    for i in range(columns):
        okno.columnconfigure(index=i, weight=0)
#---------------------------------------------------------------------------------------

def show_window_3():
    global vobla, bem
    row, columns = 3, 1
    for i in range(row):
        okno.rowconfigure(index=i, weight=1)
    for i in range(columns):
        okno.columnconfigure(index=i, weight=1)
    vobla.grid(row=1, column=0, ipadx=4, ipady=4, sticky="news", padx=20, pady=20)
    bem.grid(row=2, column=0, ipadx=4, ipady=4, sticky="news", padx=420, pady=5)
def forget_window_3():
    global vobla, bem
    vobla.grid_forget()
    bem.grid_forget()
    rows, columns = 3, 1
    for i in range(rows):
        okno.rowconfigure(index=i, weight=0)
    for i in range(columns):
        okno.columnconfigure(index=i, weight=0)

def handler_widget_button():
    forget_window_1()
    show_window_2()
def handler_bem():
    forget_window_3()
    show_window_2()
def handler_knopka():
    ar = widget_textbox.get("1.0", "end")
    # widget_textbox.delete("1.0", "end")
    if widget_combobox.get() == "Азбука Морзе":
        logic.morz(ar)
    elif widget_combobox.get() == "Шифр Цезаря":
        logic.cesar(ar)
    else:
        logic.atbash(ar)
    forget_window_2()
    show_window_3()
#---------------------------------------------------------------
okno = ctk.CTk()  # создаём окно и привязываем его переменной okno
okno.title("Программа для шифрования текста")  # устанавливаем заголовок окна
okno.geometry("1000x500")  # устанавливаем размеры окна
my_font = ctk.CTkFont(family="Arial Black", size=22)  # задаём шрифт
iphone2=ctk.CTkFont(family="Arial Black", size=14)  # задаём шрифт
##################################################################################################
# виджеты для окна 1
zagolovok = ctk.CTkLabel(master=okno)
zagolovok.configure(text="Программа для шифровния текста", font=my_font)

# задаём цветовое оформление всего приложения
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("green")

opisanie = ctk.CTkLabel(master=okno)
opisanie.configure(text="Проект Мухаметзянова Эмиля, "
                        "эта программа работает только на русском языке", font=iphone2)

widget_button = ctk.CTkButton(master=okno)
widget_button.configure(text="Начать", font=my_font, command=handler_widget_button)
###########################################################################################################
# виджеты для окна 2
elems = ["Азбука Морзе", "Шифр Цезаря", "Шифр Атбаша"]  # список элементов
widget_combobox = ctk.CTkComboBox(master=okno)
widget_combobox.configure(font=iphone2, values=elems, state="readonly", justify="center")  # values=список элементов # state="readonly" - только для чтения
widget_combobox.set("Азбука Морзе")  # значение элемента по умолчанию

widget_textbox = ctk.CTkTextbox(master=okno)
widget_textbox.configure(font=my_font)

knopka=ctk.CTkButton(master=okno)
knopka.configure(text="Сгенерировать", font=iphone2, command=handler_knopka)
####################################################################################################
bem=ctk.CTkButton(master=okno)
bem.configure(text="Повотрить", font=iphone2, command=handler_bem)

vobla = ctk.CTkTextbox(master=okno)
vobla.configure(font=my_font, state="disabled")

show_window_1()
okno.mainloop()