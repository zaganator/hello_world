def prime(limit):
    primes = [1,2,3]
    numbers = []
    odd = []
    for num in range(2,limit):
        numbers.append(num)
    for num in numbers:
        if num % 2 != 0:
            odd.append(num)
    print(f'these are in fact the odd number\n{odd}')
    print(f'how many odd numbers:{len(odd)}')
    for num in odd:
        index = 0
        if num % odd[index] != 0:
            primes.append(num)
            index += 1
    print (f'how many primes: {len(primes)}')

    return primes
limit = int(input("set a limit to find primt numbers\n"))
print (f'prime numbers \n{prime(limit)} to {limit}')
