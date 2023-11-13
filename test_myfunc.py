from myfunc import add_numbers, subtract_numbers, multiply_numbers, divide_numbers
import pytest

def test_add():
    assert add_numbers(1, 2) == 3
    assert add_numbers(-1, 1) == 0
    assert add_numbers(0, 0) == 0
    assert add_numbers(0, 0) == 0

@pytest.mark.parametrize("a, b, expected_result", [
    (6, 2, 3),
    (10, 2, 5),
    (-8, -4, 2),
    (1, 0.5, 2),
])
def test_division(a, b, expected_result):
    result = divide_numbers(a, b)
    assert result == expected_result

def test_division_by_zero():
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        divide_numbers(5, 0)




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

    




