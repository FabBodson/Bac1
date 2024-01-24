
class Entity:
    LOCALITY = "LOCALITY"
    DISTRICT = "DISTRICT"
    PROVINCE = "PROVINCE"
    REGION = "REGION"
    COUNTRY = "COUNTRY"

    def __init__(self, code, name):
        self.__code_ins = code
        tmp_name = name.split(" ")[-1]
        self.__name = tmp_name[2:] if "’" in tmp_name else tmp_name

        if name.split(" ")[0] == "Arrondissement":
            self.__level = self.DISTRICT
        elif name.split(" ")[0] == "Province":
            self.__level = self.PROVINCE
        elif name.split(" ")[0] == "Région":
            self.__level = self.REGION
        elif name.split(" ")[0] == "Pays":
            self.__level = self.COUNTRY
        else:
            self.__level = self.LOCALITY

        self.datas = {
            "TotalDeclarations": None,
            "DeclarationsInf20000": None,
            "DeclarationsInf30000": None,
            "DeclarationsInf40000": None,
            "DeclarationsSup40000": None,
            "MontantMedian": None,
            "EcartInterQuartile": None
        }

    def __getitem__(self, item):
        if item in self.datas:
            return self.datas[item]
        else:
            return -1

    def __setitem__(self, key, value):
        self.datas[key] = value

    def get_keys(self):
        key_collection = []
        for key in self.datas:
            key_collection.append(key)
        return key_collection

    @property
    def code(self):
        return self.__code_ins

    @property
    def name(self):
        return self.__name

    @property
    def level(self):
        return self.__level


class EntitySource:
    def get(self):
        pass


class EntityTarget:
    def put(self, source: EntitySource):
        pass
