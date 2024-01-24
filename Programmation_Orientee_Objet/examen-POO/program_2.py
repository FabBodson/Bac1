from ins.csv_entities import CsvEntityTarget
from ins.sqlite_entities import SqliteEntitySource
import sqlite3


def _main():
    db = sqlite3.connect("prod.db")
    try:
        with open("result.csv", "w", newline='') as csv_result:
            csv_entity = CsvEntityTarget(csv_result)
            sql_entity = SqliteEntitySource(db)
            csv_entity.put(sql_entity.get())

    except FileNotFoundError:
        print("Wrong file name")

    db.close()


if __name__ == '__main__':
    _main()
