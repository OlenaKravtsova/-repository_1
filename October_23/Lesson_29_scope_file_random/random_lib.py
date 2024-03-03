coding: 'utf-8'
import random
random.seed(4324235245435543544354) # Щоб зберегти рандон

print(random.random()) # [0 до 1]
print(int((random.random()*100))) # [0 до 100]
print(int((random.random()*50))) # [0 до 50]
print(int(3+(random.random()*(10-3)))) # [3 до 10]
for i in range(50):
    print(int(3 + random.random() * (10 - 3)), end="/")

for i in range(50): # ціле число з діапозона
    print(random.randint(3, 7), end="/")

print()

for i in range(30): # ціле число з діапозон з кроком
    print(random.randrange(1, 7, 2), end="/")
print()

lst = ["apple", "banana", "orange", "carrot", "cherry"]
# print(lst)
# random.shuffle(lst) # перемішування
# print(lst)

print(random.sample(lst, counts=[1, 1, 10, 0, 10], k=3))
