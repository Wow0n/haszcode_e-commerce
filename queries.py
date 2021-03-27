from database import mydb


def warehouse_insert(item):
    cursor = mydb.cursor()

    cursor.execute("INSERT INTO warehouse (name, quantity, price) VALUES (%s, %s, %s)",
                   (item.name, item.quantity, item.price))
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


def warehouse_delete(ID):
    cursor = mydb.cursor()

    cursor.execute('DELETE FROM warehouse WHERE warehouse.ID = %s', [ID])
    mydb.commit()

    cursor.execute("SELECT * FROM warehouse")
    return cursor.fetchall()

    cursor.close()
    mydb.close()

def client_select():
    cursor = mydb.cursor()

    cursor.execute("SELECT name, quantity, price FROM warehouse")
    return cursor.fetchall()

    cursor.close()
    mydb.close()
