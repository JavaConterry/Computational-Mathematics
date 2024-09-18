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
            print(f'list {value} was given')
            if(all(v==0 for v in value)):
                print('its all zero')
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
    
    # def to_10b(a, base):
    #     val = 0
    #     for i in range(len(a)):
    #         val+=a[i]*(base**i)
    #     return val


    def len(self):
        return len(self.value)


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
        # print(f'sub: value1={a.value}, value2={b.value}')

        len_diff = a.len() - b.len()
        for i in range(b.len()):
            temp = a.value[i]-b.value[i]-borrow
            if(temp>=0):
                return_value.value.append(temp)
                borrow=0
            else:
                return_value.value.append(base + temp)
                borrow=1
        if(len_diff>=1):
            return_value.value.append(a.value[b.len()]-borrow)
        if(len_diff>1):
            return_value.value.extend(a.value[b.len()+1:])


        # print('return_value: ', return_value.value)
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
    

    # def multiply(value1, value2):
    #     ret = BigNumber(value=0)
    #     for i in range(max(value1.length, value2.length)):
    #         temp = BigNumber.one_digit_multiplication(value1, value2.value[i])
    #         shifted_temp = BigNumber.shift(temp, i)
    #         ret = BigNumber.add(ret, shifted_temp)

    #     ret.length = len(ret.value)
    #     return ret


    def sort(a, b):
        # print(f'given to sort: a{a.value}, b{b.value}')
        if(a.len()>b.len()):
            return a, b
        elif(a.len()==b.len()):
            if(a.value[a.len()-1]>=b.value[b.len()-1]):
                return a, b
            else:
                return b, a
        else: return b, a


    # def multiply(a, b):
    #     # print(f'given a:{a.value}, b:{b.value}')
    #     if(type(a) != BigNumber or type(b) != BigNumber):
    #         print(f'{type(a)} and {type(b)} was given instead of BigNumbers')
    #         print(f'values: a:{a.value}, b:{b.value}')
    #         return 
    #     a, b = BigNumber(a.value, a.base), BigNumber(b.value, b.base)
    #     base = a.base
    #     al = a.len()
    #     bl = b.len()
    #     print(f'multiplication: a={a.value}, length={al}')
    #     print(f'multiplication: b={b.value}, length={bl}')
    #     if(al == 1 or bl == 1):
    #         a, b = Operations.sort(a, b)
    #         return Operations.one_digit_multiplication(a, b.value[0])
        

    #     A1, A0 = BigNumber(value=a.value[al//2:], base=a.base), BigNumber(value=a.value[:al//2], base=a.base)
    #     B1, B0 = BigNumber(value = b.value[bl//2:], base = b.base), BigNumber(value=b.value[:bl//2], base=b.base)
    #     print(f'multiplication: A1={A1.value}, A0={A0.value}')
    #     print(f'multiplication: B1={B1.value}, B0={B0.value}')
    #     # if(A1.value==[0]):
    #     #     return
    #     A1B1 = Operations.multiply(A1, B1)
    #     print(f'A1B1 multiplication result: {A1B1.to_10b()}, had to be: {A1.to_10b()*B1.to_10b()}')
    #     A1A0B0B1 = Operations.multiply(Operations.sub(A1,A0), Operations.sub(B0,B1))
    #     print(f'A1A0B0B1 multiplication result: {A1A0B0B1.to_10b()}, had to be: {(Operations.sub(A1,A0)).to_10b()*(Operations.sub(B0,B1)).to_10b()}')
    #     A0B0 = Operations.multiply(A0,B0)
    #     print(f'A0B0 multiplication result: {A0B0.to_10b()}, had to be: {A0.to_10b()*B0.to_10b()}')

    #     first_addition = Operations.multiply(A1B1, BigNumber(base = base, value=(base**al*2 + base**al)))
    #     print(f'Values of a second addition multiplication: A1A0B0B1={A1A0B0B1.value}, b^n={BigNumber(base**al, base).value}')
    #     secend_addition = Operations.shift(A1A0B0B1, al)
    #     third_addition = Operations.multiply(A0B0, BigNumber(base**al+1, A0B0.base))
        
    #     return Operations.add(
    #         Operations.add(first_addition, secend_addition), 
    #         third_addition)
    
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


    def shift(value, i):
        value = BigNumber(value.value, value.base)
        res = BigNumber(base = value.base)
        for j in range(i):
            res.value.append(0)
        for j in range(value.len()):
            res.value.append(value.value[j])
        return res