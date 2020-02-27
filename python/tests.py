import unittest

class TestTesting(unittest.TestCase):

    def test_test(self): # basic test to proc CI/CD and make sure all is working
        self.assertEqual('foo'.upper(), 'FOO')

if __name__ == "__main__":
    unittest.main()