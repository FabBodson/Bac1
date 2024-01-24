import unittest
import sqlite3

from ins.entities import EntitySource, Entity
from ins.sqlite_entities import SqliteEntityTarget, SqliteEntitySource


class TestSqliteEntityTarget(unittest.TestCase):
    DELETE_FROM_STATS = "DELETE FROM STATS";
    DELETE_FROM_ENTITY = "DELETE FROM ENTITIES";

    def setUp(self):
        self.db = sqlite3.connect('../tests.db')
        cursor = self.db.cursor()
        cursor.execute(TestSqliteEntityTarget.DELETE_FROM_STATS)
        cursor.execute(TestSqliteEntityTarget.DELETE_FROM_ENTITY)
        self.db.commit()

    def tearDown(self):
        self.db.close()

    def test_imports_entities(self):
        target = SqliteEntityTarget(self.db)

        target.put(StubEntitySource())

        self.assert_table_count_rows_equal("ENTITIES", 10)
        self.assert_table_count_rows_equal("ENTITIES", 2, "Waremme")
        self.assert_table_count_rows_equal("ENTITIES", 1, "Liège")

    def test_imports_stats(self):
        target = SqliteEntityTarget(self.db)

        target.put(StubEntitySource())

        self.assert_table_count_rows_equal("STATS", 70)
        self.assert_table_count_rows_equal("STATS", 10, "MontantMedian")
        self.assert_table_count_rows_equal("STATS", 10, "EcartInterQuartile")

    def assert_table_count_rows_equal(self, table_name, expected_count, name='%'):
        cursor = self.db.cursor()
        cursor.execute(f"SELECT COUNT(*) FROM {table_name} WHERE name LIKE ?", [name])
        count = cursor.fetchone()

        self.assertEqual(expected_count, count[0])


class StubEntitySource(EntitySource):
    def get(self):
        return [
            self.build(1000, "Pays Belgique", 2206795, 189883, 390778, 402447, 1223687, 43607, 35725),
            self.build(3000, "Région de Wallonie", 645299, 56550, 115478, 119165, 354106, 43079, 34693),
            self.build(60000, "Province de Liège", 195478, 17743, 35760, 36472, 105503, 42430, 33428),
            self.build(64000, "Arrondissement de Waremme", 15882, 816, 2287, 2548, 10231, 49378, 37244),
            self.build(64008, "Berloz", 650, 29, 92, 103, 426, 49891, 37244),
            self.build(64021, "Crisnée", 683, 28, 92, 99, 464, 52128, 39632),
            self.build(64034, "Hannut", 3182, 188, 475, 510, 2009, 49199, 38562),
            self.build(64056, "Oreye", 749, 37, 116, 118, 478, 48258, 36867),
            self.build(64065, "Saint-Georges-sur-Meuse", 1241, 54, 234, 246, 707, 44097, 30423),
            self.build(64074, "Waremme", 2795, 173, 440, 491, 1691, 46657, 35957)
        ]

    def build(self, ins, name, declarationsCount, less20000DeclarationCount, less30000DeclarationCount,
              less40000DeclarationCount, more40000DeclarationCount, median, interquatileDelta):
        entity = Entity(ins, name)

        entity['TotalDeclarations'] = declarationsCount
        entity['DeclarationsInf20000'] = less20000DeclarationCount
        entity['DeclarationsInf30000'] = less30000DeclarationCount
        entity['DeclarationsInf40000'] = less40000DeclarationCount
        entity['DeclarationsSup40000'] = more40000DeclarationCount
        entity['MontantMedian'] = median
        entity['EcartInterQuartile'] = interquatileDelta

        return entity


class SqliteEntitySourceTest(unittest.TestCase):
    DELETE_FROM_STATS = "DELETE FROM STATS";
    DELETE_FROM_ENTITY = "DELETE FROM ENTITIES";

    def setUp(self):
        self.db = sqlite3.connect('../tests.db')

    def tearDown(self):
        self.db.close()

    def test_get_stats(self):
        source = SqliteEntitySource(self.db)

        result = source.get()

        self.assertEqual(10, len(result))


if __name__ == '__main__':
    unittest.main()
