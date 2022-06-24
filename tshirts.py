def size(cms):
    if cms not in range(15,50): #shoulder width outside range 15-50cm considered as invalid 
        return None
    if cms < 38:
        return 'S'
    elif cms >= 38 and cms < 42:
        return 'M'
    else:
        return 'L'

assert(size(37) == 'S')
assert(size(40) == 'M')
assert(size(43) == 'L')
#added boundary value checks
assert(size(38) == 'M')
assert(size(42) == 'L')
#added invalid value checks
assert(size(-1)==None)
assert(size(0)==None)
assert(size(14)==None) 
assert(size(51)==None) 
print("All is well  :) \n")
