import math
import labmath
from collections import Counter
class DiscreteLogarithm:
    """Class for calculating the discrete logarithm. It is efficient if the multiplicative order is a smooth number.
    """
    @property
    def base(self):
        return self.__base
    @property
    def mod(self):
        return self.__mod
    @property
    def order(self):
        return self.__order
   
    def __init__(self,base:int,mod:int):
        """Parameters
        ----------
        base : int      
        mod : int
        Must be a prime
        """
        self.__base=base
        self.__mod=mod
        self.__order=labmath.multord(base,mod)
        self.__factors=list(labmath.primefac(self.__order)) 
        order=self.order 
        factors=self.__factors      
        self.__giant_steps=[None]*len(factors)
        giant_steps=self.__giant_steps
        for i,f in enumerate(factors): 
            cache={1:0}
            giant_steps[i]=cache
            size=pow(base,order//f,mod)            
            value=1           
            for cached_offset in range(f-1,f-math.isqrt(f)-1,-1):                
                value= (value*size) % mod
                cache[value]=cached_offset       
        

    def calc(self,value:int)->int:
        "Calculates discrete logarithm. Returns -1 if no result exists."
        mod=self.mod
        d=self.order
        factors=self.__factors
        giant_steps=self.__giant_steps
        base=self.base
        steps=0
        step=1       
        for i,f in enumerate(factors):    
            d=d//f
            cache=giant_steps[i]
            start=pow(value,d,mod)    
            if start != 1:
                cache_len=len(cache)
                max= f//cache_len+(f % cache_len > 0)               
                size=pow(base,d*cache_len,mod)  
                count=0 
                while count < max and (cached_offset:= cache.get(start)) is None:
                    start=(start*size) % mod            
                    count+=1
                if cached_offset is None: return -1 
                offset= (cache_len*count+cached_offset) % f
                value=(value*pow(base,offset,mod)) % mod
                steps=steps+step*offset
            base=pow(base,f,mod)   
            step*=f
        return self.order-steps

