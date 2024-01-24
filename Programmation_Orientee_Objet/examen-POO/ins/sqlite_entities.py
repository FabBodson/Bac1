from ins.entities import EntitySource

INSERT_ENTITY = """INSERT INTO ENTITIES (code, name, Level) VALUES (?, ?, ?);"""
INSERT_STATS = """INSERT INTO STATS (name, entity_code, value) VALUES (?, ?, ?);"""

SELECT_LOCALITIES = """SELECT ent.code, ent.name, s.value FROM ENTITIES ent 
                        JOIN STATS s on ent.code = s.entity_code
                        WHERE s.name = 'MontantMedian' OR s.name = 'PremierQuartile'
                        ORDER BY s.value DESC"""


class SqliteEntityTarget(EntitySource):
    def __init__(self, database):
        self.__database = database

    def put(self, source: EntitySource):
        cursor = self.database.cursor()
        for entity in source.get():
            try:
                cursor.execute(INSERT_ENTITY, (entity.code, entity.name, entity.level))

            except Exception:
                print("Insertion d'entité déjà faite.")

            for stat in entity.datas:
                try:
                    cursor.execute(INSERT_STATS, (stat, entity.code, entity.datas[stat]))
                except Exception:
                    print("Insertion de statistiques déja faite.")

        self.database.commit()

    @property
    def database(self):
        return self.__database


class SqliteEntitySource(EntitySource):
    def __init__(self, database):
        self.__database = database

    def get(self):
        cursor = self.database.cursor()
        cursor.execute(SELECT_LOCALITIES)
        return cursor.fetchmany(10)

    @property
    def database(self):
        return self.__database
