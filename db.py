"""A tiny in-memory 'database'. Almost every module imports this,
which is why Graphify will show it as a busy intersection."""

_TABLES = {"users": {}, "products": {}, "orders": {}}


def save(table, key, value):
    _TABLES[table][key] = value


def get(table, key):
    return _TABLES[table].get(key)


def all_rows(table):
    return list(_TABLES[table].values())
