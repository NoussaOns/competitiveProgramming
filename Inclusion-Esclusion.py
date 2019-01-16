n = int(input())
c = 0
for i2 in range(2):
    for i3 in range(2):
        for i5 in range(2):
            d = 1
            c1 = 0
            if i2 :
                d *= 2
                c1 +=1
            if i3:
                d*=3
                c1+=1
            if i5:
                d*=5
                c1+=1

            if c1 == 0:
                continue

            sign = 1 if c1%2 == 1 else -1
            c += sign * (n//d)
print(c)
