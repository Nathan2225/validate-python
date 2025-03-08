from validate import Validate    # The code to test
import unittest   # The test framework

class Test_TestValidate(unittest.TestCase):
    def test_zip_happy(self):
        li = ["15464", "17701", "17801", "10101", "00000"]
        #HAPPY PATH
        for string in li:
            self.assertTrue(Validate.zip(string))

    def test_zip_bad(self):
        #ABUSE
        f = open("./bins.payloads", "rb")

        for line in f:
            print(f"Attempting {line}")
            self.assertFalse(Validate.zip(str(line)))


    def test_age_happy(self):
        #HAPPY PATH
        ages = range(1, 18)

        for age in ages:
            self.assertTrue(Validate.minor(age))


    def test_age_bad(self):
        #ABUSE
        f = open("./bins.payloads", "rb")

        for line in f:
            print(f"Attempting {line}")
            self.assertFalse(Validate.minor(str(line)))


    def test_email_happy(self):
        #HAPPY PATH
        li = ["happy@gmail.com", "unhappy@yahoo.com"]
        for string in li:
            self.assertTrue(Validate.email(string))

    def test_email_bad(self):
        #ABUSE
        f = open("./bins.payloads", "rb")

        for line in f:
            print(f"Attempting {line}")
            if "@" in line and "." in line:  
                continue
            self.assertFalse(Validate.email(str(line)))


    def test_is_lat_happy(self):
        #HAPPY PATH
        for number in [-90, 0, 89.9, -5]:
            self.assertTrue(Validate.is_lat(number))

    def test_is_lat_bad(self):
        #ABUSE
        f = open("./bins.payloads", "rb")

        for line in f:
            print(f"Attempting {line}")
            self.assertFalse(Validate.is_lat(str(line)))


    def test_is_lng_happy(self):
        #HAPPY PATH
        for number in [-180, 90, 0, 95.5, 179.9]:
            self.assertTrue(Validate.is_lng(number))

    def test_is_lng_bad(self):
        #ABUSE
        f = open("./bins.payloads", "rb")

        for line in f:
            print(f"Attempting {line}")
            self.assertFalse(Validate.is_lng(str(line)))
    

    def test_is_domain_happy(self):
        #HAPPY
        li = ["Google.com", "Ya-hoo.com", "web.net", "happySite.org"]
        for string in li:
            self.assertTrue(Validate.is_domain(string))

    def test_is_domain_bad(self):
        #ABUSE
        f = open("./bins.payloads", "rb")

        for line in f:
            print(f"Attempting {line}")
            self.assertFalse(Validate.is_domain(str(line)))


    def test_is_url_happy(self):
        #HAPPY
        val_url = ["http://testing.com", "https://www.pct.edu/", "https://num-bers.org/one/two/three" ]
        for url in val_url:
            self.assertTrue(Validate.is_url(url))

    def test_is_url_bad(self):
        #ABUSE
        f = open("./bins.payloads", "rb")

        for line in f:
            print(f"Attempting {line}")
            self.assertFalse(Validate.is_url(str(line)))

    def test_grade_happy(self):
        #HAPPY
        cases = [(59, 'F'), (60, 'D'), (70, 'C'), (79, 'C'), (81, 'B'), (99, 'A'), (100, 'A')]
        for val, expected in cases:
            self.assertEqual(Validate.grade(val), expected, f"failed: {val}")


    def test_grade_bad (self):
        #ABUSE
        f = open("./bins.payloads", "rb")

        for line in f:
            line = line.strip()
            try:
                value = float(line)  
                print(f"Attempting {repr(line)}")
                self.assertIn(Validate.grade(value), {'A', 'B', 'C', 'D', 'F'})
            except ValueError:
                    with self.assertRaises(Exception, msg=f"invalid: {repr(line)}"):
                        Validate.grade(line)


    def test_sanitize_happy (self):
        #Happy
        cases = [("SELECT * FROM users", "SELECT * FROM USERS") ]
        for sql, expected in cases:
            self.assertEqual(Validate.sanitize(sql), expected, f"failed: {sql}")


    def test_sanitize_bad (self):
        #abuse
        with open("./bins.payloads", "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                san = Validate.sanitize(line)
                print(f"Attempting {repr(line)} -> {repr(san)}")

                for word in ["ADMIN", "OR", "COLLATE", "DROP", "AND", "UNION", "/*", "*/", "//", ";", "||", "&&", "--", "#", "=", "!=", "<>"]:
                    self.assertNotIn(word, san, f"failed: {repr(line)}")


    def test_strip_null_happy (self):
        #happy
        cases = [("Hello None World", "Hello  World"), ("There are None", "There are "), ("NoneNone", ""), ("Non", "Non"),]
        for text, expected in cases:
            self.assertEqual(Validate.strip_null(text), expected, f"Failed: {text}")


    def test_strip_null_bad (self):
        #abuse
        with open("./bins.payloads", "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                result = Validate.strip_null(line)
                print(f"Attempting {repr(line)} -> {repr(result)}")
                self.assertNotIn("None", result, f"'failed: {repr(line)}")


    def test_ip_happy (self):
        #happy
        cases = ["192.168.1.1", "10.0.0.255"]
        for i in cases:
            self.assertTrue(Validate.ip(i))


    def test_ip_bad (self):
        #abuse
        f = open("./bins.payloads", "rb")

        for line in f:
            print(f"Attempting {line}")
            self.assertFalse(Validate.ip(str(line)))


    def test_mac_happy (self):
        #happy
        cases = ["00:1A:2B:3C:4D:5E", "A1:B2:C3:D4:E5:F6", "aa:bb:cc:dd:ee:ff" ]
        for m in cases:
            self.assertTrue(Validate.mac(m))


    def test_mac_bad (self):
        #abuse
        f = open("./bins.payloads", "rb")

        for line in f:
            print(f"Attempting {line}")
            self.assertFalse(Validate.mac(str(line)))


    def test_md5_happy (self):
        #happy
        cases = ["d41d8cd98f00b204e9800998ecf8427e", "9e107d9d372bb6826bd81d3542a419d6", "098f6bcd4621d373cade4e832627b4f6" ]
        for m in cases:
            self.assertTrue(Validate.md5(m))


    def test_md5_bad (self):
        #abuse
        f = open("./bins.payloads", "rb")

        for line in f:
            print(f"Attempting {line}")
            self.assertFalse(Validate.md5(str(line)))



if __name__ == '__main__':
    unittest.main()
