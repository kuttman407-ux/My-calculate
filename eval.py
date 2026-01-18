while True:
    try:
        user_input=input("Введите ваш пример: ").strip().lower()
        if user_input == "выход":
            break
        result = eval(user_input)
        print(result)
    except Exception:
        print("Ошибка не корретный ввод примера")
    while True:
        choice = input("Хотите продолжить (да/нет): ").strip().lower()
        if choice == "нет":
            print("До скорого")
            exit()
        elif choice == "да":
            break
        else:
            print("Пожайлуста введите да или нет")