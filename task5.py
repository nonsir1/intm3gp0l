import csv

def task5():
    """
    Функция, которая выполняет пятое задание конкурса.
    Открывает файл и создает словарь. Записывает в него все товары ("product" - "Count")
    Затем, мы сортируем продукты по второму значению в словаре и выводим 10 первых уже отсортированный товаров по наименьшей продаваемости вне функции.
    Печатает вывод в консоль.
    """

    def getDict(r):
        """
        Возвращает уже отсортироыванный готовый словарь для вывода.
        :param r: Исходная таблица
        :return: dict - Нужный словарь согласно заданию
        """
        dic = dict()
        for l in r:
            if (l["product"], l["Category"]) not in dic:
                dic[l["product"], l["Category"]] = float(l["Count"])
            else:
                dic[l["product"], l["Category"]] += float(l["Count"])
        return sorted(dic.items(), key=lambda x: x[1])

    with open("products.csv", encoding="utf-8-sig", newline="") as prod:
        r = csv.DictReader(prod, delimiter=";", quotechar='"')
        dic = getDict(r)
        c = 0
        for i in dic:
            print(f"{i[0][1]}, {i[1]}")
            c += 1
            if c == 10:
                break

task5()