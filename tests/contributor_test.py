import unittest

from models.contributor import Contributor


class ContributorFormattingTest(unittest.TestCase):
    def setUp(self):
        Contributor.contributors.clear()

    def test_full_name_with_middle(self):
        Contributor('John', 'Allen', 'Smith')
        self.assertEqual('Smith,J.A.', Contributor.contributors[0])

    def test_name_without_middle(self):
        Contributor('John', '', 'Smith')
        self.assertEqual('Smith,J.', Contributor.contributors[0])

    def test_one_contributor(self):
        Contributor('John', 'Allen', 'Smith')
        self.assertEqual('Smith,J.A.', Contributor.get_contributors())

    def test_two_contributors(self):
        Contributor('John', '', 'Smith')
        Contributor('Jane', 'Alexa', 'Doe')
        self.assertEqual('Smith,J., & Doe,J.A.', Contributor.get_contributors())

    def test_three_contributors(self):
        Contributor('John', '', 'Smith')
        Contributor('Jane', 'Alexa', 'Doe')
        Contributor('Chris', 'Pea', 'Bacon')
        self.assertEqual('Smith,J., Doe,J.A., & Bacon,C.P.', Contributor.get_contributors())

    def test_four_contributors(self):
        Contributor('John', '', 'Smith')
        Contributor('Jane', 'Alexa', 'Doe')
        Contributor('Chris', 'Pea', 'Bacon')
        Contributor('Santa', '', 'Claus')
        self.assertEqual('Smith,J., Doe,J.A., Bacon,C.P., & Claus,S.', Contributor.get_contributors())
        pass

    def test_five_contributors(self):
        Contributor('John', '', 'Smith')
        Contributor('Jane', 'Alexa', 'Doe')
        Contributor('Chris', 'Pea', 'Bacon')
        Contributor('Santa', '', 'Claus')
        Contributor('Micheal', '', 'Myers')
        self.assertEqual('Smith,J., Doe,J.A., Bacon,C.P., Claus,S., & Myers,M.', Contributor.get_contributors())
        pass

    def test_six_contributors(self):
        Contributor('John', '', 'Smith')
        Contributor('Jane', 'Alexa', 'Doe')
        Contributor('Chris', 'Pea', 'Bacon')
        Contributor('Santa', '', 'Claus')
        Contributor('Micheal', '', 'Myers')
        Contributor('Barrack', 'H', 'Obama')
        self.assertEqual('Smith,J., Doe,J.A., Bacon,C.P., Claus,S., Myers,M., & Obama,B.H.',
                         Contributor.get_contributors())
        pass

    def test_seven_contributors(self):
        Contributor('John', '', 'Smith')
        Contributor('Jane', 'Alexa', 'Doe')
        Contributor('Chris', 'Pea', 'Bacon')
        Contributor('Santa', '', 'Claus')
        Contributor('Michael', '', 'Myers')
        Contributor('Barrack', 'H', 'Obama')
        Contributor('Luke', '', 'Cage')
        self.assertEqual('Smith,J., Doe,J.A., Bacon,C.P., Claus,S., Myers,M., Obama,B.H., & Cage,L.',
                         Contributor.get_contributors())
        pass

    def test_8_contributors(self):
        Contributor('John', '', 'Smith')
        Contributor('Jane', 'Alexa', 'Doe')
        Contributor('Chris', 'Pea', 'Bacon')
        Contributor('Santa', '', 'Claus')
        Contributor('Micheal', '', 'Myers')
        Contributor('Barrack', 'H', 'Obama')
        Contributor('Luke', '', 'Cage')
        Contributor('Matthew', 'Michael', 'Murdock')
        self.assertEqual('Smith,J., Doe,J.A., Bacon,C.P., Claus,S., Myers,M., Obama,B.H.,...Murdock,M.M.',
                         Contributor.get_contributors())
        pass


if __name__ == '__main__':
    unittest.main()
