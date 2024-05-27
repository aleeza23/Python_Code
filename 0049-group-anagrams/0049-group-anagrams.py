class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        lookup = defaultdict(list)
        
        
        for str in strs:
            array = [0] * 26
            print(ord("b"))            

            for c in str:
               
                array[ord(c) - ord("a")] += 1
                print(array)
            lookup[tuple(array)].append(str)
            
              
        return lookup.values()        