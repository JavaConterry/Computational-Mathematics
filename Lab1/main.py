from BigNumber import BigNumber, Operations

num1 = BigNumber([0,0,3], 2**32)
# print('\n', num1.value)
# print('\n', num1.to_10b())

num2 = BigNumber([0,2], 2**32)
# add = Operations.add(num1,num2)
# print('addition result: ', add.to_10b())
# sub = Operations.sub(num1,num2)
# print('substraction result: ', sub.to_10b())

# # print(BigNumber.one_digit_multiplication(BigNumber(value=19238470192), 8).to_10b())

# mul = Operations.multiply(num1, num2)
# print(f'mutiplication result:  {mul.to_10b()}, had to be {num1.to_10b()*num2.to_10b()}')

# pow2 = Operations.squere_pow(num1)
# print(f'power 2 result:  {pow2.to_10b()}, had to be {num1.to_10b()**2}')


quotient, remainder = Operations.div(num1, num2)
print(f'a: {num1.value}, b: {num2.value}')
print(f'a: {num1.to_10b()}, b: {num2.to_10b()}')
print(f'division result:  {quotient.to_10b()}, had to be {num1.to_10b()//num2.to_10b()}')
print(f'remainder :  {remainder.to_10b()}, had to be {num1.to_10b() - num1.to_10b()//num2.to_10b()}')


###
# test subdivision
# num1 = BigNumber(492845987343537419, 2**32)
# num2 = BigNumber(19234710942174981723941279783294, 2**32)
# num2 = BigNumber([8], 2**32)

# print('num1', num1.to_10b(), 'num2', num2.to_10b())
# print('num1', num1.value, 'num2', num2.value)
# sub = Operations.sub(num1, num2)
# print('sub', sub.value)
# print(f'sub result = {sub.to_10b()}; should have been: {num1.to_10b()-num2.to_10b()}')



# num = 283467432421424
# nummm = BigNumber(num, 2**32)
# print(nummm.value)
# bitted = nummm.to_2b()
# print(bitted)

# unbitted = BigNumber.from_2b(bitted, 2**32)
# print(unbitted.value)

# print(Operations.bit_shift_to_high(nummm, 3).to_10b())
# print(Operations.bit_shift_to_high(nummm, 3).to_2b())

# print(num<<3)
# print(bin(num))
# print(bin(num<<3))