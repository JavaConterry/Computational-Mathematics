from BigNumber import BigNumber, Operations
import unittest


class TestLongBugNumbers(unittest.TestCase):

    def test_sum_1(self):
        num1 = BigNumber(981234719201243134124728461234123412933947812394871290834710942340, 2**32)
        num2 = BigNumber(2346198246328917468237641929879883809238409237436, 2**32)

        add = Operations.add(num1,num2)
        self.assertEqual(add.to_10b(), 981234719201243136470926707563040881171589742274755100073120179776)
    
    def test_sum_2(self):
        num1 = BigNumber(524526508, 2**32)
        num2 = BigNumber(3984900600, 2**32)

        add = Operations.add(num1,num2)
        self.assertEqual(add.to_10b(), 4509427108)

    def test_sum_3(self):
        num1 = BigNumber(1, 2**32)
        num2 = BigNumber(1, 2**32)

        add = Operations.add(num1,num2)
        self.assertEqual(add.to_10b(), 2)
        
    def test_sum_4(self):
        num1 = BigNumber(2**32, 2**32)
        num2 = BigNumber(2**32, 2**32)

        add = Operations.add(num1,num2)
        self.assertEqual(add.to_10b(), 8589934592)

    def test_sum_5(self):
        num1 = BigNumber(2**33, 2**32)
        num2 = BigNumber(2**33, 2**32)

        add = Operations.add(num1,num2)
        self.assertEqual(add.to_10b(), 17179869184)

    def test_sum_6(self):
        num1 = BigNumber(2**64 + 2**32 - 1, 2**32)
        num2 = BigNumber(2**128 + 2**16, 2**32)

        add = Operations.add(num1,num2)
        self.assertEqual(add.to_10b(), 340282366920938463481821351509772795903)
    
    def test_sum_7(self):
        num1 = BigNumber(2**128, 2**32)
        num2 = BigNumber(1, 2**32)

        add = Operations.add(num1,num2)
        self.assertEqual(add.to_10b(), 340282366920938463463374607431768211457)


    def test_sub_1(self):
        num1 = BigNumber(981234719201243134124728461234123412933947812394871290834710942340, 2**32)
        num2 = BigNumber(2346198246328917468237641929879883809238409237436, 2**32)
        sub = Operations.sub(num1,num2)
        self.assertEqual(sub.to_10b(), 981234719201243131778530214905205944696305882514987481596301704904)
    
    def test_sub_2(self):
        num1 = BigNumber(9812347192012431341247284612394871290834710942340, 2**32)
        num2 = BigNumber(9812347192012431341247284612394852384728934729834, 2**32)
        sub = Operations.sub(num1,num2)
        self.assertEqual(sub.to_10b(), 18906105776212506)
    
    def test_sub_3(self):
        num1 = BigNumber(21348719283756712983419236441298374, 2**32)
        num2 = BigNumber(72394872384729384729834729384729, 2**32)
        sub = Operations.sub(num1,num2)
        self.assertEqual(sub.to_10b(), 21276324411371983598689401711913645)
    
    def test_sub_4(self):
        num1 = BigNumber(72134932562394871764531859749865729034, 2**32)
        num2 = BigNumber(5786278384712835463287461628347197234, 2**32)
        sub = Operations.sub(num1,num2)
        self.assertEqual(sub.to_10b(), 66348654177682036301244398121518531800)
    
    def test_sub_5(self):
        num1 = BigNumber(399579347146422797009697964653308466854, 2**32)
        num2 = BigNumber(100175957659691278902986257890128252949, 2**32)
        sub = Operations.sub(num1,num2)
        self.assertEqual(sub.to_10b(), 299403389486731518106711706763180213905)
    
    def test_sub_6(self):
        num1 = BigNumber(299403389486731518106711706763180213905, 2**32)
        num2 = BigNumber(84843000392746500277345932137348090994, 2**32)
        sub = Operations.sub(num1,num2)
        self.assertEqual(sub.to_10b(), 214560389093985017829365774625832122911)

    def test_mult_1(self):
        num1 = BigNumber(981234719201243134124728461234123412933947812394871290834710942340, 2**32)
        num2 = BigNumber(2346198246328917468237641929879883809238409237436, 2**32)
        mul = Operations.multiply(num1,num2)
        self.assertEqual(mul.to_10b(), 2302171177427004401889527047438598728509002965146275378314198208827002105483760524449559280585370984742764365440240)

    def test_mul_2(self):
        num1 = BigNumber(2918347190283471567239048791283567129034768578761273948717982356129034817983561723948717928356128934719561289374, 2**32)
        num2 = BigNumber(4709123956767329048177953671230948756792347827356092347190825762736471290834712567, 2**32)
        mul = Operations.multiply(num1,num2)
        self.assertEqual(mul.to_10b(), 13742858667928518959903291125948365205411663302791247646208616300010737655948270943404663144279028333704727788269892050095408546430317558753853850355897924922387934424803617290073501427201363058)
    
    def test_mul_3(self):
        num1 = BigNumber(4527, 8)
        num2 = BigNumber(9873, 8)
        mul = Operations.multiply(num1,num2)
        self.assertEqual(mul.to_10b(), 44695071)



    def test_div_1(self):
        num1 = BigNumber(981234719201243134124728461234123412933947812394871290834710942340, 2**32)
        num2 = BigNumber(2346198246328917468237641929879883809238409237436, 2**32)
        div, rem = Operations.div(num1,num2)
        self.assertEqual(div.to_10b(), 418223277055370449)

    def test_div_2(self):
        num1 = BigNumber(2918347190283471567239048791283567129034768578761273948717982356129034817983561723948717928356128934719561289374, 2**32)
        num2 = BigNumber(4709123956767329048177953671230948756792347827356092347190825762736471290834712567, 2**32)
        div, rem = Operations.div(num1,num2)
        self.assertEqual(div.to_10b(), 619721888205896477070134280916)


    def test_rem_1(self):
        num1 = BigNumber(981234719201243134124728461234123412933947812394871290834710942340, 2**32)
        num2 = BigNumber(2346198246328917468237641929879883809238409237436, 2**32)
        div, rem = Operations.div(num1,num2)
        self.assertEqual(rem.to_10b(), 353593676666892717496341744261955225540132013576)

    def test_rem_2(self):
        num1 = BigNumber(2918347190283471567239048791283567129034768578761273948717982356129034817983561723948717928356128934719561289374, 2**32)
        num2 = BigNumber(4709123956767329048177953671230948756792347827356092347190825762736471290834712567, 2**32)
        div, rem = Operations.div(num1,num2)
        self.assertEqual(rem.to_10b(), 3056752573856112239245181233193790722461659480060293872083113231608421467818002)


if __name__ == '__main__':
    unittest.main()