class Solution:
    def maxPackages(self, arr: list[int], totalTime: int) -> int:
        n = len(arr)
        k = min(totalTime, n)
        
        # Calculate sum for the first window
        current_sum = sum(arr[:k])
        max_sum = current_sum
        
        # Slide the window
        for i in range(k, n):
            current_sum += arr[i] - arr[i - k]
            max_sum = max(max_sum, current_sum)
            
        return max_sum
