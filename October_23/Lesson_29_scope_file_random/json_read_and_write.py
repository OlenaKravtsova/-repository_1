coding: 'utf-8'
import json

# # dump - для запису у файл, dumps - для генерації рядка
# data = {"name": "ПАша", "salary": "120 000"}
#
# # щоб уникнути кодування з кирилиці або іншої не англійської мови
# with open("data_json", "w") as file:
#     json.dump(data, file, ensure_ascii=False)

# dump - для запису у файл
data = {"name": "Pavlo", "salary": "120 000"}

with open("data_json", "w") as file:
    json.dump(data, file)
    print(type(data))

# dumps - для генерації рядка
json_string = json.dumps(data)
print(type(json_string))

# читати файл
with open("data_json", "r") as file:
    data2 = json.load(file)
    print(data2)

