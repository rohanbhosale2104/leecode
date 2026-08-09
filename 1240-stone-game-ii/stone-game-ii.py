class Solution:
    def stoneGameII(self, piles: List[int]) -> int:

        n = len(piles)

        # suffix[i] = total stones from i to end
        suffix = [0] * (n + 1)

        for i in range(n - 1, -1, -1):
            suffix[i] = suffix[i + 1] + piles[i]

        dp = {}

        def dfs(i, M):
            # Take all remaining stones
            if i >= n:
                return 0

            # If we can take all remaining stones
            if i + 2 * M >= n:
                return suffix[i]

            if (i, M) in dp:
                return dp[(i, M)]

            best = 0

            # Take X stones, where X <= 2*M
            for X in range(1, 2 * M + 1):

                # Current player gets X stones.
                # Opponent gets the best possible result from next state.
                opponent = dfs(i + X, max(M, X))

                current = suffix[i] - opponent

                best = max(best, current)

            dp[(i, M)] = best

            return best

        return dfs(0, 1)