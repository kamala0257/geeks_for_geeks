
class Solution:
    def minDiff(self, k, arr):
        n = len(arr)

        if k == 0:
            return max(arr) - min(arr)

        if k == n:
            return 0

        prefix_min = [0] * n
        prefix_max = [0] * n
        suffix_min = [0] * n
        suffix_max = [0] * n

        prefix_min[0] = prefix_max[0] = arr[0]

        for i in range(1, n):
            prefix_min[i] = min(prefix_min[i - 1], arr[i])
            prefix_max[i] = max(prefix_max[i - 1], arr[i])

        suffix_min[-1] = suffix_max[-1] = arr[-1]

        for i in range(n - 2, -1, -1):
            suffix_min[i] = min(suffix_min[i + 1], arr[i])
            suffix_max[i] = max(suffix_max[i + 1], arr[i])

        ans = float('inf')

        for i in range(n - k + 1):
            left = i - 1
            right = i + k

            if left < 0:
                diff = suffix_max[right] - suffix_min[right]
            elif right >= n:
                diff = prefix_max[left] - prefix_min[left]
            else:
                maximum = max(prefix_max[left], suffix_max[right])
                minimum = min(prefix_min[left], suffix_min[right])
                diff = maximum - minimum

            ans = min(ans, diff)

        return ans
