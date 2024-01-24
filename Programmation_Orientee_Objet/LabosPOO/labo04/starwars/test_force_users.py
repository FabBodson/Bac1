import unittest
from force_users import ForceUser, Jedi, Sith
from entity import Entity


class ForceUserTest(unittest.TestCase):

    def test_is_an_entity(self):
        princess = ForceUser('Leia Organa', 30, 5)

        self.assertIsInstance(princess, Entity)

    def test_has_name_and_hit_points_and_attack_points(self):
        princess = ForceUser('Leia Organa', 30, 5)

        self.assertEqual('Leia Organa', princess.name)
        self.assertEqual(30, princess.hit_points)
        self.assertEqual(5, princess.damage_points)

    def test_can_use_force_on_others(self):
        princess = ForceUser('Leia Organa', 30, 5)
        trooper = Entity('StormTrooper 1', 15)

        actual = princess.use_force_on(trooper)

        self.assertEqual('Leia Organa projette la force sur StormTrooper 1. Dégâts causés : 5', actual)
        self.assertEqual(10, trooper.hit_points)

    # Les tests prévus pour Entity devraient également réussir pour un ForceUser



class JediTest(unittest.TestCase):
    def test_is_a_force_user(self):
        master = Jedi('Mace Windu', 300, 25)

        self.assertIsInstance(master, ForceUser)

    def test_can_use_force_on_others(self):
        master = Jedi('Mace Windu', 300, 25)
        trooper = Entity('StormTrooper 2', 15)

        actual = master.use_force_on(trooper)

        self.assertEqual('Mace Windu projette la force sur StormTrooper 2. Dégâts causés : 25', actual)
        self.assertFalse(trooper.is_alive())

    def test_can_use_force_fury_on_others(self):
        master = Jedi('Mace Windu', 300, 25)
        master.take_hit(298)  # enters in fury mode
        at_at = Entity('AT-AT Walker', 1000)

        actual = master.use_force_on(at_at)

        self.assertEqual('Mace Windu utilise la rage de la force sur AT-AT Walker. Dégâts causés : 250', actual)
        self.assertEqual(750, at_at.hit_points)

    def test_force_fury_disappears_after_first_use(self):
        master = Jedi('Mace Windu', 300, 25)
        at_at = Entity('AT-AT Walker', 1000)
        master.take_hit(298)  # enters in fury mode
        master.use_force_on(at_at)
        actual = master.use_force_on(at_at)

        self.assertEqual(725, at_at.hit_points)
        self.assertEqual('Mace Windu projette la force sur AT-AT Walker. Dégâts causés : 25', actual)

    # Les tests prévus pour ForceUser devraient également réussir pour un Jedi



class SithTest(unittest.TestCase):
    def test_is_a_force_user(self):
        emperor = Sith('Darth Sidious', 305, 21)

        self.assertIsInstance(emperor, ForceUser)

    def test_can_use_force_on_others(self):
        emperor = Sith('Darth Sidious', 305, 21)
        master = Jedi('Mace Windu', 300, 25)

        actual = emperor.use_force_on(master)

        self.assertEqual('Darth Sidious projette la force sur Mace Windu. Dégâts causés : 21', actual)
        self.assertEqual(279, master.hit_points)

    def test_can_use_force_choke_on_others(self):
        emperor = Sith('Darth Sidious', 305, 21)
        master = Jedi('Mace Windu', 300, 25)

        for i in range(2):
            emperor.use_force_on(master)
        actual = emperor.use_force_on(master)

        self.assertEqual('Darth Sidious étrangle Mace Windu. Dégâts causés : 42', actual)
        self.assertEqual(216, master.hit_points)

    def test_can_use_force_lightning_on_others(self):
        emperor = Sith('Darth Sidious', 305, 21)
        master = Jedi('Mace Windu', 300, 25)

        for i in range(4):
            emperor.use_force_on(master)
        actual = emperor.use_force_on(master)

        self.assertEqual('Darth Sidious lance des éclairs sur Mace Windu. Dégâts causés : 105', actual)
        self.assertEqual(90, master.hit_points)

    def test_prefers_lightning_over_choke(self):
        emperor = Sith('Darth Sidious', 305, 21)
        master = Jedi('Mace Windu', 300, 25)

        for i in range(14):
            emperor.use_force_on(master)
        actual = emperor.use_force_on(master)

        self.assertEqual('Darth Sidious lance des éclairs sur Mace Windu. Dégâts causés : 105', actual)

    # Les tests prévus pour ForceUser devraient également réussir pour un Sith
