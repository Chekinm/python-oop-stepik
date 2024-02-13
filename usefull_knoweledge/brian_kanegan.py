def count_bits(n):
    res = 0
    while n:
        res += 1
        print(bin(n), bin(n-1))
        n = n & (n-1)
        print(bin(n))
    return res


for i in range(20):
    bits_count = count_bits(i)
    print(f'{bin(i)=}, {bits_count=}')

print(count_bits(100000000000000000000000000000000000000000000))
print(bin(100000000000000000000000000000000000000000000).count('1'))

a = int()

b = count_bits(29)