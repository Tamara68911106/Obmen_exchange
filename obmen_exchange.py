import requests
import json
from tkinter import*
from tkinter import messagebox as mb
from tkinter import ttk


def update_c_label(event):
    code = combobox.get()
    name = cur[code] #кур был списком, будет словарем. из него будеи=м брать по коду валюты соотвествующее значение.
    c_label.config(text=name)


def exchange():
    code = combobox.get()

    if code:
        try:
            response = requests.get('https://open.er-api.com/v6/latest/USD')
            response.raise_for_status()
            data = response.json() # раскладываем в виде питонского словаря
            if code in data['rates']:# проверяем существует ли данная валюта
                exchange_rate = data['rates'][code]
                c_name = cur[code] # в перемнную с-name из словаря - значение по ключу
                mb.showinfo("Курс обмена", f"Курс: {exchange_rate:.2f}{c_name} за 1 доллар")
            else:
                mb.showerror('Ошибка!', f"Валюта {code} не найдена")# обработка исключений
        except Exception as e:
            mb.showerror("Ошибка", f"Произошла ошибка: {e}.")
    else:
        mb.showwarning("Внимание!", "Ведите код валюты!")


cur = {  # используем словать, поэтому {
    'RUB': 'Российский рубль',
    'EUR': 'ЕВРО',
    'GBR': 'Британский фунт стерлингов',
    'JPY': 'Японская ИЕНА',
    'CNY': 'Китайский юань',
    'KZT': 'Казахский тенге',
    'UZS': 'Узбекский сум',
    'CHF': 'Швейцарский франк',
    'AED': 'Дирхам ОАЭ',
    'CAD': 'Канадский доллар',
}

window=Tk()
window.title('Курсы обмена валюты')
window.geometry("360x180")


Label(text="Выберите код валюты").pack(padx=10, pady=10)


combobox = ttk.Combobox(values=list(cur.keys()))
combobox.pack(padx=10, pady=10)
combobox.bind("<<ComboboxSelected>>", update_c_label)

# entry=Entry  выключаем поле ввода
# entry.pack(padx=10, pady=10)
c_label=ttk.Label()
c_label.pack(padx=10, pady=10)


Button(text="Получить курс обмена к доллару", command=exchange).pack(padx=10, pady=10)

window.mainloop()
