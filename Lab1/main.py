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

mul = Operations.multiply(num1, num2)
print(f'mutiplication result:  {mul.to_10b()}, had to be {num1.to_10b()*num2.to_10b()}')


###
# test subdivision
# num1 = BigNumber(492845987343537419, 2**32)
# num2 = BigNumber(19234710942174981723941279783294, 2**32)
# print(f'sub result = {Operations.sub(num1, num2).to_10b()}; should have been: {492845987343537419-19234710942174981723941279783294}')