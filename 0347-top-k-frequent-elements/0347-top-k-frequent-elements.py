class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = collections.defaultdict(int)
        bucket = [ [] for i in range(len(nums) + 1) ]

        for n in nums:
            hashmap[n] += 1

        for num, freq in hashmap.items():
            bucket[freq].append(num)

        result = []         
        for i in reversed(range(len(bucket))):
            for num in bucket[i]:
                if len(result) != k:
                    result.append(num)
        return result
        