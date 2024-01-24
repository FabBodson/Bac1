import unittest

from io import StringIO
from ins.entities import Entity
from ins.csv_entities import CsvEntitySource


class TestCsvEntitySource(unittest.TestCase):
    def setUp(self) -> None:
        self.input_str = """Nom;CodeINS;TotalDeclarations;DeclarationsInf20000;DeclarationsInf30000;DeclarationsInf40000;DéclarationsSup40000;MontantMedian;EcartInterQuartile
Pays Belgique;1000;2206795;189883;390778;402447;1223687;43607;35725
Région de Wallonie;3000;645299;56550;115478;119165;354106;43079;34693
Province de Liège;60000;195478;17743;35760;36472;105503;42430;33428
Arrondissement de Waremme;64000;15882;816;2287;2548;10231;49378;37244
Berloz;64008;650;29;92;103;426;49891;37244
Crisnée;64021;683;28;92;99;464;52128;39632
Hannut;64034;3182;188;475;510;2009;49199;38562
Oreye;64056;749;37;116;118;478;48258;36867
Saint-Georges-sur-Meuse;64065;1241;54;234;246;707;44097;30423
Waremme;64074;2795;173;440;491;1691;46657;35957"""

    def test_ignores_line_header(self):
        src = CsvEntitySource(StringIO(self.input_str))
        imported = src.get()

        self.assertEqual(len(imported), 10)

    def test_load_records_data(self):
        src = CsvEntitySource(StringIO(self.input_str))
        imported = [e for e in src.get() if (e.level == Entity.DISTRICT and e.name == "Waremme")][0]

        self.assertEqual(15882, imported["TotalDeclarations"])
        self.assertEqual(49378, imported["MontantMedian"])
        self.assertEqual(37244, imported["EcartInterQuartile"])


if __name__ == '__main__':
    unittest.main()
