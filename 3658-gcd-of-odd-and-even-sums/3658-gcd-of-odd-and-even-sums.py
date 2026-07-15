class Solution:
    def gcdOfOddEvenSums(self, n: int) -> int:
        # Calculate sum of first n odd numbers
        odd_sum = 0
        odd_num = 1
        for i in range(n):
            odd_sum += odd_num
            odd_num += 2
    
        # Calculate sum of first n even numbers
        even_sum = 0
        even_num = 2
        for i in range(n):
            even_sum += even_num
            even_num += 2
    
        # Calculate GCD
        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a
    
        return gcd(odd_sum, even_sum)