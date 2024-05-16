class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        lookup = defaultdict(list)

        for str in strs:
            lookup["".join(sorted(str))].append(str)
        return lookup.values()     
        
        