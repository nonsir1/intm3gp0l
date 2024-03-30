import csv

def task2():
    """
    Функция, которая выполняет второе задание конкурса.
    Работает с файлом products.csv, сперва открывает его.
    Сортируем нашу таблицу и получаем самый дорогой товар по первой категории (в уже отсортированной таблице) в листе.
    :return: string - Строка с решением в соответствии с требованиями задачи
    """
    def sort(r):
        """
        Реализована сортировка вставками согласно заданию.
        :param r: Лист, который подлежит сортировке
        """
        for i in range(len(r)):
            temp = r[i]
            j = i-1
            while j >= 0 and (r[j]["Category"]) > (temp["Category"]):
                r[j + 1] = r[j]
                j -= 1
            r[j + 1] = temp
        return r

    with open("products.csv", encoding="utf-8-sig", newline="") as prod:
        r = sort(list(csv.DictReader(prod, delimiter=";", quotechar='"')))

    category = r[0]["Category"]
    cost = 0.0
    p = ""
    for line in r:
        if float(line["Price per unit"]) > cost and category == line["Category"]:
            cost = max(cost, float(line["Price per unit"]))
            p = line["product"]

    return f"В категории: {category} самый дорогой товар: {p} его цена за единицу товара составляет {cost}"

print(task2())