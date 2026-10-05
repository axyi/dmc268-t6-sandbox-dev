def find_user(db, name):
    query = f"SELECT * FROM users WHERE name = '{name}'"
    return db.execute(query)


def average(values):
    return sum(values) / len(values)
