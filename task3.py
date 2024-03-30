import csv

def task3():
    """
    Функция, которая выполняет третье задание конкурса.
    Работает с файлом products.csv, сперва открывает его.
    Сортируем данные по категориям сразу, а затем после запроса пользователя сортируем по этим данным и получает запрашиваемый результат.
    Печатает вывод в консоль.
    """

    def find(category, r):
        """
        Функция производит необходимые преобразования данных.
        Выводит продукт с наименьшим кол-вом проданных единиц.
        :param category: Категория, которую необходимо найти
        :param r: Таблица по котрой следует искать
        :return: list|int - Параметры найденного продукта или 0, если товар не найден
        """
        c = 10000.0
        p = ""
        for l in r:
            if l["Category"] == category and float(l["Count"]) < c:
                c = min(float(l["Count"]), c)
                p = l["product"]
        if p == "":
            return 0
        else:
            return [p, c]

    with open("products.csv", encoding="utf-8-sig", newline="") as prod:
        r = sorted(list(csv.DictReader(prod, delimiter=";", quotechar='"')), key=lambda x: x["Category"])

    category = input()
    while category != "молоко":
        res = find(category, r)
        if res == 0:
            print("Такой категории не существует в нашей БД")
        else:
            print(f"В категории: {category} товар: {res[0]} был куплен {res[1]} раз")
        category = input()

task3()