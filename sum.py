class Solution:
    def findPairs(self, arr):
        n = len(arr)
        seen_sums = {}
        best_quad = None

        for i in range(n):
            for j in range(i + 1, n):
                curr_sum = arr[i] + arr[j]

                if curr_sum not in seen_sums:
                    seen_sums[curr_sum] = (i, j)
                else:
                    a, b = seen_sums[curr_sum]
                    # Ensure all four indices are distinct
                    if a != i and a != j and b != i and b != j:
                        candidate = [a, b, i, j]
                        if best_quad is None or candidate < best_quad:
                            best_quad = candidate

        return best_quad if best_quad is not None else [-1, -1, -1, -1]
