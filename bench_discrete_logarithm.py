import richbench
from discrete_logarithm  import DiscreteLogarithm  
from test_discrete_logarithm import test_all

def benchmark_1():
    DiscreteLogarithm(47,10000000000000000000000343).calc(191)

def benchmark_2():
    DiscreteLogarithm(47,1000000000000000000117).calc(191)
    
def benchmark_3():
    test_all(1669,9439)
 
def benchmark_4():
    DiscreteLogarithm(6,2420352901).calc(1111111) 


__benchmarks__ = [
    (benchmark_1,benchmark_1, "base 47, mod 10000000000000000000000343, value 191"),
    (benchmark_2,benchmark_2, "base 47, mod 1000000000000000000117, value 191"),
    (benchmark_3,benchmark_3, "base 1669, mod 9439, all values"),
    (benchmark_4,benchmark_4, "base 6, mod 2420352901, value 1111111")

]




