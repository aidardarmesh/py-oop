class TestFactorize(unittest.TestCase):
    def test_wrong_types_raise_exception(self):
        """
        Test that float and string types raise exception
        """
        for x in 1.5, 'string':
            with self.subTest(x=x):
                self.assertRaises(TypeError, factorize, x)
    
    def test_negative(self):
        """
        Test that negative argument raises exception
        """
        for x in -1, -10, -100:
            with self.subTest(x=x):
                self.assertRaises(ValueError, factorize, x)
    
    def test_zero_and_one_cases(self):
        """
        Test that 0 and 1 gets factors (0,) and (1,)
        """
        for x, ans in (0, (0,)), (1, (1,)):
            with self.subTest(x=x):
                self.assertEqual(factorize(x), ans)
    
    def test_simple_numbers(self):
        """
        Test that factors of prime numbers are prime numbers itself in tuple
        """
        for x, ans in (3, (3,)), (13, (13,)), (29, (29,)):
            with self.subTest(x=x):
                self.assertEqual(factorize(x), ans)
    
    def test_two_simple_multipliers(self):
        """
        Test that even and squared numbers have exactly two factors in tuple
        """
        for x, ans in (6, (2,3)), (26, (2,13)), (121, (11,11)):
            with self.subTest(x=x):
                self.assertEqual(factorize(x), ans)
    
    def test_many_multipliers(self):
        """
        Test that factorize returns more than two factors in tuple
        """
        for x, ans in (1001, (7,11,13)), (9699690, (2,3,5,7,11,13,17,19)):
            with self.subTest(x=x):
                self.assertEqual(factorize(x), ans)