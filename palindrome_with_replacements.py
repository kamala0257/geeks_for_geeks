class Solution:
    def minimumSum(self, s: str) -> int:
        n = len(s)
        answer = 0
        previous = None
        
        # Process only the left half of the string
        for i in range(n // 2):
            left = s[i]
            right = s[n - 1 - i]
            
            current = None
            if left != '?' and right != '?':
                if left != right:
                    return -1
                current = left
            elif left != '?':
                current = left
            elif right != '?':
                current = right
            else:
                # Both are '?', they can take the value of the previous character with 0 cost
                continue
            
            # If we found a fixed/determined character, calculate the difference from the previous one
            if previous is not None:
                # Multiply by 2 because the symmetric transition happens on both halves of the palindrome
                answer += 2 * abs(ord(current) - ord(previous))
                
            previous = current
            
        return answer
