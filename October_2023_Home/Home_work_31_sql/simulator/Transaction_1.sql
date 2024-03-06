CREATE TABLE IF NOT EXISTS Transaction_1(Id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, Transaction_ID INTEGER,
Service_Id INTEGER, Total_Cash FLOAT, Receipt_Date Date);
INSERT INTO Transaction_1(Transaction_ID, Service_Id, Total_Cash, Receipt_Date) VALUES (100011111, 201, 50.00, '01.05.2024');