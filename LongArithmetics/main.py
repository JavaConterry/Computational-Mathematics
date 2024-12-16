from BigNumber import BigNumber, Operations
import time #TODO

print("start")

input_base = int(input('Base of a Big Number:'))

if(input_base == 16):
    # num1 = BigNumber.from_16b('1f630dc14445ba417218cc2a7666eab74a8e294810e06918bf8c9955a9fbe95225bae29953afbf1d4ea93adbc342238fd38cb58c052ddf0747c2d634adc300499f058af68f25947a428a80d086e3cea15679dba3bff6c62f680f7f470f5dbb519271c5b1a0c298fcd037db4c337ce51e2b90e02538bbd774c9ae6a2aa3db632c9337fbb95d6d33fe2c54ed24a7cb16fc05638659fa277aae7f4dad329cbbd908292a82ee4336289e548e24efd83ddff52bbf0a75bbe8717d987b4b0b3177698b2eb5d375001f5b0dcd2aa65e7af785338d78bebed34c6874f169907968f5cd11aa89ce2194c695b831ec305bb5b687a566e3c792c01932f83e43', 2**16)
    # num2 = BigNumber.from_16b('f143ce95c6ec034bed56425d9bf12c2ec255c3f481a2265f471e87189a546aadda095acd6a4e8dd81ef8a7c9eacbff1c5c7a5898096491335f86ee7e96b2761024b643afbf3a01ea6e1b1e1ca2cf0773b3909808a7b6c947ac5275b63bab4b973ffded9ab171a85258466d743b2d309dbe401cb445f415a02f68ff7d8434e395994e9ae5cdb76a3ecc503ba26bd32dc2c9433848096da0c1aaef8d0dbf7f051de81523cc5526152a83da8f4cdf7365a14492fd090957eda02026216eca2efb6eb0f92871d174b29bec525cf1b7cc2e87bb08d501aaa4fd21c841b97e0976992ac37a8abcb05e6b57ff26a65ff14cbfcbff98429abac509e5de6a', 2**16)
    num1 = BigNumber.from_16b(input('Number 1:'), 2**16)
    num2 = BigNumber.from_16b(input('Number 2:'), 2**16)
    print("Read was complete")
    num3 = BigNumber.from_16b('2c2cd293', 2**16)
    num4 = BigNumber.from_16b('3c4', 2**16)
    # print('1:',Operations.multiply(Operations.add(num1,num2),num3))
    # print('2:',Operations.add(Operations.multiply(num1,num3), Operations.multiply(num2, num3)))
    if(Operations.multiply(Operations.add(num1,num2),num3).to_10bint() == Operations.add(Operations.multiply(num1,num3), Operations.multiply(num2, num3)).to_10bint()):
        print("(a+b)*(random c) = (ac + bc): Test was seccessful")
    def test_multiplication(a,n):
        summres = BigNumber(a.to_10bint(), a.base)
        for i in range(n.to_10bint()-1):
            summres = Operations.add(summres, a)
        if(Operations.multiply(a, n).to_16b() == summres.to_16b()): return True
        else: return False
    if(test_multiplication(num1, num4)):
        print("a*(random n) = a+....+a (n times): Test was seccessful")
    
    st = time.time()
    add = Operations.add(num1, num2)
    print("\naddition result:", add.to_16b(), f'\noperation time: {time.time()-st}')
    st = time.time()
    sub = Operations.sub(num1, num2)
    print("\nsubstitution result:", sub.to_16b(), f'\noperation time: {time.time()-st}')
    st = time.time()
    mul = Operations.multiply(num1, num2)
    print("\nmultiplication result: ", mul.to_16b(), f'\noperation time: {time.time()-st}')
    st = time.time()
    quotient, remainder = Operations.div(num1, num2)
    print(f'\ndivision result:  {quotient.to_16b()}')
    print(f'\nremainder :  {remainder.to_16b()}', f'\noperation time: {time.time()-st}')
elif(input_base == 10):
    # num1 = BigNumber(14076678201135072616114117282339279437876951566724273834935658448208687954475575267795291987725884043613197506118698461813496739331425696753135750849882259098408949181402113076106362831196925260856592353993343504313790753676147814623772073797722376871112649971922375757489727217633853744560110054192589874599857150121718902613671127857596938340576608565106708062965679597157224062851077876611504638908666061845245084911117387106037782391859240533652846665519333261142543781602025680796043668725612782337201932795850227806833595062021166984794614728694178153377209857594110692231233587364830146576531011, 2**16)
    # num2 = BigNumber(108204532840880086458821226679975803027851417304163293772482070747322223752730576902384936131378171826755519786705877801463027140770786781727099928358680286399111493921383224328384637783012272754279291444322850089275972470119446771871477843582690476148245307457352927911393249017183682430469770104181530020360331294692173587384784502002586682399701246576138163479348943370530350823185273478559739348374779000963841023335432635692993262954116940437968451685836594833986109470080175762993823624556195790456699353704291115136811961218327977294493534482956977344274500027032974101662559389799616537891823210, 2**16)
    num1 = BigNumber(int(input('Number 1')), 2**16)
    num2 = BigNumber(int(input('Number 2')), 2**16)
    print("Read was complete")
    st = time.time()
    add = Operations.add(num1, num2)
    print("\naddition result:", add.to_10bint(), f'\noperation time: {time.time()-st}')
    st = time.time()
    sub = Operations.sub(num1, num2)
    print("\nsubstitution result:", sub.to_10bint(), f'\noperation time: {time.time()-st}')
    st = time.time()
    mul = Operations.multiply(num1, num2)
    print("\nmultiplication result: ", mul.to_10bint(), f'\noperation time: {time.time()-st}')
    st = time.time()
    quotient, remainder = Operations.div(num1, num2)
    print(f'\ndivision result:  {quotient.to_16b()}')
    print(f'\nremainder :  {remainder.to_16b()}', f'\noperation time: {time.time()-st}')
else:
    print('Unsupporrted base')
