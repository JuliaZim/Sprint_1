types = {
    1: "Блокирующий",
    2: "Критический",
    3: "Значительный",
    4: "Незначительный",
    5: "Тривиальный",
}

tickets = {
    1: ["API_45", "API_76", "E2E_4"],
    2: ["UI_19", "API_65", "API_76", "E2E_45"],
    3: ["E2E_45", "API_45", "E2E_2"],
    4: ["E2E_9", "API_76"],
    5: ["E2E_2", "API_61"],
}


# Функция, которая удаляет ключи
def del_duplicate():
    # Список с уникальными тасками
    unic_lst = []
    # Перебираем словарь начиная с последнего ключа
    for key in reversed(list(tickets.keys())):
        # Создаем новый список без дубликатов
        new_value_list = []
        # Перебираем списки с тасками (значения словаря)
        for item in tickets[key]:
            # Проверка значения на уникальность
            if item not in unic_lst:
                # Если нет в списке уникальных значений, то доваляем в него, и добавляем новый список значений
                unic_lst.append(item)
                new_value_list.append(item)
        # Обновляем значение словаря новым списком
        tickets[key] = new_value_list


# Фунцкия замены ключа
def link_critical_with_task():
    for i in range(1, 6):
        # Удаляем значение по ключу и присваиваем его переменной
        value_lst = tickets.pop(i)
        # Создаем в словаре новую запись ключ-значение
        tickets[types.get(i)] = value_lst


# Вызываем функции
del_duplicate()
link_critical_with_task()

# Печатаем словарь для проверки
print(tickets)
