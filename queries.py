from database import session, Warehouse


def warehouse_insert(item):
    print("dupa")


def warehouse_select():
    records = session.query(Warehouse)
    for records in records:
        print(records)


def warehouse_delete(ID):
    print("dupa")

def client_select():
    print("dupa")
