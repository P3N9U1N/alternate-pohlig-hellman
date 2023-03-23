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


