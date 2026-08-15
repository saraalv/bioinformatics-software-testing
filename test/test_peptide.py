import unittest

from src.peptide import concatenacion_peptidos, polyh


class TestPeptido(unittest.TestCase):
  def test_codigo_no_valido(self):
    with self.assertRaises(ValueError):
        concatenacion_peptidos("ARND", "ARXD")


def test_input_peptido(self):
    self.assertEqual(
        concatenacion_peptidos("arn", "MKL"),
        "ARNMKL"
    )

    self.assertEqual(
        polyh("cge", 5),
        "CGEHHHHH"
    )


def test_concatenacion(self):
    self.assertEqual(
        concatenacion_peptidos("ARARAR", "TGGG"),
        "ARARARTGGG"
    )


def test_polyh(self):
    self.assertEqual(
        polyh("ARTART", 5),
        "ARTARTHHHHH"
    )
