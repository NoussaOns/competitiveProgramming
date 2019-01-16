from math import floor
while(1):
    try:
        step, mod = map(int, input().split())
        bad = False
        current = 0

        for i in range(mod-1):
            current = (current+step) % mod
            if current == 0:
                bad = True
                break

        if bad:
            res = 'Bad Choice'
        else:
            res = 'Good Choice'

        print('%10d%10d%4s%s\n'%(step,mod,'',res))

    except:
        break

