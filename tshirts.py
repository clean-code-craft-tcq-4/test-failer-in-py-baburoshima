def size(cms):
    if cms < 38:
        return 'S'
    elif cms > 38 and cms < 42:
        return 'M'
    else:
        return 'L'


assert(size(37) == 'S')
assert(size(40) == 'M')
assert(size(43) == 'L')
#added boundary value checks
assert(size(38) == 'S')
assert(size(42) == 'M')
#added invalid value checks
assert(size(-1)==None)
assert(size(0)==None)
#shoulder width outside range 15-60cm considered as invalid
assert(size(14)==None) 
assert(size(61)==None) 
print("All is well (maybe!)\n")
