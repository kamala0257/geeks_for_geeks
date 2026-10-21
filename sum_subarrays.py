class Solution:
    def minSubarraySum(self, arr: list[int]) -> int:
        if not arr:
            return 0
        
        current_min = arr[0]
        global_min = arr[0]
        
        for i in range(1, len(arr)):
            # Either extend the previous minimum subarray or start a new one at the current element
            current_min = min(arr[i], current_min + arr[i])
            global_min = min(global_min, current_min)
            
        return global_min
