# Alternate version of the Pohlig-Hellman algorithm

This repository contains an alternate version of the Pohlig-Hellman algorithm. It is used for solving the discrete logarithm.

## The algorithm
```python
import labmath
def alternate_pohlig_hellman(base:int,mod:int,value:int):
 d=mod-1
 factors= list(labmath.primefac(d))
 steps=0
 step=1
 for f in factors:    
    d=d//f
    start=pow(value,d,mod)    
    if start != 1:
        step2=pow(base,d,mod)         
        offset=0
        while offset < f and start != 1:
            start=(start*step2) % mod            
            offset+=1
        if start !=1: return None 
        value=(value*pow(base,offset,mod)) % mod
        steps=steps+step*offset 
    base=pow(base,f,mod)   
    step*=f
 return mod-1-steps
```

## Description
Solve the discrete logarithm:

$base^{exp} \bmod mod \equiv value$

Given the the prime factorization $factors$ of $(mod-1)$:

$f_1,f_2,\dots,f_{len(factors)}$

Find the next $value$ whose exponent is dividable by $f_1$. Repeat for $f_1\*f_2,\dots$ until $f_1*f_2\*\dots\*f_{len(factors)}$. In each repetition, the offset required to obtain the next $value$ is added up to the total number of $steps$ taken. After the algorithm is finished, the exponent is $(mod-1)$ and the solution to the discrete logarithm can be returned as $(mod-1-steps)$.  

## Performance
Did some comparision with https://github.com/jaanos/kirv/blob/master/algorithms/discreteLogarithm.py and this algorithm is slower than Pohlig-Hellman.


## Requirements
Following packages are needed:
```
pip install labmath pytest
```
