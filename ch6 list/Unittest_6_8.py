import Lists_upgrade_6_8
import unittest


class KnownValues(unittest.TestCase):
    knownValues = ((0, 'zero'),
                   (1, 'one'),
                   (2, 'two'),
                   (3, 'three'),
                   (4, 'four'),
                   (5, 'five'),
                   (6, 'six'),
                   (7, 'seven'),
                   (8, 'eight'),
                   (9, 'nine'),
                   (10, 'ten'),
                   (11, 'eleven'),
                   (12, 'twelve'),
                   (13, 'thirteen'),
                   (14, 'fourteen'),
                   (15, 'fifteen'),
                   (16, 'sixteen'),
                   (17, 'seventeen'),
                   (18, 'eighteen'),
                   (19, 'nineteen'),
                   (20, 'twenty'),
                   (30, 'thirty'),
                   (40, 'forty'),
                   (50, 'fifty'),
                   (51, 'fifty-one'),
                   (52, 'fifty-two'),
                   (60, 'sixty'),
                   (70, 'seventy'),
                   (80, 'eighty'),
                   (90, 'ninety'),
                   (100, 'one-hundred'),
                   (101, 'one-hundred and one'),
                   (109, 'one-hundred and nine'),
                   (110, 'one-hundred and ten'),
                   (211, 'two-hundred and eleven'),
                   (212, 'two-hundred and twelve'),
                   (213, 'two-hundred and thirteen'),
                   (214, 'two-hundred and fourteen'),
                   (215, 'two-hundred and fifteen'),
                   (216, 'two-hundred and sixteen'),
                   (217, 'two-hundred and seventeen'),
                   (218, 'two-hundred and eighteen'),
                   (219, 'two-hundred and nineteen'),
                   (220, 'two-hundred and twenty'),
                   (323, 'three-hundred and twenty-three'),
                   (334, 'three-hundred and thirty-four'),
                   (345, 'three-hundred and forty-five'),
                   (367, 'three-hundred and sixty-seven'),
                   (985, 'nine-hundred and eighty-five'),
                   (999, 'nine-hundred and ninety-nine'))

    def test_digitToStr_knownValues(self):
        '''digitToStr should give known result with known input'''
        for integer, spelling in self.knownValues:
            result = Lists_upgrade_6_8.digitToStr(integer)
            self.assertEqual(spelling, result)

if __name__ == '__main__':
    unittest.main()
