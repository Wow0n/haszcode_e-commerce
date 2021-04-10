from database import session, Warehouse


def warehouse_insert(item):
    record = Warehouse(name=item.name, quantity=item.quantity, price=item.price)
    session.add(record)
    session.commit()
    return "record added"


def warehouse_update(item):
    record = session.query(Warehouse).get(item.id)
    record.name = item.name
    record.quantity = item.quantity
    record.price = item.price
    session.commit()


def warehouse_select():
    records = session.query(Warehouse)
    for records in records:
        print(records.id, " ", records.name, " ", records.quantity, " ", records.price)
    return "printed in terminal"


def warehouse_delete(record_id):
    session.query(Warehouse).filter_by(id=record_id).delete()
    session.commit()
    return "record deleted"


def client_select():
    records = session.query(Warehouse)
    for records in records:
        print(records.name)
    return "printed in terminal"
