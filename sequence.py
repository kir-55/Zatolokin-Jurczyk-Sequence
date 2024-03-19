memo = []

base = 6

def calculate_v(n):
    

    if len(memo) > n:
        return memo[n]

    if n == 0:
        memo.append(1)
        return 1
    if n == 1:
        memo.append(base-1)
        return base-1

    
    v = base**n - calculate_v(n-1)
    #v = base**n - base**(n-1)
    memo.append(v)
    return v


for i in range(20):
    print(str(i) + ": " + str(calculate_v(i)%10))
