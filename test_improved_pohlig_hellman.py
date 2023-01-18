import improved_pohlig_hellman 
import labmath
def t(base:int,mod:int):
    for exp in range(1,mod):
        expected=pow(base,exp,mod)
        result=improved_pohlig_hellman.improved_pohlig_hellman(base,mod,expected)
        actual=pow(base,result,mod)        
        assert actual==expected    
    assert improved_pohlig_hellman.improved_pohlig_hellman(base,mod,1) == mod -1

def s(base:int,mod:int,value:int):
    result=improved_pohlig_hellman.improved_pohlig_hellman(base,mod,value)   
    actual=pow(base,result,mod)   
    assert actual==value  

def test_CaseSimple():
    t(10,541)
    t(5,23)

def test_CaseMedium():
    t(1669,9439)
    t(2239,7681)
    t(191,3089)
    t(173,7607)
    t(2153,4793)
    t(443,7591)
    t(2357,7213)
    t(907,6863)
    t(1283,3019)
    
def getGenerator(prime:int):
    #https://math.stackexchange.com/questions/2188836/given-a-prime-p-find-a-generator-of-mathbbz-p
    primes= list(labmath.primefac(prime-1))
    for g in range(2,prime):
        if all(pow(g,(prime-1)//p ,prime) !=1 for p in primes): return g


def test_CaseDifficult():
    s(6,2420352901,4423432)
    s(6,2420352901,4423435)
    s(6,2420352901,3)
    s(6,2420352901,1111111)


