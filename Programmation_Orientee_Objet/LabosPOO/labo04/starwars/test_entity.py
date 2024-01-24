import unittest
from entity import Entity


class EntityTest(unittest.TestCase):


    def test_has_name_and_hit_points(self):
        senator = Entity('Senator Organa', 10)

        self.assertEqual('Senator Organa', senator.name)
        self.assertEqual(10, senator.hit_points)


    def test_takes_damage(self):
        senator = Entity('Senator Organa', 10)

        senator.take_hit(9)

        self.assertEqual(1, senator.hit_points)
        self.assertTrue(senator.is_alive())


    def test_can_die(self):
        senator = Entity('Senator Organa', 10)

        senator.take_hit(10)

        self.assertEqual(0, senator.hit_points)
        self.assertFalse(senator.is_alive())