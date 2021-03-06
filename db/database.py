import sqlite3

connection = sqlite3.connect("./db/pineapplestore.db")
cursor = connection.cursor()
create_user_table = '{}{}{}'.format(
    'CREATE TABLE IF NOT EXISTS',
    ' user(id INTEGER PRIMARY KEY,',
    ' username text NOT NULL, password text NOT NULL, address text NOT NULL);'
)

cursor.execute(create_user_table)

create_history_table ='{}{}{}{}{}{}'.format(
    'CREATE TABLE IF NOT EXISTS',
    ' purchase_history(id INTEGER PRIMARY KEY,',
    ' product text, user_id INTEGER NOT NULL,',
    ' product_id INTEGER NOT NULL,',
    ' FOREIGN KEY (user_id) REFERENCES user(id),',
    ' FOREIGN KEY (product_id) REFERENCES inventory(id));'
)
cursor.execute(create_history_table)

create_inventory_table = '{}{}{}'.format(
    'CREATE TABLE IF NOT EXISTS',
    ' inventory(id INTEGER PRIMARY KEY,',
    ' product text, price FLOAT);'
)
cursor.execute(create_inventory_table)

cursor.execute('INSERT OR REPLACE INTO user VALUES(1, "hope_tambala", "qwert", "Ann Arbor");')
cursor.execute('INSERT OR REPLACE INTO user VALUES(2, "chance_murphy", "qwaszx", "Ann Arbor");')
cursor.execute('INSERT OR REPLACE INTO user VALUES(3, "jalin_parker", "zxasqw", "Ann Arbor");')
cursor.execute('INSERT OR REPLACE INTO user VALUES(4, "kangning_chen", "asdfg", "Ann Arbor");')
cursor.execute('INSERT OR REPLACE INTO user VALUES(5, "yunqi_qian", "qwerty", "Ann Arbor");')
cursor.execute('INSERT OR REPLACE INTO user VALUES(6, "tayloir_thompson", "aqwerva", "Ann Arbor");')

cursor.execute('INSERT OR REPLACE INTO inventory VALUES(1, "tshirt", 10999.99);')
cursor.execute('INSERT OR REPLACE INTO inventory VALUES(2, "shorts", 45.99);')
cursor.execute('INSERT OR REPLACE INTO inventory VALUES(3, "cardigan", 599.99);')
cursor.execute('INSERT OR REPLACE INTO inventory VALUES(4, "boots", 20050.99);')

cursor.execute('INSERT OR REPLACE INTO purchase_history VALUES(1, "tshirt", 1, 1);')

connection.commit()
connection.close()

print('Database successfully created and populated with data!')