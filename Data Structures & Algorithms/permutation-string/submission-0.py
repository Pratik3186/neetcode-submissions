from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        k = len(s1)
        if k > len(s2):
            return False

        p_count = Counter(s1)
        window_count = Counter(s2[:k])

        if window_count == p_count:
            return True

        for right in range(k, len(s2)):
            window_count[s2[right]]+= 1
            window_count[s2[right-k]] -= 1

            if window_count[s2[right-k]] ==0:
                del window_count[s2[right-k]]

            if window_count == p_count:
                return True

        return False