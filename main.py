from pprint import pprint

file_name = "receipes.txt"
file_name_1 = '3.txt'

class Receipe:
    def __init__(self, name, quant):
        self.name = name
        self.tingr = [] #Один из атрибутов - это список ингридиентов
        self.quant = quant

tingr = []
def file_reader(file_name: str) -> dict:
    with open(file_name) as file:
        receipe = [] #Список  объектов класса "Receipe"
        count = 0 #Счетчик
        ingridients = [] #Список для ингридиентов
        for line in file:
            name = line.strip() #В переменную сохраняем название рецепта
            quant = int(file.readline()) #Количество ингридиентов
            receipe.append(Receipe(name, quant))  # Создаем элементы класса Receipe и добавляем их в список
            for item in range(quant): #Цикл, который считывает количество строк по количеству ингридиентов
                d_ingr = {}  # Инициализация словаря для хранения ингридиентов
                n1, n2, n3 = file.readline().split("|")  # разбиваем строку на три переменные по разделителю
                d_ingr['ingredient_name'] = n1.strip(' ')
                d_ingr['quantity'] = n2.strip(' ')
                d_ingr['measure'] = n3.strip(' \n')  # Вычищаем служебные символы
                ingridients.append(d_ingr)
                receipe[count].tingr.append(d_ingr) #Добавялем в список ингридиентов ингридиенты
            count += 1
            file.readline()
            ingridients.clear() #Очистка списка
    return receipe

ingridients = file_reader(file_name)

print("Задача №1")

cook_book = {}
for elements in ingridients:
    cook_book[elements.name] = elements.tingr
pprint(cook_book)


print('Задание №2')
dishes = ['Запеченный картофель', 'Омлет']
person_count = 2
def get_shop_list_by_dishes(dishes, person_count):
    lists = {}
    for items in ingridients:
        if items.name in dishes:
            for elements in items.tingr:
                elements['quantity'] = float(elements['quantity']) * person_count
                lists[elements.pop('ingredient_name')] = elements
    return lists
pprint(get_shop_list_by_dishes(dishes, person_count))