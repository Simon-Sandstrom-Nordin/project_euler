import unittest
from tilda_residues.Test.lab9_main import string_in


class SyntaxTest(unittest.TestCase):

    def test_correct_syntax(self):
        self.assertEqual(string_in("""Na
H2O
Si(C3(COOH)2)4(H2O)7
Na332
#
"""), """Formeln är syntaktiskt korrekt
Formeln är syntaktiskt korrekt
Formeln är syntaktiskt korrekt
Formeln är syntaktiskt korrekt
""")

    def test_syntax2(self):
        self.assertEqual(string_in("""C(Xx4)5
C(OH4)C
C(OH4C
H2O)Fe
H0
H1C
H02C
Nacl
a
(Cl)2)3
)
2
#
"""), """Okänd atom vid radslutet 4)5
Saknad siffra vid radslutet C
Saknad högerparentes vid radslutet 
Felaktig gruppstart vid radslutet )Fe
För litet tal vid radslutet 
För litet tal vid radslutet C
För litet tal vid radslutet 2C
Saknad stor bokstav vid radslutet cl
Saknad stor bokstav vid radslutet a
Felaktig gruppstart vid radslutet )3
Felaktig gruppstart vid radslutet )
Felaktig gruppstart vid radslutet 2
""")


if __name__ == '__test__':
    unittest.main()
