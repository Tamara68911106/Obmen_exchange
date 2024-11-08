import requests
import json
from tkinter import*
from tkinter import messagebox as mb
from tkinter import ttk


def update_b_label(event):
    code = b_combobox.get()
    name = cur[code]
    b_label.config(text=name)


def update_t_label(event):
    code = t_combobox.get()
    name = cur[code] #кур был списком, будет словарем. из него будеи=м брать по коду валюты соотвествующее значение.
    t_label.config(text=name)


def exchange():
    t_code = t_combobox.get()
    b_code = b_combobox.get()


    if t_code and b_code: # сравниваем 2 условия, если t-code не пустой и b_code не пустой.
        # если пользователь выбрал 1-й, 2-й, то условие сработает, мы попадаем в try
        try:
            response = requests.get(f'https://open.er-api.com/v6/latest/{b_code}')
            response.raise_for_status()
            data = response.json() # раскладываем в виде питонского словаря
            if t_code in data['rates']:# проверяем существует ли данная валюта
                exchange_rate = data['rates'][t_code]
                t_name = cur[t_code] # в перемнную с-name из словаря - значение по ключу
                b_name = cur[b_code]
                mb.showinfo("Курс обмена", f"Курс: {exchange_rate:.2f}{t_name} за 1 {b_name}")
            else:
                mb.showerror('Ошибка!', f"Валюта {t_code} не найдена")# обработка исключений
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
    'AED': 'Дирхам ОАЭ',
    'CAD': 'Канадский доллар',
    'USD': 'Американский доллар'
}

window=Tk()
window.title('Курсы обмена валюты')
window.geometry("360x300")


Label(text="Базовая валюта").pack(padx=10, pady=10)
b_combobox = ttk.Combobox(values=list(cur.keys()))
b_combobox.pack(padx=10, pady=10)
b_combobox.bind("<<ComboboxSelected>>", update_b_label)
b_label=ttk.Label()
b_label.pack(padx=10, pady=10)



Label(text="Целевая валюта").pack(padx=10, pady=10)

t_combobox = ttk.Combobox(values=list(cur.keys())) # cur - словарь, keys - ключи
t_combobox.pack(padx=10, pady=10)
t_combobox.bind("<<ComboboxSelected>>", update_t_label)

# entry=Entry  выключаем поле ввода
# entry.pack(padx=10, pady=10)
t_label=ttk.Label()
t_label.pack(padx=10, pady=10)


Button(text="Получить курс обмена", command=exchange).pack(padx=10, pady=10)

window.mainloop()
