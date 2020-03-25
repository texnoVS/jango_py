# Создать список (супермаркет), состоящий из словарей (товары). Словари должны содержать как минимум 5 полей
# (например, номер, наименование, отдел продажи, ...). В список добавить хотя бы 10 словарей.
# Конструкция вида:
# market = [{"id":123456, "product":"coca-cola 0.5", "department": "drinks", ...} , {...}, {...}, ...].
# Реализовать функции:
# – вывода информации о всех товарах;
# – вывода информации о товаре по введенному с клавиатуры номеру;
# – вывода количества товаров, продающихся в определнном отделе;
# – обновлении всей информации о товаре по введенному номеру;
# – удалении товара по номеру.
# Провести тестирование функций.


# Импорт встроенной библиотеки для работы с датами
import datetime


# Объект продукта
class Product:
    # Конструтор объекта Product
    def __init__(self, product_id, name, department, price, date_of_manufacture, shelf_life):
        self.product_id = product_id
        self.name = name
        self.department = department
        self.price = price
        self.date_of_manufacture = date_of_manufacture
        self.shelf_life = shelf_life

    def get_product_id(self):
        return self.product_id

    def get_name(self):
        return self.name

    def set_name(self, name):
        if len(name) > 50:
            return "Название продукта не должно быть длинее 50 символов"
        self.name = name

    def get_department(self):
        return self.department

    def set_department(self, department):
        if len(department) > 50:
            return "Название категории не должно быть длинее 50 символов"
        self.department = department

    def get_price(self):
        return self.price

    def set_price(self, price):
        try:
            self.price = int(price)
        except ValueError:
            return "Вам нужно указать НОМЕР"

    def get_date_of_manufacture(self):
        return self.date_of_manufacture

    def set_date_of_manufacture(self, date_of_manufacture):
        # .split разбивает строчку на массив строк
        # "-" это сепаратор, то есть признак, по которому разбивается строка
        temp = date_of_manufacture.split("-")
        if len(temp) < 3:
            return "Вам необходимо указать дату в формате: ГОД-МЕСЯЦ-ДЕНЬ"
        try:
            # .date(year, month, day) - это метод для создания объекты datetime
            self.date_of_manufacture = datetime.date(int(temp[0]), int(temp[1]), int(temp[2]))
        except ValueError:
            return "Вам необходимо указать дату в формате: ГОД-МЕСЯЦ-ДЕНЬ"

    def get_shelf_life(self):
        return self.shelf_life

    def set_shelf_life(self, shelf_life):
        try:
            self.shelf_life = int(shelf_life)
        except ValueError:
            return "Вам нужно указать срок хранения в виде цифры"


# Создаем базу данных нашего магазина
market = []
# Добавляем продукты в бд
market.append(Product(115, "Coca-cola", "напитки", 150, datetime.date(2020, 1, 5), 180))
market.append(Product(166, "Сникерс", "сладости", 150, datetime.date(2020, 1, 5), 210))
market.append(Product(1122, "Kinder", "сладости", 150, datetime.date(2020, 1, 5), 365))
market.append(Product(1155, "Греча", "крупы", 150, datetime.date(2020, 1, 5), 730))
market.append(Product(765, "Туалетная бумага Zeva Deluxe", "товары для дома", 150, datetime.date(2020, 1, 5), 730))
market.append(Product(992, "Молоко Веселый молочник", "молочные продукты", 150, datetime.date(2020, 1, 5), 5))
market.append(Product(748, "Хлеб jango", "мучные изделия", 150, datetime.date(2020, 1, 5), 14))
market.append(Product(936, "Йогрут Тема", "молочные продукты", 150, datetime.date(2020, 1, 5), 7))
market.append(Product(550, "Огурцы", "овощи", 150, datetime.date(2020, 1, 5), 7))
market.append(Product(277, "Помидор", "овощи", 150, datetime.date(2020, 1, 5), 14))
market.append(Product(1333, "Картошка", "овощи", 150, datetime.date(2020, 1, 5), 60))


def show_product(product):
    print("--------")
    print("Id: " + str(product.get_product_id()))
    print("Название: " + str(product.get_name()))
    print("Категория товара: " + str(product.get_department()))
    print("Цена: " + str(product.get_price()))
    print("Дата изготовления: " + str(product.get_date_of_manufacture()))
    print("Срок годности (в сутках): " + str(product.get_shelf_life()))


def show_products():
    for product in market:
        show_product(product)
    print("\n")


