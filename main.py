from pprint import pprint

file_name = "receipes.txt"

def file_reader(file_name: str) -> dict:
    with open(file_name) as file:
        cook_book = {}
        for line in file:
            name = line.strip() #В переменную сохраняем название рецепта
            ingridients = []
            for item in range(int(file.readline())): #Цикл, который считывает количество строк по количеству ингридиентов
                d_ingr = {} #Инициализация словаря для хранения ингридиентов
                n1, n2, n3 = file.readline().split("|")
                d_ingr['ingredient_name'] = n1.strip(' ')
                d_ingr['quantity'] = n2.strip(' ')
                d_ingr['measure'] = n3.strip(' \n')
            cook_book[name] = d_ingr #Ключом словаря делаем название переменной а в значение добавляем словарь  с ингридиентами
            file.readline() #считываем пустую строку для перехода к следующему рецепту
    return cook_book
catalog = file_reader(file_name)
print(catalog)
