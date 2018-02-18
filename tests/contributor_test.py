import unittest
from models.contributor import Contributor


class ContributorTest(unittest.TestCase):
    def test_full_name_with_middle(self):
        Contributor('Malakai', 'Allen', 'Whearry')
        self.assertEqual('Whearry,M.A.', Contributor.contributors[0])

    def test_name_without_middle(self):
        Contributor('Allen', '', 'Whearry')
        self.assertEqual('Whearry,A.', Contributor.contributors[1])


if __name__ == '__main__':
    unittest.main()
