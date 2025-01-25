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
        self.assertEqual(barret.to_10bint(), 231725314)

    def test_barrett_reduction_2(self):
        num1 = BigNumber([3546738466, 732342468, 423847294, 342384617], 2**32)
        print("\n", num1.value)
        num2 = BigNumber([42839473,32984712], 2**32)
        print("\n", num2.value)
        # print(num1.to_10bint(), num2.to_10bint())
        barret = Operations.BarrettReduction(num1, num2)
        self.assertEqual(barret.to_10bint(), 18159940178792610)

    # def test_shift_div(self):
    #     num = BigNumber([3546738466, 732342468, 423847294, 342384617], 2**32)
    #     self.assertEqual(Operations.bit_shift_div(num, 2).value, [3546738466, 732342468])

    # def test_gcd(self):
    #     num1 = BigNumber(4619837461356123846912184762983712389476157612739487679356128034719235786123497190283847, 2**32)
    #     # num2 = BigNumber(2134769827635128348712093758712347901283479568612938478, 2**32)
    #     num2 = BigNumber(21347698276351283487120937568612938473, 2**32)
    #     n = BigNumber(598127345618293475134, 2**32)
    #     self.assertEqual(Operations.gcd(num1, num2).to_10bint(), 1)
    
    # def test_mod_sum(self):
    #     num1 = BigNumber(4619837461356123846912184762983712389476157612739487679356128034719235786123497190283847, 2**32)
    #     num2 = BigNumber(2134769827635128348712093758712347901283479568612938478, 2**32)
    #     n = BigNumber(598127345618293475134, 2**32)
    #     self.assertEqual(Operations.module_sum(num1, num2, n).to_10bint(), 67495119264455811811)
    
    # def test_mod_sub(self):
    #     num1 = BigNumber(4619837461356123846912184762983712389476157612739487679356128034719235786123497190283847, 2**32)
    #     num2 = BigNumber(2134769827635128348712093758712347901283479568612938478, 2**32)
    #     n = BigNumber(598127345618293475134, 2**32)
    #     self.assertEqual(Operations.module_sub(num1, num2, n).to_10bint(), 168932874256972177767)
    
    # def test_mod_mul(self):
    #     num1 = BigNumber(4619837461356123846912184762983712389476157612739487679356128034719235786123497190283847, 2**32)
    #     num2 = BigNumber(2134769827635128348712093758712347901283479568612938478, 2**32)
    #     n = BigNumber(598127345618293475134, 2**32)
    #     self.assertEqual(Operations.module_mul(num1, num2, n).to_10bint(), 516672823612632166610)

    # def test_mod_squere(self):
    #     num1 = BigNumber(4619837461356123846912184762983712389476157612739487679356128034719235786123497190283847, 2**32)
    #     # num2 = BigNumber(2134769827635128348712093758712347901283479568612938478, 2**32)
    #     n = BigNumber(598127345618293475134, 2**32)
    #     self.assertEqual(Operations.module_power_two(num1, n).to_10bint(), 441637460045564998099)

    # def test_mod_power(self):
    #     num1 = BigNumber(4619837461356123846912184762983712389476157612739487679356128034719235786123497190283847, 2**32)
    #     num2 = BigNumber(2134769827635128348712093758712347901283479568612938478, 2**32)
    #     n = BigNumber(598127345618293475134, 2**32)
    #     self.assertEqual(Operations.module_power(num1, num2, n).to_10bint(), 156903068102560592065)



    
        
    


if __name__ == '__main__':
    try:
        unittest.main()
    except:
        print()