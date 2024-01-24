from model import Bus


class Result:

    def __init__(self):
        self.__buses = []

    def __len__(self):
        return len(self.__buses)

    def __getitem__(self, item):
        return self.__buses[item]

    def __lt__(self, other):
        if not isinstance(other, self.__class__):
            return False
        if len(self.__buses) == len(other.__buses):
            return self.empty_seats < other.empty_seats
        else:
            return len(self.__buses) < len(other.__buses)

    @property
    def buses(self):
        return self.__buses.copy()

    @property
    def empty_seats(self):
        return sum([bus.empty_seats for bus in self.__buses])

    def add_bus(self, bus):
        self.__buses.append(bus)


def first_fit(families, capacity):
    result = Result()
    for family in families:
        for bus in result:
            if bus.can_add(family):
                bus.add(family)
                break
        else:
            bus = Bus(capacity)
            bus.add(family)
            result.add_bus(bus)
    return result


def first_fit_decreasing(families, capacity):
    return first_fit(__sort(families.copy()), capacity)


def full_bin(families, capacity):
    result = Result()
    families = __sort(families.copy())
    while len(families) > 0:
        bus = Bus(capacity)
        families = __fill_bus(bus, families)
        result.add_bus(bus)
    return result


def __sort(families):
    return sorted(families, key=lambda family: family.size, reverse=True)


def __fill_bus(bus, families):
    impossible = False
    index = 0
    while bus.empty_seats != 0 or len(families) > 0 or impossible:
        family = families[index]
        if bus.can_add(family):
            bus.add(family)
            families.remove(family)
            index = 0
            continue
        index += 1
        if index == len(families):
            break
    return families
