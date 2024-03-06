import sqlite3

connection = sqlite3.connect("orders.db", isolation_level=None)  # isolation_level=None - ������� �� � ������ �������
cursor = connection.cursor()



# ������ ������ ����������
# 1 ������
import pprint
# pprint.pprint(list(result))  # ��� �������� �����������
#
# for i in result:
#    print(i)

# 2 ������
# print(result.fetchall()) # ��������� ���

# 3 ������
# print(result.fetchone()) # ������ �� ������
# print(result.fetchone())
# print(result.fetchone())

# 4 ������
# pprint.pprint(result.fetchmany(4)) # ������ �� �������

# cursor.execute("INSERT INTO Vendors(name, item, deal, price) VALUES ('Snigana', 'Car-sedan2', 4, 500);")
# result = cursor.execute("select * from Vendors;")
# pprint.pprint(result.fetchall())

# connection.commit() # ������ ���� � �� ��� ������ isolated level �� ����� ��� �����

# ������ ����� � ����������� ����� � ��� �����
# ������ 1 � ������
# deal_id = 3
# price = 10
# result = cursor.execute(f'select * from Vendors where deal={deal_id} and price>{price};')
# pprint.pprint(result.fetchall())

# ������ 2 tuple
# result = cursor.execute(f'select * from Vendors where deal=(?) and price>(?);', (3,10))
# result = cursor.execute(f'select * from Vendors where deal=(?);', (3,)) # ��������� ����� ������
# pprint.pprint(result.fetchall())

# ������ 3 dict
# result = cursor.execute(f'select * from Vendors where deal=:deal_id and price> :price;',
#                         {'deal_id':3, 'price':10})

# г�� ���� ���������(execute)
# 1 ������ �� ���������� ���������� cursor.execute(f'select * from Vendors where deal=(?) and price>(?);', (3,10))
# 2 ������ executemany
# cursor.executemany("INSERT INTO Vendors(name, item, deal, price) VALUES ((?), (?), (?), (?));",
#                   [('Pavlo21', 'Car-sedan44', 4, 101),
#                    ('Pavlo11', 'Car-sedan56', 4, 102),
#                    ('Pavlo1', 'Car-sedan67', 4, 101)])

# 3 ������ executescript
# with open('script.sql', 'r') as f:
#     cursor.executescript(f.read())




cursor.close()
connection.close()