def show_product_by_id():
    print("Введите id продукта:")
    # Блок try. В нем мы проверяем, происходит ли в вызывемых функциях, внутри его блока ошибки
    # Тут у нас дурачек пользователь может ввести буквы вместо цифр,
    # из за чего функция int выкинет ошибку (тип ошибки будет ValueError)
    try:
        product_id = int(input())
    # Тут мы обрабатываем наш ValueError
    except ValueError:
        return print("Вам нужно указать НОМЕР(id) продукта!\n")
    searching_elm_status = False
    # searching_elm_status покажет, нашли ли мы элемент, который искали в бд
    for product in market:
        # Если id текущего элемента равен id, переданный пользователем с клавиатуры,
        # Залетаем в наш if
        if product.get_product_id() == product_id:
            # Нужно указать, что мы нашли искомый элемент, поэтому temp равно True
            searching_elm_status = True
            show_product(product)
            print("\n")
            break
    # Если элемент не был найдем, то жизнь боль как бы да
    if searching_elm_status == False:
        print("Продукт с " + str(product_id) + " id не найден\n")


def show_counter_of_pr_depart():
    print("Введите название отдела:")
    depart_name = input()
    # counter - счетчик найденных элементов в бд
    counter = 0
    for product in market:
        if product.get_department() == depart_name:
            counter = counter + 1
    print("В отделе " + depart_name + " найдено " + str(counter) + " продуктов\n")


def update_product():
    print("Введите id продукта:")
    # Блок try. В нем мы проверяем, происходит ли в вызывемых функциях, внутри его блока ошибки
    # Тут у нас дурачек пользователь может ввести буквы вместо цифр,
    # из за чего функция int выкинет ошибку (тип ошибки будет ValueError)
    try:
        product_id = int(input())
    # Тут мы обрабатываем наш ValueError
    except ValueError:
        return print("Вам нужно указать НОМЕР(id) продукта!\n")
    searching_elm_status = False
    # searching_elm_status покажет, нашли ли мы элемент, который искали в бд
    for product in market:
        # Если id текущего элемента равен id, переданный пользователем с клавиатуры,
        # залетаем в наш if
        if product.get_product_id() == product_id:
            # Нужно указать, что мы нашли искомый элемент, поэтому temp равно True
            searching_elm_status = True
            check = True
            while check:
                print("\nВведите имя продукта:")
                # По дефолту, переменная temp будет пустая
                # Если наш setter вернет ошибку, то мы выведем ее в консоль
                temp = product.set_name(input())
                if temp:
                    print(temp)
                else:
                    check = False
            check = True
            while check:
                print("\nВведите имя радела:")
                temp = product.set_department(input())
                if temp:
                    print(temp)
                else:
                    check = False
            check = True
            while check:
                print("\nВведите цену продукта:")
                temp = product.set_price(input())
                if temp:
                    print(temp)
                else:
                    check = False
            check = True
            while check:
                print("\nВведите дату изготовления:")
                temp = product.set_date_of_manufacture(input())
                if temp:
                    print(temp)
                else:
                    check = False
            check = True
            while check:
                print("\nУкажите срок годности продукта:")
                temp = product.set_shelf_life(input())
                if temp:
                    print(temp)
                else:
                    check = False
            print("\n")
            break
    if not searching_elm_status:
        print("Продукт с id " + str(product_id) + " не найден\n")


def delete_product_by_id():
    print("Введите id продукта:")
    try:
        product_id = int(input())
    except ValueError:
        return print("Вам нужно указать НОМЕР(id) продукта!\n")
    # Номер итерации (как i в циклах C++)
    index = 0
    # Индекс элемента, который мы ищем
    # -1 потому что в массивах такого индекса нету,
    # и нам удобно его использовать как показатель того, что элемент с заданным пользователем id НЕ найден
    index_of_element = -1
    for product in market:
        if product.get_product_id() == product_id:
            index_of_element = index
            break
        index = index + 1
    market.pop(index_of_element)
    if index_of_element == -1:
        print("Продукт с id " + str(product_id) + " не найден\n")


# Меню выбора функций
while True:
    print("--------------Выберете функцию--------------")
    print("0 - выход")
    print("1 - вывод информации о всех товарах")
    print("2 - вывод информации о товаре по введенному с клавиатуры номеру (id)")
    print("3 - вывода количества товаров, продающихся в определнном отделе")
    print("4 - обновление всей информации о товаре по введенному номеру (id)")
    print("5 - удалении товара по номеру (id) \n")
    print("Выберете функцию:")
    # Сохраняем введенный пользователем номер в user_choice
    # input() возвращает тип string
    user_choice = input()
    if user_choice == "0":
        break
    elif user_choice == "1":
        show_products()
    elif user_choice == "2":
        show_product_by_id()
    elif user_choice == "3":
        show_counter_of_pr_depart()
    elif user_choice == "4":
        update_product()
    elif user_choice == "5":
        delete_product_by_id()
    else:
        print("Такой функции нету, попробуйте еще раз \n")
