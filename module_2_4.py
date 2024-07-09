numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_prime = []
for i in range(0, len(numbers)):
    is_prime = True
    if numbers[i] == 1:
        continue
    elif numbers[i] == 2:
        primes.append(numbers[i])
        continue
    elif numbers[i] > 2:
        for j in range(numbers[i],1,-1):
            if numbers[i] % j == 0  and  j != numbers[i]:
                is_prime = False
                break
            else:
                is_prime = True
        if is_prime:
            primes.append(numbers[i])
        else:
            not_prime.append(numbers[i])
print('Primes:', primes)
print('Not Primes:',not_prime)



