def average(values):
    total = 0
    for v in values:
        total += v
    return total / len(values)


def find_user(db, name):
    query = "SELECT * FROM users WHERE name = '" + name + "'"
    return db.execute(query)
