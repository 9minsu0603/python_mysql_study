import inspect

from connection.connection_study01 import connect


def connect_pool01():
    print("\n=={}() ==".format(inspect.stack()[0][3]))
    connection = DatabaseConnectionPool.get_instance().get_connection()
    print(type(connection), connection)
    connection.close()


def explicitly_connection_pool():
    print("\n=={}() ==".format(inspect.stack()[0][3]))
    connection = ExplicitlyConnectionPool.get_instance()
    print("ConnectionPool {}".format(connectionPool))
    connection = connectionPool.get_connection()
    print("Connection {}".format(connection))
    connection.close()


def implicitly_connection_pool():
    print("\n=={}() ==".format(inspect.stack()[0][3]))
    connection = implicitlyConnectionPool.get_instance()
    print("ConnectionPool {}".format(connectionPool))
    connection = connectionPool.get_connection()
    print("Connection {}".format(connection))
    connection.close()


if __name__ == "__main__":
    # for i in range(20):
    #     connect_pool01()

    explicitly_connection_pool()
    implicitly_connection_pool()