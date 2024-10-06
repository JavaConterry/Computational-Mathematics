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
    

    def to_2b(self):
        result = []
        for val in self.value:
            result.extend(BigNumber(val, base=2).value)
        return result


    def from_2b(value, base):
        val = 0
        for i in range(len(value)):
            val+=value[i]*(2**i)
        return BigNumber(val, base)


    def len(self):
        return len(self.value)


    def bit_len(a):
        return len(a.to_2b())


    def isBiggerOrEqThan(self, b):
        if(self.len()>b.len()):
            return True
        elif(self.len()==b.len()):
            if(self.value[self.len()-1]>=b.value[b.len()-1]):
                return True
            else:
                return False
        else: return False

    
    def isSmallerThan(self, b):
        if(self.len()>b.len()):
            return False
        elif(self.len()==b.len()):
            if(self.value[self.len()-1]<b.value[b.len()-1]):
                return True
            else:
                return False
        else: return True



class Operations:
    def add(a, b):
        if(type(a) != BigNumber or type(b) != BigNumber):
            print('Unable to add not BigNumbers')
            return
        
        a, b = Operations.sort(a, b)

        base = a.base
        carry = 0
        return_value = BigNumber(base=a.base)
        for i in range(b.len()):
            temp = a.value[i]+b.value[i]+carry
            return_value.value.append(temp & (base - 1))
            carry = temp >> int(math.log2(base))


        len_diff = a.len() - b.len()
        if(len_diff>=1):
            return_value.value.append(a.value[b.len()]+carry)
        if(len_diff>1):
            return_value.value.extend(a.value[b.len()+1:])

        return_value.length = len(return_value.value)
        return return_value
    

    def sub(a, b):
        if(type(a) != BigNumber or type(b) != BigNumber):
            print('Unable to substract not BigNumbers')
            return
        
        a, b = Operations.sort(a, b)

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
        if(a.len()-i>1):
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
        if(a.len()>b.len()):
            return a, b
        elif(a.len()==b.len()):
            if(a.value[a.len()-1]>=b.value[b.len()-1]):
                return a, b
            else:
                return b, a
        else: return b, a


    def multiply(a, b):
        if(type(a) != BigNumber or type(b) != BigNumber):
            print('Only BigNumber types are allowed for multiplication.')
            return

        base = a.base
        al = a.len()
        bl = b.len()
        
        if al == 1 or bl == 1:
            return Operations.one_digit_multiplication(a, b.value[0])

        mid = min(al, bl) // 2
        A1, A0 = BigNumber(value=a.value[mid:], base=a.base), BigNumber(value=a.value[:mid], base=a.base)
        B1, B0 = BigNumber(value=b.value[mid:], base=b.base), BigNumber(value=b.value[:mid], base=b.base)
        
        A1B1 = Operations.multiply(A1, B1)
        A0B0 = Operations.multiply(A0, B0)

        middle_term = Operations.sub(
            Operations.sub(
                Operations.multiply(Operations.add(A1, A0), Operations.add(B1, B0)),
                A1B1
            ), A0B0
        )

        A1B1_shifted = Operations.shift(A1B1, 2 * mid)
        middle_term_shifted = Operations.shift(middle_term, mid)

        result = Operations.add(Operations.add(A1B1_shifted, middle_term_shifted), A0B0)
        return result
    

    def squere_pow(a):
        return Operations.multiply(a, a)


    # def div(a, b):
    #     a, b = Operations.sort(a, b)
    #     k = b.len()
    #     R = BigNumber(a.value, a.base)
    #     Q = BigNumber(0, a.base)
    #     while R.isBiggerOrEqThan(b):
    #         t = R.len()
    #         # C = Operations.shift(b, t-k)
    #         C = Operations.bit_shift_to_high(b, t-k)
    #         print(f'C before second shift {C.value}')
    #         if(R.isSmallerThan(C)):
    #             print('too high')
    #             t = t-1
    #             # C = Operations.shift(b, t-k)
    #         C = Operations.bit_shift_to_high(b, t-k)
    #         print(f'C after second shift {C.value}')
    #         R = Operations.sub(R, C)
    #         Q = Operations.add(Q, BigNumber(2**(t-k), a.base))
    #         print(f'current R {R.value}; b {b.value}')
    #     return Q, R
    

    # def bit_shift_to_high(big_number, n):
    #     if(type(big_number) != BigNumber):
    #         print('Only BigNumber types are allowed for Operations.bit_shift_to_high.')
    #         return
    #     bit_number = big_number.to_2b()
    #     print(f'given binary: {bit_number}')
    #     shifted = [0 for _ in range(n)]
    #     shifted.extend(bit_number)
    #     print(f'resulted binary after {n} shift to high: {shifted}')
    #     # print(type(bit_number))
    #     return BigNumber.from_2b(bit_number, big_number.base)


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
        # k = b.len()
        k = b.bit_len()
        R = BigNumber(a.value, a.base)  # R is the remainder, initially a
        Q = BigNumber(0, a.base)        # Q is the quotient, initially 0

        while R.isBiggerOrEqThan(b):
            # t = R.len()
            t = R.bit_len()
            # Shift divisor `b` left by (t - k) positions
            C = Operations.bit_shift_to_high(b, t - k)
            # print(f'C before adjustment: {C.value}')
            
            # If `R` is smaller than `C`, reduce the shift amount
            if R.isSmallerThan(C):
                t -= 1
                C = Operations.bit_shift_to_high(b, t - k)
            
            # print(f'C after adjustment: {C.value}')
            R = Operations.sub(R, C)
            Q = Operations.add(Q, BigNumber(2**(t - k), a.base))
            print(f'Updated R (remainder): {R.value}; Updated Q (quotient): {Q.value}')
        
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