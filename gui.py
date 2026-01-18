import tkinter as tk # импортируем нашу библиотеку 

def calculate():#создаем функцию calculate для рассчетов
    example = entry.get() #Берем текст из поля ввода
    try:#констурция при которой мы выполняем часть кода 
        result = eval(example)  #можно сказать это сердце программы ведь eval помогает для решения примеров 
        label_res.config(text=f"Результат : {result}",fg="black", ) # метка с названием и выводом нашего результата а .config это настройка нашего label
    except Exception:# а это вторая часть когда срабатывает когда у наш происходит ошибка (ошибки разделяютя на виды со своими названиями)
        label_res.config(text="Ошибка!", fg ="red")# вывод в случаи ошибки с настройкой 
def clear():#функция очистик
    entry.delete(0, tk.END) #Стирает текст в поле ввода
    label_res.config(text="Тут будет ответ",fg = "black") #Сбрасывает надпись
def add_digit(digit):#вроде фунция для добавление через нажатие кнопки , цифру в конец
    # Берем то что есть уже в поле и добавлем цифру в конец
    current = entry.get()# берем текст из поля ввода
    entry.delete(0, tk.END)
    entry.insert(0, current + str(digit)) 


#Создание окна для себя 

root = tk.Tk() #создания окна
root.columnconfigure(0, weight=1) #все эти три команды нужны для расстежния и заполнения пронстранства
root.columnconfigure(1, weight=1)
root.columnconfigure(2, weight=1)
root.title("Мой калькулятор (-_-)")# название приложения
#Поле ввода

entry = tk.Entry(root, font=("Arial",18))# поле ввода задаем шрифт и размер шрифта
entry.grid(row=0,column=0,columnspan=3,pady=10)# pady - это отступ сверхву и снизу , grid это настройка наших кнопок row - ряд , column - колонна , columnspan - размах столбов
buttons = [
    '7', '8', '9',
    '4', '5', '6',
    '1', '2', '3', # создание кнопок в массиве 
    '0', '.', '+',  
    '-', '*', '/'
]
#цикл отрисовки кнопок
row_val = 1 
col_val = 0

for button_text in buttons:
    #Создает кнопку 
    #lambada позволяет передать аргумент в функцию calculate прямо из кнопки
    action = lambda x=button_text: add_digit(x)
    tk.Button(root, text=button_text, width=5 , height=2, command=action).grid(row=row_val,column=col_val,sticky = "nsew")
  
    
    col_val += 1
    if col_val > 2:
        col_val = 0
        row_val += 1


#Кнопка рассчитать

btn = tk.Button(root, text="=", command = calculate,bg="orange")
btn.grid(row=6,column=0,columnspan=2,sticky="nsew")

btn_clear = tk.Button(root, text="C", command=clear,bg="red")
btn_clear.grid(row=6,column=2,sticky="nsew")

#Надпись для вывода результата

label_res = tk.Label(root,text="Ответ", font=("Arial", 14),)
label_res.grid(row=7, column=0,columnspan=3,pady=20)

root.mainloop()