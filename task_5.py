class TestCase:
    def __init__(self, steps={}, result=None):
        self.steps = steps
        self.result = result

    # Добавляет шаг тест-кейса
    def set_step(self, step_number, step_text):
        self.steps[step_number] = step_text

    # Удаляем шаг по ключу
    def delete_step(self, step_number):
        self.steps.pop(step_number)

    # Устанавливаем ожидаемый результат
    def set_result(self, result):
        self.result = result

    # Вывод инфо о ТК
    def get_test_case(self):
        print("{\n    'Шаги': {")
        for step_number, step_description in self.steps.items():
            print(f"        {step_number}: '{step_description}',")
        print(f"    }},\n    'Ожидаемый результат': '{self.result}'\n}}")


test_case_1 = TestCase()
test_case_1.set_step(1, "Перейти на сайт")
test_case_1.set_step(3, "Перейти в раздел Товары")
test_case_1.delete_step(3)
test_case_1.set_step(2, "Перейти в раздел Товары")
test_case_1.set_step(3, "Нажать кнопку «В корзину» у первого товара")
test_case_1.set_result("Товар окажется в корзине")
test_case_1.get_test_case()

test_case_2 = TestCase()
test_case_2.set_step(1, "Перейти на сайт")
test_case_2.set_step(2, "Перейти в раздел Корзина")
test_case_2.set_step(3, 'Нажать кнопку "Удалить"')
test_case_2.set_result("Товар удален из корзины")
test_case_2.get_test_case()
