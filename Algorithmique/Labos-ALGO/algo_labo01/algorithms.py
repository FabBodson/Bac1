from algo_labo01.model import Bus


class Result:
    def __init__(self):
        self.buses = []

    def print_bus(self):
        print("Navettes nécessaires:", len(self.buses))
        for bus in self.buses:
            index = self.buses.index(bus)
            if index < len(self.buses):
                print(f'#{index + 1}', end=" ")
                print(f'{", ".join([family for family in bus.families])} - emplacements vides = {self.buses[index].capacity}')


def first_fit(families, capacity):
    i = 0
    result = Result()

    result.buses.append(Bus([], capacity))
    for family in families:
        if (result.buses[i].capacity - family.number) >= 0:
            result.buses[i].families.append(family.name)
            result.buses[i].update_capacity(family)

        else:
            result.buses.append(Bus([], capacity))
            i += 1
            result.buses[i].families.append(family.name)
            result.buses[i].update_capacity(family)

    return result


def first_fit_decreasing(families, total_family_people, capacity):
    result = Result()
    families = tri_selection(families)
    result.buses.append(Bus([], capacity))

    for bus in result.buses:
        for family in families:
            if (bus.capacity - family.number) >= 0:
                if len(families) <= 2:
                    bus.families.append(family.name)
                    bus.update_capacity(family)
                    total_family_people -= family.number
                else:
                    bus.families.append(family.name)
                    bus.update_capacity(family)
                    total_family_people -= family.number
                    families.remove(family)

        if total_family_people > 0:
            result.buses.append(Bus([], capacity))

    return result


def full_bin(families, capacity):
    result = Result()
    i = 0

    for family in families:
        for family_bis in families:
            if (family.number + family_bis.number) == capacity:
                result.buses.append(Bus([], capacity))
                result.buses[i].families.append(family.name)
                result.buses[i].families.append(family_bis.name)
                result.buses[i].update_capacity(family)
                result.buses[i].update_capacity(family_bis)

                i += 1
                families.remove(family)

    return result


def tri_selection(families):
    for family in families:
        i = families.index(family)
        index_max = i
        maximum = families[i].number
        for j in range(i+1, len(families)):
            if families[j].number > maximum:
                index_max = j
                maximum = families[j].number
        tmp = families[i]
        families[i] = families[index_max]
        families[index_max] = tmp

    return families
