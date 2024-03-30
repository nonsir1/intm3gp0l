import csv

def task4():
    """
    Функция, которая выполняет четвертое задание конкурса.
    В первую очередь, добавляет столбец "promocode" и считает для него значения.
    А затем открывает новый файл products_promo.csv и добавляет в него этот столбец.
    """
    def promo(name, date):
        """
        Функция для генерации промокодов согласно техническому заданию.
        Реализован при помощи сдвигов по строчкам.
        :param name: Имя товара
        :param date: Дата поступления товара
        :return: Готовый промокод
        """
        d, m, y = date.split(".")
        return f"{name[:2]}{d}{name[-2:][::-1]}{m[::-1]}".upper()


    with open("products.csv", encoding="utf-8-sig", newline="") as prod:
        r = csv.DictReader(prod, delimiter=";", quotechar='"')
        prod_promos = []
        for l in r:
            l["promocode"] = promo(l["product"], l["Date"])
            prod_promos.append(l)

    with open("product_promo.csv", "w", encoding="utf-8-sig", newline="") as prod_new:
        w = csv.DictWriter(prod_new, fieldnames=["Category", "product", "Date", "Price per unit", "Count", "promocode"], delimiter=";")
        w.writeheader()
        w.writerows(prod_promos)

task4()