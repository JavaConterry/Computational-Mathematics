import math

class BigNumber:
    def __init__(self, value=None, base=2**32):
        self.base = base
                    
        val = []
        if(value == None):
            self.value = []
            self.length = 0
            return
        if(value == 0):
            self.value = [0]
            self.length = 1
            return
        if(type(value) == list):
            if(all(v==0 for v in value)):
                self.value = [0]    
            else:
                i= len(value)-1
                while value[i]==0 and i>=0:
                    i-=1
                self.value = value[:i+1]
            return
        
        while value!=0:
            val.append(value%base)
            value //= base

        self.value = val
        self.length = len(self.value)


    def to_10b(self):
        val = 0
        for i in range(len(self.value)):
            val+=self.value[i]*(self.base**i)
        return val


    def from_2b(value, base):
        val = 0
        for i in range(len(value)):
            val+=value[i]*(2**i)
        return BigNumber(val, base)


    def to_2b(self):
        result = []
        for i in range(len(self.value)):
            val = self.value[i]
            bin2add = BigNumber(val, base=2).value
            if(len(bin2add) < self.base and i<len(self.value)-1): # fill with zeros between β bits
                bin2add.extend([0]*(int(math.log2(self.base))-len(bin2add))) 
            result.extend(bin2add)
        return result
        # return (BigNumber.from_2b(result, base=self.base)).value


    def len(self):
        return len(self.value)


    def bit_len(a):
        return len(a.to_2b())


    def isBiggerOrEqThan(self, b):
        if(self.len()>b.len()):
            return True
        elif(self.len()==b.len()):
            i = self.len()-1
            while(self.value[i]==b.value[i] and i>0):
                i-=1
            if(self.value[i]>=b.value[i]):
                return True
            else:
                return False
        else: return False

    
    def isSmallerThan(self, b):
        return not self.isBiggerOrEqThan(b)



