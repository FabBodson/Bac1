import sqlite3
from ins.csv_entities import CsvEntitySource
from ins.sqlite_entities import SqliteEntityTarget


def create_tables(db_file, db, cursor):
    with open(db_file) as db_script:
        queries = db_script.readlines()
        for query in queries:
            try:
                cursor.execute(query)
            except Exception:
                print("Table déjà créée.")
        db.commit()


def _main():
    db_prod = sqlite3.connect('prod.db')

    cursor_prod = db_prod.cursor()

    try:
        create_tables("database_ddl.sql", db_prod, cursor_prod)

    except FileNotFoundError:
        print(f"File(s) not found.")

    try:
        with open("data.csv", encoding="utf-8") as csv_file:
            csv_entity = CsvEntitySource(csv_file)
            entities = csv_entity.get()

            db_prod = sqlite3.connect('prod.db')

            sql_entity_prod = SqliteEntityTarget(db_prod)

            sql_entity_prod.put(entities)

    except FileNotFoundError:
        print(f"File 'data.csv' not found.")

    db_prod.close()


if __name__ == '__main__':
    _main()
