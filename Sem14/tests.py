import unittest
from remove_ch import remove_char


class TestRemove_char(unittest.TestCase):
    def test_no_change(self):
        self.assertEqual(remove_char('qwer'), 'qwer')

    def test_result_is_str(self):
        self.assertIsInstance(remove_char('qwer'),str)

    def test_space(self):
        self.assertIn(' ', remove_char('qwer qwer'))

    def test_none(self):
        self.assertIsNotNone(remove_char('qwer'))


if __name__ == '__main__':
    unittest.main(verbosity=1)
