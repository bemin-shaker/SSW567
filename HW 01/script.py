import unittest


def classify_triangle(a, b, c):
    if (c ** 2 == (a ** 2 + b ** 2)):
        return "Right"
    elif (a == b == c):
        return "Equilateral"
    elif ((a == b and b != c) or (a == c and c != b) or (b == c and a != b)):
        return "Isosceles"
    elif (a != b and b != c and a != c):
        return "Scalene"


class TestTriangles(unittest.TestCase):
    def testSet1(self):
        self.assertEqual(classify_triangle(3, 4, 5), 'Right',
                         '3,4,5 is a Right triangle')
        self.assertEqual(classify_triangle(10, 10, 5), 'Isosceles',
                         '10,10,5 is an Isosceles triangle')
        self.assertEqual(classify_triangle(1, 2, 3), 'Scalene',
                         '1,2,3 is an Scalene triangle')

    def testSet2(self):
        self.assertEqual(classify_triangle(1, 1, 1),
                         'Equilateral', '1,1,1 should be equilateral')
        self.assertEqual(classify_triangle(10, 10, 10),
                         'Equilateral', '10,10,10 should be equilateral')


classify_triangle(9, 3, 6)

if __name__ == '__main__':
    classify_triangle(1, 2, 3)
    classify_triangle(1, 1, 1)

    unittest.main(exit=True)
