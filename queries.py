from database import mydb

def warehouse_insert(item):
    cursor = mydb.cursor()

    cursor.execute("INSERT INTO warehouse (name, quantity, price) VALUES (%s, %s, %s)", (item.name, item.quantity, item.price))
    mydb.commit()

    cursor.execute("SELECT * FROM warehouse")
    return cursor.fetchall()

    cursor.close()
    mydb.close()


def warehouse_select():
    cursor = mydb.cursor()

    cursor.execute("SELECT * FROM warehouse")
    return cursor.fetchall()

    cursor.close()
    mydb.close()