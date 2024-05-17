def generate_primes(n):
    primes = []
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False
    
    for i in range(2, n + 1):
        if is_prime[i]:
            primes.append(i)
            for j in range(i * i, n + 1, i):
                is_prime[j] = False
    
    return primes

def isWinner(x, nums):
    maria_wins = 0
    ben_wins = 0
    
    for n in nums:
        if n == 1:
            ben_wins += 1
            continue
        
        primes = generate_primes(n)
        if len(primes) % 2 == 0:
            ben_wins += 1
        else:
            maria_wins += 1
    
    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None

# Test cases
x = 3
nums = [4, 5, 1]
print(isWinner(x, nums))  # Output: "None"

