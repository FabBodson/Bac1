import unittest

from ins.entities import Entity


class TestEntity(unittest.TestCase):
    def test_has_a_code_and_a_name_and_level(self):
        self.assert_entity_has_code_name_level(Entity(62063, "Liège"), 62063, "Liège", Entity.LOCALITY)
        self.assert_entity_has_code_name_level(Entity(60000, "Province de Liège"), 60000, "Liège", Entity.PROVINCE)
        self.assert_entity_has_code_name_level(Entity(81000, "Arrondissement d’Arlon"), 81000, "Arlon", Entity.DISTRICT)
        self.assert_entity_has_code_name_level(Entity(3000, "Région de Wallonnie"), 3000, "Wallonnie", Entity.REGION)
        self.assert_entity_has_code_name_level(Entity(1000, "Pays de Belgique"), 1000, "Belgique", Entity.COUNTRY)

    def assert_entity_has_code_name_level(self, entity, code, name, level):
        self.assertEqual(code, entity.code)
        self.assertEqual(name, entity.name)
        self.assertEqual(level, entity.level)

    def test_indexes_stats(self):
        entity = Entity(62063, "Liege")

        entity["MontantMedian"] = 36524
        entity["EcartInterQuartile"] = 33020

        self.assertEqual(entity["MontantMedian"], 36524)
        self.assertEqual(entity["EcartInterQuartile"], 33020)
        self.assertEqual(entity["RienDuTout"], -1)

    def test_provides_with_stat_key(self):
        entity = Entity(62063, "Liege")

        entity["MontantMedian"] = 36524
        entity["EcartInterQuartile"] = 33020

        self.assertIn('MontantMedian', entity.get_keys())
        self.assertIn('EcartInterQuartile', entity.get_keys())


if __name__ == '__main__':
    unittest.main()
