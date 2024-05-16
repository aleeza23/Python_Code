class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        lookup = defaultdict(list)
        
        
        for str in strs:
            array = [0]*26
            
            for c in str:
                array[ord(c) - ord("a")] += 1
            lookup[tuple(array)].append(str)
              
        return lookup.values()       


    
        
        