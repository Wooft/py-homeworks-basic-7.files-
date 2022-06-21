from pprint import pprint

file_name = "receipes.txt"

def file_reader(file_name: str) -> dict:
    with open(file_name) as file:
        res = {}
        for line in file:
            name = line.strip()
            ingridients = []
            for item in range(int(file.readline())):
                ingridient = file.readline()
                ingridients.append(ingridient.strip())
            res[name] = ingridients
            file.readline()
    return res
catalog = file_reader(file_name)
pprint(catalog)