class Operations:
    def add(a, b):
        if(type(a) != BigNumber or type(b) != BigNumber):
            print('Unable to add not BigNumbers')
            return
        
        a, b = Operations.sort(a, b)

        b.value.extend([0]*(a.len()-b.len()))

        base = a.base
        carry = 0
        return_value = BigNumber(base=a.base)
        for i in range(b.len()):
            temp = a.value[i]+b.value[i]+carry
            return_value.value.append(temp & (base - 1))
            carry = temp >> int(math.log2(base))

        if(carry==1):
            return_value.value.append(carry)
        return_value.length = len(return_value.value)
        return return_value
    

    def sub(a, b):
        if(type(a) != BigNumber or type(b) != BigNumber):
            print('Unable to substract not BigNumbers')
            return
        
        a, b = Operations.sort(a, b)
        diff = a.to_10b() - b.to_10b()
        base = a.base
        borrow = 0
        return_value = BigNumber(base=a.base)

        i=0
        while(i<b.len() or borrow == 1):
            if i>=b.len():  bval = 0 
            else:           bval = b.value[i]
            temp = a.value[i]-bval-borrow
            if(temp>=0):
                return_value.value.append(temp)
                borrow=0
            else:
                return_value.value.append(base + temp)
                borrow=1
            i+=1
        # if(len_diff>=1):
            # return_value.value.append(a.value[b.len()]-borrow)
        if(a.len()-i>=1):
            return_value.value.extend(a.value[i:])

        return_value.length = len(return_value.value)
        return return_value
    

    def one_digit_multiplication(value, b):
        base = value.base
        ret = BigNumber(base=base)
        carry = 0
        for i in range(value.len()):
            temp = value.value[i]*b + carry
            ret.value.append(temp & (base-1))
            carry = temp >> int(math.log2(base))
        ret.value.append(carry)
        ret.length = len(ret.value)
        return ret
    

    def sort(a, b):
        a, b = BigNumber(a.value, a.base),BigNumber(b.value, b.base)
        if(a.isBiggerOrEqThan(b)):
            return a, b
        else:
            return b, a


    def multiply_karatzuba(a, b):
        #TODO Won't work until signed numbers are realized
        if(type(a) != BigNumber or type(b) != BigNumber):
            print('Only BigNumber types are allowed for multiplication.')
            return

        base = a.base
        al = a.len()
        bl = b.len()
        
        if al == 1 or bl == 1:
            result = Operations.one_digit_multiplication(a, b.value[0])
            return result

        mid = min(al, bl) // 2
        A1, A0 = BigNumber(value=a.value[mid:], base=a.base), BigNumber(value=a.value[:mid], base=a.base)
        B1, B0 = BigNumber(value=b.value[mid:], base=b.base), BigNumber(value=b.value[:mid], base=b.base)
        
        A1B1 = Operations.multiply_karatzuba(A1, B1)
        print(f"A1 * B1 = {A1B1.to_10b()}, ::: Had to be {A1.to_10b() * B1.to_10b()}")

        A0B0 = Operations.multiply_karatzuba(A0, B0)
        print(f"A0 * B0 = {A0B0.to_10b()}, ::: Had to be {A0.to_10b() * B0.to_10b()}")

        A1pA0mB1pB0 = Operations.multiply_karatzuba(Operations.add(A1, A0), Operations.add(B1, B0))
        middle_term = Operations.sub(
            Operations.sub(
                A1pA0mB1pB0,
                A1B1
            ), A0B0
        )

        v1,v0,k1,k0 = A1.to_10b(),A0.to_10b(),B1.to_10b(),B0.to_10b()
        print(f"Middle term = {middle_term.to_10b()}, ::: Had to be {((v1+v0)*(k1+k0))-(v1*k1)-(v0*k0)}")

        A1B1_shifted = Operations.shift(A1B1, 2 * mid)
        # print(f"A1B1 shifted = {A1B1_shifted}")

        middle_term_shifted = Operations.shift(middle_term, mid)
        # print(f"Middle term shifted = {middle_term_shifted}")

        result = Operations.add(Operations.add(A1B1_shifted, middle_term_shifted), A0B0)
        print(f"Final result = {result.to_10b()}, ::: Had to be {A1B1_shifted.to_10b() + middle_term_shifted.to_10b() + A0B0.to_10b()}")
        
        return result

    def equalize_length(a,b):
        if(not b.isSmallerThan(a)):
            a, b = Operations.sort()
        b.value.extend([0]*(a.len()-b.len()))
        return a,b


    def multiply(a, b):
        a, b = Operations.sort(a,b)
        # a, b = Operations.equalize_length(a,b)
        c = BigNumber(0, a.base); n = b.len()
        for i in range(n):
            temp = Operations.one_digit_multiplication(a, b.value[i])
            temp = Operations.shift(temp, i)
            c = Operations.add(c, temp)
        return c

    def squere_pow(a):
        return Operations.multiply(a, a)


    def shift(value, i):
        value = BigNumber(value.value, value.base)
        res = BigNumber(base = value.base)
        for j in range(i):
            res.value.append(0)
        for j in range(value.len()):
            res.value.append(value.value[j])
        return res


    def div(a, b):
        if not (isinstance(a, BigNumber) and isinstance(b, BigNumber)):
            print("Only BigNumber types are allowed for division.")
            return

        if b.to_10b() == 0:
            print("Cannot divide by zero.")
            return

        a, b = Operations.sort(a, b)
        k = b.bit_len()
        R = BigNumber(a.value, a.base)
        Q = BigNumber(0, a.base)

        while R.isBiggerOrEqThan(b):
            t = R.bit_len()
            C = Operations.bit_shift_to_high(b, t - k)
            
            if R.isSmallerThan(C):
                t -= 1
                C = Operations.bit_shift_to_high(b, t - k)
                
            R = Operations.sub(R, C)
            Q = Operations.add(Q, BigNumber(2**(t - k), a.base))

            print(f'Updated R (remainder): {R.to_10b()}; Updated Q (quotient): {Q.to_10b()}; b is {b.to_10b()}')

        return Q, R  # Return the quotient and remainder



    def bit_shift_to_high(big_number, n):
        if not isinstance(big_number, BigNumber):
            print('Only BigNumber types are allowed for Operations.bit_shift_to_high.')
            return

        bit_number = big_number.to_2b()
        # print(f'Given binary: {bit_number}')

        # Shift the binary number left by `n` positions
        shifted = [0] * n + bit_number
        # print(f'Resulted binary after {n} shifts to high: {shifted}')
        
        # Convert back to BigNumber
        return BigNumber.from_2b(shifted, big_number.base)