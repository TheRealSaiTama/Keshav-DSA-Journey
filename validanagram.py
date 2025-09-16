class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dict1 = {}
        for ch in s:
            if ch not in dict1:
                dict1[ch] = 1
            else:
                dict1[ch] += 1

        dict2 = {}
        for ch in t:
            if ch not in dict2:
                dict2[ch] = 1
            else:
                dict2[ch] += 1

        return dict1 == dict2
