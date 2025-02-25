from validate import Validate    # The code to test
import unittest   # The test framework

class Test_TestValidate(unittest.TestCase):
    def test_zip_happy(self):
        #HAPPY PATH
        self.assertTrue(Validate.zip("17701"))

    def test_zip_bad(self):
        #ABUSE
        f = open("blns.payloads", "rb")

        for line in f:
            print(f"Attempting {line}")
            self.assertFalse(Validate.zip(str(line)))

if __name__ == '__main__':
    unittest.main()
