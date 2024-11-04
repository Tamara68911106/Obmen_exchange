import requests
import json
from tkinter import*
from tkinter import messagebox as mb

def exchenge():
    code = entry.get()

    if code:
        try:
            response = requests.get('https://open.er-api.com/v6/latest/USD')
            response.raise_for_status()
            data = response.json() # раскладываем в виде питонского словаря
            if code in data['rates']:# проверяем существует ли данная валюта
                exchange_rate = data['rates'][code]
                mb.showinfo("Курс обмена", f"Курс: {exchange-rate}{code}"f" за 1 доллар")
            else:
                mb.showerroк('Ошибка!', f"Валюта {code} не найдена")# обработка исключений
        except Exception as e:
            mb.showerror("Ошибка", f"Произошла ошибка: {e}.")
    else:
        mb.showwarning("Внимание!", "Ведите код валюты!")

window=Tk()
window.title('КУрсы обмена валюты')
window.geometry("360x180")

Label(text="Введите код валюты").pack(padx=10, pady=10)


entry=Entry()
entry.pack(padx=10, pady=10)

Button(text="Получить курс обмена к доллару", command=exchange).pack(padx=10, pady=10)

window.mainloop()
