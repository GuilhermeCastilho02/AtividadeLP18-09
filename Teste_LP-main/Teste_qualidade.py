from utils import parse_date, time_delta, extract_lines, time_delta_txt
import unittest

class TestFuncDistData1(unittest.TestCase):
    def testQualidade_1(self):
        datas_inexistentes_1 = parse_date("0 de Agosto de 2023")
        expected_1 = ValueError
        self.assertEqual(datas_inexistentes_1, expected_1)

    def testQualidade_2(self):
        datas_inexistentes_2 = parse_date("31 de Fevereiro de 2023")
        expected_2 = ValueError
        self.assertEqual(datas_inexistentes_2, expected_2)

    def testQualidade_3(self):
        datas_inexistentes_3 = time_delta('31 de janeiro de 2023','18 de Janeiro de 2024')
        expected_3 = 352
        self.assertEqual(datas_inexistentes_3, expected_3)

    def testQualidade_4(self):
        datas_inexistentes_4 = time_delta('31 de janeiro de 2023000000000000','18 de Janeiro de 2024')
        expected_4 = ValueError
        self.assertEqual(datas_inexistentes_4, expected_4)

    def testQualidade_6(self):
        datas_inexistentes_6 = time_delta('31 de janeiro de 2024', '18 de Janeiro de 2023')
        expected_6 = 378
        self.assertEqual(datas_inexistentes_6, expected_6)



if __name__ == "__main__":
    unittest.main()

