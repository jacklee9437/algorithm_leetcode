class Solution:
    def countPrimes(self, n: int) -> int:
        if n <= 1 :
            return 0
        
        primes = [True] * n
        primes[0] = primes[1] = False
        
        
        for i in range(2, int(n ** (1/2))+1) :
            if primes[i] :
                for j in range(i*2, n, i) :
                    primes[j] = False
        
        
        return primes.count(True)