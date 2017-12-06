import unittest

from guess import Guess

class TestGuess(unittest.TestCase):

    def setUp(self):
        self.g1 = Guess('default')

    def tearDown(self):
        pass

    def testDisplayCurrent(self):
        a_list = ['d', 'e', 'f' ,'a' ,'u' ,'l' ,'t']
        self.g1.guess('e')
        self.assertEqual(self.g1.displayCurrent(), '_ e _ _ _ _ _ ')
        self.g1.guess('a')
        self.assertEqual(self.g1.displayCurrent(), '_ e _ a _ _ _ ')
        self.g1.guess('t')
        self.assertEqual(self.g1.displayCurrent(), '_ e _ a _ _ t ')
        self.g1.guess('u')
        self.assertEqual(self.g1.displayCurrent(), '_ e _ a u _ t ')
        self.g1.guess('d')
        self.assertEqual(self.g1.displayCurrent(), 'd e _ a u _ t ')
        self.g1.guess('f')
        self.assertEqual(self.g1.displayCurrent(), 'd e f a u _ t ')
        self.g1.guess('l')
        self.assertEqual(self.g1.displayCurrent(), 'd e f a u l t ')

    def testDisplayGuessed(self):
        self.g1.guess('e')
        self.assertEqual(self.g1.displayGuessed(), ' e ')
        self.g1.guess('n')
        self.assertEqual(self.g1.displayGuessed(), ' e n ')
        self.g1.guess('a')
        self.assertEqual(self.g1.displayGuessed(), ' a e n ')
        self.g1.guess('t')
        self.assertEqual(self.g1.displayGuessed(), ' a e n t ')
        self.g1.guess('u')
        self.assertEqual(self.g1.displayGuessed(), ' a e n t u ')
        self.g1.guess('k')
        self.assertEqual(self.g1.displayGuessed(), ' a e k n t u ')
        self.g1.guess('s')
        self.assertEqual(self.g1.displayGuessed(), ' a e k n s t u ')

    def finished(self):
        self.g1.secretWord = 'default'
        self.assertTrue(self.g1.finished)

if __name__ == '__main__':
    unittest.main()
