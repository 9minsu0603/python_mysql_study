import inspect

from connection.connection_study01 import connect


def connect01():
    print("\n=={}() ==".format(inspect.stack()[0][3]))
    db = read_db_config()
    print(type(db), db)

def connect02():
    print("\n=={}() ==".format(inspect.stack()[0][3]))
    connect_use_config()

if __name__ == "__main__":
    for i in range(20):
        connect01()