class Solution:
    def goodIndices(self, arr):
        n = len(arr)
        state = [0] * n

        for i in range(n):
            if state[i] != 0:
                continue

            path = []
            pos = {}
            j = i

            while 0 <= j < n and state[j] == 0 and j not in pos:
                pos[j] = len(path)
                path.append(j)
                j += arr[j]

            if j < 0 or j >= n:
                result = 1
            elif state[j] != 0:
                result = state[j]
            elif j in pos:
                result = 2
            else:
                result = 2

            for k in reversed(path):
                state[k] = result

        return state.count(1)
