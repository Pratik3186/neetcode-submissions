class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = {
            ')':'(',
            '}':'{',
            ']':'['
        }
        for ch in s:
            if ch in '({[':
                stack.append(ch)
            else:
                if not stack:
                    return True
                if stack[-1] != paris[ch]:
                    return False
                stack.pop()
        return len(nums) == 0
        