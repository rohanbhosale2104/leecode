from math import gcd

class Solution:
    def findKthSmallest(self, coins, k):
        
        # Remove duplicate coins
        coins = list(set(coins))
        
        n = len(coins)

        def lcm(a, b):
            return a // gcd(a, b) * b

        def count(x):
            total = 0

            # Inclusion-Exclusion
            for mask in range(1, 1 << n):
                curr_lcm = 1
                bits = 0
                valid = True

                for i in range(n):
                    if mask & (1 << i):
                        curr_lcm = lcm(curr_lcm, coins[i])

                        # LCM already larger than x
                        if curr_lcm > x:
                            valid = False
                            break

                        bits += 1

                if not valid:
                    continue

                value = x // curr_lcm

                if bits % 2 == 1:
                    total += value
                else:
                    total -= value

            return total

        # Binary search
        left = 1
        right = min(coins) * k

        while left < right:
            mid = (left + right) // 2

            if count(mid) >= k:
                right = mid
            else:
                left = mid + 1

        return left