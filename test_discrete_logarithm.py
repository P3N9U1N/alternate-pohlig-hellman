from discrete_logarithm  import DiscreteLogarithm  
import labmath
import pytest

@pytest.mark.skip
def test_all(base:int,mod:int): 
    d=DiscreteLogarithm(base,mod)  
    order=labmath.multord(base,mod)
    value=base
    for expected in range(1,order+1): 
        actual=d.calc(value)        
        assert actual==expected    
        value=(value*base) % mod    

@pytest.mark.skip
def test_single_case_with_generator(base:int,mod:int,value:int):
    result=DiscreteLogarithm(base,mod).calc(value)   
    actual=pow(base,result,mod)   
    assert actual==value  

@pytest.mark.skip
def test_all_values_without_solution(base:int,mod:int):
    d=DiscreteLogarithm(base,mod)
    arr=[False]*mod
    value=base
    for exp in range(mod):
        arr[value]=True
        value=(value*base)%mod
    for i in range(len(arr)):
        if not arr[i]:
            actual=d.calc(i)
            assert actual == -1   

def test_case_simple():    
    test_all(3,89)
    test_all(5,89)
    test_all(10,541)
    test_all(5,23)

def test_case_medium():
    test_all(1669,9439)
    test_all(2239,7681)
    test_all(191,3089)
    test_all(173,7607)
    test_all(2153,4793)
    test_all(443,7591)
    test_all(2357,7213)
    test_all(907,6863)
    test_all(1283,3019)
    test_all(907,6863)

def get_generator(prime:int):
    #https://math.stackexchange.com/questions/2188836/given-a-prime-p-find-a-generator-of-mathbbz-p
    primes= list(labmath.primefac(prime-1))
    for g in range(2,prime):
        if all(pow(g,(prime-1)//p ,prime) !=1 for p in primes): return g


def test_case_difficult():    
    test_single_case_with_generator(6,2420352901,4423432)
    test_single_case_with_generator(6,2420352901,4423435)
    test_single_case_with_generator(6,2420352901,3)
    test_single_case_with_generator(6,2420352901,1111111)
    test_single_case_with_generator(6,2420352901,1111111)
    test_single_case_with_generator(47,1000000000000000000117,191)
    test_single_case_with_generator(47,1000000000000000000117,194225671)
    test_single_case_with_generator(47,1000000000000000000117,19)
    test_single_case_with_generator(47,1000000000000000000117,86794562214523)
    test_single_case_with_generator(47,1000000000000000000117,32123)
    test_single_case_with_generator(47,1000000000000000000117,4325345435555)
    test_single_case_with_generator(47,1000000000000000000117,11111)
    test_single_case_with_generator(47,1000000000000000000117,454353456)
    test_single_case_with_generator(47,10000000000000000000000343,191)
    

    
def test_case_fail():
    test_all_values_without_solution(5,89)
    test_all_values_without_solution(443,7591)
    test_all_values_without_solution(2357,7213)
    test_all_values_without_solution(907,6863)

@pytest.mark.skip
def test_single_exponent(base:int,mod:int,exp:int):
        expected=pow(base,exp,mod)
        result=DiscreteLogarithm(base,mod).calc(expected)
        actual=pow(base,result,mod)
        assert actual==expected




