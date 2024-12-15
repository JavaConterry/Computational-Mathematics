from BigNumber import BigNumber, Operations
import unittest


class TestLongBigNumbers_Lab2(unittest.TestCase):

    def test_gcd_1(self):
        num1 = BigNumber(5, 2**32)
        num2 = BigNumber(1, 2**32)
        gcd = Operations.gcd(num1, num2)
        self.assertEqual(gcd.to_10bint(), 1)
    def test_gcd_2(self):
        num1 = BigNumber(213471234817623412, 2**32)
        num2 = BigNumber(23412341341234, 2**32)
        gcd = Operations.gcd(num1, num2)
        self.assertEqual(gcd.to_10bint(), 2)

    def test_barrett_reduction(self):
        num1 = BigNumber([3546738466, 732342468], 2**32)
        num2 = BigNumber([473264528], 2**32)
        # print(num1.to_10bint(), num2.to_10bint())
        barret = Operations.BarrettReduction(num1, num2)
        self.assertEqual(barret.to_10bint(), 448079218)
    # def test_barrett_reduction_2(self):
    #     num1 = BigNumber(234712461283416234, 2**32)
    #     num2 = BigNumber(473264528, 2**32)
    #     # print(num1.to_10bint(), num2.to_10bint())
    #     barret = Operations.BarrettReduction(num1, num2)
    #     self.assertEqual(barret.to_10bint(), 47158042)




if __name__ == '__main__':
    try:
        unittest.main()
    except:
        print()