import math, copy

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
        # val.extend([0 for i in range(32-len(val))])

        self.value = val
        self.length = len(self.value)


    def to_10bint(self):
        val = 0
        for i in range(len(self.value)):
            val+=self.value[i]*(self.base**i)
        return val


    def from_2b(value, base):
        val = 0
        for i in range(len(value)):
            val+=int(value[i])*(2**i)
        return BigNumber(val, base)
    

    def from_16b(value, base):
        if not isinstance(value, str):
            return
        val = 0
        for i in range(len(value)):
            if value[i] in {'a', 'b', 'c', 'd', 'e', 'f'}:
                val+=(10 + ord(value[i]) - ord('a'))*(16**(len(value)-1-i))
            else:    
                val+=int(value[i])*(16**(len(value)-1-i))
        return BigNumber(val, base)
    

    def to_16b(value):
        val = BigNumber(value.to_10bint(), 16)
        s = ''
        for i in range(len(val.value)):
            v = val.value[(len(val.value)-1-i)]
            if(v>=10):
                s+=chr(v+ord('a')-10)
            else:
                s+=str(v)
        return s

    def to_2b(self):
        if(math.log2(self.base)%2 != 0):
            print('Not Supported for such value base')
            return
        result = []
        for i in range(len(self.value)):
            val = self.value[i]
            bin2add = BigNumber(val, base=2).value
            if(len(bin2add) < self.base and i<len(self.value)-1): # fill with zeros between β bits
                bin2add.extend([0]*abs((int(math.log2(self.base))-len(bin2add))))
            result.extend(bin2add)
        return result
        # return (BigNumber.from_2b(result, base=self.base)).value

    def print_2b(self):
        val = self.to_2b()
        return ''.join(map(str, reversed(val)))

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
    
    def isEven(self):
        b2 = self.to_2b()
        if b2 ==0:
            return True
        return False
    
    def isZero(self):
        for i in self.value:
            if i!=0:
                return False
        return True



