from configparser import ConfigParser


def read_db_config(filename='config.ini', section='mysql'):
    parser = ConfigParser()
    parser.read(filename)

    db = {}
    if parser.has_section(section):
        for item in parser.items(section):
            db[item[0]] = item[1]

    else:
        raise Exception('{0} not found in the {1} file'.format(sections, filename))
    return db