from logger import log_history

while True:
    while True:
        try:
            a = float(input("Введите ваше число: "))
            break
        except ValueError:
            print("Тут ошибка , нужно вводить только числа ")
    while True:
        c = input("Введите команду которую хотите совершить: ")
        if c  in ["+","-","*","/"]:
            break
        print("Ошибка такой операции не существует")
            
    while True:
        try:
            b = float(input("Введите ваше число: "))
            if c == "/" and b == 0:
                 print("Ошибка на ноль вводить нельзя! Введите другое число")
                 continue
            break
        except ValueError:
            print("Тут ошибка , нужно вводить только числа ")
        
    if c == "+":
        res = a + b
        print("Сумма чисел равна : ", res)
        log_history(f"{a} + {b} = {res}")
    elif c == "-":
        res = a - b
        print("Разность чисел равна: ", res)
        log_history(f"{a} - {b} = {res}")
    elif c == "/":
        res = a / b
        print("Деление числа ", a, " на число ", b, " равна", res)
        log_history(f"{a} / {b} = {res}")
    elif c == "*":
        res = a * b
        print("Умножение числа ", a, " на число ", b, " равна", res)
        log_history(f"{a} * {b} = {res}")
    else:
        print("Error")
    while True:
        choice = input("Хотите продолжить (да/нет): ").strip().lower()
        if choice == "нет":
            print("До скорого")
            exit()
        elif choice == "да":
            break
        else:
            print("Пожайлуста введите да или нет")