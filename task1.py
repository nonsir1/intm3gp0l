import csv

def task1():
    """
    Функция, которая выполняет первое задание конкурса.
    В первую очередь, добавляет столбец "Total" и считает для него значения.
    А затем открывает новый файл products_new.csv и добавляет в него этот столбец.
    После этого, функция выводит итоговую сумму для категории "Закуски" в консоль.
    :return: float - Итоговая сумма для категории "Закуски"
    """
    with open("products.csv", encoding="utf-8-sig", newline="") as prod:
        r = list(csv.DictReader(prod, delimiter=";", quotechar='"'))
        for l in r:
            l["total"] = float(l["Price per unit"]) * float(l["Count"])

    with open("products_new.csv", "w", encoding="utf-8-sig", newline="") as prod_new:
        w = csv.DictWriter(prod_new, fieldnames=["Category", "product", "Date", "Price per unit", "Count", "total"], delimiter=";")
        w.writeheader()
        w.writerows(r)

    out = 0
    for l in r:
        if "Закуски" in l["Category"]:
            out += float(l["total"])
    return out

print(task1())