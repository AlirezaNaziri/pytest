from myfunc import add_numbers



def test_add():
    assert add_numbers(1, 2) == 3
    assert add_numbers(-1, 1) == 0
    assert add_numbers(0, 0) == 0






# import unittest
# class TestAddNumbers(unittest.TestCase):
#     def test_add_positive_numbers(self):
#         result =add_numbers(3,5)
#         self.assertEqual(result,8)

#     def test_add_negative_numbers(self):
#         result =add_numbers(-3,-4)
#         self.assertEqual(result,-7)

#     def test_add_mixed_numbers(self):
#         result =add_numbers(3,-5)
#         self.assertEqual(result,-2)

# if __name__ == '__main__':
#     unittest.main()

    




