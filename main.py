from pprint import pprint

file_name = "receipes.txt"
file_name_1 = '3.txt'

class receipe:
    def __init__(self, name, quani):
        name = ''
        qiani = str()

class ingrigient:
    def __init__(self, name, quantity, mean):
        name = ''
        quantity = int()
        mean = ''

def file_reader(file_name: str) -> dict:
    with open(file_name) as file:
        cook_book = {}
        for line in file:
            name = line.strip() #В переменную сохраняем название рецепта
            ingridients = []
            for item in range(int(file.readline())): #Цикл, который считывает количество строк по количеству ингридиентов
                d_ingr = {} #Инициализация словаря для хранения ингридиентов
                n1, n2, n3 = file.readline().split("|") #разбиваем строку на три переменные по разделителю
                d_ingr['ingredient_name'] = n1.strip(' ')
                d_ingr['quantity'] = n2.strip(' ')
                d_ingr['measure'] = n3.strip(' \n') #Вычищаем служебные символы
                ingridients.append(d_ingr)
            cook_book[name] = ingridients #Ключом словаря делаем название переменной а в значение добавляем список словарей с ингридиентами
            file.readline() #считываем пустую строку для перехода к следующему рецепту
    return cook_book
pprint(file_reader(file_name))

print('Задание №2')

dishes = ['Фахитос', 'Шаверма']
pers_c = 3
def get_shop_list_by_dishes(dishes, pers_c):
    res_dict = {}
    for items in dishes:
        for keys, values in file_reader(file_name).items():
            if keys == items:
              for elements in values:
                elements['quantity'] = float(elements['quantity']) * pers_c
                res_dict[elements.pop('ingredient_name')] = elements
    return res_dict

pprint(get_shop_list_by_dishes(dishes, pers_c))


list_of_files = ['1.txt', '2.txt', '3.txt']

print()
print('Задание №3')

def documents_reader(list_of_files) -> dict:
  content = {}
  name_f = {}
  for values in list_of_files:
    with open(values) as file:
      list_of_sting = []
      for line in file:
        list_of_sting.append(line.strip())
    name_f[len(list_of_sting)] = values
    content[len(list_of_sting)] = list_of_sting
  return [content, name_f]

new_file = '123.txt'
list_d = documents_reader(list_of_files)

def documents_writer(new_file, list_d):
    sort_content = {}
    content = list_d[0]
    name_f = list_d[1]
    with open(new_file, "w+") as file:
        sorted_keys = sorted(content, key=content.get)
        sorted_keys.reverse()
        for values in sorted_keys:
            sort_content[values] = content[values]
        for keys, items in sort_content.items():
            for key_name, value_name in name_f.items():
                if key_name == keys:
                    file.write(f'Название файла: {value_name} \n')
            file.write(f'Количество строк: {str(keys)} \n')
            for sttri in items:
                file.write(f'{sttri} \n')
            file.write('\n')
print(documents_writer(new_file, list_d))
