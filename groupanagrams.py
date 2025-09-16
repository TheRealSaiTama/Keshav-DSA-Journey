class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict1 = {}
        for string in strs:
            sort = ''.join(sorted(string))
            if sort in dict1:
                dict1[sort].append(string)
            else:
                dict1[sort] = [string]

        return list(dict1.values())


dict1 = {}
for string in strs:
    count = [0]*26
    for ch in string:
        count[ord(ch) - ord('a')] += 1
    key = tuple(count)
    if key in dict1:
        dict1[key].append(string)
    else:
        dict1[key] = [string]

return list(dict1.values())
