class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        n = len(t)
        pointer = 0
        for i in range(n):
            if pointer >= len(s):
                break
            if s[pointer] == t[i]:
                pointer += 1

        return pointer == len(s)
