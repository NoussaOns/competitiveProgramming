primes = [2,3,5,7]
n = 100

def inc_exe(idx = 0,d=1,sign = -1):
    if idx == 4:
        if d==1:
            return 0
        return sign * n // d
    return inc_exe(idx+1,d,sign) + inc_exe(idx+1, d*primes[idx],-1 * sign)

print(inc_exe())