class Operations:
    def add(a, b):
        if(type(a) != BigNumber or type(b) != BigNumber):
            print('Unable to add not BigNumbers')
            return
        
        a, b = Operations.sort(a, b)

        b.value.extend([0]*abs((a.len()-b.len())))

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
        a, b = Operations.equalize_length(a,b)
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
    

    def __isBigNumberInput(a,b):
        if(type(a) != BigNumber or type(b) != BigNumber):
            return False
        return True


    def equalize_length(a,b):
        lena, lenb = len(a.value), len(b.value)
        if lena > lenb:
            b.value = b.value + [0]*(abs(lena-lenb))
        elif lena < lenb:
            a.value = a.value + [0]*(abs(lena-lenb))
        return a,b


    def long_comparison(a, b):
        ac, bc = copy.deepcopy(a),copy.deepcopy(b)
        if(not Operations.__isBigNumberInput(ac,bc)):
            print('Not BigNumbers are given as input')
            return
        
        ac,bc = Operations.equalize_length(ac,bc)
        i = ac.len() -1
        while(i>=0 and ac.value[i] == bc.value[i]):
            i-=1
        if(i==-1):
            return 0
        else:
            if(ac.value[i]>bc.value[i]):
                return 1
            else:
                return -1
        

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
        # print(f"A1 * B1 = {A1B1.to_10bint()}, ::: Had to be {A1.to_10bint() * B1.to_10bint()}")

        A0B0 = Operations.multiply_karatzuba(A0, B0)
        # print(f"A0 * B0 = {A0B0.to_10b()}, ::: Had to be {A0.to_10bint() * B0.to_10bint()}")

        A1pA0mB1pB0 = Operations.multiply_karatzuba(Operations.add(A1, A0), Operations.add(B1, B0))
        middle_term = Operations.sub(
            Operations.sub(
                A1pA0mB1pB0,
                A1B1
            ), A0B0
        )

        v1,v0,k1,k0 = A1.to_10bint(),A0.to_10bint(),B1.to_10bint(),B0.to_10bint()
        # print(f"Middle term = {middle_term.to_10bint()}, ::: Had to be {((v1+v0)*(k1+k0))-(v1*k1)-(v0*k0)}")

        A1B1_shifted = Operations.shift(A1B1, 2 * mid)
        # print(f"A1B1 shifted = {A1B1_shifted}")

        middle_term_shifted = Operations.shift(middle_term, mid)
        # print(f"Middle term shifted = {middle_term_shifted}")

        result = Operations.add(Operations.add(A1B1_shifted, middle_term_shifted), A0B0)
        # print(f"Final result = {result.to_10bint()}, ::: Had to be {A1B1_shifted.to_10bint() + middle_term_shifted.to_10bint() + A0B0.to_10b()}")
        
        return result

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

        if b.to_10bint() == 0:
            print("Cannot divide by zero.")
            return

        # a, b = Operations.sort(a, b)
        k = b.bit_len()
        R = BigNumber(a.value, a.base)
        Q = BigNumber(0, a.base)

        while(Operations.long_comparison(R, b) >= 0):
            t = R.bit_len()
            C = Operations.bit_shift_to_high(b, t - k)
            
            if(Operations.long_comparison(R, C) < 0):
                t -= 1
                C = Operations.bit_shift_to_high(b, t - k)

            R = BigNumber(Operations.sub(R, C).value, a.base)
            Q = BigNumber(Operations.add(Q, BigNumber(2**(t - k), a.base)).value,a.base)

        return Q, R  # Return the quotient and remainder



    def bit_shift_to_high(big_number, n):
        if not isinstance(big_number, BigNumber):
            print('Only BigNumber types are allowed for Operations.bit_shift_to_high.')
            return

        bit_number = big_number.to_2b()
        shifted = [0] * abs(n) + bit_number

        return BigNumber.from_2b(shifted, big_number.base)
    

    def power(a, b):
        C = BigNumber(1, a.base)
        D = []
        D.append(BigNumber(1, a.base))
        D.append(a)

        for i in range(2, b.base-1):
            D.append(Operations.multiply(D[len(D)-1], a))
        for i in range(b.len()-1, 0):
            C = Operations.multiply(C, D[b.value[i]])
            if i!=0:
                for k in range(1, math.log2(a.base)):
                    C = Operations.multiply(C, C)
        return C



    def min(a,b):
        if Operations.long_comparison(a,b)<1:
            return a
        return b


    #gcd - НСД
    # Using Stein algorithm
    def gcd(a,b):
        if not (isinstance(a, BigNumber) and isinstance(b, BigNumber)):
            print('Only BigNumber types are allowed.')
            return
        
        two = BigNumber(2, a.base)
        d = BigNumber(1, a.base)
        while(a.isEven() and b.isEven()):
            a = Operations.div(a,two)[0]
            b = Operations.div(b,two)[0]
            d = Operations.multiply(d, two)
        while(a.isEven()):
            a = Operations.div(a,two)[0]
        while(not b.isZero()):
            while(b.isEven()):
                b = Operations.div(b,two)[0]
            a,b = Operations.min(a,b), Operations.sub(a,b)
        d = Operations.multiply(d,a)
        return d
    

    def BarrettReduction(x :BigNumber,n :BigNumber):
        if(x.len() != n.len()*2):
            print('Barrett reduction requires to have 2k=|x|=2|n|')
        k = x.len()//2
        mue = Operations.div(BigNumber(x.base**(2*k)),n)[0]
        q = BigNumber(x.value[:k+1], x.base)
        q = Operations.multiply(q, mue)
        print('qmue:', q.to_10bint())
        q.value = q.value[:q.len()-(k+1)]
        print('qcut:', q.to_10bint())
        print('x', x.to_10bint())
        print('q*n', Operations.multiply(q,n).to_10bint())
        r = Operations.sub(x, Operations.multiply(q,n))
        print(r.value)
        while(Operations.long_comparison(r,n)>=0):
            r = Operations.sub(r,n)
        return r
    

    def module_sum(a,b,n):
        a = Operations.BarrettReduction(a,n)
        b = Operations.BarrettReduction(b,n)
        return Operations.add(a,b)
    
    def module_sub(a,b,n):
        a = Operations.BarrettReduction(a,n)
        b = Operations.BarrettReduction(b,n)
        return Operations.sub(a,b)
    
    