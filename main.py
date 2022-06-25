from pprint import pprint

file_name = "receipes.txt"
file_name_1 = '3.txt'

class Receipe:
    def __init__(self, name, quant):
        self.name = name
        self.tingr = [] #Один из атрибутов - это список ингридиентов
        self.quant = quant
    def __str__(self):
        return self.name
    __repr__ = __str__


class Ingrigient:
    def __init__(self, ingr_name, ingr_quantity, ingr_measure):
        self.name = ingr_name
        self.quantity = ingr_quantity
        self.mean = ingr_measure
    def __str__(self):
        return self.name
    __repr__ = __str__

def file_reader(file_name: str) -> dict:
    with open(file_name) as file:
        receipe = []
        ingridients = []
        tingr = []
        count = 0
        for line in file:
            name = line.strip() #В переменную сохраняем название рецепта
            quant = int(file.readline())
            for item in range(quant): #Цикл, который считывает количество строк по количеству ингридиентов
                n1, n2, n3 = file.readline().split("|") #разбиваем строку на три переменные по разделителю
                ingr_name = n1.strip(' ')
                ingr_quantity = float(n2.strip(' '))
                ingr_measure = n3.strip(' \n')
                ingridients.append(Ingrigient(ingr_name, ingr_quantity, ingr_measure))
                tingr.append(ingr_name)
            receipe.append(Receipe(name, quant))
            print(name)
            receipe[count].tingr = tingr #вывод на экран списка ингридиентов
            print(receipe[count].tingr)
            count += 1
            tingr.clear()
            file.readline()
    allist = [receipe, ingridients]
    return allist

receipes = file_reader(file_name)[0]
print(receipes[1].__dict__) #Проверка содержимого объекта класса

ingridients = file_reader(file_name)[1]
print(ingridients[1].__dict__)


print('Задание №2')


print()
print('Задание №3')

list_of_files = ['1.txt', '2.txt', '3.txt']

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
