from database import session, Warehouse


def warehouse_insert(item):
    temp = Warehouse(name=item.name, quantity=item.quantity, price=item.price)
    session.add(temp)
    session.commit()


def warehouse_update(item):
    print("dupa")


def warehouse_select():
    records = session.query(Warehouse)
    for records in records:
        print(records.id, " ", records.name, " ", records.quantity, " ", records.price)
    return "printed in terminal"


def warehouse_delete(ID):
    print("dupa")


def client_select():
    records = session.query(Warehouse)
    for records in records:
        print(records.name)
    return "printed in terminal"
